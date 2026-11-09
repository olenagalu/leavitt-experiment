"""
Chain-topology helpers for client.py.

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


def build_chain_prompt(
    agent_name,
    my_symbols,
    conversation_history,
    num_agents,
    current_round,
    can_answer,
    chain_contacts,
    preferred_contact=None,
    already_shared_full_list=False,
    last_own_message="none",
    discussion_rounds=None,
    pending_question_text="none",
):
    symbols_str = ", ".join(my_symbols)
    figures_list = ", ".join(my_symbols)
    recipients_text = ", ".join(chain_contacts)
    fallback_recipient = preferred_contact or (random.choice(chain_contacts) if chain_contacts else "")
    history_text = format_history(conversation_history)

    if len(chain_contacts) == 1:
        return f"""
{intro_section(agent_name, num_agents, symbols_str)}

Chain topology:

* You can send one private message per turn.
* You may send it only to this valid recipient: {recipients_text}.
* Only this recipient will see your message.
* You may pass useful information between your recipient and the rest of the chain.

{discussion_rules(recipients_text, can_answer, recipient_scope="your allowed recipient", tell_target="your allowed recipient")}

{current_state(agent_name, figures_list, recipients_text, fallback_recipient, already_shared_full_list, last_own_message, pending_question_text, allowed_label="Allowed recipient", include_suggested=False)}

{recent_messages_section(history_text)}

{output_format(recipients_text, figures_list, can_answer, exact_recipient=True)}
"""

    return f"""
{intro_section(agent_name, num_agents, symbols_str)}

Chain topology:

* You can send one private message per turn.
* You may send it only to one of these valid recipients: {recipients_text}.
* You choose which valid recipient receives your CHAT message.
* If your response does not include a valid recipient, the system will choose one allowed recipient for this turn.
* Only the selected recipient will see your message.
* You may pass useful information from one allowed recipient to the other allowed recipient.

{discussion_rules(recipients_text, can_answer)}

{current_state(agent_name, figures_list, recipients_text, fallback_recipient, already_shared_full_list, last_own_message, pending_question_text)}

{recent_messages_section(history_text)}

{output_format(recipients_text, figures_list, can_answer)}
"""


def parse_chain_response(raw, agent_name, chain_contacts):
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
    normalized_contacts = {
        normalize_agent_name(contact): contact
        for contact in chain_contacts
    }

    if DEBUG:
        print(f"[DEBUG] Extracted TO target from {agent_name}: {raw_target}")
        print(f"[DEBUG] Normalized TO target from {agent_name}: {normalized_target}")

    if not raw_target:
        if DEBUG:
            print(f"[WARN] No TO target from {agent_name}.")
        return {"action": "invalid", "raw": raw}
    elif normalized_target not in normalized_contacts:
        original_target = raw_target
        if DEBUG:
            print(f"[WARN] Invalid TO target from {agent_name}: {original_target}.")
        return {"action": "invalid", "raw": raw}
    else:
        target = normalized_contacts[normalized_target]
        target_source = "agent"

    if DEBUG:
        print(f"[DEBUG] Final selected TO target from {agent_name}: {target}")

    if not text:
        text = raw

    return {
        "action": "chat",
        "target": target,
        "text": text,
        "raw": raw,
        "target_source": target_source,
        "original_target": raw_target,
    }
