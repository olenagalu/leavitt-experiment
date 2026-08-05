"""
Y-topology helpers for client.py.

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


def build_y_prompt(
    agent_name,
    my_symbols,
    conversation_history,
    num_agents,
    current_round,
    can_answer,
    y_contacts,
    preferred_contact=None,
    already_shared_full_list=False,
    last_own_message="none",
    discussion_rounds=None,
    pending_question_text="none",
):
    symbols_str = ", ".join(my_symbols)
    figures_list = ", ".join(my_symbols)
    recipients_text = ", ".join(y_contacts)
    fallback_recipient = preferred_contact or (random.choice(y_contacts) if y_contacts else "")
    history_text = format_history(conversation_history)
    normalized_agent = normalize_agent_name(agent_name)

    if normalized_agent in ("Agent1", "Agent2", "Agent5"):
        only_recipient = y_contacts[0] if y_contacts else fallback_recipient
        if normalized_agent == "Agent5":
            route_rule = "* Send your full figure list and useful evidence to Agent4 so it can reach Agent3."
        else:
            route_rule = "* Send your full figure list and useful evidence to Agent3."
        return f"""
{intro_section(agent_name, num_agents, symbols_str)}

Y topology:

* You are an end agent.
* You can send messages only to {only_recipient}.
* You can send one private message per turn.
* You may send it only to this valid recipient: {only_recipient}.
* If your response does not include {only_recipient} as the recipient, the system will choose {only_recipient} for this turn.
* Only {only_recipient} will see your message.
* {only_recipient} may pass your useful information to other agents.

Role-specific rules:
{route_rule}
* Let Agent3 compare the lists and submit the final answer.

{discussion_rules(only_recipient, can_answer, recipient_scope=only_recipient, tell_target=only_recipient)}

{current_state(agent_name, figures_list, only_recipient, only_recipient, already_shared_full_list, last_own_message, pending_question_text, allowed_label="Allowed recipient")}

{recent_messages_section(history_text)}

{output_format(only_recipient, figures_list, can_answer, exact_recipient=True)}
"""

    if normalized_agent == "Agent3":
        return f"""
{intro_section("Agent3", num_agents, symbols_str)}

Y topology:

* You are the central agent.
* You can send messages to Agent1, Agent2, or Agent4.
* Agent1 and Agent2 can send messages only to you.
* Agent4 can send messages to you or Agent5.
* You can send one private message per turn.
* You may send it only to one of these valid recipients: {recipients_text}.
* You choose which valid recipient receives your CHAT message.
* If your response does not include a valid recipient, the system will choose one allowed recipient for this turn.
* Only the selected recipient will see your message.
* You may pass useful information from one allowed recipient to the other allowed recipients.
* Information from Agent5 can reach you only through Agent4.

Role-specific rules:
* Collect figure information from Agent1, Agent2, and Agent4.
* Compare the received lists with your own list and submit the shared figure when confirmed.

{discussion_rules(recipients_text, can_answer)}

{current_state("Agent3", figures_list, recipients_text, fallback_recipient, already_shared_full_list, last_own_message, pending_question_text)}

{recent_messages_section(history_text)}

{output_format(recipients_text, figures_list, can_answer)}
"""

    return f"""
{intro_section("Agent4", num_agents, symbols_str)}

Y topology:

* You connect Agent3 and Agent5.
* You can send messages to Agent3 or Agent5.
* Agent3 can send messages to Agent1, Agent2, or you.
* Agent5 can send messages only to you.
* You can send one private message per turn.
* You may send it only to one of these valid recipients: {recipients_text}.
* You choose which valid recipient receives your CHAT message.
* If your response does not include a valid recipient, the system will choose one allowed recipient for this turn.
* Only the selected recipient will see your message.
* You may pass useful information from Agent3 to Agent5 or from Agent5 to Agent3.
* Information between Agent5 and the other agents must pass through you.

Role-specific rules:
* Pass your own and Agent5's useful figure information to Agent3.
* Pass Agent3's useful information back to Agent5 when needed.

{discussion_rules(recipients_text, can_answer)}

{current_state("Agent4", figures_list, recipients_text, fallback_recipient, already_shared_full_list, last_own_message, pending_question_text)}

{recent_messages_section(history_text)}

{output_format(recipients_text, figures_list, can_answer)}
"""


def parse_y_response(raw, agent_name, y_contacts):
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
        for contact in y_contacts
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
