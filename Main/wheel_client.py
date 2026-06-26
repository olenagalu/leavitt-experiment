"""
Wheel-topology helpers for client.py.

This module is imported by client.py and is not intended to run directly.
"""

import re


DEBUG = False
DEFAULT_DISCUSSION_ROUNDS = 1


def normalize_agent_name(name):
    stripped = str(name).strip()
    cleaned = re.sub(r"[^\w\s]", "", stripped)
    match = re.fullmatch(r"agent\s*(\d+)", cleaned, flags=re.IGNORECASE)
    if match:
        return f"Agent{int(match.group(1))}"
    return stripped


def get_wheel_recipients(agent_name):
    recipients_by_agent = {
        "Agent1": ["Agent5"],
        "Agent2": ["Agent5"],
        "Agent3": ["Agent5"],
        "Agent4": ["Agent5"],
        "Agent5": ["Agent1", "Agent2", "Agent3", "Agent4"],
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
):
    symbols_str = ", ".join(my_symbols)
    figures_list = ", ".join(my_symbols)
    wheel_recipients = wheel_recipients or get_wheel_recipients(agent_name)
    recipients_text = ", ".join(wheel_recipients)
    recipient_choices_text = f"<one of: {recipients_text}>" if recipients_text else "<no valid recipients>"
    preferred_text = preferred_recipient or "choose one valid recipient"
    shared_full_list_text = "yes" if already_shared_full_list else "no"
    recent_sources_text = ", ".join(wheel_recipients) if wheel_recipients else "VALID RECIPIENTS"
    turn_mode = "answer" if can_answer else "discussion"
    try:
        discussion_rounds = int(discussion_rounds)
    except (TypeError, ValueError):
        discussion_rounds = DEFAULT_DISCUSSION_ROUNDS
    discussion_rounds = max(0, discussion_rounds)
    answer_start_round = discussion_rounds + 1
    final_answer_allowed = "yes" if can_answer else "no"
    normalized_agent = normalize_agent_name(agent_name)

    history_text = ""
    history_limit = 10 if normalized_agent == "Agent5" else 5
    for msg in conversation_history[-history_limit:]:
        sender = msg.get("sender", "SYSTEM")
        text = msg.get("text", "")
        history_text += f"[{sender}]: {text}\n"

    if not history_text:
        history_text = "(No received messages yet.)\n"

    if normalized_agent == "Agent5":
        discussion_instruction = "During discussion, collect missing full lists from valid recipients."
    else:
        discussion_instruction = "During discussion, send your own full list if you have not sent it. After that, respond only to central-hub requests using your own figures."

    if can_answer and normalized_agent == "Agent5":
        turn_block = f"""
YOUR TURN:
Current round: {current_round}
Discussion-only rounds: {discussion_rounds}
Answer allowed starting round: {answer_start_round}
Final answer allowed: {final_answer_allowed}

Final answer is allowed now, but not required.
If unsure, keep discussing.

Use ACTION: ANSWER only if exactly one figure appears in all five lists: all four received lists and your own list.
If any full list is missing, use ACTION: CHAT.
Do not answer from repeated figure names.
Do not answer from majority agreement.
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
    elif can_answer:
        turn_block = f"""
YOUR TURN:
Current round: {current_round}
Discussion-only rounds: {discussion_rounds}
Answer allowed starting round: {answer_start_round}
Final answer allowed: {final_answer_allowed}

This is answer-allowed mode, but you are not the solving agent.
You must use ACTION: CHAT only.
Send your own full list if you have not sent it. After that, respond only to central-hub requests using your own figures.

Use:

ACTION: CHAT
TO: {recipient_choices_text}
MESSAGE: <short message>
"""
    else:
        turn_block = f"""
YOUR TURN:
Current round: {current_round}
Discussion-only rounds: {discussion_rounds}
Answer allowed starting round: {answer_start_round}
Final answer allowed: {final_answer_allowed}

This is still the discussion stage.
You must use ACTION: CHAT only.
Do not use ACTION: ANSWER before round {answer_start_round}.

{discussion_instruction}

Use:

ACTION: CHAT
TO: {recipient_choices_text}
MESSAGE: <short message>
"""

    if normalized_agent == "Agent5":
        role_prompt = f"""
You are the central hub in a wheel topology.

Your figures:
{symbols_str}

Goal:
Find the one figure shared by all agents.

Your valid recipients:
{recipients_text}

You can send messages only to your valid recipients.
The other agents cannot talk to each other.
Only you can collect all lists and find the common figure.

Rules:
* You are the central hub in a wheel topology.
* You must collect one full figure list from each valid recipient.
* You must use your own figure list as the fifth list.
* You must compare all five lists to find one common figure before answering.
* The final answer must appear in all four received lists and in your own list.
* Do not ask candidate yes/no questions.
* Do not ask broad comparison questions.
* Do not ask one recipient about another recipient.
* If exactly one figure appears in all five lists and final answer is allowed, use ACTION: ANSWER.
* Use only these figures: square, circle, triangle, diamond, cross, asterisk.
* Do not guess.
"""
    else:
        role_prompt = f"""
You are {agent_name} in a wheel topology.

Your figures:
{symbols_str}

Your valid recipients:
{recipients_text}

You can send messages only to your valid recipients.
Task: send your own figure list to your valid recipient. After that, answer only questions about your own figures.

Rules:
* Send one private message per turn.
* Choose exactly one valid recipient.
* Send your full figure list to your valid recipient.
* After sending your full list, respond only to requests from your valid recipient.
* Use only your own figures.
* If asked whether you have a specific figure, answer yes or no using only your own figures.
* Do not compare your list with another agent's list.
* Do not compare lists.
* Do not ask questions.
* Do not suggest a final answer.
* Do not say what another agent has.
* Use only these figures: square, circle, triangle, diamond, cross, asterisk.
* Do not guess.
"""

    return f"""
{role_prompt}

Timing:

* Rounds 1 through {discussion_rounds} are discussion only.
* Round {answer_start_round} and later is answer-allowed mode.
* With discussion_rounds = 1, round 2 is the first answer-allowed round.
* In answer-allowed mode, the central hub should compare the full lists received from valid recipients with its own list.
* Submit a final answer only if exactly one figure appears in all five lists.
* If unsure, continue discussion.

Valid figures:
Valid figures are only: square, circle, triangle, diamond, cross, asterisk.
Use only your own figures and received messages.

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


def parse_wheel_response(raw, agent_name, wheel_recipients):
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
    normalized_recipients = {
        normalize_agent_name(recipient): recipient
        for recipient in wheel_recipients
    }

    if DEBUG:
        print(f"[DEBUG] Extracted TO target from {agent_name}: {raw_target}")
        print(f"[DEBUG] Normalized TO target from {agent_name}: {normalized_target}")

    if not raw_target:
        target = wheel_recipients[0] if wheel_recipients else ""
        target_source = "client_default"
        if DEBUG:
            print(f"[WARN] No TO target from {agent_name}. Defaulted to {target}.")
    elif normalized_target not in normalized_recipients:
        original_target = raw_target
        target = wheel_recipients[0] if wheel_recipients else ""
        target_source = "client_default"
        if DEBUG:
            print(f"[WARN] Invalid TO target from {agent_name}: {original_target}. Defaulted to {target}.")
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
