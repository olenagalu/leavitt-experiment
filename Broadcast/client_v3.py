"""
client - v3 
"""

# imports
import socket
import json
import sys
import time
import requests

# ====================================================================== CONFIG
OLLAMA_URL = "http://127.0.0.1:11434"
MODEL_NAME = "gemma3:4b"
# ====================================================================== OLLAMA

def check_ollama():
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


def query_model(agent_name, my_symbols, conversation_history):
    """
    Ask model to either share information, reason about the common symbol,
    or submit a final answer.

    Returns a dict: {"action": "chat", "text": "..."} or {"action": "answer", "word": "square"}
    """

    symbols_str = "  ".join(my_symbols)

    history_text = ""
    for msg in conversation_history[-15:]:
        sender = msg.get("sender", "SYSTEM")
        text = msg.get("text", "")
        history_text += f"[{sender}]: {text}\n"

    system_prompt = f"""You are {agent_name}, participating in a symbol-matching experiment.

YOUR SYMBOLS: {symbols_str}

TASK: There is exactly ONE symbol that both you and the other agent share. Find it.

RULES:
- You can see only YOUR symbols. You cannot see the other agent's symbols.
- On your turn you must do ONE of two things:
  OPTION A: Share information or ask a question. Respond with:
    ACTION: CHAT
    MESSAGE: <your message to the other agent>
  OPTION B: Submit your final answer (only when you are confident). Respond with:
    ACTION: ANSWER
    WORD: <the full common figure word>

STRATEGY:
- Start by telling the other agent what symbols you have.
- When the other agent shares their symbols, compare with yours.
- The common symbol is the one that appears in BOTH lists.
- Once you identify it, submit the full word (for example: square, not just s).

IMPORTANT:
- Always use the exact format above (ACTION: CHAT/ANSWER).
- Keep messages short and direct.
- Only submit ANSWER when you are sure."""

    user_prompt = "Here is the conversation so far:\n\n"
    if history_text:
        user_prompt += history_text
    else:
        user_prompt += "(No messages yet — you are going first.)\n"
    user_prompt += "\nIt is your turn. Respond with ACTION: CHAT or ACTION: ANSWER."

    payload = {
        "model": MODEL_NAME,
        "system": system_prompt,
        "prompt": user_prompt,
        "stream": False,
        "keep_alive": 300,
    }

    try:
        resp = requests.post(f"{OLLAMA_URL}/api/generate", json=payload, timeout=120)
        resp.raise_for_status()
        raw = resp.json().get("response", "").strip()
    except Exception as e:
        print(f"[OLLAMA ERROR] {e}")
        return {"action": "chat", "text": f"(error: {e})"}

    print(f"[MODEL RAW] {raw}")

    # ---- Parse the model's structured response ----
    return parse_model_response(raw)


def parse_model_response(raw):
    """
    Parse the ACTION: CHAT/ANSWER format from the model output.
    Falls back to treating the whole thing as a chat message.
    """
    raw_upper = raw.upper()

    # Check for ANSWER
    if "ACTION: ANSWER" in raw_upper or "ACTION:ANSWER" in raw_upper:
        # Prefer WORD:, support SYMBOL: for backward compatibility.
        for line in raw.split("\n"):
            line_stripped = line.strip()
            upper = line_stripped.upper()
            if upper.startswith("WORD:") or upper.startswith("SYMBOL:"):
                word = line_stripped.split(":", 1)[1].strip().strip("` '\"")
                if len(word) > 0:
                    return {"action": "answer", "word": word}

        # Fallback: look for a lone symbol character in the response
        # This handles cases where the model says "The answer is #"
        return {"action": "chat", "text": raw}

    # Check for CHAT
    if "ACTION: CHAT" in raw_upper or "ACTION:CHAT" in raw_upper:
        for line in raw.split("\n"):
            line_stripped = line.strip()
            if line_stripped.upper().startswith("MESSAGE:"):
                msg = line_stripped.split(":", 1)[1].strip()
                return {"action": "chat", "text": msg}

    # Fallback: treat the entire output as a chat message
    return {"action": "chat", "text": raw}


# ================================================================ NETWORKING

def send_json(sock, msg_dict):
    raw = json.dumps(msg_dict) + "\n"
    sock.sendall(raw.encode("utf-8"))


def recv_json(sock, timeout=None):
    if timeout:
        sock.settimeout(timeout)
    try:
        data = sock.recv(8192)
        if not data:
            return None
        return json.loads(data.decode("utf-8").strip())
    except socket.timeout:
        return {"type": "timeout"}
    except (json.JSONDecodeError, ConnectionResetError, OSError):
        return None
    finally:
        sock.settimeout(None)


# ================================================================ AGENT

class LeavittAgent:
    def __init__(self, server_host, server_port, name):
        self.server_host = server_host
        self.server_port = server_port
        self.name = name
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_symbols = []
        self.conversation_history = []
        self.running = True
        self.answered = False

    def connect(self):
        print(f"[{self.name}] Connecting to {self.server_host}:{self.server_port}...")
        try:
            self.sock.connect((self.server_host, self.server_port))
            print(f"[{self.name}] Connected!")
        except ConnectionRefusedError:
            print(f"[{self.name}] ERROR: Server not reachable.")
            return
        except Exception as e:
            print(f"[{self.name}] Connection error: {e}")
            return

        try:
            self._main_loop()
        except KeyboardInterrupt:
            print(f"\n[{self.name}] Interrupted.")
        finally:
            self.sock.close()
            print(f"[{self.name}] Disconnected.")

    def _main_loop(self):
        while self.running:
            msg = recv_json(self.sock, timeout=300)

            if msg is None:
                print(f"[{self.name}] Lost connection.")
                break

            msg_type = msg.get("type", "")

            # ---- Handshake ----
            if msg_type == "nickname_request":
                send_json(self.sock, {"type": "nickname", "name": self.name})

            elif msg_type == "welcome":
                print(f"[{self.name}] {msg.get('text', '')}")

            # ---- Experiment starts — receive our symbols ----
            elif msg_type == "experiment_start":
                self.my_symbols = msg.get("your_symbols", [])
                num_agents = msg.get("num_agents", 2)
                print(f"[{self.name}] EXPERIMENT START")
                print(f"[{self.name}] My symbols: {self.my_symbols}")
                print(f"[{self.name}] Agents in experiment: {num_agents}")

            # ---- System message ----
            elif msg_type == "system":
                text = msg.get("text", "")
                print(f"[{self.name}] SYSTEM: {text}")
                self.conversation_history.append({"sender": "SYSTEM", "text": text})

            # ---- Chat from other agent ----
            elif msg_type == "chat":
                sender = msg.get("sender", "?")
                text = msg.get("text", "")
                print(f"[{self.name}] {sender}: {text}")
                self.conversation_history.append({"sender": sender, "text": text})

            # ---- Our turn ----
            elif msg_type == "your_turn":
                if self.answered:
                    send_json(self.sock, {"type": "chat", "text": "I have already submitted my answer."})
                    continue

                print(f"[{self.name}] >>> Thinking...")
                t0 = time.time()

                result = query_model(self.name, self.my_symbols, self.conversation_history)

                elapsed = time.time() - t0
                print(f"[{self.name}] >>> Decision ({elapsed:.1f}s): {result}")

                if result["action"] == "answer":
                    word = result["word"]
                    send_json(self.sock, {"type": "answer", "word": word})
                    self.answered = True
                    self.conversation_history.append({
                        "sender": self.name,
                        "text": f"[SUBMITTED ANSWER: {word}]",
                    })
                else:
                    text = result.get("text", "...")
                    send_json(self.sock, {"type": "chat", "text": text})
                    self.conversation_history.append({"sender": self.name, "text": text})

            # ---- Experiment over ----
            elif msg_type == "experiment_end":
                res = msg.get("result", "?")
                sym = msg.get("common_word", msg.get("common_symbol", "?"))
                answers = msg.get("answers", {})
                t = msg.get("time_seconds", 0)
                msgs = msg.get("total_messages", 0)

                print(f"\n[{self.name}] ========== EXPERIMENT COMPLETE ==========")
                print(f"[{self.name}]   Result:        {res.upper()}")
                print(f"[{self.name}]   Common symbol: {sym}")
                print(f"[{self.name}]   All answers:   {answers}")
                print(f"[{self.name}]   Time:          {t}s")
                print(f"[{self.name}]   Messages:      {msgs}")
                print(f"[{self.name}] =========================================\n")
                self.running = False

            elif msg_type == "timeout":
                continue


# ====================================================================== CLI

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python leavitt_client.py <server_host> <server_port> [agent_name]")
        print("Example: python leavitt_client.py 192.168.1.100 5000 AgentAlpha")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    name = sys.argv[3] if len(sys.argv) >= 4 else f"Agent_{int(time.time()) % 10000}"

    print(f"[INIT] Agent:  {name}")
    print(f"[INIT] Model:  {MODEL_NAME}")
    print(f"[INIT] Checking Ollama...")

    ok, status = check_ollama()
    if not ok:
        print(f"[INIT] FAILED: {status}")
        sys.exit(1)
    print(f"[INIT] Ollama OK")

    agent = LeavittAgent(server_host, server_port, name)
    agent.connect()
