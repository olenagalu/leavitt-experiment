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
import re
from circle_client import build_circle_prompt, parse_circle_response
from chain_client import build_chain_prompt, parse_chain_response
from y_client import build_y_prompt, parse_y_response
from wheel_client import build_wheel_prompt, parse_wheel_response

# ====================================================================== CONFIG
OLLAMA_URL = "http://127.0.0.1:11434"
MODEL_NAME = "gemma4:e2b-it-qat"
OLLAMA_TEMPERATURE = 0.2        # randomness; lower values make agents more deterministic
OLLAMA_TOP_P = 1.0              # word-choice pool; lower values reduce weird wording
OLLAMA_REPEAT_PENALTY = 1.0     # 1 = no penalty; higher values reduce repetitiveness
OLLAMA_NUM_PREDICT = 27         # maximum generated tokens; limits response length
SERVER_IP = "192.168.0.140"
SERVER_PORT = 5001
RECONNECT_DELAY_SECONDS = 5
VALID_FIGURES = {"square", "circle", "triangle", "diamond", "cross", "asterisk"}
# ====================================================================== OLLAMA


def normalize_figure_answer(value):
    text = str(value or "").strip().lower()
    text = re.sub(r"^[^a-z]+|[^a-z]+$", "", text)
    return text if text in VALID_FIGURES else ""


def extract_figure_answer(value):
    text = str(value or "")
    exact = normalize_figure_answer(text)
    if exact:
        return exact

    explicit = explicit_answer_from_message(text)
    if explicit:
        return explicit

    mentioned = []
    for figure in VALID_FIGURES:
        if text_mentions_figure(text, figure):
            mentioned.append(figure)
    return mentioned[0] if len(mentioned) == 1 else ""


def text_mentions_figure(text, figure):
    return bool(re.search(rf"\b{re.escape(figure)}\b", str(text or ""), flags=re.IGNORECASE))


def text_rules_out_figure(text, figure):
    lowered = str(text or "").lower()
    patterns = [
        rf"\b(?:do not|don't|dont|cannot|can't|cant)\s+have\s+{re.escape(figure)}\b",
        rf"\b{re.escape(figure)}\s+(?:is\s+)?not\s+in\s+(?:my|their|his|her)\s+list\b",
        rf"\bno\s+{re.escape(figure)}\b",
        rf"\bwithout\s+{re.escape(figure)}\b",
    ]
    return any(re.search(pattern, lowered) for pattern in patterns)


def active_private_figure(messages, my_symbols, agent_name=None, num_agents=None):
    private_figures = [normalize_figure_answer(symbol) for symbol in my_symbols]
    private_figures = [symbol for symbol in private_figures if symbol]
    support = {figure: set() for figure in private_figures}
    ruled_out = set()
    own_agent = normalize_agent_label(agent_name) if agent_name else ""
    total_agents = max(2, min(5, int(num_agents))) if num_agents else 2
    required_support = max(1, total_agents - 1)

    for msg in messages or []:
        sender = msg.get("sender", "") if isinstance(msg, dict) else ""
        normalized_sender = normalize_agent_label(sender)
        if own_agent and normalized_sender == own_agent:
            continue
        text = msg.get("text", "") if isinstance(msg, dict) else str(msg)
        for figure in private_figures:
            if text_rules_out_figure(text, figure):
                ruled_out.add(figure)
            if text_mentions_figure(text, figure):
                support[figure].add(normalized_sender or "unknown")

    candidates = [
        (len(senders), figure)
        for figure, senders in support.items()
        if len(senders) >= required_support and figure not in ruled_out
    ]
    if not candidates:
        return ""
    candidates.sort(reverse=True)
    return candidates[0][1]


def private_fallback_target(topology, preferred_target, circle_neighbors, chain_contacts, y_contacts, wheel_recipients):
    contacts_by_topology = {
        "circle": circle_neighbors,
        "chain": chain_contacts,
        "y": y_contacts,
        "wheel": wheel_recipients,
    }
    contacts = contacts_by_topology.get(topology, []) or []
    normalized_preferred = normalize_agent_label(preferred_target)
    for contact in contacts:
        if normalize_agent_label(contact) == normalized_preferred:
            return contact
    return contacts[0] if contacts else ""


def preferred_recipient_order(valid_recipients, preferred_target):
    contacts = list(valid_recipients or [])
    normalized_preferred = normalize_agent_label(preferred_target)
    preferred = [
        contact
        for contact in contacts
        if normalize_agent_label(contact) == normalized_preferred
    ]
    return preferred + [contact for contact in contacts if contact not in preferred]


def answer_without_figure_message(raw):
    lines = []
    for line in str(raw or "").splitlines():
        stripped = line.strip()
        upper = stripped.upper()
        if not stripped:
            continue
        if upper.startswith("ACTION:") or upper.startswith("WORD:") or upper.startswith("SYMBOL:"):
            continue
        lines.append(stripped)
    return " ".join(lines).strip() or "I need more evidence before submitting a final answer."


def raw_model_message(raw):
    return str(raw or "").strip() or "I need more evidence before submitting a final answer."


def explicit_answer_from_message(text):
    body = str(text or "")
    figure_words = "|".join(sorted(re.escape(figure) for figure in VALID_FIGURES))
    patterns = [
        r"\b(?:final\s+answer|answer|common\s+figure|shared\s+figure|common\s+symbol)\s*(?:is|:|should\s+be|may\s+be|might\s+be)\s+([a-z]+)\b",
        r"\b(?:submit|choose)\s+(?:ANSWER\s*:?\s*)?([a-z]+)\b",
        rf"\b({figure_words})\b\s+(?:is|seems|appears|looks|must\s+be|should\s+be|may\s+be|might\s+be)\s+(?:the\s+)?(?:common|shared)\s+(?:figure|symbol)\b",
        rf"\b({figure_words})\b\s+(?:is|seems|appears|looks|must\s+be|should\s+be|may\s+be|might\s+be)\s+(?:the\s+)?(?:one\s+)?shared\s+by\s+all\b",
        rf"\ball\s+(?:agents|of\s+us|of\s+them|participants)\s+(?:share|have)\s+({figure_words})\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, body, flags=re.IGNORECASE)
        if match:
            figure = normalize_figure_answer(match.group(1))
            if figure:
                return figure
    return ""


def normalize_ollama_options(options=None):
    options = options if isinstance(options, dict) else {}

    def number(name, fallback, minimum, maximum, integer=False):
        raw = options.get(name, fallback)
        try:
            selected = float(raw)
        except (TypeError, ValueError):
            print(f"[OLLAMA OPTIONS WARN] Invalid {name}={raw!r}; using fallback {fallback}.")
            selected = fallback
        if selected < minimum or selected > maximum:
            print(f"[OLLAMA OPTIONS WARN] Invalid {name}={raw!r}; using fallback {fallback}.")
            selected = fallback
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


def read_jetson_temperatures():
    """Read all Linux thermal-zone sensors available on this Jetson."""
    thermal_root = "/sys/class/thermal"
    sensors = {}
    try:
        zone_names = sorted(
            name for name in os.listdir(thermal_root)
            if name.startswith("thermal_zone")
        )
    except OSError:
        return sensors

    for zone_name in zone_names:
        zone_path = os.path.join(thermal_root, zone_name)
        try:
            with open(os.path.join(zone_path, "type"), "r", encoding="utf-8") as source:
                sensor_name = source.read().strip() or zone_name
            with open(os.path.join(zone_path, "temp"), "r", encoding="utf-8") as source:
                raw_temperature = float(source.read().strip())
        except (OSError, ValueError):
            continue
        temperature_c = raw_temperature / 1000 if abs(raw_temperature) >= 1000 else raw_temperature
        unique_name = sensor_name
        suffix = 2
        while unique_name in sensors:
            unique_name = f"{sensor_name}_{suffix}"
            suffix += 1
        sensors[unique_name] = round(temperature_c, 2)
    return sensors


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
    circle_shared_full_list_recipients=None,
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
        circle_history = circle_recent_messages or []
        last_own_message = get_last_own_message(agent_name, conversation_history)
        shared_recipients = [
            neighbor
            for neighbor in circle_neighbors
            if neighbor in (circle_shared_full_list_recipients or set())
        ]
        unshared_recipients = [
            neighbor
            for neighbor in circle_neighbors
            if neighbor not in shared_recipients
        ]
        already_shared_full_list = bool(circle_neighbors) and not unshared_recipients
        pending_question_text = format_pending_question(get_pending_question(agent_name, circle_history))
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
            shared_recipients,
            unshared_recipients,
            last_own_message,
            discussion_rounds,
            pending_question_text,
        )
    elif topology == "chain":
        system_prompt = "You are a participant in the figure-matching experiment. Follow the user's instructions exactly."
        chain_history = chain_recent_messages if chain_recent_messages is not None else conversation_history
        last_own_message = get_last_own_message(agent_name, conversation_history)
        already_shared_full_list = has_shared_figures(agent_name, conversation_history, my_symbols)
        pending_question_text = format_pending_question(get_pending_question(agent_name, conversation_history))
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
            pending_question_text,
        )
    elif topology == "y":
        system_prompt = "You are a participant in the figure-matching experiment. Follow the user's instructions exactly."
        y_history = y_recent_messages if y_recent_messages is not None else conversation_history
        last_own_message = get_last_own_message(agent_name, conversation_history)
        already_shared_full_list = has_shared_figures(agent_name, conversation_history, my_symbols)
        pending_question_text = format_pending_question(get_pending_question(agent_name, conversation_history))
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
            pending_question_text,
        )
    elif topology == "wheel":
        system_prompt = "You are a participant in the figure-matching experiment. Follow the user's instructions exactly."
        wheel_history = wheel_recent_messages if wheel_recent_messages is not None else conversation_history
        last_own_message = get_last_own_message(agent_name, conversation_history)
        already_shared_full_list = has_shared_figures(agent_name, conversation_history, my_symbols)
        pending_question_text = format_pending_question(get_pending_question(agent_name, conversation_history))
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
            pending_question_text,
        )
    else:
        system_prompt = f"""
You are {agent_name}, one of {num_agents} agents in a figure-matching experiment.

Your figures:
{symbols_str}

Goal:
Find the one figure shared by all agents.
Reach the correct answer using as few total messages across all agents as possible.

Rules:
- Keep the whole response under 77 tokens.
- Use only your figures and received messages.
- If you have not shared your full figure list yet, your next message should share only your full figure list.
- After that, compare received messages with your own list.
- If no figure has been proposed, propose one possible common figure only if it is in your list and appears in another agent's message.
- Confirm and submit ANSWER figure only if it is in your own list.
- If another agent proposes a figure that is not in your list, say you do not have it and redirect discussion toward figures that overlap with your list and received messages.
- Ask for missing figure lists only if needed.
- Do not submit ANSWER immediately.
- When final answers are allowed and you see the common figure, submit ANSWER for it instead of sending another confirmation.
- Do not submit ANSWER for a figure that is not in your own private list.
- Do not repeat your previous message.
- Stay only inside the figure task.

Valid figures:
Valid figures are only: asterisk, circle, cross, diamond, square, triangle.
"""

        recent_history = conversation_history[-15:]
        history_text = ""
        for msg in recent_history:
            sender = msg.get("sender", "SYSTEM")
            text = msg.get("text", "")
            history_text += f"[{sender}]: {text}\n"

        last_own_message = get_last_own_message(agent_name, conversation_history)

        user_prompt = f"""
Current state:

You are: {agent_name}
Your figures: {figures_list}
Final answer allowed: {"yes" if can_answer else "no"}
Previous message: {last_own_message}

Recent messages:
"""

        if history_text:
            user_prompt += history_text
        else:
            user_prompt += "(No public messages yet — you are going first.)\n"

        if can_answer:
            user_prompt += f"""
YOUR TURN:
You may send one message now.
Final answer is allowed.

Submit ANSWER when one figure in your own private list is clearly supported by messages from most agents.
Do not broadcast another confirmation when your evidence is strong enough to submit ANSWER.

If you are still discussing, write any short useful message.
If you are submitting the final answer, write ANSWER: one figure word and nothing else.

Final answer words you may use: {figures_list}
"""
        else:
            user_prompt += """
YOUR TURN:
You must send an informative discussion message now.
Do not submit ANSWER yet.

If you have not shared your full figure list yet, your next message should share it. Otherwise compare received messages with your own list, confirm or reject proposed figures, or ask for missing figure lists only if needed.

Write any short useful broadcast message. Do not use an answer-only figure word yet.
"""

    print(f"[OLLAMA OPTIONS USED] {selected_ollama_options}")

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

    # ---- Parse the model's strict response ----
    if topology == "circle":
        return parse_strict_response(
            raw,
            preferred_recipient_order(circle_neighbors, preferred_neighbor),
            infer_message_answers=False,
        )
    if topology == "chain":
        return parse_strict_response(raw, chain_contacts)
    if topology == "y":
        return parse_strict_response(raw, y_contacts)
    if topology == "wheel":
        return parse_strict_response(raw, wheel_recipients)
    return parse_strict_response(raw, ["BROADCAST"])


# Decides whether the agent’s response is a chat message or answer.
def parse_strict_response(raw, valid_recipients=None, infer_message_answers=True):
    """
    Parse the required output format:
      MESSAGE AgentX: text
      TO: AgentX
      MESSAGE: text
      BROADCAST: text
      ANSWER: figure

    Broadcast stays strict. Private-routing modes prefer the agent's chosen
    recipient, but fall back to the first allowed recipient when the model gives
    message text without a usable target.
    """
    valid_recipients = valid_recipients or []
    text = str(raw or "").strip()
    first_nonempty = next((line.strip() for line in text.splitlines() if line.strip()), "")
    if not first_nonempty:
        return {"action": "invalid", "raw": raw}

    bare_figure = normalize_figure_answer(first_nonempty)
    if bare_figure:
        return {"action": "answer", "word": bare_figure, "raw": raw}

    answer_match = re.match(r"ANSWER\s*:\s*(.+)$", first_nonempty, flags=re.IGNORECASE)
    if answer_match:
        return {"action": "answer", "word": extract_figure_answer(answer_match.group(1)), "raw": raw}
    answer_match = re.match(r"ANSWER\b\s+(.+)$", first_nonempty, flags=re.IGNORECASE)
    if answer_match:
        return {"action": "answer", "word": extract_figure_answer(answer_match.group(1)), "raw": raw}
    if re.match(r"ACTION\s*:\s*ANSWER\b", first_nonempty, flags=re.IGNORECASE):
        for line in text.splitlines():
            word_match = re.match(r"\s*(WORD|SYMBOL)\s*:\s*(.+)$", line, flags=re.IGNORECASE)
            if word_match:
                return {"action": "answer", "word": extract_figure_answer(word_match.group(2)), "raw": raw}
        return {"action": "invalid", "raw": raw}

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    has_message_intent = any(
        re.match(r"(MESSAGE|BROADCAST|TO|ACTION\s*:\s*CHAT)\b", line, flags=re.IGNORECASE)
        for line in lines
    )
    if not has_message_intent:
        for line in lines:
            labeled_answer = re.match(
                r"(?:FINAL\s+ANSWER|ANSWER|WORD|SYMBOL)\s*:?\s*(.+)?$",
                line,
                flags=re.IGNORECASE,
            )
            if labeled_answer:
                word = extract_figure_answer(labeled_answer.group(1) or "")
                if word:
                    return {"action": "answer", "word": word, "raw": raw}
        for line in lines:
            bare_line_figure = normalize_figure_answer(line)
            if bare_line_figure:
                return {"action": "answer", "word": bare_line_figure, "raw": raw}

    if valid_recipients == ["BROADCAST"]:
        broadcast_match = re.match(r"BROADCAST\s*:\s*(.+)$", first_nonempty, flags=re.IGNORECASE)
        if broadcast_match:
            return {
                "action": "chat",
                "target": "ALL",
                "text": broadcast_match.group(1).strip(),
                "raw": raw,
                "target_source": "agent",
                "original_target": "ALL",
            }
        broadcast_match = re.match(r"BROADCAST\b\s*[-–]?\s*(.+)$", first_nonempty, flags=re.IGNORECASE)
        if broadcast_match:
            return {
                "action": "chat",
                "target": "ALL",
                "text": broadcast_match.group(1).strip(),
                "raw": raw,
                "target_source": "client_recovered_format",
                "original_target": "ALL",
            }
        if re.match(r"ACTION\s*:\s*CHAT\b", first_nonempty, flags=re.IGNORECASE):
            for line in text.splitlines():
                message_match = re.match(r"\s*MESSAGE\s*:\s*(.+)$", line, flags=re.IGNORECASE)
                if message_match:
                    return {
                        "action": "chat",
                        "target": "ALL",
                        "text": message_match.group(1).strip(),
                        "raw": raw,
                        "target_source": "client_recovered_format",
                        "original_target": "ALL",
                    }
        message_match = re.match(r"MESSAGE\s*:\s*(.+)$", first_nonempty, flags=re.IGNORECASE)
        if message_match:
            return {
                "action": "chat",
                "target": "ALL",
                "text": message_match.group(1).strip(),
                "raw": raw,
                "target_source": "client_recovered_format",
                "original_target": "ALL",
            }
        for line in text.splitlines()[1:]:
            answer_match = re.match(r"\s*ANSWER\s*:?\s*(.+)$", line, flags=re.IGNORECASE)
            if answer_match:
                return {"action": "answer", "word": extract_figure_answer(answer_match.group(1)), "raw": raw}
            broadcast_match = re.match(r"\s*(BROADCAST|MESSAGE)\s*:?\s*(.+)$", line, flags=re.IGNORECASE)
            if broadcast_match:
                return {
                    "action": "chat",
                    "target": "ALL",
                    "text": broadcast_match.group(2).strip(),
                    "raw": raw,
                    "target_source": "client_recovered_format",
                    "original_target": "ALL",
                }
        if first_nonempty:
            return {
                "action": "chat",
                "target": "ALL",
                "text": text,
                "raw": raw,
                "target_source": "client_recovered_plain_text",
                "original_target": "ALL",
            }
        return {"action": "invalid", "raw": raw}

    normalized_recipients = {
        normalize_agent_label(recipient): recipient
        for recipient in valid_recipients
        }

    raw_target = ""
    message_text = ""

    message_match = re.match(r"MESSAGE\s+([^:]+)\s*:\s*(.+)$", first_nonempty, flags=re.IGNORECASE)
    if message_match:
        raw_target = message_match.group(1).strip()
        message_text = message_match.group(2).strip()
    else:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        for index, line in enumerate(lines):
            upper = line.upper()
            if upper.startswith("TO:"):
                raw_target = line.split(":", 1)[1].strip()
                inline_message = re.search(r"\bMESSAGE\s*:\s*(.+)$", raw_target, flags=re.IGNORECASE)
                if inline_message:
                    message_text = inline_message.group(1).strip()
                    raw_target = raw_target[:inline_message.start()].strip()
            elif upper.startswith("MESSAGE:"):
                message_text = line.split(":", 1)[1].strip()
                if not message_text:
                    message_text = " ".join(
                        extra
                        for extra in lines[index + 1:]
                        if not re.match(r"^(ACTION|TO|WORD|SYMBOL)\s*:", extra, flags=re.IGNORECASE)
                    ).strip()

        if not raw_target:
            target_match = re.search(
                r"\bTO\s*:\s*(.*?)(?=\s+MESSAGE\s*:|$)",
                text,
                flags=re.IGNORECASE | re.DOTALL,
            )
            if target_match:
                raw_target = target_match.group(1).strip()
                inline_message = re.search(r"\bMESSAGE\s*:\s*(.+)$", raw_target, flags=re.IGNORECASE | re.DOTALL)
                if inline_message:
                    message_text = inline_message.group(1).strip()
                    raw_target = raw_target[:inline_message.start()].strip()

        if not message_text:
            message_match_anywhere = re.search(r"\bMESSAGE\s*:\s*(.+)$", text, flags=re.IGNORECASE | re.DOTALL)
            if message_match_anywhere:
                message_text = message_match_anywhere.group(1).strip()

    if not message_text and text:
        message_text = text

    if message_text:
        # Circle mode often uses phrases like "shared by all" as discussion
        # evidence. Only non-circle modes recover those chat sentences as answers.
        # Bare figure words and explicit ANSWER formats are still handled above.
        if infer_message_answers:
            explicit_answer = explicit_answer_from_message(message_text)
            if explicit_answer:
                return {"action": "answer", "word": explicit_answer, "raw": raw}

        normalized_target = normalize_agent_label(raw_target)
        target = normalized_recipients.get(normalized_target)
        target_source = "agent"
        if target is None and valid_recipients:
            target = valid_recipients[0]
            target_source = "client_default" if not raw_target else "client_default_invalid"
        if target is None:
            return {"action": "invalid", "raw": raw}
        return {
            "action": "chat",
            "target": target,
            "text": message_text,
            "raw": raw,
            "target_source": target_source,
            "original_target": raw_target,
        }

    return {"action": "invalid", "raw": raw}


def normalize_agent_label(name):
    stripped = str(name).strip()
    if stripped.upper() == "ALL":
        return "ALL"
    cleaned = re.sub(r"[^\w\s]", "", stripped)
    match = re.fullmatch(r"agent\s*(\d+)", cleaned, flags=re.IGNORECASE)
    if match:
        return f"Agent{int(match.group(1))}"
    return stripped


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

    return {"action": "invalid", "raw": raw}


def get_last_own_message(agent_name, conversation_history):
    for msg in reversed(conversation_history):
        if msg.get("sender") == agent_name:
            return msg.get("text", "")
    return "none"


def get_pending_question(agent_name, conversation_history):
    normalized_agent = normalize_agent_label(agent_name)
    agent_number_match = re.fullmatch(r"Agent(\d+)", normalized_agent)
    agent_pattern = (
        rf"\bAgent\s*{agent_number_match.group(1)}\b"
        if agent_number_match
        else rf"\b{re.escape(normalized_agent)}\b"
    )
    for msg in reversed(conversation_history):
        sender = msg.get("sender", "")
        text = msg.get("text", "")
        if sender == agent_name:
            return None
        if "?" not in text:
            continue
        asks_this_agent = (
            re.search(agent_pattern, text, flags=re.IGNORECASE)
            or re.search(r"\byou\b|\byour\b", text, flags=re.IGNORECASE)
            or not re.search(r"\bAgent\s*\d+\b", text, flags=re.IGNORECASE)
        )
        if asks_this_agent:
            return {"sender": sender, "text": text}
    return None


def format_pending_question(pending_question):
    if not pending_question:
        return "none"
    return f'{pending_question.get("sender", "UNKNOWN")} asked: {pending_question.get("text", "")}'


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
            circle_shared_full_list_recipients = set()
            ollama_options = normalize_ollama_options()
            recv_buffer = b""
            trial_active = False
            current_trial_id = None

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
                        "model_name": MODEL_NAME,
                    })

                elif msg_type == "welcome":
                    assigned_name = msg.get("agent_name")
                    if assigned_name:
                        agent_name = assigned_name
                        print(f"[SERVER] Assigned name: {agent_name}")

                elif msg_type == "restart_client":
                    restart_process(sock)

                elif msg_type == "temperature_request":
                    temperatures = read_jetson_temperatures()
                    send_json(sock, {
                        "type": "temperature_report",
                        "request_id": msg.get("request_id"),
                        "agent_name": agent_name,
                        "recorded_at": time.time(),
                        "temperatures_c": temperatures,
                        "max_temperature_c": max(temperatures.values()) if temperatures else None,
                    })

                elif msg_type == "experiment_start":
                    trial_active = True
                    current_trial_id = msg.get("trial_id")
                    conversation_history = []
                    circle_shared_full_list_recipients = set()
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
                    print("[START] Trial progress: total messages, no discussion rounds")
                    if topology == "circle":
                        print(f"[START] Circle neighbors: {circle_neighbors}")
                    if topology == "chain":
                        print(f"[START] Chain contacts: {chain_contacts}")
                    if topology == "y":
                        print(f"[START] Y contacts: {y_contacts}")
                    if topology == "wheel":
                        print(f"[START] Wheel recipients: {wheel_recipients}")
                    print(f"[START] Ollama options: {ollama_options}")

                elif msg_type == "system":
                    text = msg.get("text", "")
                    print(f"[SYSTEM] {text}")
                    if trial_active and topology not in ("circle", "chain", "y", "wheel"):
                        conversation_history.append({"sender": "SYSTEM", "text": text})

                elif msg_type == "chat":
                    if msg.get("trial_id") != current_trial_id:
                        print(
                            f"[STALE CHAT IGNORED] trial_id={msg.get('trial_id')!r}; "
                            f"current={current_trial_id!r}."
                        )
                        continue
                    sender = msg.get("sender", "UNKNOWN")
                    text = msg.get("text", "")
                    print(f"[{sender}] {text}")
                    if not trial_active:
                        print("[STALE CHAT IGNORED] No active trial.")
                        continue
                    conversation_history.append({"sender": sender, "text": text})

                elif msg_type == "reset_chat_history":
                    if current_trial_id is not None and msg.get("trial_id") != current_trial_id:
                        print(
                            f"[STALE RESET IGNORED] trial_id={msg.get('trial_id')!r}; "
                            f"current={current_trial_id!r}."
                        )
                        continue
                    conversation_history = []
                    circle_shared_full_list_recipients = set()
                    print("[ROUND] Chat history reset for new round.")

                elif msg_type == "your_turn":
                    if msg.get("trial_id") != current_trial_id:
                        print(
                            f"[STALE TURN IGNORED] trial_id={msg.get('trial_id')!r}; "
                            f"current={current_trial_id!r}."
                        )
                        continue
                    if not trial_active:
                        print("[STALE TURN IGNORED] No active trial.")
                        continue
                    if not agent_name:
                        print("[WARN] No agent name assigned yet.")
                        send_json(sock, {
                            "type": "chat",
                            "trial_id": current_trial_id,
                            "text": "I am ready.",
                        })
                        continue

                    turn_topology = msg.get("topology", topology)
                    if msg.get("reset_chat_history") and conversation_history:
                        conversation_history = []
                        print("[ROUND] Chat history reset for new round.")
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

                    current_round = msg.get("message_count", msg.get("round", 0))
                    can_answer = bool(msg.get("can_answer", True))
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
                        circle_shared_full_list_recipients,
                        ollama_options,
                    )

                    private_target = private_fallback_target(
                        turn_topology,
                        {
                            "circle": preferred_neighbor,
                            "chain": preferred_chain_contact,
                            "y": preferred_y_contact,
                            "wheel": preferred_wheel_recipient,
                        }.get(turn_topology, ""),
                        circle_neighbors,
                        chain_contacts,
                        y_contacts,
                        wheel_recipients,
                    )

                    if decision.get("action") == "answer":
                        raw_word = decision.get("word", "")
                        word = extract_figure_answer(raw_word)
                        raw = decision.get("raw", "")
                        print(f"[SEND ANSWER ATTEMPT] {raw}")
                        if not can_answer and turn_topology != "circle":
                            text = raw_model_message(raw)
                            if turn_topology in ("circle", "chain", "y", "wheel") and private_target:
                                print(f"[EARLY ANSWER FALLBACK CHAT] {agent_name} -> {private_target}: {text}")
                                conversation_history.append({"sender": agent_name, "text": f"To {private_target}: {text}"})
                                send_json(sock, {
                                    "type": "chat",
                                    "trial_id": current_trial_id,
                                    "target": private_target,
                                    "text": text,
                                    "raw": raw,
                                    "target_source": "client_assigned",
                                    "original_target": decision.get("target", ""),
                                })
                            else:
                                print(f"[EARLY ANSWER FALLBACK CHAT] {text}")
                                conversation_history.append({"sender": agent_name, "text": text})
                                send_json(sock, {
                                    "type": "chat",
                                    "trial_id": current_trial_id,
                                    "text": text,
                                    "raw": raw,
                                })
                            continue
                        if not word:
                            text = raw_model_message(raw)
                            if turn_topology in ("circle", "chain", "y", "wheel") and private_target:
                                print(f"[ANSWER FALLBACK CHAT] {agent_name} -> {private_target}: {text}")
                                conversation_history.append({"sender": agent_name, "text": f"To {private_target}: {text}"})
                                send_json(sock, {
                                    "type": "chat",
                                    "trial_id": current_trial_id,
                                    "target": private_target,
                                    "text": text,
                                    "raw": raw,
                                    "target_source": "client_assigned",
                                    "original_target": decision.get("target", ""),
                                })
                                continue
                            print(f"[ANSWER FALLBACK CHAT] {text}")
                            conversation_history.append({"sender": agent_name, "text": text})
                            send_json(sock, {
                                "type": "chat",
                                "trial_id": current_trial_id,
                                "text": text,
                                "raw": raw,
                            })
                            continue
                        send_json(sock, {
                            "type": "answer",
                            "trial_id": current_trial_id,
                            "word": word,
                            "raw": raw,
                        })
                    elif decision.get("action") == "invalid":
                        raw = decision.get("raw", "")
                        if turn_topology in ("circle", "chain", "y", "wheel") and private_target:
                            text = raw_model_message(raw)
                            print(f"[INVALID FALLBACK CHAT] {agent_name} -> {private_target}: {text}")
                            conversation_history.append({"sender": agent_name, "text": f"To {private_target}: {text}"})
                            send_json(sock, {
                                "type": "chat",
                                "trial_id": current_trial_id,
                                "target": private_target,
                                "text": text,
                                "raw": raw,
                                "target_source": "client_assigned",
                                "original_target": decision.get("original_target", ""),
                            })
                            continue
                        print("[SEND INVALID OUTPUT]")
                        send_json(sock, {
                            "type": "invalid",
                            "trial_id": current_trial_id,
                            "raw": raw,
                        })
                    else:
                        raw = decision.get("raw", "")
                        text = decision.get("text", "")
                        if turn_topology in ("circle", "chain", "y", "wheel"):
                            target = decision.get("target", "")
                            print(f"{agent_name} -> {target}: {text}")
                        else:
                            print(f"[SEND CHAT] {text}")
                        payload = {
                            "type": "chat",
                            "trial_id": current_trial_id,
                            "text": text,
                            "raw": raw,
                        }
                        if turn_topology in ("circle", "chain", "y", "wheel"):
                            payload["target"] = decision.get("target", "")
                        if turn_topology in ("circle", "chain", "y", "wheel"):
                            payload["target_source"] = decision.get("target_source", "")
                            payload["original_target"] = decision.get("original_target", "")
                        own_text = (
                            f"To {decision.get('target', '')}: {text}"
                            if turn_topology in ("circle", "chain", "y", "wheel")
                            else text
                        )
                        conversation_history.append({"sender": agent_name, "text": own_text})
                        if (
                            turn_topology == "circle"
                            and target
                            and all(symbol.lower() in text.lower() for symbol in my_symbols)
                        ):
                            circle_shared_full_list_recipients.add(target)
                        send_json(sock, payload)

                elif msg_type in ("result", "experiment_end"):
                    if msg.get("trial_id") != current_trial_id:
                        print(
                            f"[STALE RESULT IGNORED] trial_id={msg.get('trial_id')!r}; "
                            f"current={current_trial_id!r}."
                        )
                        continue
                    print("\n[RESULT]")
                    print(json.dumps(msg, indent=2))
                    trial_active = False
                    current_trial_id = None
                    conversation_history = []
                    circle_shared_full_list_recipients = set()
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
