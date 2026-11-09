"""
Wheel-topology helpers for client.py.

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


def get_wheel_recipients(agent_name):
    recipients_by_agent = {
        "Agent1": ["Agent3"],
        "Agent2": ["Agent3"],
        "Agent3": ["Agent1", "Agent2", "Agent4", "Agent5"],
        "Agent4": ["Agent3"],
        "Agent5": ["Agent3"],
    }
    return recipients_by_agent.get(normalize_agent_name(agent_name), [])


def build_wheel_prompt(
    agent_name,
    my_symbols,
    conversation_history,
    num_agents,
    current_round,
    can_answer,
    wheel_recipients=None,
    preferred_recipient=None,
    already_shared_full_list=False,
    last_own_message="none",
    discussion_rounds=None,
    pending_question_text="none",
):
    symbols_str = ", ".join(my_symbols)
    figures_list = ", ".join(my_symbols)
    wheel_recipients = wheel_recipients or get_wheel_recipients(agent_name)
    recipients_text = ", ".join(wheel_recipients)
    fallback_recipient = preferred_recipient or (random.choice(wheel_recipients) if wheel_recipients else "")
    normalized_agent = normalize_agent_name(agent_name)
    history_text = format_history(conversation_history)

    if normalized_agent == "Agent3":
        return f"""
{intro_section("Agent3", num_agents, symbols_str)}

Wheel topology:

* You are the central agent.
* You can send messages to Agent1, Agent2, Agent4, or Agent5.
* Agent1, Agent2, Agent4, and Agent5 can send messages only to you.
* You can send one private message per turn.
* You may send it only to one of these valid recipients: {recipients_text}.
* You choose which valid recipient receives your CHAT message.
* If your response does not include a valid recipient, the system will choose one allowed recipient for this turn.
* Only the selected recipient will see your message.
* You may pass useful information from one allowed recipient to the other allowed recipients.
* Collect information from Agent1, Agent2, Agent4, and Agent5.
* Wait until you have received the full figure lists from Agent1, Agent2, Agent4, and Agent5.
* Compare all four received lists with your own list.
* Find the one figure that appears in all five agents' lists.
* Submit that figure.


{discussion_rules(recipients_text, can_answer)}

{current_state("Agent3", figures_list, recipients_text, fallback_recipient, already_shared_full_list, last_own_message, pending_question_text)}

{recent_messages_section(history_text)}

{output_format(recipients_text, figures_list, can_answer)}
"""

    return f"""
{intro_section(agent_name, num_agents, symbols_str)}

Wheel topology:

* Agent3 is the central agent.
* You can send messages only to Agent3.
* Agent3 can send messages to Agent1, Agent2, Agent4, or Agent5.
* You can send one private message per turn.
* You may send it only to this valid recipient: Agent3.
* If your response does not include Agent3 as the recipient, the system will choose Agent3 for this turn.
* Only Agent3 will see your message.
* Agent3 may pass your useful information to the other agents.
* Let Agent3 find the common figure and submit the final answer because Agent3 is the central node.

{discussion_rules("Agent3", can_answer, recipient_scope="Agent3", tell_target="Agent3")}

{current_state(agent_name, figures_list, "Agent3", "Agent3", already_shared_full_list, last_own_message, pending_question_text, allowed_label="Allowed recipient")}

{recent_messages_section(history_text)}

{output_format("Agent3", figures_list, can_answer, exact_recipient=True)}
"""


def parse_wheel_response(raw, agent_name, wheel_recipients):
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
    normalized_recipients = {
        normalize_agent_name(recipient): recipient
        for recipient in wheel_recipients
    }

    if DEBUG:
        print(f"[DEBUG] Extracted TO target from {agent_name}: {raw_target}")
        print(f"[DEBUG] Normalized TO target from {agent_name}: {normalized_target}")

    if not raw_target:
        if DEBUG:
            print(f"[WARN] No TO target from {agent_name}.")
        return {"action": "invalid", "raw": raw}
    elif normalized_target not in normalized_recipients:
        original_target = raw_target
        if DEBUG:
            print(f"[WARN] Invalid TO target from {agent_name}: {original_target}.")
        return {"action": "invalid", "raw": raw}
    else:
        target = normalized_recipients[normalized_target]
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
