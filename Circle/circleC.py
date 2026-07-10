"""
LEAVITT CLIENT - CIRCLE topology, variable Jetson count (2-5)

Program receives prompts from the server, asks
the local Gemma model for a response, and sends the response back to the server.
"""

# imports
import socket
import json
import sys
import time
import requests
import platform

# ====================================================================== CONFIG
OLLAMA_URL = "http://127.0.0.1:11434"
MODEL_NAME = "gemma3:4b"
OLLAMA_TEMPERATURE = 0.0
OLLAMA_TOP_P = 0.7              # fewer weird word choices, the smaller number -> more repetetive but less words
OLLAMA_REPEAT_PENALTY = 1.3     # less looping/repeating
OLLAMA_NUM_PREDICT = 80         # limits response length
SERVER_IP = "192.168.0.140"
SERVER_PORT = 5001
RECONNECT_DELAY_SECONDS = 5
# ====================================================================== OLLAMA

def check_ollama():
    # Pre-flight check: server reachable and target model available locally.
    try:
        resp = requests.get(OLLAMA_URL, timeout=5)
        if resp.status_code != 200:
            return False, "Ollama not responding"
    except requests.ConnectionError:
        return False, f"Cannot connect to Ollama at {OLLAMA_URL}. Run: ollama serve"

    try:
        resp = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        models = [m["name"] for m in resp.json().get("models", [])]
        if not any(MODEL_NAME.split(":")[0] in m for m in models):
            return False, f"Model '{MODEL_NAME}' not found. Run: ollama pull {MODEL_NAME}"
    except Exception as e:
        return False, f"Error checking models: {e}"

    return True, "OK"


# Sends the experiment prompt to the local Gemma model and returns this agent’s reply.
def generate_agent_reply(prompt):
    """
    Ask model to respond to the server-provided circle-topology prompt.

    Returns a dict: {"action": "chat", "text": "..."} or {"action": "answer", "word": "square"}
    """

    # Non-streaming generation keeps parsing logic simple and deterministic.
    payload = {
        "model": MODEL_NAME,
        "system": "Follow the server prompt exactly. Stay inside the figure-matching task.",
        "prompt": prompt,
        "stream": False,
        "keep_alive": 300,
        "options": {
            "temperature": OLLAMA_TEMPERATURE,
            "top_p": OLLAMA_TOP_P,
            "repeat_penalty": OLLAMA_REPEAT_PENALTY,
            "num_predict": OLLAMA_NUM_PREDICT,
        },
    }

    try:
        resp = requests.post(f"{OLLAMA_URL}/api/generate", json=payload, timeout=240)
        resp.raise_for_status()
        raw = resp.json().get("response", "").strip()
    except Exception as e:
        print(f"[OLLAMA ERROR] {e}")
        return {"action": "chat", "text": f"(error: {e})"}

    print(f"[MODEL RAW] {raw}")

    # ---- Parse the model's structured response ----
    return classify_agent_response(raw)


# Decides whether the agent’s response is a chat message or a final answer.
def classify_agent_response(raw):
    """
    Parse the ACTION: CHAT/ANSWER format from the model output.
    Falls back to treating the whole thing as a chat message.
    """
    raw_upper = raw.upper()

    # Structured parse first; fallback to chat to keep the client resilient.
    # Check for ANSWER
    if "ACTION: ANSWER" in raw_upper or "ACTION:ANSWER" in raw_upper:
        answer_lines = []
        for line in raw.split("\n"):
            line_stripped = line.strip()
            upper = line_stripped.upper()
            if upper.startswith("WORD:") or upper.startswith("SYMBOL:"):
                word = line_stripped.split(":", 1)[1].strip().strip("` '\"")
                if len(word) > 0:
                    return {"action": "answer", "word": word}
            elif line_stripped and not upper.startswith("ACTION:"):
                answer_lines.append(line_stripped)

        if answer_lines:
            return {"action": "answer", "word": answer_lines[0].strip("` '\"")}

        return {"action": "chat", "text": raw}

    # Check for CHAT
    if "ACTION: CHAT" in raw_upper or "ACTION:CHAT" in raw_upper:
        chat_lines = []
        for line in raw.split("\n"):
            line_stripped = line.strip()
            upper = line_stripped.upper()
            if upper.startswith("MESSAGE:"):
                msg = line_stripped.split(":", 1)[1].strip()
                return {"action": "chat", "text": msg}
            if line_stripped and not upper.startswith("ACTION:"):
                chat_lines.append(line_stripped)
        if chat_lines:
            return {"action": "chat", "text": chat_lines[0]}

    # Fallback: treat the entire output as a chat message
    return {"action": "chat", "text": raw}


def send_json(sock, payload):
    data = (json.dumps(payload) + "\n").encode("utf-8")
    sock.sendall(data)


def recv_json_line(sock):
    buf = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            return None
        buf += chunk
        if b"\n" in buf:
            line, _rest = buf.split(b"\n", 1)
            return json.loads(line.decode("utf-8"))


def main():
    ok, msg = check_ollama()
    if not ok:
        print(f"[STARTUP ERROR] {msg}")
        sys.exit(1)

    print("[STARTUP] Ollama check passed.")

    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print(f"[CONNECT] Connecting to {SERVER_IP}:{SERVER_PORT} ...")
            sock.connect((SERVER_IP, SERVER_PORT))
            print("[CONNECT] Connected to server.")

            conversation_history = []
            agent_name = None
            my_symbols = []
            num_agents = 2
            hostname = platform.node().split(".", 1)[0].lower()

            while True:
                msg = recv_json_line(sock)
                if msg is None:
                    print("[SERVER] Disconnected.")
                    break

                msg_type = msg.get("type")

                if msg_type == "nickname_request":
                    send_json(sock, {"type": "nickname", "hostname": hostname})
                    continue

                if msg_type == "welcome":
                    assigned_name = msg.get("agent_name")
                    if assigned_name:
                        agent_name = assigned_name
                        print(f"[SERVER] Assigned name: {agent_name}")

                elif msg_type == "experiment_start":
                    agent_name = msg["agent_name"]
                    my_symbols = msg["your_symbols"]
                    num_agents = msg.get("num_agents", num_agents)
                    print(f"\n[START] I am {agent_name}")
                    print(f"[START] My figures: {my_symbols}")
                    print(f"[START] Number of agents: {num_agents}")
                    conversation_history = []

                elif msg_type == "system":
                    text = msg.get("text", "")
                    print(f"[SYSTEM] {text}")
                    conversation_history.append({"sender": "SYSTEM", "text": text})

                elif msg_type == "chat":
                    sender = msg.get("sender", "UNKNOWN")
                    text = msg.get("text", "")
                    print(f"[{sender}] {text}")
                    conversation_history.append({"sender": sender, "text": text})

                elif msg_type == "your_turn":
                    prompt = msg.get("prompt", "")
                    if not prompt:
                        print("[WARN] Missing server prompt.")
                        send_json(sock, {"type": "chat", "text": "I need the local circle prompt."})
                        continue

                    decision = generate_agent_reply(prompt)
                    action = decision.get("action")

                    if action == "answer":
                        word = decision.get("word", "").strip()
                        if word:
                            print(f"[SEND ANSWER] {word}")
                            send_json(sock, {"type": "answer", "word": word})
                        else:
                            fallback = "I need more evidence."
                            print(f"[SEND CHAT] {fallback}")
                            send_json(sock, {"type": "chat", "text": fallback})
                    else:
                        text = decision.get("text", "").strip() or "I need more evidence."
                        print(f"[SEND CHAT] {text}")
                        send_json(sock, {"type": "chat", "text": text})

                elif msg_type == "result":
                    print("\n[RESULT]")
                    print(json.dumps(msg, indent=2))
                    break

                else:
                    print(f"[UNKNOWN MESSAGE] {msg}")

        except ConnectionRefusedError:
            print("[CONNECT ERROR] Server unavailable.")
        except KeyboardInterrupt:
            print("\n[CLIENT] Exiting.")
            try:
                sock.close()
            except Exception:
                pass
            sys.exit(0)
        except Exception as e:
            print(f"[CLIENT ERROR] {e}")
        finally:
            try:
                sock.close()
            except Exception:
                pass

        print(f"[RETRY] Reconnecting in {RECONNECT_DELAY_SECONDS} seconds...")
        time.sleep(RECONNECT_DELAY_SECONDS)


if __name__ == "__main__":
    main()
