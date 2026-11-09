"""
LEAVITT - CLIENT
"""

# imports
import socket
import json
import hashlib
import os
import sys
import time
import requests
import platform
import re
import threading
import traceback
from datetime import datetime, timezone
from pathlib import Path
from circle_client import build_circle_prompt, parse_circle_response
from chain_client import build_chain_prompt, parse_chain_response
from y_client import build_y_prompt, parse_y_response
from wheel_client import build_wheel_prompt, parse_wheel_response

# ====================================================================== CONFIG
OLLAMA_URL = "http://127.0.0.1:11434"
MODEL_NAME = "gemma4:e2b-it-qat"
OLLAMA_THINK = True
OLLAMA_TEMPERATURE = 0.2        # randomness; lower values make agents more deterministic
OLLAMA_TOP_P = 1.0              # word-choice pool; lower values reduce weird wording
OLLAMA_REPEAT_PENALTY = 1.0     # 1 = no penalty; higher values reduce repetitiveness
OLLAMA_NUM_PREDICT = 4096       # safety ceiling shared by thinking and visible output
MAX_VISIBLE_RESPONSE_TOKENS = 80
SERVER_IP = "192.168.0.140"
SERVER_PORT = 5001
RECONNECT_DELAY_SECONDS = 5
OLLAMA_REQUEST_TIMEOUT_SECONDS = 180
VALID_FIGURES = {"square", "circle", "triangle", "diamond", "cross", "asterisk"}
# ====================================================================== OLLAMA


DIAGNOSTIC_DIR = Path(
    os.environ.get(
        "LEAVITT_DIAGNOSTICS_DIR",
        str(Path.home() / "Desktop" / "leavitt-diagnostics"),
    )
).expanduser()
DIAGNOSTIC_LOG = DIAGNOSTIC_DIR / f"client-events-{platform.node().split('.')[0].lower()}.jsonl"
_DIAGNOSTIC_LOCK = threading.Lock()
VERBOSE_DIAGNOSTICS = os.environ.get("LEAVITT_VERBOSE_DIAGNOSTICS", "").strip().lower() in {
    "1", "true", "yes", "on",
}
ESSENTIAL_DIAGNOSTIC_EVENTS = {
    "ollama_preflight_failed",
    "ollama_warmup_failed",
    "server_connect_failed",
    "client_exception",
    "client_keyboard_interrupt",
}


def _read_text(path):
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace").strip()
    except OSError:
        return None


def _sha256(path):
    try:
        digest = hashlib.sha256()
        with Path(path).open("rb") as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()
    except OSError:
        return None


def append_diagnostic(event, **details):
    """Append best-effort diagnostics without changing client control flow."""
    if not VERBOSE_DIAGNOSTICS and event not in ESSENTIAL_DIAGNOSTIC_EVENTS:
        return
    record = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "monotonic_seconds": round(time.monotonic(), 6),
        "event": event,
        "hostname": platform.node(),
        "pid": os.getpid(),
        **details,
    }
    try:
        with _DIAGNOSTIC_LOCK:
            DIAGNOSTIC_DIR.mkdir(parents=True, exist_ok=True)
            with DIAGNOSTIC_LOG.open("a", encoding="utf-8") as output:
                output.write(json.dumps(record, sort_keys=True, default=str) + "\n")
                output.flush()
    except OSError as exc:
        print(f"[DIAGNOSTIC WARN] Could not write {DIAGNOSTIC_LOG}: {exc}", flush=True)


def process_identity():
    uptime_text = _read_text("/proc/uptime")
    return {
        "boot_id": _read_text("/proc/sys/kernel/random/boot_id"),
        "uptime_seconds": uptime_text.split()[0] if uptime_text else None,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "client_path": str(Path(__file__).resolve()),
        "client_sha256": _sha256(__file__),
        "model_name": MODEL_NAME,
        "ollama_url": OLLAMA_URL,
        "server_ip": SERVER_IP,
        "server_port": SERVER_PORT,
    }


def normalize_figure_answer(value):
    text = str(value or "").strip().lower()
    text = re.sub(r"^[^a-z]+|[^a-z]+$", "", text)
    return text if text in VALID_FIGURES else ""


def extract_figure_answer(value):
    text = str(value or "")
    exact = normalize_figure_answer(text)
    if exact:
        return exact

    explicit = explicit_answer_from_message(text)
    if explicit:
        return explicit

    mentioned = []
    for figure in VALID_FIGURES:
        if text_mentions_figure(text, figure):
            mentioned.append(figure)
    return mentioned[0] if len(mentioned) == 1 else ""


def text_mentions_figure(text, figure):
    return bool(re.search(rf"\b{re.escape(figure)}\b", str(text or ""), flags=re.IGNORECASE))


def text_rules_out_figure(text, figure):
    lowered = str(text or "").lower()
    patterns = [
        rf"\b(?:do not|don't|dont|cannot|can't|cant)\s+have\s+{re.escape(figure)}\b",
        rf"\b{re.escape(figure)}\s+(?:is\s+)?not\s+in\s+(?:my|their|his|her)\s+list\b",
        rf"\bno\s+{re.escape(figure)}\b",
        rf"\bwithout\s+{re.escape(figure)}\b",
    ]
    return any(re.search(pattern, lowered) for pattern in patterns)


def active_private_figure(messages, my_symbols, agent_name=None, num_agents=None):
    private_figures = [normalize_figure_answer(symbol) for symbol in my_symbols]
    private_figures = [symbol for symbol in private_figures if symbol]
    support = {figure: set() for figure in private_figures}
    ruled_out = set()
    own_agent = normalize_agent_label(agent_name) if agent_name else ""
    total_agents = max(2, min(5, int(num_agents))) if num_agents else 2
    required_support = max(1, total_agents - 1)

    for msg in messages or []:
        sender = msg.get("sender", "") if isinstance(msg, dict) else ""
        normalized_sender = normalize_agent_label(sender)
        if own_agent and normalized_sender == own_agent:
            continue
        text = msg.get("text", "") if isinstance(msg, dict) else str(msg)
        for figure in private_figures:
            if text_rules_out_figure(text, figure):
                ruled_out.add(figure)
            if text_mentions_figure(text, figure):
                support[figure].add(normalized_sender or "unknown")

    candidates = [
        (len(senders), figure)
        for figure, senders in support.items()
        if len(senders) >= required_support and figure not in ruled_out
    ]
    if not candidates:
        return ""
    candidates.sort(reverse=True)
    return candidates[0][1]


def private_fallback_target(topology, preferred_target, circle_neighbors, chain_contacts, y_contacts, wheel_recipients):
    contacts_by_topology = {
        "circle": circle_neighbors,
        "chain": chain_contacts,
        "y": y_contacts,
        "wheel": wheel_recipients,
    }
    contacts = contacts_by_topology.get(topology, []) or []
    normalized_preferred = normalize_agent_label(preferred_target)
    for contact in contacts:
        if normalize_agent_label(contact) == normalized_preferred:
            return contact
    return contacts[0] if contacts else ""


def preferred_recipient_order(valid_recipients, preferred_target):
    contacts = list(valid_recipients or [])
    normalized_preferred = normalize_agent_label(preferred_target)
    preferred = [
        contact
        for contact in contacts
        if normalize_agent_label(contact) == normalized_preferred
    ]
    return preferred + [contact for contact in contacts if contact not in preferred]


def answer_without_figure_message(raw):
    lines = []
    for line in str(raw or "").splitlines():
        stripped = line.strip()
        upper = stripped.upper()
        if not stripped:
            continue
        if upper.startswith("ACTION:") or upper.startswith("WORD:") or upper.startswith("SYMBOL:"):
            continue
        lines.append(stripped)
    return " ".join(lines).strip()


def raw_model_message(raw):
    return str(raw or "").strip()


def visible_response_token_count(value):
    """Conservatively count visible word and punctuation token-like units."""
    return len(re.findall(r"\w+|[^\w\s]", str(value or ""), flags=re.UNICODE))


def strip_embedded_thinking(value):
    """Extract only the visible final channel when an adapter embeds thought tags."""
    text = str(value or "")
    if "<|channel>thought" in text:
        _, separator, text = text.partition("<channel|>")
        if not separator:
            return ""
    elif "<think>" in text.lower():
        closing_tag = re.search(r"</think\s*>", text, flags=re.IGNORECASE)
        if not closing_tag:
            return ""
        text = text[closing_tag.end():]
    text = re.sub(r"^\s*<\|channel>(?:final|analysis)\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*<turn\|>\s*$", "", text, flags=re.IGNORECASE)
    return text.strip()


def model_response_diagnostics(decision):
    """Small timing metadata sent to the server; never includes thought text."""
    keys = (
        "request_id",
        "ollama_response",
        "extracted_response",
        "ollama_done_reason",
        "ollama_eval_count",
        "thinking_chars",
        "thinking_chunks",
        "response_chars",
        "response_chunks",
        "time_to_first_thinking_seconds",
        "thinking_time_seconds",
        "thinking_stream_time_seconds",
        "thinking_to_response_gap_seconds",
        "time_to_first_response_seconds",
        "response_time_seconds",
        "total_generation_time_seconds",
        "visible_response_tokens",
        "visible_response_limit",
        "validation_error",
    )
    metadata = {key: decision.get(key) for key in keys}
    metadata["parser_action"] = decision.get("action", "invalid")
    return metadata


def explicit_answer_from_message(text):
    body = str(text or "")
    figure_words = "|".join(sorted(re.escape(figure) for figure in VALID_FIGURES))
    patterns = [
        r"\b(?:final\s+answer|answer|common\s+figure|shared\s+figure|common\s+symbol)\s*(?:is|:|should\s+be|may\s+be|might\s+be)\s+([a-z]+)\b",
        r"\b(?:submit|choose)\s+(?:ANSWER\s*:?\s*)?([a-z]+)\b",
        rf"\b({figure_words})\b\s+(?:is|seems|appears|looks|must\s+be|should\s+be|may\s+be|might\s+be)\s+(?:the\s+)?(?:common|shared)\s+(?:figure|symbol)\b",
        rf"\b({figure_words})\b\s+(?:is|seems|appears|looks|must\s+be|should\s+be|may\s+be|might\s+be)\s+(?:the\s+)?(?:one\s+)?shared\s+by\s+all\b",
        rf"\ball\s+(?:agents|of\s+us|of\s+them|participants)\s+(?:share|have)\s+({figure_words})\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, body, flags=re.IGNORECASE)
        if match:
            figure = normalize_figure_answer(match.group(1))
            if figure:
                return figure
    return ""


def normalize_ollama_options(options=None):
    options = options if isinstance(options, dict) else {}

    def number(name, fallback, minimum, maximum, integer=False):
        raw = options.get(name, fallback)
        try:
            selected = float(raw)
        except (TypeError, ValueError):
            print(f"[OLLAMA OPTIONS WARN] Invalid {name}={raw!r}; using fallback {fallback}.")
            selected = fallback
        if selected < minimum or selected > maximum:
            print(f"[OLLAMA OPTIONS WARN] Invalid {name}={raw!r}; using fallback {fallback}.")
            selected = fallback
        return int(round(selected)) if integer else round(selected, 3)

    return {
        "temperature": number("temperature", OLLAMA_TEMPERATURE, 0, 2),
        "top_p": number("top_p", OLLAMA_TOP_P, 0, 1),
        "repeat_penalty": number("repeat_penalty", OLLAMA_REPEAT_PENALTY, 0, 3),
        "num_predict": number("num_predict", OLLAMA_NUM_PREDICT, 1, 32768, integer=True),
    }

def check_ollama():
    # Pre-flight check: server reachable and target model available locally.
    try:
        resp = requests.get(OLLAMA_URL, timeout=5)
        if resp.status_code != 200:
            return False, "Ollama not responding"
    except requests.ConnectionError:
        return False, f"Cannot connect to Ollama at {OLLAMA_URL}. Run: ollama serve"

    try:
        resp = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        models = [m["name"] for m in resp.json().get("models", [])]
        if MODEL_NAME not in models:
            return False, f"Model '{MODEL_NAME}' not found. Run: ollama pull {MODEL_NAME}"
    except Exception as e:
        return False, f"Error checking models: {e}"

    return True, "OK"


# Sends the experiment prompt to the local Gemma model and returns this agent’s reply.
def generate_agent_reply(
    agent_name,
    my_symbols,
    conversation_history,
    num_agents,
    current_round,
    can_answer,
    topology="broadcast",
    circle_neighbors=None,
    server_prompt=None,
    circle_recent_messages=None,
    preferred_neighbor=None,
    discussion_rounds=None,
    chain_contacts=None,
    chain_recent_messages=None,
    preferred_chain_contact=None,
    y_contacts=None,
    y_recent_messages=None,
    preferred_y_contact=None,
    wheel_recipients=None,
    wheel_recent_messages=None,
    preferred_wheel_recipient=None,
    circle_shared_full_list_recipients=None,
    ollama_options=None,
    diagnostic_context=None,
):
    """
    Ask model to discuss possible common symbols or answer when allowed.

    Returns a dict with action, parsed fields, and the raw model response.
    """

    symbols_str = "  ".join(my_symbols)
    figures_list = ", ".join(my_symbols)
    circle_neighbors = circle_neighbors or []
    chain_contacts = chain_contacts or []
    y_contacts = y_contacts or []
    wheel_recipients = wheel_recipients or []
    selected_ollama_options = normalize_ollama_options(ollama_options)

    num_agents = max(2, min(5, int(num_agents)))

    if topology == "circle":
        system_prompt = "You are a participant in the figure-matching experiment. Follow the user's instructions exactly."
        circle_history = circle_recent_messages or []
        last_own_message = get_last_own_message(agent_name, conversation_history)
        shared_recipients = [
            neighbor
            for neighbor in circle_neighbors
            if neighbor in (circle_shared_full_list_recipients or set())
        ]
        unshared_recipients = [
            neighbor
            for neighbor in circle_neighbors
            if neighbor not in shared_recipients
        ]
        already_shared_full_list = bool(circle_neighbors) and not unshared_recipients
        pending_question_text = format_pending_question(get_pending_question(agent_name, circle_history))
        user_prompt = build_circle_prompt(
            agent_name,
            my_symbols,
            circle_history,
            num_agents,
            current_round,
            can_answer,
            circle_neighbors,
            preferred_neighbor,
            already_shared_full_list,
            shared_recipients,
            unshared_recipients,
            last_own_message,
            discussion_rounds,
            pending_question_text,
        )
    elif topology == "chain":
        system_prompt = "You are a participant in the figure-matching experiment. Follow the user's instructions exactly."
        chain_history = chain_recent_messages if chain_recent_messages is not None else conversation_history
        last_own_message = get_last_own_message(agent_name, conversation_history)
        already_shared_full_list = has_shared_figures(agent_name, conversation_history, my_symbols)
        pending_question_text = format_pending_question(get_pending_question(agent_name, conversation_history))
        user_prompt = build_chain_prompt(
            agent_name,
            my_symbols,
            chain_history,
            num_agents,
            current_round,
            can_answer,
            chain_contacts,
            preferred_chain_contact,
            already_shared_full_list,
            last_own_message,
            discussion_rounds,
            pending_question_text,
        )
    elif topology == "y":
        system_prompt = "You are a participant in the figure-matching experiment. Follow the user's instructions exactly."
        y_history = y_recent_messages if y_recent_messages is not None else conversation_history
        last_own_message = get_last_own_message(agent_name, conversation_history)
        already_shared_full_list = has_shared_figures(agent_name, conversation_history, my_symbols)
        pending_question_text = format_pending_question(get_pending_question(agent_name, conversation_history))
        user_prompt = build_y_prompt(
            agent_name,
            my_symbols,
            y_history,
            num_agents,
            current_round,
            can_answer,
            y_contacts,
            preferred_y_contact,
            already_shared_full_list,
            last_own_message,
            discussion_rounds,
            pending_question_text,
        )
    elif topology == "wheel":
        system_prompt = "You are a participant in the figure-matching experiment. Follow the user's instructions exactly."
        wheel_history = wheel_recent_messages if wheel_recent_messages is not None else conversation_history
        last_own_message = get_last_own_message(agent_name, conversation_history)
        already_shared_full_list = has_shared_figures(agent_name, conversation_history, my_symbols)
        pending_question_text = format_pending_question(get_pending_question(agent_name, conversation_history))
        user_prompt = build_wheel_prompt(
            agent_name,
            my_symbols,
            wheel_history,
            num_agents,
            current_round,
            can_answer,
            wheel_recipients,
            preferred_wheel_recipient,
            already_shared_full_list,
            last_own_message,
            discussion_rounds,
            pending_question_text,
        )
    else:
        system_prompt = f"""
You are {agent_name}, one of {num_agents} agents in a figure-matching experiment.

Your figures:
{symbols_str}

Goal:
Find the one figure shared by all agents.
Reach the correct answer using as few total messages across all agents as possible.

Rules:
- Keep the visible final response under 80 tokens. Do not count or discuss tokens.
- Use only your figures and received messages.
- If you have not shared your full figure list yet, your next message should share only your full figure list.
- After that, compare received messages with your own list.
- If no figure has been proposed, propose one possible common figure only if it is in your list and appears in another agent's message.
- Confirm and submit ANSWER figure only if it is in your own list.
- If another agent proposes a figure that is not in your list, say you do not have it and redirect discussion toward figures that overlap with your list and received messages.
- Ask for missing figure lists only if needed.
- Do not submit ANSWER immediately.
- When final answers are allowed and you see the common figure, submit ANSWER for it instead of sending another confirmation.
- Do not submit ANSWER for a figure that is not in your own private list.
- Do not repeat your previous message.
- Stay only inside the figure task.

Valid figures:
Valid figures are only: asterisk, circle, cross, diamond, square, triangle.
"""

        recent_history = conversation_history[-15:]
        history_text = ""
        for msg in recent_history:
            sender = msg.get("sender", "SYSTEM")
            text = msg.get("text", "")
            history_text += f"[{sender}]: {text}\n"

        last_own_message = get_last_own_message(agent_name, conversation_history)

        user_prompt = f"""
Current state:

You are: {agent_name}
Your figures: {figures_list}
Final answer allowed: {"yes" if can_answer else "no"}
Previous message: {last_own_message}

Recent messages:
"""

        if history_text:
            user_prompt += history_text
        else:
            user_prompt += "(No public messages yet — you are going first.)\n"

        if can_answer:
            user_prompt += f"""
YOUR TURN:
You may send one message now.
Final answer is allowed.

Submit ANSWER when one figure in your own private list is clearly supported by messages from most agents.
Do not broadcast another confirmation when your evidence is strong enough to submit ANSWER.

If you are still discussing, write any short useful message.
If you are submitting the final answer, write ANSWER: one figure word and nothing else.

Final answer words you may use: {figures_list}
"""
        else:
            user_prompt += """
YOUR TURN:
You must send an informative discussion message now.
Do not submit ANSWER yet.

If you have not shared your full figure list yet, your next message should share it. Otherwise compare received messages with your own list, confirm or reject proposed figures, or ask for missing figure lists only if needed.

Write any short useful broadcast message. Do not use an answer-only figure word yet.
"""

    print(f"[OLLAMA OPTIONS USED] {selected_ollama_options}")

    # Stream locally so thinking and visible-output wall times can be measured
    # separately. Thinking chunks are counted and immediately discarded.
    payload = {
        "model": MODEL_NAME,
        "system": system_prompt,
        "prompt": user_prompt,
        "stream": True,
        "think": OLLAMA_THINK,
        "keep_alive": 300,
        "options": {
            "temperature": selected_ollama_options["temperature"],
            "top_p": selected_ollama_options["top_p"],
            "repeat_penalty": selected_ollama_options["repeat_penalty"],
            "num_predict": selected_ollama_options["num_predict"],
        },
    }

    request_id = f"{platform.node().split('.')[0]}-{time.time_ns()}"
    request_started = time.monotonic()
    request_context = {
        "request_id": request_id,
        "agent": agent_name,
        "topology": topology,
        "message_count": current_round,
        "can_answer": can_answer,
        "system_prompt_chars": len(system_prompt),
        "user_prompt_chars": len(user_prompt),
        "history_messages": len(conversation_history or []),
        "ollama_options": selected_ollama_options,
        **(diagnostic_context or {}),
    }
    append_diagnostic("ollama_request_started", **request_context)
    response_status = None
    visible_chunks = []
    thinking_chars = 0
    thinking_chunks = 0
    response_chunks = 0
    first_thinking_at = None
    last_thinking_at = None
    first_response_at = None
    last_response_at = None
    response_data = {}
    try:
        resp = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload,
            timeout=OLLAMA_REQUEST_TIMEOUT_SECONDS,
            stream=True,
        )
        response_status = resp.status_code
        resp.raise_for_status()
        hard_timeout_reached = threading.Event()

        def stop_overlong_stream():
            hard_timeout_reached.set()
            resp.close()

        remaining_seconds = (
            OLLAMA_REQUEST_TIMEOUT_SECONDS - (time.monotonic() - request_started)
        )
        if remaining_seconds <= 0:
            raise requests.Timeout(
                f"Ollama generation exceeded {OLLAMA_REQUEST_TIMEOUT_SECONDS} seconds."
            )
        hard_timeout = threading.Timer(remaining_seconds, stop_overlong_stream)
        hard_timeout.daemon = True
        hard_timeout.start()
        try:
            for line in resp.iter_lines(decode_unicode=True):
                if not line:
                    continue
                chunk = json.loads(line)
                now = time.monotonic()
                thought = str(chunk.get("thinking", "") or "")
                visible = str(chunk.get("response", "") or "")
                if thought:
                    if first_thinking_at is None:
                        first_thinking_at = now
                    last_thinking_at = now
                    thinking_chars += len(thought)
                    thinking_chunks += 1
                if visible:
                    if first_response_at is None:
                        first_response_at = now
                    last_response_at = now
                    visible_chunks.append(visible)
                    response_chunks += 1
                if chunk.get("done"):
                    response_data = chunk
        finally:
            hard_timeout.cancel()
        if hard_timeout_reached.is_set() or not response_data.get("done"):
            raise requests.Timeout(
                f"Ollama generation exceeded {OLLAMA_REQUEST_TIMEOUT_SECONDS} seconds "
                "or ended without a completion record."
            )
        completed_at = time.monotonic()
        ollama_response = "".join(visible_chunks)
        raw = strip_embedded_thinking(ollama_response)
        thinking_end = first_response_at or completed_at
        thinking_time_seconds = max(0.0, thinking_end - request_started)
        thinking_stream_time_seconds = (
            max(0.0, thinking_end - first_thinking_at)
            if first_thinking_at is not None else 0.0
        )
        response_time_seconds = (
            max(0.0, completed_at - first_response_at)
            if first_response_at is not None
            else 0.0
        )
        timing = {
            "time_to_first_thinking_seconds": (
                round(first_thinking_at - request_started, 6)
                if first_thinking_at is not None else None
            ),
            "thinking_time_seconds": round(thinking_time_seconds, 6),
            "thinking_stream_time_seconds": round(thinking_stream_time_seconds, 6),
            "thinking_to_response_gap_seconds": (
                round(max(0.0, first_response_at - last_thinking_at), 6)
                if first_response_at is not None and last_thinking_at is not None else None
            ),
            "time_to_first_response_seconds": (
                round(first_response_at - request_started, 6)
                if first_response_at is not None else None
            ),
            "response_time_seconds": round(response_time_seconds, 6),
            "total_generation_time_seconds": round(completed_at - request_started, 6),
        }
        append_diagnostic(
            "ollama_request_finished",
            **request_context,
            duration_seconds=timing["total_generation_time_seconds"],
            http_status=response_status,
            response_chars=len(raw),
            thinking_chars=thinking_chars,
            thinking_chunks=thinking_chunks,
            response_chunks=response_chunks,
            **timing,
            done=response_data.get("done"),
            done_reason=response_data.get("done_reason"),
            total_duration_ns=response_data.get("total_duration"),
            load_duration_ns=response_data.get("load_duration"),
            prompt_eval_count=response_data.get("prompt_eval_count"),
            prompt_eval_duration_ns=response_data.get("prompt_eval_duration"),
            eval_count=response_data.get("eval_count"),
            eval_duration_ns=response_data.get("eval_duration"),
        )
        if not raw:
            print("[OLLAMA WARN] Model produced no visible response after thinking.")
            print("[OLLAMA DEBUG] Prompt sent to model:")
            print(user_prompt or system_prompt)
    except Exception as e:
        print(f"[OLLAMA ERROR] {e}")
        append_diagnostic(
            "ollama_request_failed",
            **request_context,
            duration_seconds=round(time.monotonic() - request_started, 6),
            http_status=response_status,
            exception_type=type(e).__name__,
            error=str(e),
            response_body=(resp.text[:1000] if response_status is not None else None),
        )
        return {
            "action": "infrastructure_error",
            "error": str(e),
            "exception_type": type(e).__name__,
            "request_id": request_id,
        }

    print(f"[MODEL RAW] {raw}")

    visible_tokens = visible_response_token_count(raw)
    if visible_tokens > MAX_VISIBLE_RESPONSE_TOKENS:
        decision = {
            "action": "invalid",
            "raw": raw,
            "validation_error": (
                f"Visible response exceeded the {MAX_VISIBLE_RESPONSE_TOKENS}-token limit "
                f"({visible_tokens} token-like units)."
            ),
        }
    elif topology == "circle":
        decision = parse_strict_response(
            raw,
            preferred_recipient_order(circle_neighbors, preferred_neighbor),
            infer_message_answers=False,
        )
    elif topology == "chain":
        decision = parse_strict_response(raw, chain_contacts)
    elif topology == "y":
        decision = parse_strict_response(raw, y_contacts)
    elif topology == "wheel":
        decision = parse_strict_response(raw, wheel_recipients)
    else:
        decision = parse_strict_response(raw, ["BROADCAST"])
    decision.update({
        "request_id": request_id,
        "ollama_response": ollama_response,
        "extracted_response": raw,
        "ollama_done_reason": response_data.get("done_reason"),
        "ollama_eval_count": response_data.get("eval_count"),
        "thinking_chars": thinking_chars,
        "thinking_chunks": thinking_chunks,
        "response_chars": len(raw),
        "response_chunks": response_chunks,
        "visible_response_tokens": visible_tokens,
        "visible_response_limit": MAX_VISIBLE_RESPONSE_TOKENS,
        **timing,
    })
    return decision


# Decides whether the agent’s response is a chat message or answer.
def parse_strict_response(raw, valid_recipients=None, infer_message_answers=True):
    """
    Parse the required output format:
      MESSAGE AgentX: text
      TO: AgentX
      MESSAGE: text
      BROADCAST: text
      ANSWER: figure

    Broadcast stays strict. Private-routing modes prefer the agent's chosen
    recipient, but fall back to the first allowed recipient when the model gives
    message text without a usable target.
    """
    valid_recipients = valid_recipients or []
    text = str(raw or "").strip()
    first_nonempty = next((line.strip() for line in text.splitlines() if line.strip()), "")
    if not first_nonempty:
        return {"action": "invalid", "raw": raw}

    bare_figure = normalize_figure_answer(first_nonempty)
    if bare_figure:
        return {"action": "answer", "word": bare_figure, "raw": raw}

    answer_match = re.match(r"ANSWER\s*:\s*(.+)$", first_nonempty, flags=re.IGNORECASE)
    if answer_match:
        return {"action": "answer", "word": extract_figure_answer(answer_match.group(1)), "raw": raw}
    answer_match = re.match(r"ANSWER\b\s+(.+)$", first_nonempty, flags=re.IGNORECASE)
    if answer_match:
        return {"action": "answer", "word": extract_figure_answer(answer_match.group(1)), "raw": raw}
    if re.match(r"ACTION\s*:\s*ANSWER\b", first_nonempty, flags=re.IGNORECASE):
        for line in text.splitlines():
            word_match = re.match(r"\s*(WORD|SYMBOL)\s*:\s*(.+)$", line, flags=re.IGNORECASE)
            if word_match:
                return {"action": "answer", "word": extract_figure_answer(word_match.group(2)), "raw": raw}
        return {"action": "invalid", "raw": raw}

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    has_message_intent = any(
        re.match(r"(MESSAGE|BROADCAST|TO|ACTION\s*:\s*CHAT)\b", line, flags=re.IGNORECASE)
        for line in lines
    )
    if not has_message_intent:
        for line in lines:
            labeled_answer = re.match(
                r"(?:FINAL\s+ANSWER|ANSWER|WORD|SYMBOL)\s*:?\s*(.+)?$",
                line,
                flags=re.IGNORECASE,
            )
            if labeled_answer:
                word = extract_figure_answer(labeled_answer.group(1) or "")
                if word:
                    return {"action": "answer", "word": word, "raw": raw}
        for line in lines:
            bare_line_figure = normalize_figure_answer(line)
            if bare_line_figure:
                return {"action": "answer", "word": bare_line_figure, "raw": raw}

    if valid_recipients == ["BROADCAST"]:
        broadcast_match = re.match(r"BROADCAST\s*:\s*(.+)$", first_nonempty, flags=re.IGNORECASE)
        if broadcast_match:
            return {
                "action": "chat",
                "target": "ALL",
                "text": broadcast_match.group(1).strip(),
                "raw": raw,
                "target_source": "agent",
                "original_target": "ALL",
            }
        broadcast_match = re.match(r"BROADCAST\b\s*[-–]?\s*(.+)$", first_nonempty, flags=re.IGNORECASE)
        if broadcast_match:
            return {
                "action": "chat",
                "target": "ALL",
                "text": broadcast_match.group(1).strip(),
                "raw": raw,
                "target_source": "client_recovered_format",
                "original_target": "ALL",
            }
        if re.match(r"ACTION\s*:\s*CHAT\b", first_nonempty, flags=re.IGNORECASE):
            for line in text.splitlines():
                message_match = re.match(r"\s*MESSAGE\s*:\s*(.+)$", line, flags=re.IGNORECASE)
                if message_match:
                    return {
                        "action": "chat",
                        "target": "ALL",
                        "text": message_match.group(1).strip(),
                        "raw": raw,
                        "target_source": "client_recovered_format",
                        "original_target": "ALL",
                    }
        message_match = re.match(r"MESSAGE\s*:\s*(.+)$", first_nonempty, flags=re.IGNORECASE)
        if message_match:
            return {
                "action": "chat",
                "target": "ALL",
                "text": message_match.group(1).strip(),
                "raw": raw,
                "target_source": "client_recovered_format",
                "original_target": "ALL",
            }
        for line in text.splitlines()[1:]:
            answer_match = re.match(r"\s*ANSWER\s*:?\s*(.+)$", line, flags=re.IGNORECASE)
            if answer_match:
                return {"action": "answer", "word": extract_figure_answer(answer_match.group(1)), "raw": raw}
            broadcast_match = re.match(r"\s*(BROADCAST|MESSAGE)\s*:?\s*(.+)$", line, flags=re.IGNORECASE)
            if broadcast_match:
                return {
                    "action": "chat",
                    "target": "ALL",
                    "text": broadcast_match.group(2).strip(),
                    "raw": raw,
                    "target_source": "client_recovered_format",
                    "original_target": "ALL",
                }
        if first_nonempty:
            return {
                "action": "chat",
                "target": "ALL",
                "text": text,
                "raw": raw,
                "target_source": "client_recovered_plain_text",
                "original_target": "ALL",
            }
        return {"action": "invalid", "raw": raw}

    normalized_recipients = {
        normalize_agent_label(recipient): recipient
        for recipient in valid_recipients
        }

    raw_target = ""
    message_text = ""

    message_match = re.match(r"MESSAGE\s+([^:]+)\s*:\s*(.+)$", first_nonempty, flags=re.IGNORECASE)
    if message_match:
        raw_target = message_match.group(1).strip()
        message_text = message_match.group(2).strip()
    else:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        for index, line in enumerate(lines):
            upper = line.upper()
            if upper.startswith("TO:"):
                raw_target = line.split(":", 1)[1].strip()
                inline_message = re.search(r"\bMESSAGE\s*:\s*(.+)$", raw_target, flags=re.IGNORECASE)
                if inline_message:
                    message_text = inline_message.group(1).strip()
                    raw_target = raw_target[:inline_message.start()].strip()
            elif upper.startswith("MESSAGE:"):
                message_text = line.split(":", 1)[1].strip()
                if not message_text:
                    message_text = " ".join(
                        extra
                        for extra in lines[index + 1:]
                        if not re.match(r"^(ACTION|TO|WORD|SYMBOL)\s*:", extra, flags=re.IGNORECASE)
                    ).strip()

        if not raw_target:
            target_match = re.search(
                r"\bTO\s*:\s*(.*?)(?=\s+MESSAGE\s*:|$)",
                text,
                flags=re.IGNORECASE | re.DOTALL,
            )
            if target_match:
                raw_target = target_match.group(1).strip()
                inline_message = re.search(r"\bMESSAGE\s*:\s*(.+)$", raw_target, flags=re.IGNORECASE | re.DOTALL)
                if inline_message:
                    message_text = inline_message.group(1).strip()
                    raw_target = raw_target[:inline_message.start()].strip()

        if not message_text:
            message_match_anywhere = re.search(r"\bMESSAGE\s*:\s*(.+)$", text, flags=re.IGNORECASE | re.DOTALL)
            if message_match_anywhere:
                message_text = message_match_anywhere.group(1).strip()

    if not message_text and text:
        message_text = text

    if message_text:
        # Circle mode often uses phrases like "shared by all" as discussion
        # evidence. Only non-circle modes recover those chat sentences as answers.
        # Bare figure words and explicit ANSWER formats are still handled above.
        if infer_message_answers:
            explicit_answer = explicit_answer_from_message(message_text)
            if explicit_answer:
                return {"action": "answer", "word": explicit_answer, "raw": raw}

        normalized_target = normalize_agent_label(raw_target)
        target = normalized_recipients.get(normalized_target)
        target_source = "agent"
        if target is None and valid_recipients:
            target = valid_recipients[0]
            target_source = "client_default" if not raw_target else "client_default_invalid"
        if target is None:
            return {"action": "invalid", "raw": raw}
        return {
            "action": "chat",
            "target": target,
            "text": message_text,
            "raw": raw,
            "target_source": target_source,
            "original_target": raw_target,
        }

    return {"action": "invalid", "raw": raw}


def normalize_agent_label(name):
    stripped = str(name).strip()
    if stripped.upper() == "ALL":
        return "ALL"
    cleaned = re.sub(r"[^\w\s]", "", stripped)
    match = re.fullmatch(r"agent\s*(\d+)", cleaned, flags=re.IGNORECASE)
    if match:
        return f"Agent{int(match.group(1))}"
    return stripped


def classify_agent_response(raw):
    """
    Parse enough to identify ACTION: CHAT or ACTION: ANSWER.
    Does not rewrite the model's wording.
    Falls back to treating the whole thing as a chat message.
    """
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

    if "ACTION: CHAT" in raw_upper or "ACTION:CHAT" in raw_upper:
        for line in raw.split("\n"):
            line_stripped = line.strip()
            if line_stripped.upper().startswith("MESSAGE:"):
                msg = line_stripped.split(":", 1)[1].strip()
                return {"action": "chat", "text": msg, "raw": raw}

    return {"action": "invalid", "raw": raw}


def get_last_own_message(agent_name, conversation_history):
    for msg in reversed(conversation_history):
        if msg.get("sender") == agent_name:
            return msg.get("text", "")
    return "none"


def get_pending_question(agent_name, conversation_history):
    normalized_agent = normalize_agent_label(agent_name)
    agent_number_match = re.fullmatch(r"Agent(\d+)", normalized_agent)
    agent_pattern = (
        rf"\bAgent\s*{agent_number_match.group(1)}\b"
        if agent_number_match
        else rf"\b{re.escape(normalized_agent)}\b"
    )
    for msg in reversed(conversation_history):
        sender = msg.get("sender", "")
        text = msg.get("text", "")
        if sender == agent_name:
            return None
        if "?" not in text:
            continue
        asks_this_agent = (
            re.search(agent_pattern, text, flags=re.IGNORECASE)
            or re.search(r"\byou\b|\byour\b", text, flags=re.IGNORECASE)
            or not re.search(r"\bAgent\s*\d+\b", text, flags=re.IGNORECASE)
        )
        if asks_this_agent:
            return {"sender": sender, "text": text}
    return None


def format_pending_question(pending_question):
    if not pending_question:
        return "none"
    return f'{pending_question.get("sender", "UNKNOWN")} asked: {pending_question.get("text", "")}'


def has_shared_figures(agent_name, conversation_history, my_symbols):
    own_messages = [
        msg.get("text", "").lower()
        for msg in conversation_history
        if msg.get("sender") == agent_name
    ]
    return any(all(symbol.lower() in text for symbol in my_symbols) for text in own_messages)


def send_json(sock, payload):
    data = (json.dumps(payload) + "\n").encode("utf-8")
    sock.sendall(data)


def recv_json_line(sock, recv_buffer):
    while b"\n" not in recv_buffer:
        chunk = sock.recv(4096)
        if not chunk:
            return None, recv_buffer
        recv_buffer += chunk

    line, recv_buffer = recv_buffer.split(b"\n", 1)
    return json.loads(line.decode("utf-8")), recv_buffer


def restart_process(sock=None):
    print("[RESTART] Restart requested by dashboard. Restarting client process...", flush=True)
    if sock is not None:
        try:
            sock.close()
        except Exception:
            pass
    os.execv(sys.executable, [sys.executable] + sys.argv)


def main():
    append_diagnostic("client_process_started", **process_identity())
    ok, msg = check_ollama()
    if not ok:
        print(f"[STARTUP ERROR] {msg}")
        append_diagnostic("ollama_preflight_failed", reason=msg)
        sys.exit(1)

    print("[STARTUP] Ollama check passed.")
    append_diagnostic("ollama_preflight_passed")

    print("[STARTUP] Warming up model...")
    warmup_started = time.monotonic()
    try:
        warmup_response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": "Say ready.",
                "stream": False,
                "think": False,
                "keep_alive": 300,
                "options": {
                    "temperature": 0.0,
                    "num_predict": 5,
                },
            },
            timeout=OLLAMA_REQUEST_TIMEOUT_SECONDS,
        )
        warmup_response.raise_for_status()
        print("[STARTUP] Model warmup complete.")
        append_diagnostic(
            "ollama_warmup_finished",
            duration_seconds=round(time.monotonic() - warmup_started, 6),
            http_status=warmup_response.status_code,
        )
    except Exception as e:
        print(f"[STARTUP WARN] Model warmup failed: {e}")
        append_diagnostic(
            "ollama_warmup_failed",
            duration_seconds=round(time.monotonic() - warmup_started, 6),
            exception_type=type(e).__name__,
            error=str(e),
        )

    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print(f"[CONNECT] Connecting to {SERVER_IP}:{SERVER_PORT} ...")
            append_diagnostic("server_connect_attempt", server_ip=SERVER_IP, server_port=SERVER_PORT)
            sock.connect((SERVER_IP, SERVER_PORT))
            print("[CONNECT] Connected to server.")
            append_diagnostic(
                "server_connected",
                server_ip=SERVER_IP,
                server_port=SERVER_PORT,
                local_address=sock.getsockname(),
                peer_address=sock.getpeername(),
            )

            conversation_history = []
            agent_name = None
            my_symbols = []
            num_agents = 2
            topology = "broadcast"
            circle_neighbors = []
            chain_contacts = []
            y_contacts = []
            wheel_recipients = []
            circle_shared_full_list_recipients = set()
            ollama_options = normalize_ollama_options()
            discussion_rounds = None
            recv_buffer = b""
            trial_active = False
            current_trial_id = None

            while True:
                msg, recv_buffer = recv_json_line(sock, recv_buffer)
                if msg is None:
                    print("[SERVER] Disconnected.")
                    append_diagnostic(
                        "server_disconnected",
                        agent=agent_name,
                        trial_id=current_trial_id,
                        topology=topology,
                        trial_active=trial_active,
                    )
                    break

                msg_type = msg.get("type")

                if msg_type == "nickname_request":
                    hostname = platform.node().split(".")[0].lower()
                    print(f"[SERVER] Nickname request. Sending hostname: {hostname}")
                    send_json(sock, {
                        "type": "nickname",
                        "hostname": hostname,
                        "model_name": MODEL_NAME,
                    })

                elif msg_type == "welcome":
                    assigned_name = msg.get("agent_name")
                    if assigned_name:
                        agent_name = assigned_name
                        print(f"[SERVER] Assigned name: {agent_name}")

                elif msg_type == "restart_client":
                    restart_process(sock)

                elif msg_type == "experiment_start":
                    resuming_trial = bool(msg.get("resume"))
                    trial_active = True
                    current_trial_id = msg.get("trial_id")
                    conversation_history = []
                    circle_shared_full_list_recipients = set(
                        msg.get("circle_shared_full_list_recipients") or []
                    )
                    agent_name = msg["agent_name"]
                    my_symbols = msg["your_symbols"]
                    num_agents = msg.get("num_agents", num_agents)
                    topology = msg.get("topology", "broadcast")
                    circle_neighbors = msg.get("circle_neighbors", [])
                    chain_contacts = msg.get("chain_contacts", msg.get("chain_neighbors", []))
                    y_contacts = msg.get("y_contacts", [])
                    wheel_recipients = msg.get("wheel_recipients", [])
                    ollama_options = normalize_ollama_options(msg.get("ollama_options", ollama_options))
                    discussion_rounds = msg.get("discussion_rounds")
                    print(f"\n[{'RESUME' if resuming_trial else 'START'}] I am {agent_name}")
                    print(f"[START] My figures: {my_symbols}")
                    print(f"[START] Number of agents: {num_agents}")
                    print(f"[START] Topology: {topology}")
                    print("[START] Trial progress: total messages, no discussion rounds")
                    if topology == "circle":
                        print(f"[START] Circle neighbors: {circle_neighbors}")
                    if topology == "chain":
                        print(f"[START] Chain contacts: {chain_contacts}")
                    if topology == "y":
                        print(f"[START] Y contacts: {y_contacts}")
                    if topology == "wheel":
                        print(f"[START] Wheel recipients: {wheel_recipients}")
                    print(f"[START] Ollama options: {ollama_options}")
                    append_diagnostic(
                        "experiment_resumed" if resuming_trial else "experiment_started",
                        trial_id=current_trial_id,
                        agent=agent_name,
                        topology=topology,
                        ollama_options=ollama_options,
                    )

                elif msg_type == "experiment_resume":
                    trial_active = True
                    current_trial_id = msg.get("trial_id")
                    agent_name = msg["agent_name"]
                    my_symbols = msg["your_symbols"]
                    num_agents = msg.get("num_agents", num_agents)
                    topology = msg.get("topology", "broadcast")
                    discussion_rounds = msg.get("discussion_rounds")
                    ollama_options = normalize_ollama_options(msg.get("ollama_options", ollama_options))
                    conversation_history = list(msg.get("conversation_history") or [])
                    circle_neighbors = msg.get("circle_neighbors", [])
                    chain_contacts = msg.get("chain_contacts", [])
                    y_contacts = msg.get("y_contacts", [])
                    wheel_recipients = msg.get("wheel_recipients", [])
                    circle_shared_full_list_recipients = set(
                        msg.get("circle_shared_full_list_recipients") or []
                    )
                    print(f"\n[RESUME] Rejoined trial {current_trial_id} as {agent_name}.")
                    print(f"[RESUME] Restored {len(conversation_history)} chat messages.")
                    append_diagnostic(
                        "experiment_resumed",
                        trial_id=current_trial_id,
                        agent=agent_name,
                        topology=topology,
                        restored_history_messages=len(conversation_history),
                        ollama_options=ollama_options,
                    )

                elif msg_type == "system":
                    text = msg.get("text", "")
                    print(f"[SYSTEM] {text}")
                    if trial_active and topology not in ("circle", "chain", "y", "wheel"):
                        conversation_history.append({"sender": "SYSTEM", "text": text})

                elif msg_type == "chat":
                    if msg.get("trial_id") != current_trial_id:
                        print(
                            f"[STALE CHAT IGNORED] trial_id={msg.get('trial_id')!r}; "
                            f"current={current_trial_id!r}."
                        )
                        continue
                    sender = msg.get("sender", "UNKNOWN")
                    text = msg.get("text", "")
                    print(f"[{sender}] {text}")
                    if not trial_active:
                        print("[STALE CHAT IGNORED] No active trial.")
                        continue
                    conversation_history.append({"sender": sender, "text": text})

                elif msg_type == "reset_chat_history":
                    if current_trial_id is not None and msg.get("trial_id") != current_trial_id:
                        print(
                            f"[STALE RESET IGNORED] trial_id={msg.get('trial_id')!r}; "
                            f"current={current_trial_id!r}."
                        )
                        continue
                    conversation_history = []
                    circle_shared_full_list_recipients = set()
                    print("[ROUND] Chat history reset for new round.")

                elif msg_type == "your_turn":
                    if msg.get("trial_id") != current_trial_id:
                        print(
                            f"[STALE TURN IGNORED] trial_id={msg.get('trial_id')!r}; "
                            f"current={current_trial_id!r}."
                        )
                        continue
                    if not trial_active:
                        print("[STALE TURN IGNORED] No active trial.")
                        continue
                    if not agent_name:
                        print("[WARN] No agent name assigned yet.")
                        send_json(sock, {
                            "type": "invalid",
                            "trial_id": current_trial_id,
                            "raw": "",
                            "reason": "No agent identity was assigned for this turn.",
                        })
                        continue

                    turn_topology = msg.get("topology", topology)
                    if msg.get("reset_chat_history") and conversation_history:
                        conversation_history = []
                        print("[ROUND] Chat history reset for new round.")
                    circle_recent_messages = None
                    chain_recent_messages = None
                    y_recent_messages = None
                    wheel_recent_messages = None
                    preferred_neighbor = ""
                    preferred_chain_contact = ""
                    preferred_y_contact = ""
                    preferred_wheel_recipient = ""
                    discussion_rounds = msg.get("discussion_rounds")
                    if turn_topology == "circle":
                        agent_name = msg.get("agent_name", agent_name)
                        my_symbols = msg.get("your_symbols", my_symbols)
                        circle_neighbors = msg.get("circle_neighbors", circle_neighbors)
                        circle_recent_messages = msg.get("recent_messages", [])
                        preferred_neighbor = msg.get("preferred_neighbor", "")
                        if discussion_rounds is None:
                            answer_allowed_from_round = msg.get("answer_allowed_from_round")
                            if answer_allowed_from_round is not None:
                                try:
                                    discussion_rounds = max(0, int(answer_allowed_from_round) - 1)
                                except (TypeError, ValueError):
                                    discussion_rounds = None
                    elif turn_topology == "chain":
                        agent_name = msg.get("agent_name", agent_name)
                        my_symbols = msg.get("your_symbols", my_symbols)
                        chain_contacts = msg.get("chain_contacts", msg.get("chain_neighbors", chain_contacts))
                        chain_recent_messages = msg.get("recent_messages", [])
                        preferred_chain_contact = msg.get("preferred_contact", msg.get("preferred_neighbor", ""))
                        if discussion_rounds is None:
                            answer_allowed_from_round = msg.get("answer_allowed_from_round")
                            if answer_allowed_from_round is not None:
                                try:
                                    discussion_rounds = max(0, int(answer_allowed_from_round) - 1)
                                except (TypeError, ValueError):
                                    discussion_rounds = None
                    elif turn_topology == "y":
                        agent_name = msg.get("agent_name", agent_name)
                        my_symbols = msg.get("your_symbols", my_symbols)
                        y_contacts = msg.get("y_contacts", y_contacts)
                        y_recent_messages = msg.get("recent_messages", [])
                        preferred_y_contact = msg.get("preferred_contact", msg.get("preferred_neighbor", ""))
                        if discussion_rounds is None:
                            answer_allowed_from_round = msg.get("answer_allowed_from_round")
                            if answer_allowed_from_round is not None:
                                try:
                                    discussion_rounds = max(0, int(answer_allowed_from_round) - 1)
                                except (TypeError, ValueError):
                                    discussion_rounds = None
                    elif turn_topology == "wheel":
                        agent_name = msg.get("agent_name", agent_name)
                        my_symbols = msg.get("your_symbols", my_symbols)
                        wheel_recipients = msg.get("wheel_recipients", wheel_recipients)
                        wheel_recent_messages = msg.get("recent_messages", [])
                        preferred_wheel_recipient = msg.get("preferred_recipient", msg.get("preferred_neighbor", ""))
                        if discussion_rounds is None:
                            answer_allowed_from_round = msg.get("answer_allowed_from_round")
                            if answer_allowed_from_round is not None:
                                try:
                                    discussion_rounds = max(0, int(answer_allowed_from_round) - 1)
                                except (TypeError, ValueError):
                                    discussion_rounds = None
                    else:
                        discussion_rounds = msg.get("discussion_rounds", discussion_rounds)

                    current_round = msg.get("message_count", msg.get("round", 0))
                    can_answer = bool(msg.get("can_answer", True))
                    server_prompt = msg.get("prompt")
                    ollama_options = normalize_ollama_options(msg.get("ollama_options", ollama_options))
                    decision = generate_agent_reply(
                        agent_name,
                        my_symbols,
                        conversation_history,
                        num_agents,
                        current_round,
                        can_answer,
                        turn_topology,
                        circle_neighbors,
                        server_prompt,
                        circle_recent_messages,
                        preferred_neighbor,
                        discussion_rounds,
                        chain_contacts,
                        chain_recent_messages,
                        preferred_chain_contact,
                        y_contacts,
                        y_recent_messages,
                        preferred_y_contact,
                        wheel_recipients,
                        wheel_recent_messages,
                        preferred_wheel_recipient,
                        circle_shared_full_list_recipients,
                        ollama_options,
                        {
                            "trial_id": current_trial_id,
                            "server_turn_type": msg_type,
                        },
                    )
                    response_diagnostics = model_response_diagnostics(decision)
                    if decision.get("action") == "infrastructure_error":
                        send_json(sock, {
                            "type": "ollama_error",
                            "trial_id": current_trial_id,
                            "error": decision.get("error", "Unknown Ollama error"),
                            "exception_type": decision.get("exception_type", ""),
                            **response_diagnostics,
                        })
                        continue

                    private_target = private_fallback_target(
                        turn_topology,
                        {
                            "circle": preferred_neighbor,
                            "chain": preferred_chain_contact,
                            "y": preferred_y_contact,
                            "wheel": preferred_wheel_recipient,
                        }.get(turn_topology, ""),
                        circle_neighbors,
                        chain_contacts,
                        y_contacts,
                        wheel_recipients,
                    )

                    if decision.get("action") == "answer":
                        raw_word = decision.get("word", "")
                        word = extract_figure_answer(raw_word)
                        raw = decision.get("raw", "")
                        print(f"[SEND ANSWER ATTEMPT] {raw}")
                        if not can_answer and turn_topology != "circle":
                            text = raw_model_message(raw)
                            if turn_topology in ("circle", "chain", "y", "wheel") and private_target:
                                print(f"[EARLY ANSWER FALLBACK CHAT] {agent_name} -> {private_target}: {text}")
                                conversation_history.append({"sender": agent_name, "text": f"To {private_target}: {text}"})
                                send_json(sock, {
                                    "type": "chat",
                                    "trial_id": current_trial_id,
                                    "target": private_target,
                                    "text": text,
                                    "raw": raw,
                                    "target_source": "client_assigned",
                                    "original_target": decision.get("target", ""),
                                    **response_diagnostics,
                                })
                            else:
                                print(f"[EARLY ANSWER FALLBACK CHAT] {text}")
                                conversation_history.append({"sender": agent_name, "text": text})
                                send_json(sock, {
                                    "type": "chat",
                                    "trial_id": current_trial_id,
                                    "text": text,
                                    "raw": raw,
                                    **response_diagnostics,
                                })
                            continue
                        if not word:
                            text = raw_model_message(raw)
                            if turn_topology in ("circle", "chain", "y", "wheel") and private_target:
                                print(f"[ANSWER FALLBACK CHAT] {agent_name} -> {private_target}: {text}")
                                conversation_history.append({"sender": agent_name, "text": f"To {private_target}: {text}"})
                                send_json(sock, {
                                    "type": "chat",
                                    "trial_id": current_trial_id,
                                    "target": private_target,
                                    "text": text,
                                    "raw": raw,
                                    "target_source": "client_assigned",
                                    "original_target": decision.get("target", ""),
                                    **response_diagnostics,
                                })
                                continue
                            print(f"[ANSWER FALLBACK CHAT] {text}")
                            conversation_history.append({"sender": agent_name, "text": text})
                            send_json(sock, {
                                "type": "chat",
                                "trial_id": current_trial_id,
                                "text": text,
                                "raw": raw,
                                **response_diagnostics,
                            })
                            continue
                        send_json(sock, {
                            "type": "answer",
                            "trial_id": current_trial_id,
                            "word": word,
                            "raw": raw,
                            **response_diagnostics,
                        })
                    elif decision.get("action") == "invalid":
                        raw = decision.get("raw", "")
                        print("[SEND INVALID OUTPUT]")
                        send_json(sock, {
                            "type": "invalid",
                            "trial_id": current_trial_id,
                            "raw": raw,
                            "reason": decision.get("validation_error") or "Invalid or empty model output.",
                            **response_diagnostics,
                        })
                    else:
                        raw = decision.get("raw", "")
                        text = decision.get("text", "")
                        if turn_topology in ("circle", "chain", "y", "wheel"):
                            target = decision.get("target", "")
                            print(f"{agent_name} -> {target}: {text}")
                        else:
                            print(f"[SEND CHAT] {text}")
                        payload = {
                            "type": "chat",
                            "trial_id": current_trial_id,
                            "text": text,
                            "raw": raw,
                            **response_diagnostics,
                        }
                        if turn_topology in ("circle", "chain", "y", "wheel"):
                            payload["target"] = decision.get("target", "")
                        if turn_topology in ("circle", "chain", "y", "wheel"):
                            payload["target_source"] = decision.get("target_source", "")
                            payload["original_target"] = decision.get("original_target", "")
                        own_text = (
                            f"To {decision.get('target', '')}: {text}"
                            if turn_topology in ("circle", "chain", "y", "wheel")
                            else text
                        )
                        conversation_history.append({"sender": agent_name, "text": own_text})
                        if (
                            turn_topology == "circle"
                            and target
                            and all(symbol.lower() in text.lower() for symbol in my_symbols)
                        ):
                            circle_shared_full_list_recipients.add(target)
                        send_json(sock, payload)

                elif msg_type in ("result", "experiment_end"):
                    if msg.get("trial_id") != current_trial_id:
                        print(
                            f"[STALE RESULT IGNORED] trial_id={msg.get('trial_id')!r}; "
                            f"current={current_trial_id!r}."
                        )
                        continue
                    print("\n[RESULT]")
                    print(json.dumps(msg, indent=2))
                    append_diagnostic(
                        "experiment_finished",
                        trial_id=current_trial_id,
                        agent=agent_name,
                        topology=topology,
                        result=msg.get("result"),
                        success=msg.get("success"),
                        interrupted_by_disconnect=msg.get("interrupted_by_disconnect"),
                        time_seconds=msg.get("time_seconds"),
                    )
                    trial_active = False
                    current_trial_id = None
                    conversation_history = []
                    circle_shared_full_list_recipients = set()
                    my_symbols = []
                    circle_neighbors = []
                    chain_contacts = []
                    y_contacts = []
                    wheel_recipients = []
                    print("[SERVER] Waiting for next trial start...")
                    continue

                else:
                    print(f"[UNKNOWN MESSAGE] {msg}")

        except ConnectionRefusedError:
            print("[CONNECT ERROR] Server unavailable.")
            append_diagnostic(
                "server_connect_failed",
                server_ip=SERVER_IP,
                server_port=SERVER_PORT,
                exception_type="ConnectionRefusedError",
            )
        except KeyboardInterrupt:
            print("\n[CLIENT] Exiting.")
            append_diagnostic(
                "client_keyboard_interrupt",
                agent=locals().get("agent_name"),
                trial_id=locals().get("current_trial_id"),
            )
            try:
                sock.close()
            except Exception:
                pass
            sys.exit(0)
        except Exception as e:
            print(f"[CLIENT ERROR] {e}")
            append_diagnostic(
                "client_exception",
                agent=locals().get("agent_name"),
                trial_id=locals().get("current_trial_id"),
                topology=locals().get("topology"),
                exception_type=type(e).__name__,
                error=str(e),
                traceback=traceback.format_exc(),
            )
        finally:
            try:
                sock.close()
            except Exception:
                pass

        print(f"[RETRY] Reconnecting in {RECONNECT_DELAY_SECONDS} seconds...")
        append_diagnostic(
            "server_reconnect_wait",
            delay_seconds=RECONNECT_DELAY_SECONDS,
            agent=locals().get("agent_name"),
            trial_id=locals().get("current_trial_id"),
        )
        time.sleep(RECONNECT_DELAY_SECONDS)


if __name__ == "__main__":
    main()
