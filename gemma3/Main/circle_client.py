"""
Circle-topology helpers for client.py.

This module is imported by client.py and is not intended to run directly.
"""

import random
import re

from shared_features_client import current_state, discussion_rules, format_history, intro_section, output_format, recent_messages_section


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
    unshared_full_list_recipients = unshared_full_list_recipients or []
    suggested_recipient = unshared_full_list_recipients[0] if unshared_full_list_recipients else fallback_recipient
    history_text = format_history(conversation_history)

    return f"""
{intro_section(agent_name, num_agents, symbols_str)}

Ring topology:
- You can send one private message per turn.
- You may send it only to one of these valid recipients: {recipients_text}.
- You choose which valid recipient receives your CHAT message.
- If your response does not include a valid recipient, the system will choose one allowed recipient for this turn.
- Only the selected recipient will see your message.
- You may pass useful information from one allowed recipient to the other allowed recipient.

{discussion_rules(recipients_text, can_answer)}

{current_state(agent_name, figures_list, recipients_text, suggested_recipient, already_shared_full_list, last_own_message, pending_question_text)}

{recent_messages_section(history_text)}

{output_format(recipients_text, figures_list, can_answer)}
"""


def parse_circle_response(raw, agent_name, circle_neighbors):
    raw_upper = raw.upper()
    first_nonempty = next((line.strip() for line in raw.splitlines() if line.strip()), "")

    def clean_answer_word(value):
        return value.strip().strip("` '\".,;:")

    def is_one_word(value):
        return bool(re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", clean_answer_word(value)))

    def last_one_word_line():
        for line in reversed(raw.splitlines()):
            line_stripped = line.strip()
            if is_one_word(line_stripped):
                return clean_answer_word(line_stripped)
        return ""

    answer_match = re.match(r"ANSWER\s*:\s*(.+)$", first_nonempty, flags=re.IGNORECASE)
    if answer_match:
        word = clean_answer_word(answer_match.group(1))
        return {"action": "answer", "word": word, "raw": raw}

    if "ACTION: ANSWER" in raw_upper or "ACTION:ANSWER" in raw_upper:
        word = ""
        for line in raw.split("\n"):
            line_stripped = line.strip()
            upper = line_stripped.upper()
            if upper.startswith("WORD:") or upper.startswith("SYMBOL:") or upper.startswith("MESSAGE:"):
                word = clean_answer_word(line_stripped.split(":", 1)[1])
                break
        if not word:
            word = last_one_word_line()
        return {"action": "answer", "word": word, "raw": raw}

    if is_one_word(first_nonempty):
        return {"action": "answer", "word": clean_answer_word(first_nonempty), "raw": raw}

    if "MESSAGE:" not in raw_upper:
        routed_answer_word = last_one_word_line()
        if routed_answer_word and re.search(r"\bTO\s*:", raw, flags=re.IGNORECASE):
            return {"action": "answer", "word": routed_answer_word, "raw": raw}

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
