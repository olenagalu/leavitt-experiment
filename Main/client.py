"""
LEAVITT - CLIENT  
"""

# imports
import socket
import json
import sys
import time
import requests
import platform
from circle_client import build_circle_prompt, parse_circle_response

# ====================================================================== CONFIG
OLLAMA_URL = "http://127.0.0.1:11434"
MODEL_NAME = "gemma3:4b"
OLLAMA_TEMPERATURE = 0.0
OLLAMA_TOP_P = 0.7              # fewer weird word choices, the smaller number -> more repetetive but less words
OLLAMA_REPEAT_PENALTY = 1.3     # less looping/repeating
OLLAMA_NUM_PREDICT = 70         # limits response length
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
def generate_agent_reply(
    agent_name,
    my_symbols,
    conversation_history,
    num_agents,
    current_round,
    can_answer,
    topology="broadcast",
    circle_neighbors=None,
    server_prompt=None,
    circle_recent_messages=None,
    preferred_neighbor=None,
):
    """
    Ask model to discuss possible common symbols or answer when allowed.

    Returns a dict with action, parsed fields, and the raw model response.
    """

    symbols_str = "  ".join(my_symbols)
    figures_list = ", ".join(my_symbols)
    circle_neighbors = circle_neighbors or []

    num_agents = max(2, min(5, int(num_agents)))

    if topology == "circle":
        system_prompt = "You are a participant in the figure-matching experiment. Follow the user's instructions exactly."
        circle_history = circle_recent_messages if circle_recent_messages is not None else conversation_history
        last_own_message = get_last_own_message(agent_name, conversation_history)
        already_shared_full_list = has_shared_figures(agent_name, conversation_history, my_symbols)
        user_prompt = build_circle_prompt(
            agent_name,
            my_symbols,
            circle_history,
            num_agents,
            current_round,
            can_answer,
            circle_neighbors,
            preferred_neighbor,
            already_shared_full_list,
            last_own_message,
        )
    else:
        system_prompt = f"""
You are {agent_name}, one of {num_agents} agents in a figure-matching experiment.

Your figures:
{symbols_str}

Goal:
Find the one figure shared by all agents.

Rules:
- Use only your figures and received messages.
- First share your full figure list.
- If no figure has been proposed, propose one possible common figure only if it is in your list and appears in another agent's message.
- Confirm another proposal only if that figure is in your list.
- Reject another proposal if that figure is not in your list.
- Rounds 1 and 2 are discussion only. Do not submit a final answer in those rounds.
- In round 3 and later, you may submit a final answer if you believe the group has enough evidence.
- Keep the message short.
- Do not repeat your previous message.
- Stay only inside the figure task.

Valid figures:
square, circle, triangle, diamond, cross, asterisk
"""

        history_text = ""
        for msg in conversation_history[-5:]:
            sender = msg.get("sender", "SYSTEM")
            text = msg.get("text", "")
            history_text += f"[{sender}]: {text}\n"

        last_own_message = get_last_own_message(agent_name, conversation_history)
        shared_figures = "yes" if has_shared_figures(agent_name, conversation_history, my_symbols) else "no"

        user_prompt = f"""
CURRENT STATE:
- You are: {agent_name}
- Total agents: {num_agents}
- Current round: {current_round}
- Final answer allowed now: {"yes" if can_answer else "no"}
- Your figures: {figures_list}
- You already shared your figures: {shared_figures}
- Your previous message: {last_own_message}

RECENT PUBLIC MESSAGES:
"""

        if history_text:
            user_prompt += history_text
        else:
            user_prompt += "(No public messages yet — you are going first.)\n"

        if can_answer:
            user_prompt += """
YOUR TURN:
This is the answer stage.
You may continue discussion or submit a final answer if you believe the group has enough evidence.

Use one of:

ACTION: CHAT
MESSAGE: <short message>

or

ACTION: ANSWER
WORD: <figure>
"""
        else:
            user_prompt += """
YOUR TURN:
This is the discussion stage.
You are not allowed to submit a final answer yet.
Continue discussion: share figures, compare overlap, propose, confirm, or reject.

Use only:

ACTION: CHAT
MESSAGE: <your message>
"""

    # Non-streaming generation keeps parsing logic simple and deterministic.
    payload = {
        "model": MODEL_NAME,
        "system": system_prompt,
        "prompt": user_prompt,
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
        resp = requests.post(f"{OLLAMA_URL}/api/generate", json=payload, timeout=120)
        resp.raise_for_status()
        raw = resp.json().get("response", "")
        if not raw.strip():
            print("[OLLAMA WARN] Empty response from model.")
            print("[OLLAMA DEBUG] Prompt sent to model:")
            print(user_prompt or system_prompt)
    except Exception as e:
        print(f"[OLLAMA ERROR] {e}")
        return {"action": "chat", "text": f"(error: {e})"}

    print(f"[MODEL RAW] {raw}")

    # ---- Parse the model's structured response ----
    if topology == "circle":
        return parse_circle_response(raw, agent_name, circle_neighbors)
    return classify_agent_response(raw)


# Decides whether the agent’s response is a chat message or answer.
def classify_agent_response(raw):
    """
    Parse enough to identify ACTION: CHAT or ACTION: ANSWER.
    Does not rewrite the model's wording.
    Falls back to treating the whole thing as a chat message.
    """
    raw_upper = raw.upper()

    if "ACTION: ANSWER" in raw_upper or "ACTION:ANSWER" in raw_upper:
        word = ""
        for line in raw.split("\n"):
            line_stripped = line.strip()
            upper = line_stripped.upper()
            if upper.startswith("WORD:") or upper.startswith("SYMBOL:"):
                word = line_stripped.split(":", 1)[1].strip().strip("` '\"")
                break
        return {"action": "answer", "word": word, "raw": raw}

    if "ACTION: CHAT" in raw_upper or "ACTION:CHAT" in raw_upper:
        for line in raw.split("\n"):
            line_stripped = line.strip()
            if line_stripped.upper().startswith("MESSAGE:"):
                msg = line_stripped.split(":", 1)[1].strip()
                return {"action": "chat", "text": msg, "raw": raw}

    return {"action": "chat", "text": raw, "raw": raw}


def get_last_own_message(agent_name, conversation_history):
    for msg in reversed(conversation_history):
        if msg.get("sender") == agent_name:
            return msg.get("text", "")
    return "none"


def has_shared_figures(agent_name, conversation_history, my_symbols):
    own_messages = [
        msg.get("text", "").lower()
        for msg in conversation_history
        if msg.get("sender") == agent_name
    ]
    return any(all(symbol.lower() in text for symbol in my_symbols) for text in own_messages)


def send_json(sock, payload):
    data = (json.dumps(payload) + "\n").encode("utf-8")
    sock.sendall(data)


def recv_json_line(sock, recv_buffer):
    while b"\n" not in recv_buffer:
        chunk = sock.recv(4096)
        if not chunk:
            return None, recv_buffer
        recv_buffer += chunk

    line, recv_buffer = recv_buffer.split(b"\n", 1)
    return json.loads(line.decode("utf-8")), recv_buffer


def main():
    ok, msg = check_ollama()
    if not ok:
        print(f"[STARTUP ERROR] {msg}")
        sys.exit(1)

    print("[STARTUP] Ollama check passed.")

    print("[STARTUP] Warming up model...")
    try:
        requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": "Say ready.",
                "stream": False,
                "keep_alive": 300,
                "options": {
                    "temperature": 0.0,
                    "num_predict": 5,
                },
            },
            timeout=120,
        )
        print("[STARTUP] Model warmup complete.")
    except Exception as e:
        print(f"[STARTUP WARN] Model warmup failed: {e}")

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
            topology = "broadcast"
            circle_neighbors = []
            recv_buffer = b""

            while True:
                msg, recv_buffer = recv_json_line(sock, recv_buffer)
                if msg is None:
                    print("[SERVER] Disconnected.")
                    break

                msg_type = msg.get("type")

                if msg_type == "nickname_request":
                    hostname = platform.node().split(".")[0].lower()
                    print(f"[SERVER] Nickname request. Sending hostname: {hostname}")
                    send_json(sock, {
                        "type": "nickname",
                        "hostname": hostname,
                    })

                elif msg_type == "welcome":
                    assigned_name = msg.get("agent_name")
                    if assigned_name:
                        agent_name = assigned_name
                        print(f"[SERVER] Assigned name: {agent_name}")

                elif msg_type == "experiment_start":
                    agent_name = msg["agent_name"]
                    my_symbols = msg["your_symbols"]
                    num_agents = msg.get("num_agents", num_agents)
                    topology = msg.get("topology", "broadcast")
                    circle_neighbors = msg.get("circle_neighbors", [])
                    print(f"\n[START] I am {agent_name}")
                    print(f"[START] My figures: {my_symbols}")
                    print(f"[START] Number of agents: {num_agents}")
                    print(f"[START] Topology: {topology}")
                    if topology == "circle":
                        print(f"[START] Circle neighbors: {circle_neighbors}")
                    conversation_history = []

                elif msg_type == "system":
                    text = msg.get("text", "")
                    print(f"[SYSTEM] {text}")
                    if topology != "circle":
                        conversation_history.append({"sender": "SYSTEM", "text": text})

                elif msg_type == "chat":
                    sender = msg.get("sender", "UNKNOWN")
                    text = msg.get("text", "")
                    print(f"[{sender}] {text}")
                    conversation_history.append({"sender": sender, "text": text})

                elif msg_type == "your_turn":
                    if not agent_name:
                        print("[WARN] No agent name assigned yet.")
                        send_json(sock, {"type": "chat", "text": "I am ready."})
                        continue

                    turn_topology = msg.get("topology", topology)
                    circle_recent_messages = None
                    preferred_neighbor = ""
                    if turn_topology == "circle":
                        agent_name = msg.get("agent_name", agent_name)
                        my_symbols = msg.get("your_symbols", my_symbols)
                        circle_neighbors = msg.get("circle_neighbors", circle_neighbors)
                        circle_recent_messages = msg.get("recent_messages", [])
                        preferred_neighbor = msg.get("preferred_neighbor", "")

                    current_round = msg.get("round", 1)
                    can_answer = bool(msg.get("can_answer", False))
                    server_prompt = msg.get("prompt")
                    decision = generate_agent_reply(
                        agent_name,
                        my_symbols,
                        conversation_history,
                        num_agents,
                        current_round,
                        can_answer,
                        turn_topology,
                        circle_neighbors,
                        server_prompt,
                        circle_recent_messages,
                        preferred_neighbor,
                    )

                    if decision.get("action") == "answer":
                        word = decision.get("word", "")
                        raw = decision.get("raw", "")
                        print(f"[SEND ANSWER ATTEMPT] {raw}")
                        send_json(sock, {"type": "answer", "word": word, "raw": raw})
                    else:
                        raw = decision.get("raw", "")
                        text = decision.get("text", "")
                        print(f"[SEND CHAT] {text}")
                        payload = {"type": "chat", "text": text, "raw": raw}
                        if turn_topology == "circle":
                            payload["target"] = decision.get("target", "")
                        conversation_history.append({"sender": agent_name, "text": text})
                        send_json(sock, payload)

                elif msg_type in ("result", "experiment_end"):
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
