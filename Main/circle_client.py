"""
Circle-topology helpers for client.py.

This module is imported by client.py and is not intended to run directly.
"""

import re


DEBUG = False
DEFAULT_DISCUSSION_ROUNDS = 6


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
    last_own_message="none",
    discussion_rounds=None,
):
    symbols_str = ", ".join(my_symbols)
    figures_list = ", ".join(my_symbols)
    recipients_text = ", ".join(circle_neighbors)
    recipient_choices_text = f"<one of: {recipients_text}>" if recipients_text else "<no valid recipients>"
    preferred_text = preferred_neighbor or "choose either valid recipient"
    shared_full_list_text = "yes" if already_shared_full_list else "no"
    recent_sources_text = " OR ".join(circle_neighbors) if circle_neighbors else "VALID RECIPIENTS"
    turn_mode = "answer" if can_answer else "discussion"
    try:
        discussion_rounds = int(discussion_rounds)
    except (TypeError, ValueError):
        discussion_rounds = DEFAULT_DISCUSSION_ROUNDS
    discussion_rounds = max(0, discussion_rounds)
    answer_start_round = discussion_rounds + 1
    final_answer_allowed = "yes" if can_answer else "no"

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

Use ACTION: ANSWER only if one figure is in your list and is supported by messages from all agents.
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
Share useful information, compare figure lists, respond to questions, or pass useful information from one allowed recipient to another.

Use:

ACTION: CHAT
TO: {recipient_choices_text}
MESSAGE: <short message>
"""

    return f"""
You are {agent_name}, one of {num_agents} agents in a figure-matching experiment.

Your figures:
{symbols_str}

Goal:
Find the one figure shared by all agents.

Circle topology:

* You can send one private message per turn.
* You may send it only to one of these valid recipients: {recipients_text}.
* Only the selected recipient will see your message.
* You may pass useful information from one valid recipient to the other valid recipient.

Rules:

* First, choose one valid recipient to whom you will talk.
* Use only your figures and messages received from valid recipients.
* First share your full figure list with one valid recipient.
* After you already shared your full list, do not repeat the full list unless it is useful for comparison.
* If another agent asked a question, answer it.
* Compare your figures with information from received messages.
* Share useful matches, non-matches, possible overlaps, or candidate figures.
* You may propose a possible common figure only if it is in your list and appears in information from another agent.
* Confirm another proposal only if that figure is in your list.
* Reject another proposal if that figure is not in your list.
* Rounds 1 through {discussion_rounds} are discussion only. Do not submit a final answer in those rounds.
* Round {answer_start_round} and later is answer-allowed mode. You may either continue discussion or submit a final answer.
* Submit a final answer only if one figure is clearly supported by the messages.
* If unsure, continue discussion.
* Do not repeat your previous message.

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


def parse_circle_response(raw, agent_name, circle_neighbors):
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
    normalized_neighbors = {
        normalize_agent_name(neighbor): neighbor
        for neighbor in circle_neighbors
    }

    if DEBUG:
        print(f"[DEBUG] Extracted TO target from {agent_name}: {raw_target}")
        print(f"[DEBUG] Normalized TO target from {agent_name}: {normalized_target}")

    if not raw_target:
        target = circle_neighbors[0] if circle_neighbors else ""
        if DEBUG:
            print(f"[WARN] No TO target from {agent_name}. Defaulted to {target}.")
    elif normalized_target not in normalized_neighbors:
        original_target = raw_target
        target = circle_neighbors[0] if circle_neighbors else ""
        if DEBUG:
            print(f"[WARN] Invalid TO target from {agent_name}: {original_target}. Defaulted to {target}.")
    else:
        target = normalized_neighbors[normalized_target]

    if DEBUG:
        print(f"[DEBUG] Final selected TO target from {agent_name}: {target}")

    if not text:
        text = raw

    return {"action": "chat", "target": target, "text": text, "raw": raw}
