"""
LEAVITT - CLIENT  
"""

# imports
import socket
import json
import os
import sys
import time
import requests
import platform
from circle_client import build_circle_prompt, parse_circle_response
from chain_client import build_chain_prompt, parse_chain_response
from y_client import build_y_prompt, parse_y_response
from wheel_client import build_wheel_prompt, parse_wheel_response

# ====================================================================== CONFIG
OLLAMA_URL = "http://127.0.0.1:11434"
MODEL_NAME = "gemma3:4b"
OLLAMA_TEMPERATURE = 0.2
OLLAMA_TOP_P = 0.7              # fewer weird word choices, the smaller number -> more repetetive but less words
OLLAMA_REPEAT_PENALTY = 1.3     # less looping/repeating
OLLAMA_NUM_PREDICT = 70         # limits response length
SERVER_IP = "192.168.0.140"
SERVER_PORT = 5001
RECONNECT_DELAY_SECONDS = 5
# ====================================================================== OLLAMA

def normalize_ollama_options(options=None):
    options = options if isinstance(options, dict) else {}

    def number(name, fallback, minimum, maximum, integer=False):
        try:
            selected = float(options.get(name, fallback))
        except (TypeError, ValueError):
            selected = fallback
        selected = max(minimum, min(maximum, selected))
        return int(round(selected)) if integer else round(selected, 3)

    return {
        "temperature": number("temperature", OLLAMA_TEMPERATURE, 0, 2),
        "top_p": number("top_p", OLLAMA_TOP_P, 0, 1),
        "repeat_penalty": number("repeat_penalty", OLLAMA_REPEAT_PENALTY, 0, 3),
        "num_predict": number("num_predict", OLLAMA_NUM_PREDICT, 1, 300, integer=True),
    }

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
    discussion_rounds=None,
    chain_contacts=None,
    chain_recent_messages=None,
    preferred_chain_contact=None,
    y_contacts=None,
    y_recent_messages=None,
    preferred_y_contact=None,
    wheel_recipients=None,
    wheel_recent_messages=None,
    preferred_wheel_recipient=None,
    ollama_options=None,
):
    """
    Ask model to discuss possible common symbols or answer when allowed.

    Returns a dict with action, parsed fields, and the raw model response.
    """

    symbols_str = "  ".join(my_symbols)
    figures_list = ", ".join(my_symbols)
    circle_neighbors = circle_neighbors or []
    chain_contacts = chain_contacts or []
    y_contacts = y_contacts or []
    wheel_recipients = wheel_recipients or []
    selected_ollama_options = normalize_ollama_options(ollama_options)

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
            discussion_rounds,
        )
    elif topology == "chain":
        system_prompt = "You are a participant in the figure-matching experiment. Follow the user's instructions exactly."
        chain_history = chain_recent_messages if chain_recent_messages is not None else conversation_history
        last_own_message = get_last_own_message(agent_name, conversation_history)
        already_shared_full_list = has_shared_figures(agent_name, conversation_history, my_symbols)
        user_prompt = build_chain_prompt(
            agent_name,
            my_symbols,
            chain_history,
            num_agents,
            current_round,
            can_answer,
            chain_contacts,
            preferred_chain_contact,
            already_shared_full_list,
            last_own_message,
            discussion_rounds,
        )
    elif topology == "y":
        system_prompt = "You are a participant in the figure-matching experiment. Follow the user's instructions exactly."
        y_history = y_recent_messages if y_recent_messages is not None else conversation_history
        last_own_message = get_last_own_message(agent_name, conversation_history)
        already_shared_full_list = has_shared_figures(agent_name, conversation_history, my_symbols)
        user_prompt = build_y_prompt(
            agent_name,
            my_symbols,
            y_history,
            num_agents,
            current_round,
            can_answer,
            y_contacts,
            preferred_y_contact,
            already_shared_full_list,
            last_own_message,
            discussion_rounds,
        )
    elif topology == "wheel":
        system_prompt = "You are a participant in the figure-matching experiment. Follow the user's instructions exactly."
        wheel_history = wheel_recent_messages if wheel_recent_messages is not None else conversation_history
        last_own_message = get_last_own_message(agent_name, conversation_history)
        already_shared_full_list = has_shared_figures(agent_name, conversation_history, my_symbols)
        user_prompt = build_wheel_prompt(
            agent_name,
            my_symbols,
            wheel_history,
            num_agents,
            current_round,
            can_answer,
            wheel_recipients,
            preferred_wheel_recipient,
            already_shared_full_list,
            last_own_message,
            discussion_rounds,
        )
    else:
        try:
            discussion_rounds = int(discussion_rounds)
        except (TypeError, ValueError):
            discussion_rounds = 3
        discussion_rounds = max(0, discussion_rounds)
        answer_start_round = discussion_rounds + 1
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
- Rounds 1 through {discussion_rounds} are discussion only. Do not submit a final answer in those rounds.
- Round {answer_start_round} and later is answer-allowed mode. You may either continue discussion or submit a final answer.
- Submit a final answer only if one figure is clearly supported by the messages.
- If unsure, continue discussion.
- Do not repeat your previous message.
- Stay only inside the figure task.

Valid figures:
Valid figures are only: square, circle, triangle, diamond, cross, asterisk.
"""

        history_text = ""
        for msg in conversation_history[-5:]:
            sender = msg.get("sender", "SYSTEM")
            text = msg.get("text", "")
            history_text += f"[{sender}]: {text}\n"

        last_own_message = get_last_own_message(agent_name, conversation_history)
        shared_figures = "yes" if has_shared_figures(agent_name, conversation_history, my_symbols) else "no"

        turn_mode = "answer" if can_answer else "discussion"

        user_prompt = f"""
CURRENT STATE:
- You are: {agent_name}
- Total agents: {num_agents}
- Current round: {current_round}
- Turn mode: {turn_mode}
- Discussion-only rounds: {discussion_rounds}
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
Final answer is allowed now, but not required.

If one figure is clearly supported, submit it as the final answer.
If evidence is still missing or more than one figure is possible, continue discussion.

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
This is discussion mode.
You must continue the discussion.
Do not submit a final answer yet.

Share useful information, compare figure lists, respond to questions, confirm or reject possible candidates, and narrow the possible common figure.

Use only:

ACTION: CHAT
MESSAGE: <short message>
"""

    user_prompt += f"""
Response length:
- Limit each message to {selected_ollama_options["num_predict"]} tokens or fewer.
"""

    # Non-streaming generation keeps parsing logic simple and deterministic.
    payload = {
        "model": MODEL_NAME,
        "system": system_prompt,
        "prompt": user_prompt,
        "stream": False,
        "keep_alive": 300,
        "options": {
            "temperature": selected_ollama_options["temperature"],
            "top_p": selected_ollama_options["top_p"],
            "repeat_penalty": selected_ollama_options["repeat_penalty"],
            "num_predict": selected_ollama_options["num_predict"],
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
    if topology == "chain":
        return parse_chain_response(raw, agent_name, chain_contacts)
    if topology == "y":
        return parse_y_response(raw, agent_name, y_contacts)
    if topology == "wheel":
        return parse_wheel_response(raw, agent_name, wheel_recipients)
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


def restart_process(sock=None):
    print("[RESTART] Restart requested by dashboard. Restarting client process...", flush=True)
    if sock is not None:
        try:
            sock.close()
        except Exception:
            pass
    os.execv(sys.executable, [sys.executable] + sys.argv)


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
            chain_contacts = []
            y_contacts = []
            wheel_recipients = []
            ollama_options = normalize_ollama_options()
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

                elif msg_type == "restart_client":
                    restart_process(sock)

                elif msg_type == "experiment_start":
                    agent_name = msg["agent_name"]
                    my_symbols = msg["your_symbols"]
                    num_agents = msg.get("num_agents", num_agents)
                    topology = msg.get("topology", "broadcast")
                    circle_neighbors = msg.get("circle_neighbors", [])
                    chain_contacts = msg.get("chain_contacts", msg.get("chain_neighbors", []))
                    y_contacts = msg.get("y_contacts", [])
                    wheel_recipients = msg.get("wheel_recipients", [])
                    ollama_options = normalize_ollama_options(msg.get("ollama_options", ollama_options))
                    discussion_rounds = msg.get("discussion_rounds")
                    print(f"\n[START] I am {agent_name}")
                    print(f"[START] My figures: {my_symbols}")
                    print(f"[START] Number of agents: {num_agents}")
                    print(f"[START] Topology: {topology}")
                    print(f"[START] Discussion-only rounds: {discussion_rounds}")
                    if topology == "circle":
                        print(f"[START] Circle neighbors: {circle_neighbors}")
                    if topology == "chain":
                        print(f"[START] Chain contacts: {chain_contacts}")
                    if topology == "y":
                        print(f"[START] Y contacts: {y_contacts}")
                    if topology == "wheel":
                        print(f"[START] Wheel recipients: {wheel_recipients}")
                    print(f"[START] Ollama options: {ollama_options}")
                    conversation_history = []

                elif msg_type == "system":
                    text = msg.get("text", "")
                    print(f"[SYSTEM] {text}")
                    if topology not in ("circle", "chain", "y", "wheel"):
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
                    chain_recent_messages = None
                    y_recent_messages = None
                    wheel_recent_messages = None
                    preferred_neighbor = ""
                    preferred_chain_contact = ""
                    preferred_y_contact = ""
                    preferred_wheel_recipient = ""
                    discussion_rounds = msg.get("discussion_rounds")
                    if turn_topology == "circle":
                        agent_name = msg.get("agent_name", agent_name)
                        my_symbols = msg.get("your_symbols", my_symbols)
                        circle_neighbors = msg.get("circle_neighbors", circle_neighbors)
                        circle_recent_messages = msg.get("recent_messages", [])
                        preferred_neighbor = msg.get("preferred_neighbor", "")
                        if discussion_rounds is None:
                            answer_allowed_from_round = msg.get("answer_allowed_from_round")
                            if answer_allowed_from_round is not None:
                                try:
                                    discussion_rounds = max(0, int(answer_allowed_from_round) - 1)
                                except (TypeError, ValueError):
                                    discussion_rounds = None
                    elif turn_topology == "chain":
                        agent_name = msg.get("agent_name", agent_name)
                        my_symbols = msg.get("your_symbols", my_symbols)
                        chain_contacts = msg.get("chain_contacts", msg.get("chain_neighbors", chain_contacts))
                        chain_recent_messages = msg.get("recent_messages", [])
                        preferred_chain_contact = msg.get("preferred_contact", msg.get("preferred_neighbor", ""))
                        if discussion_rounds is None:
                            answer_allowed_from_round = msg.get("answer_allowed_from_round")
                            if answer_allowed_from_round is not None:
                                try:
                                    discussion_rounds = max(0, int(answer_allowed_from_round) - 1)
                                except (TypeError, ValueError):
                                    discussion_rounds = None
                    elif turn_topology == "y":
                        agent_name = msg.get("agent_name", agent_name)
                        my_symbols = msg.get("your_symbols", my_symbols)
                        y_contacts = msg.get("y_contacts", y_contacts)
                        y_recent_messages = msg.get("recent_messages", [])
                        preferred_y_contact = msg.get("preferred_contact", msg.get("preferred_neighbor", ""))
                        if discussion_rounds is None:
                            answer_allowed_from_round = msg.get("answer_allowed_from_round")
                            if answer_allowed_from_round is not None:
                                try:
                                    discussion_rounds = max(0, int(answer_allowed_from_round) - 1)
                                except (TypeError, ValueError):
                                    discussion_rounds = None
                    elif turn_topology == "wheel":
                        agent_name = msg.get("agent_name", agent_name)
                        my_symbols = msg.get("your_symbols", my_symbols)
                        wheel_recipients = msg.get("wheel_recipients", wheel_recipients)
                        wheel_recent_messages = msg.get("recent_messages", [])
                        preferred_wheel_recipient = msg.get("preferred_recipient", msg.get("preferred_neighbor", ""))
                        if discussion_rounds is None:
                            answer_allowed_from_round = msg.get("answer_allowed_from_round")
                            if answer_allowed_from_round is not None:
                                try:
                                    discussion_rounds = max(0, int(answer_allowed_from_round) - 1)
                                except (TypeError, ValueError):
                                    discussion_rounds = None
                    else:
                        discussion_rounds = msg.get("discussion_rounds", discussion_rounds)

                    current_round = msg.get("round", 1)
                    can_answer = bool(msg.get("can_answer", False))
                    server_prompt = msg.get("prompt")
                    ollama_options = normalize_ollama_options(msg.get("ollama_options", ollama_options))
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
                        discussion_rounds,
                        chain_contacts,
                        chain_recent_messages,
                        preferred_chain_contact,
                        y_contacts,
                        y_recent_messages,
                        preferred_y_contact,
                        wheel_recipients,
                        wheel_recent_messages,
                        preferred_wheel_recipient,
                        ollama_options,
                    )

                    if decision.get("action") == "answer":
                        word = decision.get("word", "")
                        raw = decision.get("raw", "")
                        print(f"[SEND ANSWER ATTEMPT] {raw}")
                        send_json(sock, {"type": "answer", "word": word, "raw": raw})
                    else:
                        raw = decision.get("raw", "")
                        text = decision.get("text", "")
                        if turn_topology in ("chain", "y", "wheel"):
                            target = decision.get("target", "")
                            print(f"{agent_name} -> {target}: {text}")
                        else:
                            print(f"[SEND CHAT] {text}")
                        payload = {"type": "chat", "text": text, "raw": raw}
                        if turn_topology in ("circle", "chain", "y", "wheel"):
                            payload["target"] = decision.get("target", "")
                        if turn_topology in ("chain", "y", "wheel"):
                            payload["target_source"] = decision.get("target_source", "")
                            payload["original_target"] = decision.get("original_target", "")
                        conversation_history.append({"sender": agent_name, "text": text})
                        send_json(sock, payload)

                elif msg_type in ("result", "experiment_end"):
                    print("\n[RESULT]")
                    print(json.dumps(msg, indent=2))
                    conversation_history = []
                    my_symbols = []
                    circle_neighbors = []
                    chain_contacts = []
                    y_contacts = []
                    wheel_recipients = []
                    print("[SERVER] Waiting for next trial start...")
                    continue

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
