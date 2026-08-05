"""
Shared prompt sections for private-message topology clients.

Topology files own their connection descriptions. This module centralizes the
shared intro, discussion, answer, state, history, and output sections.
"""


FIGURES = [
    "square",
    "circle",
    "triangle",
    "diamond",
    "cross",
    "asterisk",
]


def intro_section(agent_name, num_agents, symbols_str):
    figures_list = ", ".join(FIGURES)
    num_total_figures = len(FIGURES)
    return f"""
You are {agent_name}, one of {num_agents} agents in a figure-matching experiment.

There are {num_total_figures} total possible figures: {figures_list}.
Each agent has 5 figures.
Exactly 1 figure is shared by all 5 agents: Agent1, Agent2, Agent3, Agent4, and Agent5.

Your figures:
{symbols_str}

Goal:
Find the one figure shared by all agents.
"""


def format_history(conversation_history, limit=15):
    history_text = ""
    for msg in (conversation_history or [])[-limit:]:
        sender = msg.get("sender", "SYSTEM")
        text = msg.get("text", "")
        history_text += f"{sender}: {text}\n"
    return history_text or "(No received messages yet.)\n"


def recent_messages_section(history_text):
    return f"""
Recent messages:
{history_text}
"""


def answer_rule(can_answer):
    if can_answer:
        return "* Submit ANSWER only when one figure in your own private list is clearly supported by received messages."
    return "* Do not submit ANSWER yet. Keep sharing or comparing useful figure information."


def discussion_rules(recipients_text, can_answer, recipient_scope="allowed recipients", tell_target="another agent"):
    return f"""
Rules:
- Use only your private figures and messages received from {recipient_scope}.
- If you send a CHAT message, choose one valid recipient from: {recipients_text}.
- If you have not shared your full list, share it with one allowed recipient from: {recipients_text}.
- If there is a question for you, answer it first and after that share useful information about matches, non-matches, or possible shared figures..
- If one figure in your list has evidence from the other five agents, submit it now.
- Compare your figures with information from received messages.
- Share useful matches, non-matches, or possible shared figures.
- If you see a figure that is not in your list, tell {tell_target}.
- If the discussed figure is not in your private list, reject it and continue discussion.
{answer_rule(can_answer)}
- Do not claim to have a figure unless it is in your private list.
- Submit ANSWER only when messages show that the same figure is present for Agent1, Agent2, Agent3, Agent4, and Agent5.
- Never submit a figure that is not in your private list.
- Do not repeat your messages.
"""


def current_state(
    agent_name,
    figures_list,
    recipients_text,
    preferred_recipient,
    already_shared_full_list,
    last_own_message,
    pending_question_text,
    allowed_label="Allowed recipients",
    include_suggested=True,
):
    shared_full_list_text = "yes" if already_shared_full_list else "no"
    suggested_line = (
        f"Suggested recipient for this turn if you need a default: {preferred_recipient}\n"
        if include_suggested
        else ""
    )
    return f"""
Current state:

You are: {agent_name}
Your figures: {figures_list}
{allowed_label}: {recipients_text}
{suggested_line}Already shared your figures: {shared_full_list_text}
Previous message: {last_own_message}
Question to answer now: {pending_question_text}
"""


def answer_output(figures_list, can_answer, include_to=False, recipients_text=""):
    if not can_answer:
        return ""
    to_line = f"TO: <one of: {recipients_text}>\n" if include_to else ""
    return f"""
or:

ACTION: ANSWER
{to_line}WORD: <one of: {figures_list}>
"""


def output_format(recipients_text, figures_list, can_answer, exact_recipient=False, include_answer_to=False):
    to_value = recipients_text if exact_recipient else f"<one of: {recipients_text}>"
    return f"""
Output exactly one:

ACTION: CHAT
TO: {to_value}
MESSAGE: <short useful message>
{answer_output(figures_list, can_answer, include_to=include_answer_to, recipients_text=recipients_text)}
"""
