"""
Y-topology helpers for client.py.

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
    preferred_text = fallback_recipient or "choose one valid recipient"
    shared_full_list_text = "yes" if already_shared_full_list else "no"
    recent_sources_text = ", ".join(y_contacts) if y_contacts else "VALID RECIPIENTS"
    normalized_agent = normalize_agent_name(agent_name)
    if normalized_agent == "Agent3":
        role_text = "the junction agent"
        movement_rule = "Agent1 and Agent2 can only reach the group through you. Agent5 can only be reached through Agent4."
    elif normalized_agent == "Agent4":
        role_text = "the bridge agent"
        movement_rule = "Agent5 can only reach the group through you. Help useful information move between Agent3 and Agent5."
    elif len(y_contacts) == 1:
        role_text = "an endpoint agent"
        movement_rule = "Information from the rest of the group must come through your valid recipient."
    else:
        role_text = "an agent"
        movement_rule = "Help useful information move through your part of the Y."

    history_text = ""
    for msg in conversation_history[-15:]:
        sender = msg.get("sender", "SYSTEM")
        text = msg.get("text", "")
        history_text += f"[{sender}]: {text}\n"

    if not history_text:
        history_text = "(No received messages yet.)\n"

    answer_priority = (
        f"7. Submit ANSWER only as one of your own figure words ({figures_list}) and only when that figure has support from received messages as the strongest common candidate."
        if can_answer
        else "7. Do not submit ANSWER yet. Send one useful discussion message instead."
    )
    answer_rule = (
        "* Submit ANSWER only when one figure in your own private list is clearly supported by received messages."
        if can_answer
        else "* Do not submit ANSWER yet. Keep sharing or comparing useful figure information."
    )
    answer_output = (
        f"""
or:

ACTION: ANSWER
WORD: <one of: {figures_list}>
"""
        if can_answer
        else ""
    )

    turn_block = f"""
YOUR TURN:
You must send exactly one valid message or answer this turn. Do not stay silent.

Decision priority:
1. You are {agent_name}. Speak only as {agent_name}.
2. If "Question you should answer now" is not none, send a private reply to the agent who asked that question.
3. If you have not shared your full private figure list yet, send your full private figure list to one valid recipient.
4. After your full private figure list has been shared, compare received messages with your own list and send one useful discussion message.
5. If a discussed or proposed figure is not in your private list, reject it and redirect discussion toward figures that overlap with your own list and received messages.
6. If a discussed or proposed figure is in your private list, confirm it or pass that useful information to another valid recipient.
{answer_priority}
8. You must output exactly one valid action this turn. Do not stay silent.

Output exactly one:

ACTION: CHAT
TO: <one of: {recipients_text}>
MESSAGE: <short useful message>
{answer_output}
Do not copy these instructions or placeholder words into your response.
"""

    return f"""
You are {agent_name}. Speak only as {agent_name}.
You are {role_text} in a Y topology.

Your figures:
{symbols_str}

Goal:
Find the one figure shared by all agents.
Reach the correct answer using as few total messages across all agents as possible.

Your valid recipients:
{recipients_text}

Y topology:
* You can send only one private message per turn.
* You choose exactly one valid Y recipient for each CHAT message: {recipients_text}.
* If your response does not include a valid recipient, the system will choose one allowed recipient for this turn.
* Only the selected recipient will see your message.
* You cannot talk directly to agents outside your valid recipients.
* {movement_rule}
* Do not assume that all agents saw every message.

Rules:
* Use only your figures and messages you received.
* If "Question you should answer now" is not none, send your message to the agent who asked and answer that question first.
* Share your full figure list with a recipient only once.
* After you already shared your full list with someone, do not list all figures again for that same recipient.
* Compare received messages with your own list.
* Ask for missing figure lists only if needed.
* Do not keep asking about one specific figure. Ask for a missing full list once, or share a comparison/update.
* If another agent proposes a figure that is not in your own list, say you do not have that figure and redirect discussion toward figures that overlap with your own list and received messages.
{answer_rule}
* Never submit ANSWER for a figure that is not in your own list.
* You must send exactly one valid message or answer this turn. Do not stay silent.
* Do not repeat your previous message.

CURRENT STATE:

* You are: {agent_name}
* Total agents: {num_agents}
* Your figures: {figures_list}
* Valid recipients for {agent_name}: {recipients_text}
* Suggested recipient for this turn if you need a default: {preferred_text}
* You already shared your figures: {shared_full_list_text}
* Your previous message: {last_own_message}
* Question you should answer now: {pending_question_text}

RECENT MESSAGES RECEIVED FROM {recent_sources_text}:
{history_text}

{turn_block}
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
