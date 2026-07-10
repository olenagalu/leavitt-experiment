"""
Circle-topology helpers for client.py.

This module is imported by client.py and is not intended to run directly.
"""

import random
import re


DEBUG = False
def normalize_agent_name(name):
    stripped = str(name).strip()
    cleaned = re.sub(r"[^\w\s]", "", stripped)
    match = re.fullmatch(r"agent\s*(\d+)", cleaned, flags=re.IGNORECASE)
    if match:
        return f"Agent{int(match.group(1))}"
    return stripped


def build_circle_prompt(
    agent_name,
    my_symbols,
    conversation_history,
    num_agents,
    current_round,
    can_answer,
    circle_neighbors,
    preferred_neighbor=None,
    already_shared_full_list=False,
    shared_full_list_recipients=None,
    unshared_full_list_recipients=None,
    last_own_message="none",
    discussion_rounds=None,
    pending_question_text="none",
):
    symbols_str = ", ".join(my_symbols)
    figures_list = ", ".join(my_symbols)
    recipients_text = ", ".join(circle_neighbors)
    fallback_recipient = preferred_neighbor or (random.choice(circle_neighbors) if circle_neighbors else "")
    shared_full_list_recipients = shared_full_list_recipients or []
    unshared_full_list_recipients = unshared_full_list_recipients or []
    suggested_recipient = (
        unshared_full_list_recipients[0]
        if unshared_full_list_recipients
        else fallback_recipient
    )

    history_text = ""
    for msg in conversation_history[-15:]:
        sender = msg.get("sender", "SYSTEM")
        text = msg.get("text", "")
        history_text += f"[{sender}]: {text}\n"

    if not history_text:
        history_text = "(No received messages yet.)\n"

    return f"""
You are {agent_name}, one of {num_agents} agents in a figure-matching experiment.

Your figures:
{symbols_str}

Goal:
Find the one figure shared by all {num_agents} agents.

You may do exactly one action:
MESSAGE recipient: message
final answer: one figure word only

Valid chat recipients: {recipients_text}

Rules:
- Keep the whole response under 77 tokens.
- Before sending message, choose one valid recipient from: {recipients_text}.
- Use only your private figures and messages received from allowed recipients.
- Only the selected recipient sees your discussion message.
- If you have not shared your full figure list yet, your next message should share only your full figure list.
- After that, compare received messages with your own list.
- If no figure has been proposed, propose one possible common figure only if it is in your list and appears in another agent's message.
- Confirm and submit ANSWER figure only if it is in your own list.
- If another agent proposes a figure that is not in your list, say you do not have it and redirect discussion toward figures that overlap with your list and received messages.
- Do not submit ANSWER immediately.
- When you see the common figure, submit ANSWER for it instead of sending another confirmation.
- Do not submit ANSWER for a figure that is not in your own private list.
- Do not repeat your previous message.
- Stay only inside the figure task.



Current state:

You are: {agent_name}
Your figures: {figures_list}
Final answer allowed: {"yes" if can_answer else "no"}
Allowed recipients: {recipients_text}
Suggested recipient for this turn if you need a default: {suggested_recipient}
Previous message: {last_own_message}

Recent messages:
{history_text}

Output exactly one line and nothing else.
For discussion, use: MESSAGE <one of: {recipients_text}>: <short useful message>
For final ANSWER, use only one of these figure words: {figures_list}
"""


def parse_circle_response(raw, agent_name, circle_neighbors):
    raw_upper = raw.upper()
    first_nonempty = next((line.strip() for line in raw.splitlines() if line.strip()), "")
    answer_match = re.match(r"ANSWER\s*:\s*(.+)$", first_nonempty, flags=re.IGNORECASE)
    if answer_match:
        word = answer_match.group(1).strip().strip("` '\"")
        return {"action": "answer", "word": word, "raw": raw}

    if "ACTION: ANSWER" in raw_upper or "ACTION:ANSWER" in raw_upper:
        word = ""
        for line in raw.split("\n"):
            line_stripped = line.strip()
            upper = line_stripped.upper()
            if upper.startswith("WORD:") or upper.startswith("SYMBOL:"):
                word = line_stripped.split(":", 1)[1].strip().strip("` '\"")
                break
        return {"action": "answer", "word": word, "raw": raw}

    raw_target = ""
    text = ""
    message_target_match = re.match(
        r"\s*MESSAGE\s+(Agent\s*\d+)\s*:\s*(.+)$",
        raw,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if message_target_match:
        raw_target = message_target_match.group(1).strip()
        text = message_target_match.group(2).strip()

    lines = raw.split("\n")
    for index, line in enumerate(lines):
        if raw_target and text:
            break
        line_stripped = line.strip()
        upper = line_stripped.upper()
        if upper.startswith("TO:"):
            raw_target = line_stripped.split(":", 1)[1].strip()
            message_index = raw_target.upper().find("MESSAGE:")
            if message_index != -1:
                text = raw_target[message_index + len("MESSAGE:"):].strip()
                raw_target = raw_target[:message_index].strip()
            continue
        elif upper.startswith("MESSAGE:"):
            text = line_stripped.split(":", 1)[1].strip()
            if not text:
                remaining = []
                for extra_line in lines[index + 1:]:
                    extra_stripped = extra_line.strip()
                    extra_upper = extra_stripped.upper()
                    if (
                        extra_upper.startswith("ACTION:")
                        or extra_upper.startswith("TO:")
                        or extra_upper.startswith("WORD:")
                        or extra_upper.startswith("SYMBOL:")
                    ):
                        break
                    if extra_stripped:
                        remaining.append(extra_stripped)
                text = "\n".join(remaining).strip()
            break

    if not raw_target:
        target_match = re.search(
            r"\bTO\s*:\s*(.*?)(?=\s+MESSAGE\s*:|$)",
            raw,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if target_match:
            raw_target = target_match.group(1).strip()

    if not text and "MESSAGE:" in raw_upper:
        message_index = raw_upper.find("MESSAGE:")
        text = raw[message_index + len("MESSAGE:"):].strip()

    if not text:
        text = raw

    normalized_target = normalize_agent_name(raw_target)
    normalized_neighbors = {
        normalize_agent_name(neighbor): neighbor
        for neighbor in circle_neighbors
    }

    if DEBUG:
        print(f"[DEBUG] Extracted TO target from {agent_name}: {raw_target}")
        print(f"[DEBUG] Normalized TO target from {agent_name}: {normalized_target}")

    if not raw_target:
        target = random.choice(circle_neighbors) if circle_neighbors else ""
        if DEBUG:
            print(f"[WARN] No TO target from {agent_name}. Defaulted to {target}.")
    elif normalized_target not in normalized_neighbors:
        original_target = raw_target
        target = random.choice(circle_neighbors) if circle_neighbors else ""
        if DEBUG:
            print(f"[WARN] Invalid TO target from {agent_name}: {original_target}. Defaulted to {target}.")
    else:
        target = normalized_neighbors[normalized_target]

    if DEBUG:
        print(f"[DEBUG] Final selected TO target from {agent_name}: {target}")

    if not text:
        text = raw

    return {"action": "chat", "target": target, "text": text, "raw": raw}
