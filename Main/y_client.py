"""
Y-topology helpers for client.py.

This module is imported by client.py and is not intended to run directly.
"""

import re


DEBUG = False
DEFAULT_DISCUSSION_ROUNDS = 8


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
):
    symbols_str = ", ".join(my_symbols)
    figures_list = ", ".join(my_symbols)
    recipients_text = ", ".join(y_contacts)
    recipient_choices_text = f"<one of: {recipients_text}>" if recipients_text else "<no valid recipients>"
    preferred_text = preferred_contact or "choose one valid recipient"
    shared_full_list_text = "yes" if already_shared_full_list else "no"
    recent_sources_text = ", ".join(y_contacts) if y_contacts else "VALID RECIPIENTS"
    turn_mode = "answer" if can_answer else "discussion"
    try:
        discussion_rounds = int(discussion_rounds)
    except (TypeError, ValueError):
        discussion_rounds = DEFAULT_DISCUSSION_ROUNDS
    discussion_rounds = max(0, discussion_rounds)
    answer_start_round = discussion_rounds + 1
    final_answer_allowed = "yes" if can_answer else "no"
    try:
        round_number = int(current_round)
    except (TypeError, ValueError):
        round_number = 1
    full_list_rule = (
        "* First, share your full figure list with one valid recipient.\n"
        if round_number <= 1
        else ""
    )
    normalized_agent = normalize_agent_name(agent_name)

    history_text = ""
    for msg in conversation_history[-5:]:
        sender = msg.get("sender", "SYSTEM")
        text = msg.get("text", "")
        history_text += f"[{sender}]: {text}\n"

    if not history_text:
        history_text = "(No received messages yet.)\n"

    if can_answer:
        turn_block = f"""
YOUR TURN:
Final answer is allowed now, but not required.
If unsure, keep discussing.

Use ACTION: ANSWER only if one figure is in your list and is clearly supported by the received messages.
Do not guess.
If more than one figure is still possible, use ACTION: CHAT.

Use one of:

ACTION: CHAT
TO: {recipient_choices_text}
MESSAGE: <short message>

or

ACTION: ANSWER
WORD: <figure>
"""
    else:
        turn_block = f"""
YOUR TURN:
This is still the discussion stage.
Do not submit a final answer.
Use ACTION: CHAT only.
Share useful information, compare figure lists, answer questions, or pass useful information from one valid recipient to another.

Use:

ACTION: CHAT
TO: {recipient_choices_text}
MESSAGE: <short message>
"""

    if normalized_agent == "Agent3":
        role_prompt = f"""
You are Agent3, the junction agent in a Y topology.

Your figures:
{symbols_str}

Goal:
Find the one figure shared by all agents.

Your valid recipients:
{recipients_text}

You can talk to Agent1, Agent2, and Agent4.
Agent1 and Agent2 can only reach the group through you.
Agent5 can only be reached through Agent4.
You must help useful information move between the branches.

Rules:
* Send one private message per turn.
* Choose exactly one valid recipient before writing the message.
* Choose the recipient who most needs the information or the suggested recipient.
* Use only your figures and messages you received.
{full_list_rule}
* Compare information from different branches.
* Pass useful matches, rejected figures, and possible candidates between branches.
* As the conversation continues, narrow the possible common figures.
* You may propose a possible common figure only if it is in your own list and appears in information received from another agent.
* Confirm another proposal only if that figure is in your own list.
* Reject another proposal if that figure is not in your own list.
* Do not guess.
* Do not repeat your previous message.
"""
    elif normalized_agent == "Agent4":
        role_prompt = f"""
You are Agent4, the bridge agent in a Y topology.

Your figures:
{symbols_str}

Goal:
Find the one figure shared by all agents.

Your valid recipients:
{recipients_text}

You can talk to Agent3 and Agent5.
Agent5 can only reach the group through you.
You should help useful information move between Agent3 and Agent5.

Rules:
* Send one private message per turn.
* Choose exactly one valid recipient before writing the message.
* Choose the recipient who most needs the information or the suggested recipient.
* Use only your figures and messages you received.
{full_list_rule}
* Compare information from Agent3 and Agent5.
* Pass useful matches, rejected figures, and possible candidates between Agent3 and Agent5.
* As the conversation continues, narrow the possible common figures.
* You may propose a possible common figure only if it is in your own list and appears in information received from another agent.
* Confirm another proposal only if that figure is in your own list.
* Reject another proposal if that figure is not in your own list.
* Do not guess.
* Do not repeat your previous message.
"""
    elif len(y_contacts) == 1:
        role_prompt = f"""
You are {agent_name}, an endpoint agent in a Y topology.

Your figures:
{symbols_str}

Goal:
Find the one figure shared by all agents.

Your only valid recipient:
{recipients_text}

You can talk only to {recipients_text}.
You cannot talk directly to other agents.
Information from the rest of the group must come through your valid recipient.

Rules:
* Send one private message per turn.
* Send your message only to {recipients_text}.
* Use only your figures and messages you received.
{full_list_rule}
* Compare your figures with received information.
* Share useful matches, rejected figures, and possible candidates.
* As the conversation continues, narrow the possible common figures.
* You may propose a possible common figure only if it is in your own list and appears in information received from another agent.
* Confirm another proposal only if that figure is in your own list.
* Reject another proposal if that figure is not in your own list.
* Do not guess.
* Do not repeat your previous message.
"""
    else:
        role_prompt = f"""
You are {agent_name}, an agent in a Y topology.

Your figures:
{symbols_str}

Goal:
Find the one figure shared by all agents.

Your valid recipients:
{recipients_text}

Rules:
* Send one private message per turn.
* Choose exactly one valid recipient before writing the message.
* Use only your figures and messages you received.
{full_list_rule}
* Share useful matches, rejected figures, and possible candidates.
* As the conversation continues, narrow the possible common figures.
* Do not guess.
* Do not repeat your previous message.
"""

    return f"""
{role_prompt}

Timing:

* Rounds 1 through {discussion_rounds} are discussion only. Do not submit a final answer in those rounds.
* Round {answer_start_round} and later is answer-allowed mode. You may either continue discussion or submit a final answer.
* Submit a final answer only if one figure is clearly supported by received messages.
* If unsure, continue discussion.

Valid figures:
Valid figures are only: square, circle, triangle, diamond, cross, asterisk.

CURRENT STATE:

* You are: {agent_name}
* Total agents: {num_agents}
* Current round: {current_round}
* Turn mode: {turn_mode}
* Final answer allowed: {final_answer_allowed}
* Discussion-only rounds: {discussion_rounds}
* Your figures: {figures_list}
* Valid recipients for {agent_name}: {recipients_text}
* Suggested recipient for this turn: {preferred_text}
* You already shared your figures: {shared_full_list_text}
* Your previous message: {last_own_message}

RECENT MESSAGES RECEIVED FROM {recent_sources_text}:
{history_text}

{turn_block}
"""


def parse_y_response(raw, agent_name, y_contacts):
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

    raw_target = ""
    text = ""
    lines = raw.split("\n")
    for index, line in enumerate(lines):
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
        target = y_contacts[0] if y_contacts else ""
        target_source = "client_default"
        if DEBUG:
            print(f"[WARN] No TO target from {agent_name}. Defaulted to {target}.")
    elif normalized_target not in normalized_contacts:
        original_target = raw_target
        target = y_contacts[0] if y_contacts else ""
        target_source = "client_default"
        if DEBUG:
            print(f"[WARN] Invalid TO target from {agent_name}: {original_target}. Defaulted to {target}.")
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
