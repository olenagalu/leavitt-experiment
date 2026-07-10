"""
Wheel-topology helpers for client.py.

This module is imported by client.py and is not intended to run directly.
"""

import re


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
    normalized_agent = normalize_agent_name(agent_name)
    final_answer_allowed = "yes" if can_answer else "no"

    history_text = ""
    history_limit = 10 if normalized_agent == "Agent5" else 5
    for msg in conversation_history[-history_limit:]:
        sender = msg.get("sender", "SYSTEM")
        text = msg.get("text", "")
        history_text += f"[{sender}]: {text}\n"

    if not history_text:
        history_text = "(No received messages yet.)\n"

    if normalized_agent == "Agent5":
        discussion_instruction = "During discussion, compare received lists and candidate figures from valid recipients."
    else:
        discussion_instruction = "During discussion, send your own full list if you have not sent it. After that, compare received messages with your own list."

    if normalized_agent == "Agent5" and can_answer:
        turn_block = f"""
YOUR TURN:
Total messages sent so far: {current_round}
Final answer allowed: yes

Final answer is allowed, but it is not required.
If unsure, keep discussing.

Use ANSWER only if final answers are allowed and one figure is clearly supported by the conversation.
If unsure, continue discussion.

Use exactly one of these formats and nothing else:

MESSAGE AgentX: <short message>
AgentX must be one of: {recipients_text}

ANSWER: <figure>
"""
    elif normalized_agent == "Agent5":
        turn_block = f"""
YOUR TURN:
Total messages sent so far: {current_round}
Final answer allowed: no

You must send an informative private message now.
Do not submit ANSWER yet.
If you have not shared your full figure list yet, your next message should share it. Otherwise compare received messages with your own list, confirm or reject proposed figures, or share useful figure comparisons.

Use exactly this format and nothing else:

MESSAGE AgentX: <short useful message containing figure information or requesting a missing full list>
AgentX must be one of: {recipients_text}
"""
    else:
        turn_block = f"""
YOUR TURN:
Total messages sent so far: {current_round}
Final answer allowed: {final_answer_allowed}

You may send one message now.
If you have not shared your full figure list yet, your next message should share it. Otherwise compare received messages with your own list, confirm or reject proposed figures, or share useful figure comparisons.

Use exactly one of these formats and nothing else:

MESSAGE AgentX: <short message>
AgentX must be one of: {recipients_text}
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
Help useful figure information move through the group.

Rules:
* You are the central hub in a wheel topology.
* Use your own figure list and received messages to find the common figure.
* Compare received lists and candidate figures with your own list.
* Confirm a proposed figure only if it is in your own list.
* Reject a proposed figure if it is not in your own list.
* Do not ask candidate yes/no questions.
* Do not ask broad comparison questions.
* Do not ask one recipient about another recipient.
* Submit ANSWER only when final answers are allowed and one figure is clearly supported by the conversation.
* Use only these figures: square, circle, triangle, diamond, cross, asterisk.
* """
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
* Send one private message whenever the server asks for your next message.
* Choose exactly one valid recipient.
* If you have not shared your full figure list yet, your next message should share it.
* After that, compare received messages with your own list.
* Use only your own figures.
* Confirm a proposed figure only if it is in your own list.
* Reject a proposed figure if it is not in your own list.
* Do not suggest a final answer.
* Do not say what another agent has.
* Use only these figures: square, circle, triangle, diamond, cross, asterisk.
* """

    return f"""
{role_prompt}

Trial progress:

* There are no discussion rounds.
* The trial is measured by total messages sent by all agents.
* Submit ANSWER only when final answers are allowed and one figure is clearly supported by the conversation.
* If unsure, continue discussion.
* 
Valid figures:
Valid figures are only: square, circle, triangle, diamond, cross, asterisk.
Use only your own figures and received messages.

CURRENT STATE:

* You are: {agent_name}
* Total agents: {num_agents}
* Total messages sent so far: {current_round}
* Final answer allowed: {final_answer_allowed}
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
