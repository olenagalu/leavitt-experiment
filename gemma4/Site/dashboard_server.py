import argparse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
import mimetypes
import os
import pwd
import random
import re
import select
import shutil
import socket
import subprocess
import sys
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


FIGURES = ["square", "circle", "triangle", "diamond", "cross", "asterisk"]
MIN_PARTICIPANTS = 2
MAX_PARTICIPANTS = 5
DEFAULT_FIGURES_PER_CARD = 3
MAX_ROUNDS_PER_TRIAL = 10
DEFAULT_MAX_MESSAGES_PER_TRIAL = 50
DEFAULT_MAX_MESSAGES_BY_TOPOLOGY = {"circle": 40}
MIN_MESSAGES_PER_TRIAL = 1
MAX_MESSAGES_PER_TRIAL = 500
CIRCLE_ANSWER_MESSAGE_GATE = 5
EFFICIENCY_MAX_ROUNDS_BY_AGENTS = {2: 3, 3: 3, 4: 4, 5: 4}
CIRCLE_EFFICIENCY_LIMIT_BY_AGENTS = {2: 4, 3: 5, 4: 6, 5: 8}
CIRCLE_HARD_STOP_BY_AGENTS = {2: 6, 3: 7, 4: 8, 5: 10}
VALID_TOPOLOGIES = {"broadcast", "circle", "chain", "y", "wheel"}
FIXED_FIVE_AGENT_TOPOLOGIES = {"circle", "chain", "y", "wheel"}
AUTO_TRIAL_TARGET = 50
REPORT_CHECKPOINT_INTERVAL_TRIALS = 10
CIRCLE_STUDY_TOPOLOGIES = ("circle",)
Y_STUDY_TOPOLOGIES = ("y",)
WHEEL_STUDY_TOPOLOGIES = ("wheel",)
CHAIN_STUDY_TOPOLOGIES = ("chain",)
REMAINING_STUDY_TOPOLOGIES = ("y", "chain", "wheel")
FULL_STUDY_TOPOLOGIES = ("broadcast", "circle", "y", "wheel", "chain")
LEAVITT_STUDY_TOPOLOGIES = ("circle", "y", "wheel", "chain")
FOUR_TOPOLOGY_STUDY_TOPOLOGIES = ("circle", "chain", "y", "wheel")
FULL_STUDY_TEMPERATURES = (0.0, 0.5, 1.0)
FOUR_TOPOLOGY_STUDY_TEMPERATURES = (0.0, 0.05, 0.1, 0.2, 1.0)
CIRCLE_STUDY_TEMPERATURES = FOUR_TOPOLOGY_STUDY_TEMPERATURES
Y_STUDY_TEMPERATURES = FOUR_TOPOLOGY_STUDY_TEMPERATURES
WHEEL_STUDY_TEMPERATURES = FOUR_TOPOLOGY_STUDY_TEMPERATURES
WHEEL_TEMPERATURE_1_STUDY_TEMPERATURES = (1.0,)
CHAIN_STUDY_TEMPERATURES = FOUR_TOPOLOGY_STUDY_TEMPERATURES
FULL_STUDY_BATCH_COUNT = len(FULL_STUDY_TOPOLOGIES) * len(FULL_STUDY_TEMPERATURES)
DEFAULT_TEMPERATURE_PAUSE_MINUTES = 5
DEFAULT_TOPOLOGY_PAUSE_MINUTES = 15
MIN_COOLING_PAUSE_MINUTES = 0
MAX_COOLING_PAUSE_MINUTES = 180
POWER_OFF_DELAY_SECONDS = 10
POWER_OFF_RETRY_SECONDS = 10
STUDY_STOP_FAILURE_POWEROFF_DELAY_SECONDS = 15 * 60
CLIENT_TURN_TIMEOUT_SECONDS = 185
OLLAMA_SERVICE = "ollama.service"
REMOTE_SYSTEMCTL = "/usr/bin/systemctl"
REMOTE_SUDO = "/usr/bin/sudo"
OLLAMA_RESTART_COMMAND_TIMEOUT_SECONDS = 30
OLLAMA_RESTART_RETRY_SECONDS = 5
OLLAMA_RESTART_WAIT_STATUS_SECONDS = 30
OLLAMA_RESTART_INTERVAL_TRIALS = 25
OLLAMA_MODEL_NAME = "gemma4:e2b-it-qat"
OLLAMA_WARMUP_TIMEOUT_SECONDS = 180
STUDY_PROGRESS_EVENTS = {
    "full_study_started",
    "full_study_batch_started",
    "trial_requested",
    "trial_started",
    "chat",
    "answer",
    "trial_finished",
}
DIAGNOSTIC_EVENT_KINDS = {
    "server",
    "client_joined",
    "client_left",
    "client_reload_completed",
    "clients_reload_finished",
    "study_reconnect_wait_started",
    "study_reconnect_restored",
    "trial_paused_disconnect",
    "trial_resumed_disconnect",
    "turn_retried_after_reconnect",
    "stale_response_ignored",
    "timeout",
    "client_ollama_error",
    "trial_requested",
    "trial_started",
    "trial_finished",
    "trial_interrupted",
    "full_study_started",
    "full_study_batch_started",
    "ollama_restart_readiness",
    "ollama_batch_restart_started",
    "ollama_batch_restart_host_finished",
    "ollama_batch_restart_waiting",
    "ollama_batch_restart_completed",
    "ollama_batch_restart_failed",
    "ollama_warmup_started",
    "ollama_warmup_host_finished",
    "ollama_warmup_waiting",
    "ollama_warmup_completed",
    "auto_trials_restart_failed",
    "full_study_completed",
    "full_study_failed",
}


def invoking_user_home():
    """Return the desktop user's home even when the dashboard runs under sudo."""
    sudo_user = os.environ.get("SUDO_USER", "").strip()
    if sudo_user and sudo_user != "root":
        try:
            return Path(pwd.getpwnam(sudo_user).pw_dir)
        except KeyError:
            pass
    return Path.home()


def is_jetson_device():
    """Refuse local power-off unless the dashboard is actually running on a Jetson."""
    for model_path in (Path("/proc/device-tree/model"), Path("/sys/firmware/devicetree/base/model")):
        try:
            model = model_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if "jetson" in model.lower() or "nvidia" in model.lower():
            return True
    return False


DEFAULT_REPORT_ROOT = invoking_user_home() / "Desktop" / "leavitt-report"
DATA_ROOT = Path(os.environ.get("LEAVITT_DATA_DIR", DEFAULT_REPORT_ROOT)).expanduser()
DEFAULT_OLLAMA_OPTIONS = {
    "temperature": 0.2,
    "top_p": 1.0,
    "repeat_penalty": 1.0,
    "num_predict": 4096,
}
EXPECTED_STUDY_MODEL = "gemma4:e2b-it-qat"
JETSON_SSH_USER = "minds_user"
JETSON_ADDRESSES = {
    "jetson1": "192.168.0.151",
    "jetson2": "192.168.0.152",
    "jetson3": "192.168.0.153",
    "jetson4": "192.168.0.154",
    "jetson5": "192.168.0.155",
}
JETSON_HOSTNAMES = list(JETSON_ADDRESSES)
IP_TO_JETSON = {address: name for name, address in JETSON_ADDRESSES.items()}
JETSON_CLIENT_SERVICE = "leavitt-client.service"
HOSTNAME_TO_AGENT = {
    "jetson1": "Agent1",
    "jetson2": "Agent2",
    "jetson3": "Agent3",
    "jetson4": "Agent4",
    "jetson5": "Agent5",
}


def get_y_contacts(agent_id):
    contacts_by_agent = {
        1: [3],
        2: [3],
        3: [1, 2, 4],
        4: [3, 5],
        5: [4],
    }
    return contacts_by_agent.get(agent_id, [])


def get_wheel_contacts(agent_id):
    contacts_by_agent = {
        1: [3],
        2: [3],
        3: [1, 2, 4, 5],
        4: [3],
        5: [3],
    }
    return contacts_by_agent.get(agent_id, [])


def display_topology_name(topology):
    labels = {
        "broadcast": "Broadcast",
        "circle": "Circle",
        "chain": "Chain",
        "y": "Y topology",
        "wheel": "Wheel",
    }
    return labels.get(topology, str(topology))


def normalize_hostname(hostname):
    return str(hostname).strip().lower().split(".", 1)[0]


def display_agent_name(name):
    return HOSTNAME_TO_AGENT.get(normalize_hostname(name), str(name))


def internal_agent_name(name):
    text = str(name).strip()
    match = re.fullmatch(r"agent\s*(\d+)", text, flags=re.IGNORECASE)
    if match:
        return f"jetson{int(match.group(1))}"
    return normalize_hostname(text)


def get_agent_id(name):
    match = re.search(r"(\d+)", str(name))
    return int(match.group(1)) if match else None


def get_jetson_number(name):
    match = re.search(r"jetson\s*(\d+)", normalize_hostname(name))
    return int(match.group(1)) if match else None


def normalize_figure_answer(value):
    text = str(value or "").strip().lower()
    text = re.sub(r"^[^a-z]+|[^a-z]+$", "", text)
    return text if text in FIGURES else ""


def generate_jetson_sets(nicknames, seed=None):
    clean_nicknames = [n.strip() for n in nicknames]
    if len(set(clean_nicknames)) != len(clean_nicknames):
        raise ValueError("Nicknames must be unique.")

    n = len(clean_nicknames)
    if not (MIN_PARTICIPANTS <= n <= MAX_PARTICIPANTS):
        raise ValueError(f"num_jetsons must be between {MIN_PARTICIPANTS} and {MAX_PARTICIPANTS}.")

    rng = random.Random(seed)

    if n == 2:
        pool = rng.sample(FIGURES, 5)
        common_figure = rng.choice(pool)
        others = [f for f in pool if f != common_figure]
        rng.shuffle(others)
        assignments = {
            clean_nicknames[0]: [common_figure, others[0], others[1]],
            clean_nicknames[1]: [common_figure, others[2], others[3]],
        }
        for card in assignments.values():
            rng.shuffle(card)
        return common_figure, assignments, 5, 3

    pool_size = n + 1
    pool = rng.sample(FIGURES, pool_size)
    common_figure = rng.choice(pool)
    non_common = [f for f in pool if f != common_figure]
    rng.shuffle(non_common)

    assignments = {}
    for idx, nickname in enumerate(clean_nicknames):
        card = [f for f in pool if f != non_common[idx]]
        rng.shuffle(card)
        assignments[nickname] = card
    return common_figure, assignments, pool_size, n


def get_efficiency_limit(topology, num_agents):
    if topology == "circle":
        return CIRCLE_EFFICIENCY_LIMIT_BY_AGENTS.get(num_agents, 8)
    if topology in ("chain", "y", "wheel"):
        return 10
    return EFFICIENCY_MAX_ROUNDS_BY_AGENTS.get(num_agents, 4)


def get_hard_stop_round(topology, num_agents):
    if topology == "circle":
        return CIRCLE_HARD_STOP_BY_AGENTS.get(num_agents, MAX_ROUNDS_PER_TRIAL)
    return MAX_ROUNDS_PER_TRIAL


def default_max_messages_for_topology(topology):
    return DEFAULT_MAX_MESSAGES_BY_TOPOLOGY.get(topology, DEFAULT_MAX_MESSAGES_PER_TRIAL)


def normalize_max_messages(value, topology=None):
    try:
        messages = int(value)
    except (TypeError, ValueError):
        messages = default_max_messages_for_topology(topology)
    return max(MIN_MESSAGES_PER_TRIAL, min(MAX_MESSAGES_PER_TRIAL, messages))


def ollama_restart_due(completed_trials, target_trials):
    """Return whether an unfinished automated batch reached a maintenance interval."""
    return (
        completed_trials > 0
        and completed_trials < target_trials
        and completed_trials % OLLAMA_RESTART_INTERVAL_TRIALS == 0
    )


def normalize_ollama_options(value):
    source = value if isinstance(value, dict) else {}

    def number(name, minimum, maximum, integer=False):
        fallback = DEFAULT_OLLAMA_OPTIONS[name]
        raw = source.get(name, fallback)
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
        "temperature": number("temperature", 0, 2),
        "top_p": number("top_p", 0, 1),
        "repeat_penalty": number("repeat_penalty", 0, 3),
        "num_predict": number("num_predict", 1, 32768, integer=True),
    }


def normalize_cooling_options(value):
    source = value if isinstance(value, dict) else {}

    def minutes(name, fallback):
        try:
            selected = float(source.get(name, fallback))
        except (TypeError, ValueError):
            selected = fallback
        return round(max(MIN_COOLING_PAUSE_MINUTES, min(MAX_COOLING_PAUSE_MINUTES, selected)), 2)

    return {
        "between_temperatures_minutes": minutes(
            "between_temperatures_minutes",
            DEFAULT_TEMPERATURE_PAUSE_MINUTES,
        ),
        "between_topologies_minutes": minutes(
            "between_topologies_minutes",
            DEFAULT_TOPOLOGY_PAUSE_MINUTES,
        ),
    }


def evaluate_efficiency(found, has_answer, messages_used, num_agents, topology, max_messages):
    max_efficient_messages = max_messages
    if not has_answer:
        return "failed_no_answer", "No answer was submitted before the hard stop.", max_efficient_messages
    if not found:
        return "failed_wrong_answer", "Agents submitted a wrong answer.", max_efficient_messages
    if messages_used <= max_efficient_messages:
        return (
            "success_efficient",
            f"Agents found the correct figure after {messages_used} total messages.",
            max_efficient_messages,
        )
    return (
        "success_slow",
        f"Agents found the correct figure, but used {messages_used} total messages.",
        max_efficient_messages,
    )


def run_identifier():
    """Return a unique identifier that does not depend on the system clock."""
    return f"run-{uuid.uuid4().hex[:12]}"


def temperature_label(value):
    return f"{float(value):g}"


def append_json_line(path, payload):
    append_json_lines(path, [payload])


def append_json_lines(path, payloads):
    payloads = list(payloads)
    if not payloads:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as output:
        for payload in payloads:
            output.write(json.dumps(payload, sort_keys=True) + "\n")
        output.flush()
        os.fsync(output.fileno())


def atomic_write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    with temporary_path.open("w", encoding="utf-8") as output:
        output.write(text)
        output.flush()
        os.fsync(output.fileno())
    os.replace(temporary_path, path)


def atomic_write_json(path, payload):
    atomic_write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def load_json_lines(path):
    if not path.exists():
        return []
    records = []
    with path.open("r", encoding="utf-8") as source:
        for line in source:
            if line.strip():
                records.append(json.loads(line))
    return records


def markdown_table(headers, rows, numeric_columns=None, markdown_alignment=True):
    """Render a Markdown table whose columns also align in plain-text editors."""
    numeric_columns = set(numeric_columns or [])
    string_rows = [[str(cell) for cell in row] for row in rows]
    widths = []
    for index, header in enumerate(headers):
        cell_widths = [len(row[index]) for row in string_rows if index < len(row)]
        widths.append(max([len(str(header)), 3, *cell_widths]))

    def formatted_row(cells):
        values = []
        for index, width in enumerate(widths):
            value = str(cells[index]) if index < len(cells) else ""
            values.append(value.rjust(width) if index in numeric_columns else value.ljust(width))
        return "| " + " | ".join(values) + " |"

    separators = [
        ("-" * (width - 1) + ":")
        if markdown_alignment and index in numeric_columns
        else ("-" * width)
        for index, width in enumerate(widths)
    ]
    return [formatted_row(headers), formatted_row(separators), *[formatted_row(row) for row in string_rows]]


def recipient_choice_analysis(messages):
    """Summarize intentional model recipient choices and routing fallbacks."""
    choices = defaultdict(Counter)
    valid_by_sender = defaultdict(set)
    fallback_counts = Counter()

    for message in messages:
        topology = message.get("topology")
        if topology == "broadcast":
            continue
        sender = message.get("sender")
        receiver = message.get("receiver")
        if not sender or not receiver:
            continue
        valid_recipients = (
            message.get("valid_recipients")
            or message.get("valid_contacts")
            or message.get("valid_neighbors")
            or []
        )
        valid_by_sender[(topology, sender)].update(valid_recipients)
        target_source = message.get("target_source") or "unknown"
        if target_source == "agent" and receiver in valid_recipients:
            choices[(topology, sender)][receiver] += 1
        else:
            fallback_counts[(topology, sender, target_source)] += 1

    rows = []
    for (topology, sender), recipients in sorted(valid_by_sender.items()):
        ordered_recipients = sorted(recipients)
        total_choices = sum(choices[(topology, sender)].values())
        recipient_count = len(ordered_recipients)
        baseline = 1 / recipient_count if recipient_count else 0
        for receiver in ordered_recipients:
            count = choices[(topology, sender)][receiver]
            probability = count / total_choices if total_choices else 0
            smoothed_probability = (
                (count + 0.5) / (total_choices + 0.5 * recipient_count)
                if recipient_count
                else 0
            )
            rows.append({
                "topology": topology,
                "sender": sender,
                "recipient": receiver,
                "allowed_recipient_count": recipient_count,
                "choices": count,
                "total_model_choices": total_choices,
                "probability": probability,
                "uniform_baseline": baseline,
                "lift": probability / baseline if baseline else 0,
                "smoothed_probability": smoothed_probability,
            })

    fallbacks = [
        {
            "topology": topology,
            "sender": sender,
            "target_source": target_source,
            "count": count,
        }
        for (topology, sender, target_source), count in sorted(fallback_counts.items())
    ]
    return rows, fallbacks


def recipient_probability_table(recipient_rows, include_topology=False):
    headers = ["Sender", "Recipient", "Allowed recipients", "Choices", "Total explicit choices", "Probability"]
    rows = [[
        row["sender"],
        row["recipient"],
        row["allowed_recipient_count"],
        row["choices"],
        row["total_model_choices"],
        f"{row['probability'] * 100:.1f}% ({row['probability']:.3f})",
    ] for row in recipient_rows]
    numeric_columns = {2, 3, 4, 5}
    if include_topology:
        headers.insert(0, "Topology")
        rows = [
            [display_topology_name(row["topology"]), *values]
            for row, values in zip(recipient_rows, rows)
        ]
        numeric_columns = {3, 4, 5, 6}
    return markdown_table(
        headers,
        rows,
        numeric_columns=numeric_columns,
        markdown_alignment=False,
    )


def build_batch_report(
    topology,
    batch_id,
    trials,
    messages,
    target=AUTO_TRIAL_TARGET,
    temperature=None,
):
    trial_count = len(trials)
    successes = sum(1 for trial in trials if trial.get("success"))
    average_time = (
        sum(float(trial.get("time_seconds") or 0) for trial in trials) / trial_count
        if trial_count
        else 0
    )
    average_messages = (
        sum(float(trial.get("total_messages") or 0) for trial in trials) / trial_count
        if trial_count
        else 0
    )
    trials_with_disconnects = sum(1 for trial in trials if trial.get("disconnect_count"))
    total_disconnects = sum(int(trial.get("disconnect_count") or 0) for trial in trials)
    total_paused_seconds = sum(float(trial.get("disconnect_pause_seconds") or 0) for trial in trials)
    completed_generations = sum(int(trial.get("completed_generation_count") or 0) for trial in trials)
    total_thinking_seconds = sum(float(trial.get("total_thinking_time_seconds") or 0) for trial in trials)
    total_response_seconds = sum(float(trial.get("total_visible_response_time_seconds") or 0) for trial in trials)
    total_generation_seconds = sum(float(trial.get("total_generation_time_seconds") or 0) for trial in trials)
    success_rate = successes / trial_count if trial_count else 0
    recipient_rows, fallback_rows = recipient_choice_analysis(messages)
    selected_temperature = temperature
    if selected_temperature is None:
        for trial in trials:
            selected_temperature = (
                trial.get("temperature")
                if trial.get("temperature") is not None
                else (trial.get("ollama_options") or {}).get("temperature")
            )
            if selected_temperature is not None:
                break
    temperature_text = temperature_label(selected_temperature) if selected_temperature is not None else "-"

    lines = [
        f"# {display_topology_name(topology)} auto-trial report",
        "",
        "## Summary",
        "",
        f"- Batch: `{batch_id}`",
        f"- Model: `{EXPECTED_STUDY_MODEL}`",
        f"- Temperature: {temperature_text}",
        f"- Completed trials: {trial_count}/{target}",
        f"- Average time: {average_time:.2f} seconds",
        f"- Average total messages: {average_messages:.2f}",
        f"- Average Gemma 4 thinking time per response: {total_thinking_seconds / completed_generations:.3f} seconds" if completed_generations else "- Average Gemma 4 thinking time per response: 0.000 seconds",
        f"- Average visible-response generation time: {total_response_seconds / completed_generations:.3f} seconds" if completed_generations else "- Average visible-response generation time: 0.000 seconds",
        f"- Average complete generation time: {total_generation_seconds / completed_generations:.3f} seconds" if completed_generations else "- Average complete generation time: 0.000 seconds",
        f"- Success rate: {successes}/{trial_count} ({success_rate * 100:.1f}%)" if trial_count else "- Success rate: 0/0 (0.0%)",
        f"- Reconnect pauses: {total_disconnects} across {trials_with_disconnects} trial(s); {total_paused_seconds:.2f} paused seconds excluded from experiment time",
        "",
    ]
    success_rows = []
    for index, trial in enumerate(trials, start=1):
        result = "Success" if trial.get("success") else "Fail"
        submitted = trial.get("submitted_answer") or trial.get("submitted_figure_status") or "-"
        correct = trial.get("correct_answer") or "-"
        trial_temperature = (
            trial.get("temperature")
            if trial.get("temperature") is not None
            else (trial.get("ollama_options") or {}).get("temperature", selected_temperature)
        )
        trial_temperature_text = temperature_label(trial_temperature) if trial_temperature is not None else "-"
        success_rows.append([
            index,
            trial_temperature_text,
            result,
            submitted,
            correct,
            trial.get("total_messages", 0),
            f"{float(trial.get('time_seconds') or 0):.2f}",
            trial.get("disconnect_count", 0),
            f"{float(trial.get('disconnect_pause_seconds') or 0):.2f}",
        ])
    success_table = markdown_table(
        ["Round", "Temperature", "Result", "Submitted figure", "Correct figure", "Total messages", "Time (seconds)", "Disconnects", "Paused (seconds)"],
        success_rows,
        numeric_columns={0, 1, 5, 6, 7, 8},
        markdown_alignment=False,
    )

    lines.extend([
        "## Recipient-choice probabilities",
        "",
        "Only valid recipients explicitly selected by the model (`target_source = agent`) are included. "
        "Broadcast messages and fallback-assigned recipients are excluded.",
        "Observed probability = times the sender chose this recipient / all valid recipient choices made by that sender.",
        "Uniform expected probability = 1 / number of recipients that sender is allowed to contact.",
        "",
    ])
    if recipient_rows:
        probability_rows = []
        for row in recipient_rows:
            probability_rows.append([
                row["topology"],
                row["sender"],
                row["recipient"],
                row["allowed_recipient_count"],
                row["choices"],
                row["total_model_choices"],
                f"{row['probability'] * 100:.1f}% ({row['probability']:.3f})",
                f"{row['uniform_baseline']:.3f}",
                f"{row['lift']:.3f}",
                f"{row['smoothed_probability']:.3f}",
            ])
        lines.extend([
            "```text",
            *markdown_table(
                ["Topology", "Sender", "Recipient", "Allowed recipients", "Choices", "Total choices", "Observed probability", "Expected probability", "Lift", "Smoothed probability"],
                probability_rows,
                numeric_columns={3, 4, 5, 6, 7, 8, 9},
                markdown_alignment=False,
            ),
            "```",
        ])
    else:
        lines.append("No intentional multi-recipient choices were recorded for this batch.")

    lines.extend(["", "### Excluded fallback routes", ""])
    if fallback_rows:
        lines.extend([
            "```text",
            *markdown_table(
                ["Topology", "Sender", "Target source", "Count"],
                [[row["topology"], row["sender"], row["target_source"], row["count"]] for row in fallback_rows],
                numeric_columns={3},
                markdown_alignment=False,
            ),
            "```",
        ])
    else:
        lines.append("No fallback routes were recorded.")

    lines.extend([
        "",
        "## Success table",
        "",
        "```text",
        *success_table,
        "```",
    ])

    timing_rows = []
    for index, trial in enumerate(trials, start=1):
        timing_rows.append([
            index,
            f"{float(trial.get('trial_wall_time_seconds') or 0):.2f}",
            f"{float(trial.get('trial_active_time_seconds') or 0):.2f}",
            int(trial.get("completed_generation_count") or 0),
            f"{float(trial.get('total_thinking_time_seconds') or 0):.3f}",
            f"{float(trial.get('total_visible_response_time_seconds') or 0):.3f}",
            f"{float(trial.get('total_generation_time_seconds') or 0):.3f}",
            f"{float(trial.get('average_thinking_time_seconds') or 0):.3f}",
            f"{float(trial.get('average_visible_response_time_seconds') or 0):.3f}",
        ])
    lines.extend([
        "",
        "## Gemma 4 timing by trial",
        "",
        "Thinking and visible-response times are measured independently from streamed Ollama chunks.",
        "",
        "```text",
        *markdown_table(
            ["Trial", "Wall time (s)", "Active time (s)", "Responses", "Total thinking (s)", "Total visible response (s)", "Total generation (s)", "Average thinking (s)", "Average visible response (s)"],
            timing_rows,
            numeric_columns=set(range(9)),
            markdown_alignment=False,
        ),
        "```",
    ])

    reconnect_rows = []
    for index, trial in enumerate(trials, start=1):
        for disconnect in trial.get("disconnects") or []:
            reconnect_rows.append([
                index,
                ", ".join(disconnect.get("missing_agents") or []),
                disconnect.get("started_at") or "-",
                disconnect.get("resumed_at") or "-",
                f"{float(disconnect.get('duration_seconds') or 0):.2f}",
            ])
    lines.extend(["", "## Reconnect details", ""])
    if reconnect_rows:
        lines.extend([
            "Paused time is excluded from the trial's experiment-time measurement.",
            "",
            "```text",
            *markdown_table(
                ["Round", "Disconnected Jetsons", "Paused at (UTC)", "Resumed at (UTC)", "Paused (seconds)"],
                reconnect_rows,
                numeric_columns={0, 4},
                markdown_alignment=False,
            ),
            "```",
        ])
    else:
        lines.append("No Jetson disconnects were recorded.")

    return "\n".join(lines) + "\n"


def build_full_study_report(
    study_id,
    batches,
    status,
    target=AUTO_TRIAL_TARGET,
    cooling_options=None,
):
    completed_batches = sum(1 for batch in batches if batch.get("status") == "complete")
    completed_trials = sum(int(batch.get("completed_trials") or 0) for batch in batches)
    total_trials = len(batches) * target
    study_topologies = list(dict.fromkeys(batch.get("topology") for batch in batches if batch.get("topology")))
    study_temperatures = list(dict.fromkeys(
        temperature_label(batch.get("temperature"))
        for batch in batches
        if batch.get("temperature") is not None
    ))
    topology_names = ", ".join(display_topology_name(topology) for topology in study_topologies)
    report_title = f"{topology_names} study report" if len(study_topologies) == 1 else "Leavitt full study report"
    lines = [
        f"# {report_title}",
        "",
        "## Progress",
        "",
        f"- Study: `{study_id}`",
        f"- Status: {status}",
        f"- Completed batches: {completed_batches}/{len(batches)}",
        f"- Completed trials: {completed_trials}/{total_trials}",
        f"- Topologies: {topology_names or '-'}",
        f"- Temperatures: {', '.join(study_temperatures) or '-'}",
        "",
        "## Batch summary",
        "",
    ]
    batch_rows = []
    for batch in batches:
        report_link = (
            f"[{batch['topology']} / temperature {temperature_label(batch['temperature'])}]"
            f"({batch['topology']}/temperature-{temperature_label(batch['temperature'])}/report.md)"
            if batch.get("directory")
            else "-"
        )
        batch_rows.append([
            display_topology_name(batch["topology"]),
            temperature_label(batch["temperature"]),
            batch.get("status", "pending"),
            f"{int(batch.get('completed_trials') or 0)}/{target}",
            f"{float(batch.get('success_rate') or 0) * 100:.1f}% "
            f"({int(batch.get('successes') or 0)}/{int(batch.get('completed_trials') or 0)})",
            f"{float(batch.get('average_messages') or 0):.2f}",
            f"{float(batch.get('average_time_seconds') or 0):.2f}",
            report_link,
        ])
    lines.extend(markdown_table(
        ["Topology", "Temperature", "Status", "Trials", "Success rate", "Average total messages", "Average time (seconds)", "Detailed report"],
        batch_rows,
        numeric_columns={1, 3, 4, 5, 6},
    ))

    all_trials = []
    all_messages = []
    messages_by_temperature = defaultdict(list)
    for batch in batches:
        directory = batch.get("directory")
        if not directory:
            continue
        batch_dir = Path(directory)
        all_trials.extend(load_json_lines(batch_dir / "trials.jsonl"))
        batch_messages = load_json_lines(batch_dir / "messages.jsonl")
        temperature_key = temperature_label(batch.get("temperature"))
        for message in batch_messages:
            tagged_message = dict(message)
            tagged_message.setdefault("topology", batch.get("topology"))
            tagged_message["temperature"] = batch.get("temperature")
            all_messages.append(tagged_message)
            messages_by_temperature[temperature_key].append(tagged_message)

    if all_trials:
        successes = sum(1 for trial in all_trials if trial.get("success"))
        average_time = sum(float(trial.get("time_seconds") or 0) for trial in all_trials) / len(all_trials)
        average_messages = sum(float(trial.get("total_messages") or 0) for trial in all_trials) / len(all_trials)
        total_disconnects = sum(int(trial.get("disconnect_count") or 0) for trial in all_trials)
        trials_with_disconnects = sum(1 for trial in all_trials if trial.get("disconnect_count"))
        total_paused_seconds = sum(float(trial.get("disconnect_pause_seconds") or 0) for trial in all_trials)
        lines.extend([
            "",
            "## Overall results",
            "",
            f"- Completed trials: {len(all_trials)}/{total_trials}",
            f"- Average time: {average_time:.2f} seconds",
            f"- Average total messages: {average_messages:.2f}",
            f"- Success rate: {successes}/{len(all_trials)} ({successes / len(all_trials) * 100:.1f}%)",
            f"- Reconnect pauses: {total_disconnects} across {trials_with_disconnects} trial(s); {total_paused_seconds:.2f} paused seconds excluded from experiment time",
            "",
        ])
        if len(study_topologies) > 1:
            topology_summary_rows = []
            for topology in study_topologies:
                topology_trials = [trial for trial in all_trials if trial.get("topology") == topology]
                topology_successes = sum(1 for trial in topology_trials if trial.get("success"))
                topology_summary_rows.append([
                    display_topology_name(topology),
                    len(topology_trials),
                    topology_successes,
                    f"{topology_successes / len(topology_trials) * 100:.1f}%" if topology_trials else "0.0%",
                    f"{sum(float(trial.get('total_messages') or 0) for trial in topology_trials) / len(topology_trials):.2f}" if topology_trials else "0.00",
                    f"{sum(float(trial.get('time_seconds') or 0) for trial in topology_trials) / len(topology_trials):.2f}" if topology_trials else "0.00",
                ])
            lines.extend([
                "## Topology summary",
                "",
                *markdown_table(
                    ["Topology", "Trials", "Successes", "Success rate", "Average total messages", "Average time (seconds)"],
                    topology_summary_rows,
                    numeric_columns={1, 2, 3, 4, 5},
                ),
                "",
            ])
        lines.extend([
            "## Recipient-choice probabilities by temperature",
            "",
            "Only valid recipients explicitly selected by the model (`target_source = agent`) are included. "
            "Fallback-assigned routes are excluded from these probabilities.",
            "Observed probability = choices of this recipient / all explicit valid recipient choices by the sender at that temperature.",
            "Broadcast is not applicable because every broadcast message is delivered to all other agents.",
            "",
        ])
        temperature_keys = list(dict.fromkeys(
            temperature_label(batch.get("temperature"))
            for batch in batches
            if batch.get("temperature") is not None
        ))
        for temperature_key in temperature_keys:
            temperature_recipient_rows, _ = recipient_choice_analysis(messages_by_temperature[temperature_key])
            lines.extend([f"### Temperature {temperature_key}", ""])
            if temperature_recipient_rows:
                lines.extend([
                    "```text",
                    *recipient_probability_table(
                        temperature_recipient_rows,
                        include_topology=len(study_topologies) > 1,
                    ),
                    "```",
                    "",
                ])
            else:
                lines.extend([
                    "No explicit valid recipient choices were recorded at this temperature.",
                    "",
                ])

        lines.extend([
            "## Overall recipient-choice probabilities",
            "",
            "Only valid recipients explicitly selected by the model (`target_source = agent`) are included. "
            "Fallback-assigned routes are excluded from these probabilities.",
            "Observed probability = choices of this recipient / all explicit valid recipient choices by the sender.",
            "Broadcast is not applicable because every broadcast message is delivered to all other agents.",
            "",
        ])
        recipient_rows, fallback_rows = recipient_choice_analysis(all_messages)
        if recipient_rows:
            lines.extend([
                "```text",
                *recipient_probability_table(recipient_rows, include_topology=len(study_topologies) > 1),
                "```",
            ])
        else:
            lines.append("No explicit valid recipient choices have been recorded yet.")
        lines.extend(["", "### Excluded fallback routes", ""])
        if fallback_rows:
            fallback_headers = ["Sender", "Target source", "Count"]
            rendered_fallback_rows = [[row["sender"], row["target_source"], row["count"]] for row in fallback_rows]
            fallback_numeric_columns = {2}
            if len(study_topologies) > 1:
                fallback_headers.insert(0, "Topology")
                rendered_fallback_rows = [
                    [display_topology_name(row["topology"]), *values]
                    for row, values in zip(fallback_rows, rendered_fallback_rows)
                ]
                fallback_numeric_columns = {3}
            lines.extend([
                "```text",
                *markdown_table(
                    fallback_headers,
                    rendered_fallback_rows,
                    numeric_columns=fallback_numeric_columns,
                    markdown_alignment=False,
                ),
                "```",
            ])
        else:
            lines.append("No fallback routes were recorded.")

    selected_cooling = normalize_cooling_options(cooling_options)
    lines.extend([
        "",
        "## Cooling pauses",
        "",
        f"- Pause between temperature batches: {selected_cooling['between_temperatures_minutes']:g} minutes",
        *(
            [f"- Pause between topologies: {selected_cooling['between_topologies_minutes']:g} minutes"]
            if len(study_topologies) > 1
            else []
        ),
    ])
    return "\n".join(lines) + "\n"


class DashboardExperiment:
    def __init__(self, tcp_host, tcp_port):
        self.tcp_host = tcp_host
        self.tcp_port = tcp_port
        self.clients = {}
        self.turn_order = []
        self.recv_buffers = {}
        self.lock = threading.RLock()
        self.diagnostic_lock = threading.Lock()
        self.events = []
        self.event_id = 0
        self.results = []
        self.running = True
        self.trial_active = False
        self.trial_requested = False
        self.stop_requested = False
        self.auto_trials = False
        self.auto_topology = "circle"
        self.auto_num_agents = 5
        self.auto_discussion_rounds = None
        self.auto_ollama_options = normalize_ollama_options(None)
        self.auto_max_messages = default_max_messages_for_topology(self.auto_topology)
        self.auto_restart_delay = 2
        self.auto_trial_generation = 0
        self.auto_trial_target = AUTO_TRIAL_TARGET
        self.auto_batch_id = None
        self.auto_batch_dir = None
        self.auto_batch_started_at = None
        self.auto_batch_completed = 0
        self.full_study_active = False
        self.full_study_id = None
        self.full_study_kind = None
        self.full_study_label = None
        self.full_study_topologies = []
        self.full_study_dir = None
        self.full_study_started_at = None
        self.full_study_batches = []
        self.full_study_index = -1
        self.full_study_completed_batches = 0
        self.full_study_cooling_options = normalize_cooling_options(None)
        self.full_study_cooling = False
        self.full_study_cooling_kind = None
        self.full_study_cooling_started_at = None
        self.full_study_cooling_until = None
        self.full_study_last_progress_monotonic = None
        self.full_study_watchdog_generation = 0
        self.full_study_reconnect_started_monotonic = None
        self.full_study_reconnect_started_at = None
        self.poweroff_requested = False
        self.poweroff_source = None
        self.poweroff_readiness = None
        self.trial_counter = 0
        self.active_trial_id = None
        self.topology = "circle"
        self.num_agents = 5
        self.discussion_rounds = None
        self.ollama_options = normalize_ollama_options(None)
        self.max_messages = default_max_messages_for_topology(self.topology)
        self.cards = {}
        self.common_symbol = None
        self.circle_neighbors_by_name = {}
        self.circle_last_target_by_speaker = {}
        self.chain_contacts_by_name = {}
        self.chain_last_target_by_speaker = {}
        self.y_contacts_by_name = {}
        self.y_last_target_by_speaker = {}
        self.wheel_contacts_by_name = {}
        self.wheel_last_target_by_speaker = {}
        self.agent_histories = {}
        self.unread_agents = set()
        self.scheduler_queue = []
        self.messages_per_agent = {}
        self.message_count = 0
        self.delivery_count = 0
        self.start_time = None
        self.turn_count = 0
        self.round_number = 1
        self.current_route = None
        self.current_speaker = None
        self.trial_routes = []
        self.trial_model_responses = []
        self.trial_paused = False
        self.trial_pause_started_at = None
        self.trial_pause_started_monotonic = None
        self.trial_pause_total_seconds = 0.0
        self.trial_disconnects = []
        self.reload_batch_id = 0
        self.pending_reload_agents = set()
        self.last_waiting_event_state = None

    def start_tcp_server(self):
        thread = threading.Thread(target=self._tcp_server_loop, daemon=True)
        thread.start()

    def _tcp_server_loop(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.tcp_host, self.tcp_port))
        server_socket.listen(MAX_PARTICIPANTS)
        self.add_event("server", {"message": f"Jetson TCP server listening on {self.tcp_host}:{self.tcp_port}"})

        while self.running:
            client_socket, client_address = server_socket.accept()
            threading.Thread(
                target=self.handle_new_client,
                args=(client_socket, client_address),
                daemon=True,
            ).start()

    def send_json(self, sock, payload):
        try:
            sock.sendall((json.dumps(payload) + "\n").encode("utf-8"))
            return True
        except OSError as exc:
            self.append_server_diagnostic("socket_send_failed", {
                "socket_fileno": sock.fileno(),
                "payload_type": payload.get("type") if isinstance(payload, dict) else None,
                "exception_type": type(exc).__name__,
                "error": str(exc),
            })
            self.drop_client(sock, "send failed")
            return False

    def recv_json(self, sock, timeout=None):
        if timeout is not None:
            sock.settimeout(timeout)
        try:
            buffer = self.recv_buffers.get(sock, b"")
            while b"\n" not in buffer:
                chunk = sock.recv(4096)
                if not chunk:
                    self.drop_client(sock, "disconnected")
                    return None
                buffer += chunk
            line, buffer = buffer.split(b"\n", 1)
            self.recv_buffers[sock] = buffer
            return json.loads(line.decode("utf-8"))
        except socket.timeout:
            return {"type": "timeout"}
        except (json.JSONDecodeError, ConnectionResetError, OSError) as exc:
            self.append_server_diagnostic("socket_receive_failed", {
                "socket_fileno": sock.fileno(),
                "exception_type": type(exc).__name__,
                "error": str(exc),
            })
            self.drop_client(sock, "receive failed")
            return None
        finally:
            try:
                sock.settimeout(None)
            except OSError:
                pass

    def drop_disconnected_clients(self, socks):
        with self.lock:
            candidates = [candidate for candidate in socks if candidate in self.clients]
        if not candidates:
            return
        try:
            readable, _, _ = select.select(candidates, [], [], 0)
        except (OSError, ValueError):
            return
        for candidate in readable:
            try:
                if candidate.recv(1, socket.MSG_PEEK) == b"":
                    self.drop_client(candidate, "disconnected")
            except (BlockingIOError, socket.timeout):
                continue
            except OSError:
                self.drop_client(candidate, "receive failed")

    def recv_turn_response(
        self,
        sock,
        expected_trial_id,
        required_socks=None,
        total_timeout=CLIENT_TURN_TIMEOUT_SECONDS,
    ):
        deadline = time.monotonic() + total_timeout
        required_socks = list(required_socks or [sock])
        while time.monotonic() < deadline:
            self.drop_disconnected_clients(required_socks)
            with self.lock:
                if self.stop_requested:
                    return {"type": "stopped"}
                if any(required_sock not in self.clients for required_sock in required_socks):
                    return {"type": "disconnect"}
            resp = self.recv_json(sock, timeout=1)
            if not resp:
                with self.lock:
                    if sock not in self.clients:
                        return {"type": "disconnect"}
                continue
            if resp.get("type") == "timeout":
                continue
            if resp.get("trial_id") != expected_trial_id:
                self.add_event("stale_response_ignored", {
                    "expected_trial_id": expected_trial_id,
                    "received_trial_id": resp.get("trial_id"),
                    "response_type": resp.get("type"),
                })
                continue
            return resp
        return {"type": "timeout"}

    def drop_client(self, sock, reason):
        with self.lock:
            info = self.clients.pop(sock, None)
            self.recv_buffers.pop(sock, None)
            if sock in self.turn_order:
                self.turn_order.remove(sock)
        try:
            sock.close()
        except OSError:
            pass
        if info:
            self.add_event("client_left", {
                "agent": display_agent_name(info["name"]),
                "hostname": info["hostname"],
                "address": info.get("address"),
                "reason": reason,
            })

    def handle_new_client(self, sock, address):
        self.send_json(sock, {"type": "nickname_request"})
        resp = self.recv_json(sock, timeout=30)
        if not resp or resp.get("type") != "nickname":
            self.drop_client(sock, "invalid handshake")
            return

        # Require the router-reserved peer IP and derive identity from it. The
        # reported hostname is informational and cannot override this mapping.
        peer_ip = address[0]
        hostname = IP_TO_JETSON.get(peer_ip)
        if hostname is None:
            self.send_json(sock, {"type": "system", "text": f"Unconfigured client IP '{peer_ip}'."})
            self.drop_client(sock, "unconfigured client IP")
            return
        model_name = str(resp.get("model_name") or "").strip()[:128]

        with self.lock:
            old_sock = next((s for s, info in self.clients.items() if info.get("name") == hostname), None)
            if old_sock is not None:
                old_info = self.clients.get(old_sock)
                self.clients.pop(old_sock, None)
                self.recv_buffers.pop(old_sock, None)
                if old_sock in self.turn_order:
                    self.turn_order.remove(old_sock)
                try:
                    old_sock.close()
                except OSError:
                    pass
                if old_info:
                    self.add_event("client_left", {
                        "agent": display_agent_name(old_info["name"]),
                        "hostname": old_info["hostname"],
                        "reason": "replaced by new connection",
                    })

            self.clients[sock] = {
                "name": hostname,
                "hostname": hostname,
                "address": address,
                "model_name": model_name,
            }
            self.turn_order.append(sock)
            reload_completed = hostname in self.pending_reload_agents
            if reload_completed:
                self.pending_reload_agents.remove(hostname)
            pending_reload = [display_agent_name(name) for name in sorted(self.pending_reload_agents)]

        self.send_json(sock, {
            "type": "welcome",
            "agent_name": display_agent_name(hostname),
            "hostname": hostname,
            "text": f"Welcome {display_agent_name(hostname)} ({hostname}). Waiting for next trial start...",
        })
        self.add_event("client_joined", {
            "agent": display_agent_name(hostname),
            "hostname": hostname,
            "address": address,
            "model_name": model_name,
            "reloaded": reload_completed,
        })
        if reload_completed:
            self.add_event("client_reload_completed", {
                "agent": display_agent_name(hostname),
                "hostname": hostname,
                "pending": pending_reload,
            })
            if not pending_reload:
                self.add_event("clients_reload_finished", {"message": "All requested Jetsons reconnected."})

    def add_event(self, kind, payload):
        with self.lock:
            if self.full_study_active and kind in STUDY_PROGRESS_EVENTS:
                self.full_study_last_progress_monotonic = time.monotonic()
            self.event_id += 1
            event = {
                "id": self.event_id,
                "time": round(time.time(), 3),
                "kind": kind,
                "payload": payload,
                "snapshot": self.snapshot_locked(),
            }
            self.events.append(event)
            self.events = self.events[-300:]
        print(f"[{kind}] {payload}", flush=True)
        if kind in DIAGNOSTIC_EVENT_KINDS:
            self.append_server_diagnostic(kind, payload, event_id=event["id"])

    def append_server_diagnostic(self, event, payload=None, **details):
        """Persist compact forensic events independently of the dashboard buffer."""
        with self.lock:
            study_dir = self.full_study_dir
            record = {
                "recorded_at": datetime.now(timezone.utc).isoformat(),
                "monotonic_seconds": round(time.monotonic(), 6),
                "event": event,
                "study_id": self.full_study_id,
                "study_kind": self.full_study_kind,
                "batch_id": self.auto_batch_id,
                "trial_id": self.active_trial_id,
                "topology": self.topology,
                "temperature": self.ollama_options.get("temperature"),
                "current_speaker": self.current_speaker,
                "message_count": self.message_count,
                "connected_agents": sorted(
                    display_agent_name(info["name"])
                    for info in self.clients.values()
                ),
                "payload": payload or {},
                **details,
            }
        path = (
            study_dir / "diagnostics" / "server-events.jsonl"
            if study_dir
            else DATA_ROOT / "diagnostics" / "server-events.jsonl"
        )
        try:
            with self.diagnostic_lock:
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open("a", encoding="utf-8") as output:
                    output.write(json.dumps(record, sort_keys=True, default=str) + "\n")
                    output.flush()
        except OSError as exc:
            print(f"[DIAGNOSTIC WARN] Could not write {path}: {exc}", flush=True)

    def start_study_watchdog(self, generation):
        threading.Thread(
            target=self.run_study_watchdog,
            args=(generation,),
            daemon=True,
        ).start()

    def run_study_watchdog(self, generation):
        while True:
            wait_started = None
            wait_restored = False
            with self.lock:
                if generation != self.full_study_watchdog_generation or not self.full_study_active:
                    return
                missing_agents = self.missing_fixed_five_agents_locked()
                if not missing_agents:
                    wait_restored = self.full_study_reconnect_started_monotonic is not None
                    self.full_study_reconnect_started_monotonic = None
                    self.full_study_reconnect_started_at = None
                else:
                    if self.full_study_reconnect_started_monotonic is None:
                        self.full_study_reconnect_started_monotonic = time.monotonic()
                        self.full_study_reconnect_started_at = datetime.now(timezone.utc).isoformat()
                        wait_started = {
                            "missing": [display_agent_name(name) for name in missing_agents],
                            "started_at": self.full_study_reconnect_started_at,
                            "message": "The study is paused and will wait indefinitely for every Jetson to reconnect.",
                        }

            if wait_started:
                self.add_event("study_reconnect_wait_started", wait_started)
            if wait_restored:
                self.add_event("study_reconnect_restored", {
                    "message": "All five Jetsons reconnected. The study will continue.",
                })
            time.sleep(5)

    def snapshot_locked(self):
        connected = []
        for info in self.clients.values():
            name = info["name"]
            connected.append({
                "name": display_agent_name(name),
                "hostname": info["hostname"],
                "model": info.get("model_name", ""),
                "symbols": self.cards.get(name, []),
                "neighbors": [display_agent_name(n) for n in self.circle_neighbors_by_name.get(name, [])],
                "chainContacts": [display_agent_name(n) for n in self.chain_contacts_by_name.get(name, [])],
                "yContacts": [display_agent_name(n) for n in self.y_contacts_by_name.get(name, [])],
                "wheelRecipients": [display_agent_name(n) for n in self.wheel_contacts_by_name.get(name, [])],
            })
        connected.sort(key=lambda item: get_agent_id(item["name"]) or 999)
        return {
            "connected": connected,
            "trialActive": self.trial_active,
            "trialRequested": self.trial_requested,
            "stopRequested": self.stop_requested,
            "autoTrials": self.auto_trials,
            "autoTrialTarget": self.auto_trial_target,
            "autoTrialCompleted": self.auto_batch_completed,
            "autoBatchId": self.auto_batch_id,
            "fullStudyActive": self.full_study_active,
            "fullStudyId": self.full_study_id,
            "fullStudyKind": self.full_study_kind,
            "fullStudyLabel": self.full_study_label,
            "fullStudyTopologies": self.full_study_topologies,
            "fullStudyDirectory": str(self.full_study_dir) if self.full_study_dir else None,
            "fullStudyBatch": self.full_study_index + 1 if self.full_study_index >= 0 else 0,
            "fullStudyCompletedBatches": self.full_study_completed_batches,
            "fullStudyBatchCount": len(self.full_study_batches) or FULL_STUDY_BATCH_COUNT,
            "fullStudyTotalTrials": (len(self.full_study_batches) or FULL_STUDY_BATCH_COUNT) * AUTO_TRIAL_TARGET,
            "fullStudyCooling": self.full_study_cooling,
            "fullStudyCoolingKind": self.full_study_cooling_kind,
            "fullStudyCoolingStartedAt": self.full_study_cooling_started_at,
            "fullStudyCoolingUntil": self.full_study_cooling_until,
            "fullStudyCoolingOptions": self.full_study_cooling_options,
            "fullStudyReconnectStartedAt": self.full_study_reconnect_started_at,
            "fullStudyReconnectTimeoutSeconds": None,
            "trialPaused": self.trial_paused,
            "trialPauseStartedAt": self.trial_pause_started_at,
            "trialPauseTotalSeconds": round(self.trial_pause_total_seconds, 2),
            "poweroffRequested": self.poweroff_requested,
            "poweroffSource": self.poweroff_source,
            "poweroffReadiness": self.poweroff_readiness,
            "topology": self.topology,
            "numAgents": self.num_agents,
            "discussionRounds": self.discussion_rounds,
            "ollamaOptions": self.ollama_options,
            "maxMessages": self.max_messages,
            "round": self.round_number,
            "messages": self.message_count,
            "deliveries": self.delivery_count,
            "turns": self.turn_count,
            "commonSymbol": self.common_symbol,
            "currentRoute": self.current_route,
            "currentSpeaker": self.current_speaker,
            "results": self.results[-50:],
        }

    def snapshot(self):
        with self.lock:
            return self.snapshot_locked()

    def begin_auto_batch_locked(self):
        timestamp = run_identifier()
        if self.full_study_active and self.full_study_dir and self.full_study_index >= 0:
            batch = self.full_study_batches[self.full_study_index]
            batch_id = f"{self.auto_topology}-temperature-{temperature_label(self.auto_ollama_options['temperature'])}"
            batch_dir = self.full_study_dir / self.auto_topology / f"temperature-{temperature_label(self.auto_ollama_options['temperature'])}"
            batch_dir.mkdir(parents=True, exist_ok=False)
            batch["status"] = "running"
            batch["batch_id"] = batch_id
            batch["directory"] = str(batch_dir)
        else:
            topology_dir = DATA_ROOT / self.auto_topology
            topology_dir.mkdir(parents=True, exist_ok=True)
            batch_id = timestamp
            batch_dir = topology_dir / batch_id
            suffix = 2
            while batch_dir.exists():
                batch_dir = topology_dir / f"{batch_id}_{suffix}"
                suffix += 1
            batch_dir.mkdir(parents=True)

        self.auto_batch_id = batch_dir.name
        self.auto_batch_dir = batch_dir
        self.auto_batch_started_at = datetime.now(timezone.utc).isoformat()
        self.auto_batch_completed = 0
        self.results = []
        metadata = {
            "batch_id": self.auto_batch_id,
            "model": EXPECTED_STUDY_MODEL,
            "topology": self.auto_topology,
            "target_trials": self.auto_trial_target,
            "ollama_restart_interval_trials": OLLAMA_RESTART_INTERVAL_TRIALS,
            "ollama_warmup_model": OLLAMA_MODEL_NAME,
            "ollama_warmup_timeout_seconds_per_attempt": OLLAMA_WARMUP_TIMEOUT_SECONDS,
            "completed_trials": 0,
            "status": "running",
            "started_at": self.auto_batch_started_at,
            "ollama_options": self.auto_ollama_options,
            "max_messages_per_trial": self.auto_max_messages,
            "num_agents": self.auto_num_agents,
        }
        atomic_write_json(batch_dir / "metadata.json", metadata)
        atomic_write_text(
            batch_dir / "report.md",
            build_batch_report(
                self.auto_topology,
                self.auto_batch_id,
                [],
                [],
                self.auto_trial_target,
                self.auto_ollama_options.get("temperature"),
            ),
        )

    def write_full_study_files_locked(self, status=None):
        if not self.full_study_dir:
            return
        selected_status = status or ("running" if self.full_study_active else "complete")
        metadata = {
            "study_id": self.full_study_id,
            "model": EXPECTED_STUDY_MODEL,
            "study_kind": self.full_study_kind,
            "study_label": self.full_study_label,
            "topologies": self.full_study_topologies,
            "status": selected_status,
            "started_at": self.full_study_started_at,
            "completed_at": datetime.now(timezone.utc).isoformat() if selected_status == "complete" else None,
            "target_trials_per_batch": AUTO_TRIAL_TARGET,
            "ollama_restart_interval_trials": OLLAMA_RESTART_INTERVAL_TRIALS,
            "ollama_warmup_model": OLLAMA_MODEL_NAME,
            "ollama_warmup_timeout_seconds_per_attempt": OLLAMA_WARMUP_TIMEOUT_SECONDS,
            "total_batches": len(self.full_study_batches),
            "completed_batches": self.full_study_completed_batches,
            "total_trials": len(self.full_study_batches) * AUTO_TRIAL_TARGET,
            "cooling_options": self.full_study_cooling_options,
            "cooling": {
                "active": self.full_study_cooling,
                "kind": self.full_study_cooling_kind,
                "started_at": self.full_study_cooling_started_at,
                "until": self.full_study_cooling_until,
            },
            "batches": self.full_study_batches,
        }
        if self.full_study_kind == "four_topologies":
            metadata["formatted_data_file"] = "gemma4-50trials-data.txt"
        atomic_write_json(self.full_study_dir / "metadata.json", metadata)
        report_text = build_full_study_report(
            self.full_study_id,
            self.full_study_batches,
            selected_status,
            AUTO_TRIAL_TARGET,
            self.full_study_cooling_options,
        )
        atomic_write_text(self.full_study_dir / "report.md", report_text)
        if self.full_study_kind == "four_topologies":
            atomic_write_text(self.full_study_dir / "gemma4-50trials-data.txt", report_text)

    def configure_full_study_batch_locked(self, index):
        batch = self.full_study_batches[index]
        self.full_study_index = index
        self.auto_topology = batch["topology"]
        self.auto_num_agents = MAX_PARTICIPANTS
        self.auto_discussion_rounds = None
        options = dict(batch["ollama_options"])
        options["temperature"] = batch["temperature"]
        self.auto_ollama_options = normalize_ollama_options(options)
        self.auto_max_messages = default_max_messages_for_topology(self.auto_topology)
        self.auto_trial_target = AUTO_TRIAL_TARGET
        self.auto_trials = True
        self.begin_auto_batch_locked()
        self.write_full_study_files_locked("running")

    def run_full_study_cooling_pause(self, next_index, pause_kind, pause_seconds, generation, after_batch):
        deadline = time.monotonic() + pause_seconds
        restart_ok, restart_message = self.restart_ollama_for_study(
            generation,
            after_batch=after_batch,
        )
        if not restart_ok:
            with self.lock:
                if generation != self.auto_trial_generation or not self.full_study_active:
                    return
                self.full_study_active = False
                self.auto_trials = False
                self.full_study_cooling = False
                self.full_study_cooling_kind = None
                self.full_study_cooling_until = None
                self.write_full_study_files_locked("failed")
            self.add_event("full_study_failed", {
                "study_id": self.full_study_id,
                "study_kind": self.full_study_kind,
                "study_label": self.full_study_label,
                "message": restart_message,
                "directory": str(self.full_study_dir),
            })
            return

        while True:
            with self.lock:
                if generation != self.auto_trial_generation or not self.full_study_active:
                    return
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                break
            time.sleep(min(1, remaining))

        warmup_ok, _ = self.warm_ollama_for_study(
            generation,
            after_batch=after_batch,
        )
        if not warmup_ok:
            return

        try:
            with self.lock:
                if generation != self.auto_trial_generation or not self.full_study_active:
                    return
                self.full_study_cooling = False
                self.full_study_cooling_kind = None
                self.full_study_cooling_started_at = None
                self.full_study_cooling_until = None
                self.configure_full_study_batch_locked(next_index)
                next_batch = dict(self.full_study_batches[next_index])
        except OSError as exc:
            with self.lock:
                self.full_study_active = False
                self.auto_trials = False
                self.full_study_cooling = False
                self.full_study_batches[next_index]["status"] = "failed_to_start"
                self.write_full_study_files_locked("failed")
            self.add_event("full_study_failed", {
                "study_id": self.full_study_id,
                "study_kind": self.full_study_kind,
                "study_label": self.full_study_label,
                "message": str(exc),
                "directory": str(self.full_study_dir),
            })
            self.request_poweroff_all(
                source=f"{self.full_study_kind or 'automated'}_study_failed",
                delay=STUDY_STOP_FAILURE_POWEROFF_DELAY_SECONDS,
            )
            return

        self.add_event("full_study_batch_started", {
            "study_id": self.full_study_id,
            "batch": next_index + 1,
            "total_batches": len(self.full_study_batches),
            "topology": next_batch["topology"],
            "temperature": next_batch["temperature"],
        })
        self.schedule_next_auto_trial(delay=0, generation=generation)

    def check_ollama_restart_readiness(self, emit_event=True):
        """Verify SSH and exact passwordless sudo permissions without restarting anything."""
        def check_client(host):
            address = JETSON_ADDRESSES[host]
            remote_command = (
                f"{REMOTE_SUDO} -n -l {REMOTE_SYSTEMCTL} restart {OLLAMA_SERVICE} >/dev/null 2>&1"
            )
            command = [
                "ssh",
                "-o", "BatchMode=yes",
                "-o", "ConnectTimeout=8",
                f"{JETSON_SSH_USER}@{address}",
                remote_command,
            ]
            try:
                result = subprocess.run(command, capture_output=True, text=True, timeout=12)
                detail = result.stderr.strip() or result.stdout.strip()
                return {
                    "hostname": host,
                    "address": address,
                    "ready": result.returncode == 0,
                    "reason": "ready" if result.returncode == 0 else (
                        detail or "Passwordless sudo permission is missing."
                    ),
                }
            except (OSError, subprocess.TimeoutExpired) as exc:
                return {"hostname": host, "address": address, "ready": False, "reason": str(exc)}

        clients = []
        with ThreadPoolExecutor(max_workers=len(JETSON_HOSTNAMES)) as executor:
            futures = [executor.submit(check_client, host) for host in JETSON_HOSTNAMES]
            for future in as_completed(futures):
                clients.append(future.result())
        clients.sort(key=lambda item: get_jetson_number(item["hostname"]) or 999)
        ready = all(client["ready"] for client in clients)
        readiness = {
            "ready": ready,
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "clients": clients,
        }
        if emit_event:
            self.add_event("ollama_restart_readiness", readiness)
        return ready, readiness

    def restart_ollama_for_study(self, generation, after_batch=None, after_trial=None):
        """Restart Ollama and wait indefinitely for every Jetson, unless the run is stopped."""
        restart_point = (
            f"trial {after_trial} of the current condition"
            if after_trial is not None
            else f"completed batch {after_batch}"
        )
        self.add_event("ollama_batch_restart_started", {
            "after_batch": after_batch,
            "after_trial": after_trial,
            "services": [OLLAMA_SERVICE],
            "message": f"Restarting Ollama on all Jetsons after {restart_point}.",
        })

        def restart_client(host):
            address = JETSON_ADDRESSES[host]
            remote_command = f"{REMOTE_SUDO} -n {REMOTE_SYSTEMCTL} restart {OLLAMA_SERVICE}"
            command = [
                "ssh",
                "-o", "BatchMode=yes",
                "-o", "ConnectTimeout=8",
                f"{JETSON_SSH_USER}@{address}",
                remote_command,
            ]
            try:
                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    timeout=OLLAMA_RESTART_COMMAND_TIMEOUT_SECONDS,
                )
                detail = result.stderr.strip() or result.stdout.strip()
                return {
                    "hostname": host,
                    "address": address,
                    "ok": result.returncode == 0,
                    "reason": "Ollama restart command accepted" if result.returncode == 0 else (
                        detail or f"ssh exited {result.returncode}"
                    ),
                }
            except (OSError, subprocess.TimeoutExpired) as exc:
                return {"hostname": host, "address": address, "ok": False, "reason": str(exc)}

        def run_is_active():
            with self.lock:
                return generation == self.auto_trial_generation and (
                    self.full_study_active or self.auto_trials
                )

        def wait_before_retry():
            deadline = time.monotonic() + OLLAMA_RESTART_RETRY_SECONDS
            while time.monotonic() < deadline:
                if not run_is_active():
                    return False
                time.sleep(max(0, min(1, deadline - time.monotonic())))
            return True

        pending_restart = set(JETSON_HOSTNAMES)
        restart_results = {}
        restart_attempts = Counter()
        last_wait_event = 0.0
        while pending_restart:
            if not run_is_active():
                return False, "Automated run stopped while Ollama was restarting."
            with ThreadPoolExecutor(max_workers=len(pending_restart)) as executor:
                checks = {executor.submit(restart_client, host): host for host in pending_restart}
                for future in as_completed(checks):
                    result = future.result()
                    host = checks[future]
                    restart_attempts[host] += 1
                    restart_results[host] = result
                    if result["ok"]:
                        pending_restart.discard(host)
                        self.add_event("ollama_batch_restart_host_finished", {
                            "after_batch": after_batch,
                            "after_trial": after_trial,
                            "attempts": restart_attempts[host],
                            **result,
                        })
            if pending_restart:
                now = time.monotonic()
                if last_wait_event == 0.0 or now - last_wait_event >= OLLAMA_RESTART_WAIT_STATUS_SECONDS:
                    self.add_event("ollama_batch_restart_waiting", {
                        "after_batch": after_batch,
                        "after_trial": after_trial,
                        "phase": "restart_command",
                        "pending": [
                            {
                                "hostname": host,
                                "attempts": restart_attempts[host],
                                "reason": restart_results[host]["reason"],
                            }
                            for host in sorted(pending_restart)
                        ],
                        "message": "Waiting for Jetsons to accept the Ollama restart; retrying automatically.",
                    })
                    last_wait_event = now
                if not wait_before_retry():
                    return False, "Automated run stopped while Ollama was restarting."

        def ollama_is_ready(host):
            address = JETSON_ADDRESSES[host]
            remote_command = (
                f"{REMOTE_SYSTEMCTL} is-active --quiet {OLLAMA_SERVICE} && "
                "/usr/bin/curl --fail --silent --max-time 3 "
                "http://127.0.0.1:11434/api/tags >/dev/null"
            )
            command = [
                "ssh",
                "-o", "BatchMode=yes",
                "-o", "ConnectTimeout=8",
                f"{JETSON_SSH_USER}@{address}",
                remote_command,
            ]
            try:
                result = subprocess.run(command, capture_output=True, text=True, timeout=12)
                return result.returncode == 0
            except (OSError, subprocess.TimeoutExpired):
                return False

        pending = set(JETSON_HOSTNAMES)
        last_wait_event = 0.0
        while pending:
            if not run_is_active():
                return False, "Automated run stopped while Ollama was restarting."
            with ThreadPoolExecutor(max_workers=len(pending)) as executor:
                checks = {executor.submit(ollama_is_ready, host): host for host in pending}
                for future in as_completed(checks):
                    if future.result():
                        pending.discard(checks[future])
            if not pending:
                self.add_event("ollama_batch_restart_completed", {
                    "after_batch": after_batch,
                    "after_trial": after_trial,
                    "clients": [display_agent_name(host) for host in JETSON_HOSTNAMES],
                    "message": "Ollama restarted and its local API is healthy on all five Jetsons; client TCP connections were preserved.",
                })
                return True, "Ollama restart complete."
            now = time.monotonic()
            if last_wait_event == 0.0 or now - last_wait_event >= OLLAMA_RESTART_WAIT_STATUS_SECONDS:
                self.add_event("ollama_batch_restart_waiting", {
                    "after_batch": after_batch,
                    "after_trial": after_trial,
                    "phase": "api_recovery",
                    "pending": [{"hostname": host} for host in sorted(pending)],
                    "message": "Waiting for the local Ollama API on every Jetson; the study remains paused.",
                })
                last_wait_event = now
            if not wait_before_retry():
                return False, "Automated run stopped while waiting for Ollama recovery."

    def warm_ollama_for_study(self, generation, after_batch=None, after_trial=None):
        """Preload Gemma 4 everywhere; retry failed hosts until all succeed."""
        payload = json.dumps({
            "model": OLLAMA_MODEL_NAME,
            "prompt": "",
            "stream": False,
            "think": False,
            "keep_alive": -1,
        })
        self.add_event("ollama_warmup_started", {
            "after_batch": after_batch,
            "after_trial": after_trial,
            "model": OLLAMA_MODEL_NAME,
            "timeout_seconds_per_attempt": OLLAMA_WARMUP_TIMEOUT_SECONDS,
            "message": "Preloading Gemma 4 on all five Jetsons before experimental timing resumes.",
        })

        def run_is_active():
            with self.lock:
                return generation == self.auto_trial_generation and (
                    self.full_study_active or self.auto_trials
                )

        def warm_client(host):
            address = JETSON_ADDRESSES[host]
            remote_command = (
                "/usr/bin/curl --fail --silent --show-error "
                f"--max-time {OLLAMA_WARMUP_TIMEOUT_SECONDS} "
                "-H 'Content-Type: application/json' --data-binary @- "
                "http://127.0.0.1:11434/api/generate"
            )
            command = [
                "ssh",
                "-o", "BatchMode=yes",
                "-o", "ConnectTimeout=8",
                f"{JETSON_SSH_USER}@{address}",
                remote_command,
            ]
            started = time.monotonic()
            try:
                result = subprocess.run(
                    command,
                    input=payload,
                    capture_output=True,
                    text=True,
                    timeout=OLLAMA_WARMUP_TIMEOUT_SECONDS + 15,
                )
                detail = result.stderr.strip()
                response = None
                if result.returncode == 0:
                    try:
                        response = json.loads(result.stdout)
                    except (TypeError, json.JSONDecodeError):
                        detail = "Ollama returned an invalid warm-up response."
                ok = (
                    result.returncode == 0
                    and isinstance(response, dict)
                    and response.get("done") is True
                    and not response.get("error")
                )
                if not ok and not detail:
                    detail = (
                        str(response.get("error"))
                        if isinstance(response, dict) and response.get("error")
                        else f"Warm-up exited {result.returncode} without a completed response."
                    )
                return {
                    "hostname": host,
                    "address": address,
                    "ok": ok,
                    "reason": "Gemma 4 warm-up complete" if ok else detail,
                    "duration_seconds": round(time.monotonic() - started, 3),
                }
            except (OSError, subprocess.TimeoutExpired) as exc:
                return {
                    "hostname": host,
                    "address": address,
                    "ok": False,
                    "reason": str(exc),
                    "duration_seconds": round(time.monotonic() - started, 3),
                }

        pending = set(JETSON_HOSTNAMES)
        attempts = Counter()
        latest_results = {}
        last_wait_event = 0.0
        while pending:
            if not run_is_active():
                return False, "Automated run stopped while Gemma 4 was warming up."
            with ThreadPoolExecutor(max_workers=len(pending)) as executor:
                checks = {executor.submit(warm_client, host): host for host in pending}
                for future in as_completed(checks):
                    host = checks[future]
                    result = future.result()
                    attempts[host] += 1
                    latest_results[host] = result
                    if result["ok"]:
                        pending.discard(host)
                        self.add_event("ollama_warmup_host_finished", {
                            "after_batch": after_batch,
                            "after_trial": after_trial,
                            "attempts": attempts[host],
                            **result,
                        })
            if not pending:
                self.add_event("ollama_warmup_completed", {
                    "after_batch": after_batch,
                    "after_trial": after_trial,
                    "model": OLLAMA_MODEL_NAME,
                    "message": "Gemma 4 is loaded on all five Jetsons; experimental trials may resume.",
                })
                return True, "Gemma 4 warm-up complete."

            now = time.monotonic()
            if last_wait_event == 0.0 or now - last_wait_event >= OLLAMA_RESTART_WAIT_STATUS_SECONDS:
                self.add_event("ollama_warmup_waiting", {
                    "after_batch": after_batch,
                    "after_trial": after_trial,
                    "pending": [
                        {
                            "hostname": host,
                            "attempts": attempts[host],
                            "reason": latest_results[host]["reason"],
                        }
                        for host in sorted(pending)
                    ],
                    "message": "The study remains paused while pending Gemma 4 warm-ups retry.",
                })
                last_wait_event = now

            retry_deadline = time.monotonic() + OLLAMA_RESTART_RETRY_SECONDS
            while time.monotonic() < retry_deadline:
                if not run_is_active():
                    return False, "Automated run stopped while Gemma 4 was warming up."
                time.sleep(max(0, min(1, retry_deadline - time.monotonic())))

    def run_mid_batch_ollama_restart(self, generation, after_trial):
        restart_ok, restart_message = self.restart_ollama_for_study(
            generation,
            after_trial=after_trial,
        )
        if restart_ok:
            restart_ok, restart_message = self.warm_ollama_for_study(
                generation,
                after_trial=after_trial,
            )
        if not restart_ok:
            with self.lock:
                if generation != self.auto_trial_generation:
                    return
                self.auto_trials = False
                full_study_failed = self.full_study_active
                if full_study_failed:
                    self.full_study_active = False
                    self.write_full_study_files_locked("failed")
            if full_study_failed:
                self.add_event("full_study_failed", {
                    "study_id": self.full_study_id,
                    "study_kind": self.full_study_kind,
                    "study_label": self.full_study_label,
                    "message": restart_message,
                    "directory": str(self.full_study_dir) if self.full_study_dir else None,
                })
            else:
                self.add_event("auto_trials_restart_failed", {
                    "batch_id": self.auto_batch_id,
                    "message": restart_message,
                })
            return
        with self.lock:
            if generation != self.auto_trial_generation or not self.auto_trials:
                return
        self.schedule_next_auto_trial(delay=0, generation=generation)

    def advance_full_study(self):
        with self.lock:
            if not self.full_study_active or self.full_study_index < 0:
                return False, False, None
            batch = self.full_study_batches[self.full_study_index]
            trials = load_json_lines(self.auto_batch_dir / "trials.jsonl")
            batch["status"] = "complete"
            batch["completed_trials"] = len(trials)
            batch["successes"] = sum(1 for trial in trials if trial.get("success"))
            batch["success_rate"] = batch["successes"] / len(trials) if trials else 0
            batch["average_messages"] = (
                sum(float(trial.get("total_messages") or 0) for trial in trials) / len(trials)
                if trials else 0
            )
            batch["average_time_seconds"] = (
                sum(float(trial.get("time_seconds") or 0) for trial in trials) / len(trials)
                if trials else 0
            )
            self.full_study_completed_batches = self.full_study_index + 1
            next_index = self.full_study_index + 1
            if next_index >= len(self.full_study_batches):
                self.full_study_active = False
                self.auto_trials = False
                self.full_study_cooling = False
                self.write_full_study_files_locked("complete")
                return False, True, None
            current_topology = batch["topology"]
            next_topology = self.full_study_batches[next_index]["topology"]
            pause_kind = "temperature" if next_topology == current_topology else "topology"
            pause_minutes = (
                self.full_study_cooling_options["between_temperatures_minutes"]
                if pause_kind == "temperature"
                else self.full_study_cooling_options["between_topologies_minutes"]
            )
            pause_seconds = pause_minutes * 60
            self.full_study_cooling = True
            self.full_study_cooling_kind = pause_kind
            self.full_study_cooling_started_at = datetime.now(timezone.utc).isoformat()
            self.full_study_cooling_until = datetime.fromtimestamp(
                time.time() + pause_seconds,
                timezone.utc,
            ).isoformat()
            self.write_full_study_files_locked("running")
            self.auto_trial_generation += 1
            generation = self.auto_trial_generation
            after_batch = self.full_study_index + 1
        threading.Thread(
            target=self.run_full_study_cooling_pause,
            args=(next_index, pause_kind, pause_seconds, generation, after_batch),
            daemon=True,
        ).start()
        return True, False, None

    def persist_auto_batch_trial(self, result, routes):
        with self.lock:
            if not self.auto_trials or result.get("stopped") or not self.auto_batch_dir:
                return False, None
            batch_dir = self.auto_batch_dir
            batch_id = self.auto_batch_id
            topology = self.auto_topology
            batch_round = self.auto_batch_completed + 1
            started_at = self.auto_batch_started_at

        saved_result = dict(result)
        saved_result["batch_id"] = batch_id
        saved_result["batch_round"] = batch_round
        saved_routes = []
        for route in routes:
            saved_route = dict(route)
            saved_route["trial_id"] = result.get("trial_id")
            saved_route["batch_id"] = batch_id
            saved_route["batch_round"] = batch_round
            saved_routes.append(saved_route)

        try:
            append_json_line(batch_dir / "trials.jsonl", saved_result)
            append_json_lines(batch_dir / "messages.jsonl", saved_routes)
            trials = load_json_lines(batch_dir / "trials.jsonl")
            batch_complete = len(trials) >= self.auto_trial_target
            checkpoint_due = batch_complete or len(trials) % REPORT_CHECKPOINT_INTERVAL_TRIALS == 0
            if checkpoint_due:
                messages = load_json_lines(batch_dir / "messages.jsonl")
                atomic_write_text(
                    batch_dir / "report.md",
                    build_batch_report(
                        topology,
                        batch_id,
                        trials,
                        messages,
                        self.auto_trial_target,
                        self.auto_ollama_options.get("temperature"),
                    ),
                )
                atomic_write_json(batch_dir / "metadata.json", {
                    "batch_id": batch_id,
                    "model": EXPECTED_STUDY_MODEL,
                    "topology": topology,
                    "target_trials": self.auto_trial_target,
                    "ollama_restart_interval_trials": OLLAMA_RESTART_INTERVAL_TRIALS,
                    "completed_trials": len(trials),
                    "status": "complete" if batch_complete else "running",
                    "started_at": started_at,
                    "completed_at": datetime.now(timezone.utc).isoformat() if batch_complete else None,
                    "ollama_options": self.auto_ollama_options,
                    "max_messages_per_trial": self.auto_max_messages,
                    "num_agents": self.auto_num_agents,
                })
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            with self.lock:
                self.auto_trials = False
                self.auto_trial_generation += 1
            return False, str(exc)

        with self.lock:
            if self.auto_batch_id != batch_id:
                return False, "Auto-trial batch changed while saving a result."
            self.auto_batch_completed = len(trials)
            if batch_complete:
                self.auto_trials = False
                self.auto_trial_generation += 1
        result["batch_id"] = batch_id
        result["batch_round"] = batch_round
        return batch_complete, None

    def missing_fixed_five_agents_locked(self):
        connected_names = {info["name"] for info in self.clients.values()}
        return [
            f"jetson{number}"
            for number in range(1, MAX_PARTICIPANTS + 1)
            if f"jetson{number}" not in connected_names
        ]

    def start_trial(self, topology, num_agents, discussion_rounds=None, ollama_options=None, max_messages=None, automated=False):
        with self.lock:
            if (
                self.trial_active
                or self.trial_requested
                or ((self.auto_trials or self.full_study_active) and not automated)
            ):
                return False, "A trial is already running or waiting for Jetsons."
            self.stop_requested = False
            self.topology = topology if topology in VALID_TOPOLOGIES else "circle"
            if self.topology in FIXED_FIVE_AGENT_TOPOLOGIES:
                self.num_agents = MAX_PARTICIPANTS
                missing_agents = self.missing_fixed_five_agents_locked()
                if missing_agents:
                    missing_display = ", ".join(display_agent_name(name) for name in missing_agents)
                    return False, (
                        f"{display_topology_name(self.topology)} requires all 5 Jetsons connected. "
                        f"Missing: {missing_display}."
                    )
            else:
                self.num_agents = max(MIN_PARTICIPANTS, min(MAX_PARTICIPANTS, int(num_agents)))
            self.discussion_rounds = None
            self.ollama_options = normalize_ollama_options(ollama_options)
            self.max_messages = normalize_max_messages(max_messages, self.topology)
            self.trial_requested = True
        threading.Thread(target=self.run_experiment, daemon=True).start()
        self.add_event("trial_requested", {
            "topology": self.topology,
            "num_agents": self.num_agents,
            "discussion_rounds": None,
            "ollama_options": self.ollama_options,
            "max_messages": self.max_messages,
        })
        return True, "Trial requested."

    def stop_trial(self):
        with self.lock:
            auto_was_enabled = self.auto_trials or self.full_study_active
            automated_study_was_active = self.full_study_active
            if not self.trial_active and not self.trial_requested and not auto_was_enabled:
                return False, "No active trial to stop."
            if self.trial_active or self.trial_requested:
                self.stop_requested = True
            self.auto_trials = False
            if self.full_study_active:
                self.full_study_active = False
                self.full_study_watchdog_generation += 1
                self.full_study_cooling = False
                self.full_study_cooling_kind = None
                self.full_study_cooling_until = None
                if 0 <= self.full_study_index < len(self.full_study_batches):
                    current_batch = self.full_study_batches[self.full_study_index]
                    if current_batch.get("status") == "running":
                        current_batch["status"] = "stopped"
                self.write_full_study_files_locked("stopped")
            self.auto_trial_generation += 1
            targets = list(self.clients.keys()) if self.trial_active or self.trial_requested else []
            trial_id = self.active_trial_id
        for sock in targets:
            self.send_json(sock, {"type": "experiment_stop", "trial_id": trial_id})
        message = "Trial stop requested. Auto trials disabled." if targets else "Auto trials disabled."
        self.add_event("trial_stop_requested", {"message": message})
        if automated_study_was_active:
            self.request_poweroff_all(
                source=f"{self.full_study_kind or 'automated'}_study_stopped",
                delay=STUDY_STOP_FAILURE_POWEROFF_DELAY_SECONDS,
            )
        return True, message

    def set_auto_trials(self, enabled, topology=None, num_agents=None, discussion_rounds=None, ollama_options=None, max_messages=None):
        should_start = False
        try:
            with self.lock:
                if enabled and self.full_study_active:
                    return False, "An automated study is already running."
                was_enabled = self.auto_trials
                self.auto_trials = bool(enabled)
                self.auto_trial_generation += 1
                auto_trial_generation = self.auto_trial_generation
                if topology is not None:
                    self.auto_topology = topology if topology in VALID_TOPOLOGIES else "circle"
                if num_agents is not None:
                    if self.auto_topology in FIXED_FIVE_AGENT_TOPOLOGIES:
                        self.auto_num_agents = MAX_PARTICIPANTS
                    else:
                        self.auto_num_agents = max(MIN_PARTICIPANTS, min(MAX_PARTICIPANTS, int(num_agents)))
                self.auto_discussion_rounds = None
                self.auto_ollama_options = normalize_ollama_options(ollama_options)
                self.auto_max_messages = normalize_max_messages(max_messages, self.auto_topology)
                if self.auto_trials and not was_enabled:
                    self.begin_auto_batch_locked()
                should_start = self.auto_trials and not self.trial_active and not self.trial_requested
        except OSError as exc:
            with self.lock:
                self.auto_trials = False
            return False, f"Could not create auto-trial data folder: {exc}"
        self.add_event("auto_trials_changed", {
            "enabled": self.auto_trials,
            "batch_id": self.auto_batch_id,
            "completed": self.auto_batch_completed,
            "target": self.auto_trial_target,
        })
        if should_start:
            self.schedule_next_auto_trial(delay=0, generation=auto_trial_generation)
        return True, (
            f"Auto trials enabled for a {self.auto_trial_target}-trial batch."
            if self.auto_trials
            else "Auto trials disabled."
        )

    def start_full_study(self, ollama_options=None, cooling_options=None, study_kind="circle"):
        with self.lock:
            if self.trial_active or self.trial_requested or self.auto_trials or self.full_study_active:
                return False, "A trial or automated run is already active."
            study_presets = {
                "circle": (CIRCLE_STUDY_TOPOLOGIES, CIRCLE_STUDY_TEMPERATURES, "Circle study", "circle-study"),
                "y": (Y_STUDY_TOPOLOGIES, Y_STUDY_TEMPERATURES, "Y study", "y-study"),
                "wheel": (WHEEL_STUDY_TOPOLOGIES, WHEEL_STUDY_TEMPERATURES, "Wheel study", "wheel-study"),
                "wheel_temperature_1": (
                    WHEEL_STUDY_TOPOLOGIES,
                    WHEEL_TEMPERATURE_1_STUDY_TEMPERATURES,
                    "Wheel temperature 1 study",
                    "wheel-temperature-1-study",
                ),
                "chain": (CHAIN_STUDY_TOPOLOGIES, CHAIN_STUDY_TEMPERATURES, "Chain study", "chain-study"),
                "remaining": (REMAINING_STUDY_TOPOLOGIES, FULL_STUDY_TEMPERATURES, "Remaining topology study", "remaining-topologies-study"),
                "full": (FULL_STUDY_TOPOLOGIES, FULL_STUDY_TEMPERATURES, "Full study", "full-study"),
                "leavitt": (LEAVITT_STUDY_TOPOLOGIES, FULL_STUDY_TEMPERATURES, "Leavitt study", "leavitt-study"),
                "four_topologies": (
                    FOUR_TOPOLOGY_STUDY_TOPOLOGIES,
                    FOUR_TOPOLOGY_STUDY_TEMPERATURES,
                    "Four-topology study",
                    "four-topologies-study",
                ),
            }
            if study_kind not in study_presets:
                return False, f"Unknown study kind: {study_kind}."
            selected_topologies, selected_temperatures, study_label, study_slug = study_presets[study_kind]
            missing_agents = self.missing_fixed_five_agents_locked()
            if missing_agents:
                missing_display = ", ".join(display_agent_name(name) for name in missing_agents)
                return False, f"The {study_label} requires all 5 Jetsons connected. Missing: {missing_display}."
            wrong_models = sorted(
                display_agent_name(info["name"])
                for info in self.clients.values()
                if str(info.get("model_name") or "").strip() != EXPECTED_STUDY_MODEL
            )
            if wrong_models:
                return False, (
                    f"The {study_label} requires {EXPECTED_STUDY_MODEL} on every Jetson. "
                    f"Wrong or unreported model: {', '.join(wrong_models)}."
                )

            base_options = normalize_ollama_options(ollama_options)
            study_base_id = f"{run_identifier()}-{study_slug}"
            study_dir = DATA_ROOT / study_base_id
            suffix = 2
            while study_dir.exists():
                study_dir = DATA_ROOT / f"{study_base_id}_{suffix}"
                suffix += 1

            try:
                study_dir.mkdir(parents=True)
                self.full_study_active = True
                self.full_study_id = study_dir.name
                self.full_study_kind = study_kind
                self.full_study_label = study_label
                self.full_study_topologies = list(selected_topologies)
                self.full_study_dir = study_dir
                self.full_study_started_at = datetime.now(timezone.utc).isoformat()
                self.full_study_index = -1
                self.full_study_completed_batches = 0
                self.full_study_cooling_options = normalize_cooling_options(cooling_options)
                self.full_study_cooling = False
                self.full_study_cooling_kind = None
                self.full_study_cooling_started_at = None
                self.full_study_cooling_until = None
                self.full_study_last_progress_monotonic = time.monotonic()
                self.full_study_reconnect_started_monotonic = None
                self.full_study_reconnect_started_at = None
                self.full_study_watchdog_generation += 1
                watchdog_generation = self.full_study_watchdog_generation
                self.full_study_batches = []
                for topology in selected_topologies:
                    for temperature in selected_temperatures:
                        options = dict(base_options)
                        options["temperature"] = temperature
                        self.full_study_batches.append({
                            "topology": topology,
                            "temperature": temperature,
                            "ollama_options": normalize_ollama_options(options),
                            "status": "pending",
                            "completed_trials": 0,
                        })
                self.configure_full_study_batch_locked(0)
                self.auto_trial_generation += 1
                generation = self.auto_trial_generation
            except OSError as exc:
                self.full_study_active = False
                self.auto_trials = False
                return False, f"Could not create full-study data folders: {exc}"

        self.add_event("full_study_started", {
            "study_id": self.full_study_id,
            "study_kind": self.full_study_kind,
            "study_label": self.full_study_label,
            "topologies": self.full_study_topologies,
            "batches": len(self.full_study_batches),
            "trials_per_batch": AUTO_TRIAL_TARGET,
            "total_trials": len(self.full_study_batches) * AUTO_TRIAL_TARGET,
            "directory": str(self.full_study_dir),
            "cooling_options": self.full_study_cooling_options,
        })
        self.schedule_next_auto_trial(delay=0, generation=generation)
        self.start_study_watchdog(watchdog_generation)
        return True, (
            f"{self.full_study_label} started: {len(self.full_study_batches)} batches and "
            f"{len(self.full_study_batches) * AUTO_TRIAL_TARGET} total trials. "
            f"Cooling pauses: {self.full_study_cooling_options['between_temperatures_minutes']:g} minutes "
            f"between temperatures and {self.full_study_cooling_options['between_topologies_minutes']:g} "
            "minutes between topologies."
        )

    def local_poweroff_command(self):
        systemctl = shutil.which("systemctl") or "/usr/bin/systemctl"
        if os.geteuid() == 0:
            return [systemctl, "poweroff"]
        sudo = shutil.which("sudo") or "/usr/bin/sudo"
        return [sudo, "-n", systemctl, "poweroff"]

    def check_poweroff_readiness(self, emit_event=True):
        systemctl = "/usr/bin/systemctl"
        server_ready = is_jetson_device()
        server_reason = "Jetson server detected."
        if not server_ready:
            server_reason = "Dashboard host is not detected as an NVIDIA Jetson; local shutdown is blocked."
        elif os.geteuid() != 0:
            sudo = shutil.which("sudo") or "/usr/bin/sudo"
            local_systemctl = shutil.which("systemctl") or systemctl
            try:
                check = subprocess.run(
                    [sudo, "-n", "-l", local_systemctl, "poweroff"],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                server_ready = check.returncode == 0
                if not server_ready:
                    server_reason = check.stderr.strip() or "Server sudo permission for poweroff is missing."
            except (OSError, subprocess.TimeoutExpired) as exc:
                server_ready = False
                server_reason = str(exc)

        def check_client(host):
            address = JETSON_ADDRESSES[host]
            command = [
                "ssh",
                "-o", "BatchMode=yes",
                "-o", "ConnectTimeout=8",
                f"{JETSON_SSH_USER}@{address}",
                f"sudo -n -l {systemctl} poweroff >/dev/null 2>&1",
            ]
            try:
                result = subprocess.run(command, capture_output=True, text=True, timeout=12)
                return {
                    "hostname": host,
                    "address": address,
                    "ready": result.returncode == 0,
                    "reason": "ready" if result.returncode == 0 else (
                        result.stderr.strip() or result.stdout.strip() or f"ssh exited {result.returncode}"
                    ),
                }
            except (OSError, subprocess.TimeoutExpired) as exc:
                return {"hostname": host, "address": address, "ready": False, "reason": str(exc)}

        clients = []
        with ThreadPoolExecutor(max_workers=len(JETSON_HOSTNAMES)) as executor:
            futures = [executor.submit(check_client, host) for host in JETSON_HOSTNAMES]
            for future in as_completed(futures):
                clients.append(future.result())
        clients.sort(key=lambda item: get_jetson_number(item["hostname"]) or 999)
        ready = server_ready and all(client["ready"] for client in clients)
        readiness = {
            "ready": ready,
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "server": {"ready": server_ready, "reason": server_reason},
            "clients": clients,
        }
        with self.lock:
            self.poweroff_readiness = readiness
        if emit_event:
            self.add_event("poweroff_readiness", readiness)
        return ready, readiness

    def poweroff_log_path(self):
        with self.lock:
            if self.full_study_dir:
                return self.full_study_dir / "poweroff-log.jsonl"
        return DATA_ROOT / "poweroff-log.jsonl"

    def request_poweroff_all(self, source="manual", delay=POWER_OFF_DELAY_SECONDS):
        with self.lock:
            if self.poweroff_requested:
                return False, "A power-off sequence is already scheduled."
            if source == "manual" and (self.trial_active or self.trial_requested or self.auto_trials or self.full_study_active):
                return False, "Stop the active trial or automated study before powering off the Jetsons."
            self.poweroff_requested = True
            self.poweroff_source = source
        self.add_event("poweroff_scheduled", {
            "source": source,
            "delay_seconds": delay,
            "message": "Clients will power off first; the server will power off last.",
        })
        threading.Thread(
            target=self.run_poweroff_all,
            args=(source, delay),
            daemon=True,
        ).start()
        return True, f"Power-off sequence scheduled in {delay} seconds."

    def run_poweroff_all(self, source, delay):
        if delay > 0:
            time.sleep(delay)

        while True:
            with self.lock:
                if not self.poweroff_requested or self.poweroff_source != source:
                    return
            ready, readiness = self.check_poweroff_readiness(emit_event=True)
            if ready:
                break
            append_json_line(self.poweroff_log_path(), {
                "recorded_at": datetime.now(timezone.utc).isoformat(),
                "source": source,
                "status": "waiting_for_readiness",
                "retry_seconds": POWER_OFF_RETRY_SECONDS,
                "readiness": readiness,
            })
            self.add_event("poweroff_waiting", {
                "source": source,
                "message": (
                    "Power-off is still pending. Waiting for all Jetsons to become reachable and ready; "
                    f"checking again in {POWER_OFF_RETRY_SECONDS} seconds."
                ),
                "retry_seconds": POWER_OFF_RETRY_SECONDS,
                "readiness": readiness,
            })
            time.sleep(POWER_OFF_RETRY_SECONDS)

        def poweroff_client(host):
            address = JETSON_ADDRESSES[host]
            command = [
                "ssh",
                "-o", "BatchMode=yes",
                "-o", "ConnectTimeout=8",
                f"{JETSON_SSH_USER}@{address}",
                "sudo -n /usr/bin/systemctl poweroff",
            ]
            try:
                result = subprocess.run(command, capture_output=True, text=True, timeout=20)
                return {
                    "hostname": host,
                    "address": address,
                    "sent": result.returncode == 0,
                    "reason": "poweroff accepted" if result.returncode == 0 else (
                        result.stderr.strip() or result.stdout.strip() or f"ssh exited {result.returncode}"
                    ),
                }
            except (OSError, subprocess.TimeoutExpired) as exc:
                return {"hostname": host, "address": address, "sent": False, "reason": str(exc)}

        pending_hosts = list(JETSON_HOSTNAMES)
        client_results_by_host = {}
        while pending_hosts:
            with self.lock:
                if not self.poweroff_requested or self.poweroff_source != source:
                    return
            attempt_results = []
            with ThreadPoolExecutor(max_workers=len(pending_hosts)) as executor:
                futures = [executor.submit(poweroff_client, host) for host in pending_hosts]
                for future in as_completed(futures):
                    result = future.result()
                    attempt_results.append(result)
                    self.add_event("client_poweroff_result", result)
            for result in attempt_results:
                client_results_by_host[result["hostname"]] = result
            pending_hosts = [result["hostname"] for result in attempt_results if not result["sent"]]
            if pending_hosts:
                append_json_line(self.poweroff_log_path(), {
                    "recorded_at": datetime.now(timezone.utc).isoformat(),
                    "source": source,
                    "status": "retrying_client_poweroff",
                    "retry_seconds": POWER_OFF_RETRY_SECONDS,
                    "clients": attempt_results,
                })
                self.add_event("poweroff_waiting", {
                    "source": source,
                    "message": (
                        "Some client power-off commands failed. The accepted clients will not be retried; "
                        f"retrying the remaining clients in {POWER_OFF_RETRY_SECONDS} seconds."
                    ),
                    "retry_seconds": POWER_OFF_RETRY_SECONDS,
                    "failed_clients": [
                        result for result in attempt_results if not result["sent"]
                    ],
                })
                time.sleep(POWER_OFF_RETRY_SECONDS)

        client_results = sorted(
            client_results_by_host.values(),
            key=lambda item: get_jetson_number(item["hostname"]) or 999,
        )

        log_record = {
            "recorded_at": datetime.now(timezone.utc).isoformat(),
            "source": source,
            "status": "server_poweroff_starting",
            "clients": client_results,
        }
        append_json_line(self.poweroff_log_path(), log_record)
        self.add_event("server_poweroff_starting", {
            "source": source,
            "message": "All client commands were accepted. The server Jetson is powering off now.",
        })
        try:
            os.sync()
        except AttributeError:
            pass
        while True:
            with self.lock:
                if not self.poweroff_requested or self.poweroff_source != source:
                    return
            try:
                subprocess.Popen(
                    self.local_poweroff_command(),
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    start_new_session=True,
                )
                return
            except OSError as exc:
                append_json_line(self.poweroff_log_path(), {
                    "recorded_at": datetime.now(timezone.utc).isoformat(),
                    "source": source,
                    "status": "retrying_server_poweroff",
                    "retry_seconds": POWER_OFF_RETRY_SECONDS,
                    "error": str(exc),
                })
                self.add_event("poweroff_waiting", {
                    "source": source,
                    "message": (
                        f"Server power-off command failed: {exc}. "
                        f"Retrying in {POWER_OFF_RETRY_SECONDS} seconds."
                    ),
                    "retry_seconds": POWER_OFF_RETRY_SECONDS,
                })
                time.sleep(POWER_OFF_RETRY_SECONDS)

    def restart_clients(self):
        with self.lock:
            if self.trial_active or self.trial_requested or self.auto_trials or self.full_study_active:
                return False, "Stop the active trial or automated run before reloading Jetsons."
            old_socks = list(self.clients.keys())
            targets = [
                (host, JETSON_ADDRESSES[host])
                for host in JETSON_HOSTNAMES
            ]
            self.clients = {}
            self.turn_order = []
            self.recv_buffers = {}
            self.results = []
            self.auto_trials = False
            self.auto_trial_generation += 1
            self.auto_batch_id = None
            self.auto_batch_dir = None
            self.auto_batch_started_at = None
            self.auto_batch_completed = 0
            self.full_study_active = False
            self.full_study_id = None
            self.full_study_kind = None
            self.full_study_label = None
            self.full_study_topologies = []
            self.full_study_dir = None
            self.full_study_started_at = None
            self.full_study_batches = []
            self.full_study_index = -1
            self.full_study_completed_batches = 0
            self.full_study_cooling_options = normalize_cooling_options(None)
            self.full_study_cooling = False
            self.full_study_cooling_kind = None
            self.full_study_cooling_started_at = None
            self.full_study_cooling_until = None
            self.stop_requested = False
            self.trial_active = False
            self.trial_requested = False
            self.active_trial_id = None
            self.trial_counter = 0
            self.topology = "circle"
            self.num_agents = 5
            self.discussion_rounds = None
            self.ollama_options = normalize_ollama_options(None)
            self.max_messages = default_max_messages_for_topology(self.topology)
            self.cards = {}
            self.common_symbol = None
            self.circle_neighbors_by_name = {}
            self.circle_last_target_by_speaker = {}
            self.chain_contacts_by_name = {}
            self.chain_last_target_by_speaker = {}
            self.y_contacts_by_name = {}
            self.y_last_target_by_speaker = {}
            self.wheel_contacts_by_name = {}
            self.wheel_last_target_by_speaker = {}
            self.agent_histories = {}
            self.unread_agents = set()
            self.scheduler_queue = []
            self.messages_per_agent = {}
            self.message_count = 0
            self.delivery_count = 0
            self.start_time = None
            self.turn_count = 0
            self.round_number = 1
            self.current_route = None
            self.current_speaker = None
            self.trial_routes = []
            self.trial_model_responses = []
            self.events = []
            self.last_waiting_event_state = None
            self.reload_batch_id += 1
            batch_id = self.reload_batch_id
            self.pending_reload_agents = {name for name, _ in targets}
        for sock in old_socks:
            try:
                sock.close()
            except OSError:
                pass
        self.add_event("clients_reload_started", {
            "batch": batch_id,
            "count": len(targets),
            "agents": [display_agent_name(name) for name, _ in targets],
            "fresh": True,
        })

        threading.Thread(
            target=self.restart_clients_via_ssh,
            args=(batch_id, targets),
            daemon=True,
        ).start()
        return True, (
            "Fresh dashboard state created. "
            f"Reload started for {len(targets)} Jetson service{'s' if len(targets) != 1 else ''}."
        )

    def restart_clients_via_ssh(self, batch_id, targets):
        sent_count = 0
        for name, host in targets:
            agent = display_agent_name(name)
            self.add_event("client_reload_requested", {
                "batch": batch_id,
                "agent": agent,
                "hostname": host,
            })
            cmd = [
                "ssh",
                "-o", "BatchMode=yes",
                "-o", "ConnectTimeout=8",
                f"{JETSON_SSH_USER}@{host}",
                f"{REMOTE_SUDO} -n {REMOTE_SYSTEMCTL} restart {JETSON_CLIENT_SERVICE}",
            ]
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=20,
                )
            except subprocess.TimeoutExpired:
                with self.lock:
                    self.pending_reload_agents.discard(name)
                self.add_event("client_reload_command_failed", {
                    "batch": batch_id,
                    "agent": agent,
                    "hostname": host,
                    "reason": "SSH timeout",
                })
                continue
            except Exception as exc:
                with self.lock:
                    self.pending_reload_agents.discard(name)
                self.add_event("client_reload_command_failed", {
                    "batch": batch_id,
                    "agent": agent,
                    "hostname": host,
                    "reason": str(exc),
                })
                continue

            if result.returncode == 0:
                sent_count += 1
                self.add_event("client_reload_command_sent", {
                    "batch": batch_id,
                    "agent": agent,
                    "hostname": host,
                })
            else:
                with self.lock:
                    self.pending_reload_agents.discard(name)
                detail = result.stderr.strip() or result.stdout.strip() or f"ssh exited {result.returncode}"
                self.add_event("client_reload_command_failed", {
                    "batch": batch_id,
                    "agent": agent,
                    "hostname": host,
                    "reason": detail,
                })
        with self.lock:
            pending = [display_agent_name(name) for name in sorted(self.pending_reload_agents)]
        self.add_event("clients_reload_commands_finished", {
            "batch": batch_id,
            "sent": sent_count,
            "requested": len(targets),
            "pending": pending,
        })
        if not pending:
            self.add_event("clients_reload_finished", {"message": "No Jetsons are waiting to reconnect."})

    def schedule_next_auto_trial(self, delay=None, generation=None):
        with self.lock:
            auto_trial_generation = self.auto_trial_generation if generation is None else generation
        threading.Thread(
            target=self.maybe_start_next_auto_trial,
            args=(self.auto_restart_delay if delay is None else delay, auto_trial_generation),
            daemon=True,
        ).start()

    def maybe_start_next_auto_trial(self, delay, generation):
        if delay > 0:
            time.sleep(delay)
        with self.lock:
            if (
                generation != self.auto_trial_generation
                or not self.auto_trials
                or self.trial_active
                or self.trial_requested
            ):
                return
            topology = self.auto_topology
            num_agents = self.auto_num_agents
            discussion_rounds = self.auto_discussion_rounds
            ollama_options = self.auto_ollama_options
            max_messages = self.auto_max_messages
        ok, message = self.start_trial(
            topology,
            num_agents,
            discussion_rounds,
            ollama_options,
            max_messages,
            automated=True,
        )
        if ok:
            return
        with self.lock:
            should_retry = (
                generation == self.auto_trial_generation
                and self.auto_trials
                and not self.trial_active
                and not self.trial_requested
            )
        if should_retry:
            self.add_event("auto_trial_start_delayed", {
                "message": message,
                "retry_seconds": self.auto_restart_delay,
                "topology": topology,
            })
            self.schedule_next_auto_trial(delay=self.auto_restart_delay, generation=generation)

    def broadcast(self, payload, exclude=None, recipients=None):
        with self.lock:
            targets = list(recipients) if recipients is not None else list(self.clients.keys())
        for sock in targets:
            if sock != exclude:
                self.send_json(sock, payload)

    def wait_for_clients(self, needed):
        while self.running:
            with self.lock:
                if self.stop_requested:
                    return []
                if self.topology in FIXED_FIVE_AGENT_TOPOLOGIES:
                    required = {}
                    for sock in self.turn_order:
                        info = self.clients.get(sock)
                        if not info:
                            continue
                        number = get_jetson_number(info["name"])
                        if number is not None and 1 <= number <= needed:
                            required.setdefault(number, sock)
                    selected = [required[n] for n in range(1, needed + 1) if n in required]
                    missing = [f"Agent{n}" for n in range(1, needed + 1) if n not in required]
                else:
                    selected = [sock for sock in self.turn_order if sock in self.clients][:needed]
                    missing = []
            waiting_state = (len(selected), needed, tuple(missing))
            if waiting_state != self.last_waiting_event_state:
                self.last_waiting_event_state = waiting_state
                self.add_event("waiting", {"selected": len(selected), "needed": needed, "missing": missing})
            if len(selected) >= needed and not missing:
                self.last_waiting_event_state = None
                return selected
            time.sleep(2)
        return []

    def active_agent_names(self, active_socks):
        with self.lock:
            return [self.clients[sock]["name"] for sock in active_socks if sock in self.clients]

    def build_circle_neighbors(self, active_socks):
        names = sorted(self.active_agent_names(active_socks), key=lambda name: (get_jetson_number(name) or 999, name))
        neighbors_by_name = {}
        total = len(names)
        for index, name in enumerate(names):
            previous_name = names[(index - 1) % total]
            next_name = names[(index + 1) % total]
            neighbors_by_name[name] = list(dict.fromkeys([previous_name, next_name]))
        return neighbors_by_name

    def build_chain_contacts(self, active_socks):
        names = sorted(self.active_agent_names(active_socks), key=lambda name: (get_jetson_number(name) or 999, name))
        contacts_by_name = {}
        total = len(names)
        for index, name in enumerate(names):
            contacts = []
            if index > 0:
                contacts.append(names[index - 1])
            if index < total - 1:
                contacts.append(names[index + 1])
            contacts_by_name[name] = contacts
        return contacts_by_name

    def build_contact_map(self, active_socks, contact_func):
        active_names = set(self.active_agent_names(active_socks))
        contacts_by_name = {}
        for name in active_names:
            agent_id = get_agent_id(name)
            contacts_by_name[name] = [
                f"jetson{contact_id}"
                for contact_id in contact_func(agent_id)
                if f"jetson{contact_id}" in active_names
            ]
        return contacts_by_name

    def sock_by_name(self, active_socks, name):
        with self.lock:
            for sock in active_socks:
                info = self.clients.get(sock)
                if info and info["name"] == name:
                    return sock
        return None

    def choose_next_sock(self, active_socks, exclude=None):
        with self.lock:
            candidates = [sock for sock in active_socks if sock in self.clients]
        if exclude in candidates and len(candidates) > 1:
            candidates.remove(exclude)
        return random.choice(candidates) if candidates else None

    def record_valid_message(self, speaker, receivers):
        with self.lock:
            if self.start_time is None:
                self.start_time = time.monotonic()
            self.message_count += 1
            self.delivery_count += len(receivers)
            self.messages_per_agent[speaker] = self.messages_per_agent.get(speaker, 0) + 1
            for receiver in receivers:
                if receiver and receiver != speaker:
                    self.unread_agents.add(receiver)
            return self.message_count

    def answer_allowed_now(self, active_socks):
        with self.lock:
            active_names = [
                self.clients[sock]["name"]
                for sock in active_socks
                if sock in self.clients
            ]
            if self.topology == "circle":
                return bool(active_names)
            return bool(active_names) and all(
                self.messages_per_agent.get(name, 0) > 0
                for name in active_names
            )

    def elapsed_since_first_message(self):
        with self.lock:
            start_time = self.start_time
            paused_seconds = self.trial_pause_total_seconds
            pause_started = self.trial_pause_started_monotonic
        if start_time is None:
            return 0
        if pause_started is not None:
            paused_seconds += time.monotonic() - pause_started
        return max(0, time.monotonic() - start_time - paused_seconds)

    def resume_history_locked(self, agent_name):
        """Rebuild exactly the chat context a reconnecting client had received."""
        displayed_name = display_agent_name(agent_name)
        history = []
        for route in self.trial_routes:
            sender = route.get("sender")
            receiver = route.get("receiver")
            message = route.get("message", "")
            if self.topology == "broadcast":
                history.append({"sender": sender, "text": message})
            elif sender == displayed_name:
                original_target = route.get("original_target") or receiver
                history.append({"sender": sender, "text": f"To {original_target}: {message}"})
            elif receiver == displayed_name:
                history.append({"sender": sender, "text": message})
        return history

    def resume_payload_locked(self, agent_name, trial_id):
        displayed_name = display_agent_name(agent_name)
        shared_recipients = []
        if self.topology == "circle":
            symbols = self.cards.get(agent_name, [])
            shared_recipients = [
                route.get("receiver")
                for route in self.trial_routes
                if route.get("sender") == displayed_name
                and all(symbol.lower() in route.get("message", "").lower() for symbol in symbols)
                and route.get("receiver")
            ]
        start_payload = {
            "type": "experiment_start",
            "trial_id": trial_id,
            "agent_name": displayed_name,
            "your_symbols": self.cards.get(agent_name, []),
            "num_agents": self.num_agents,
            "topology": self.topology,
            "discussion_rounds": None,
            "ollama_options": self.ollama_options,
            "circle_shared_full_list_recipients": list(dict.fromkeys(shared_recipients)),
            "circle_neighbors": [display_agent_name(n) for n in self.circle_neighbors_by_name.get(agent_name, [])],
            "chain_contacts": [display_agent_name(n) for n in self.chain_contacts_by_name.get(agent_name, [])],
            "y_contacts": [display_agent_name(n) for n in self.y_contacts_by_name.get(agent_name, [])],
            "wheel_recipients": [display_agent_name(n) for n in self.wheel_contacts_by_name.get(agent_name, [])],
        }
        # Use experiment_start plus ordinary chat messages so clients deployed
        # before pause/resume support was added can still restore and continue.
        start_payload["resume"] = True
        history_payloads = [
            {
                "type": "chat",
                "trial_id": trial_id,
                "sender": item.get("sender", "SYSTEM"),
                "text": item.get("text", ""),
            }
            for item in self.resume_history_locked(agent_name)
        ]
        return [start_payload, *history_payloads]

    def wait_for_trial_reconnect(self, required_names, previous_socks_by_name, trial_id):
        """Pause an active trial until every required hostname is connected again."""
        pause_started_monotonic = time.monotonic()
        pause_started_at = datetime.now(timezone.utc).isoformat()
        with self.lock:
            connected_by_name = {info["name"]: sock for sock, info in self.clients.items()}
            missing = [name for name in required_names if name not in connected_by_name]
            initial_missing = list(missing)
            initial_replaced = [
                name for name in required_names
                if name in connected_by_name
                and connected_by_name[name] is not previous_socks_by_name.get(name)
            ]
            initially_affected = list(dict.fromkeys([*initial_missing, *initial_replaced]))
            self.trial_paused = True
            self.trial_pause_started_at = pause_started_at
            self.trial_pause_started_monotonic = pause_started_monotonic
        self.add_event("trial_paused_disconnect", {
            "trial_id": trial_id,
            "missing": [display_agent_name(name) for name in initially_affected],
            "started_at": pause_started_at,
            "message": "Trial state preserved. Waiting indefinitely for the required Jetson(s) to reconnect.",
        })

        while self.running:
            with self.lock:
                if self.stop_requested or self.active_trial_id != trial_id:
                    self.trial_paused = False
                    self.trial_pause_started_at = None
                    self.trial_pause_started_monotonic = None
                    return None
                connected_by_name = {info["name"]: sock for sock, info in self.clients.items()}
                missing = [name for name in required_names if name not in connected_by_name]
                if missing:
                    payloads = []
                else:
                    reconnected = [
                        name for name in required_names
                        if connected_by_name[name] is not previous_socks_by_name.get(name)
                    ]
                    payloads = [
                        (name, connected_by_name[name], self.resume_payload_locked(name, trial_id))
                        for name in reconnected
                    ]

            if missing:
                time.sleep(1)
                continue

            restore_failed = False
            for _name, sock, restore_payloads in payloads:
                for payload in restore_payloads:
                    if not self.send_json(sock, payload):
                        restore_failed = True
                        break
                if restore_failed:
                    break
            if restore_failed:
                time.sleep(1)
                continue

            resumed_at = datetime.now(timezone.utc).isoformat()
            pause_seconds = time.monotonic() - pause_started_monotonic
            with self.lock:
                if any(connected_by_name[name] not in self.clients for name in required_names):
                    continue
                self.trial_pause_total_seconds += pause_seconds
                disconnect_record = {
                    "started_at": pause_started_at,
                    "resumed_at": resumed_at,
                    "duration_seconds": round(pause_seconds, 2),
                    "missing_agents": [display_agent_name(name) for name in initially_affected],
                    "reconnected_agents": [display_agent_name(name) for name, _sock, _payloads in payloads],
                }
                self.trial_disconnects.append(disconnect_record)
                self.trial_paused = False
                self.trial_pause_started_at = None
                self.trial_pause_started_monotonic = None
            self.add_event("trial_resumed_disconnect", {
                "trial_id": trial_id,
                **disconnect_record,
                "message": "All required Jetsons reconnected. The same trial is resuming.",
            })
            return connected_by_name
        return None

    def recent_circle_messages(self, agent_id):
        return list(self.agent_histories.get(agent_id, [])[-5:])

    def recent_messages(self, agent_id):
        return list(self.agent_histories.get(agent_id, [])[-5:])

    def preferred_contact(self, speaker, contacts_by_name, last_target_by_speaker):
        contacts = contacts_by_name.get(speaker, [])
        if not contacts:
            return ""
        last_target = last_target_by_speaker.get(speaker)
        choices = [contact for contact in contacts if contact != last_target] or list(contacts)
        return display_agent_name(random.choice(choices))

    def preferred_circle_neighbor(self, speaker):
        neighbors = self.circle_neighbors_by_name.get(speaker, [])
        if not neighbors:
            return ""
        last_target = self.circle_last_target_by_speaker.get(speaker)
        if last_target in neighbors and len(neighbors) > 1:
            next_index = (neighbors.index(last_target) + 1) % len(neighbors)
            return display_agent_name(neighbors[next_index])
        return display_agent_name(neighbors[0])

    def send_turn_request(self, sock, speaker_id, speaker, round_number, can_answer):
        message_count = self.message_count
        trial_id = self.active_trial_id
        if self.topology == "circle":
            self.send_json(sock, {
                "type": "your_turn",
                "trial_id": trial_id,
                "topology": "circle",
                "round": message_count,
                "message_count": message_count,
                "can_answer": can_answer,
                "discussion_rounds": None,
                "ollama_options": self.ollama_options,
                "agent_name": display_agent_name(speaker),
                "your_symbols": self.cards[speaker],
                "circle_neighbors": [display_agent_name(n) for n in self.circle_neighbors_by_name.get(speaker, [])],
                "recent_messages": self.recent_circle_messages(speaker_id),
                "preferred_neighbor": self.preferred_circle_neighbor(speaker),
            })
        elif self.topology == "chain":
            self.send_json(sock, {
                "type": "your_turn",
                "trial_id": trial_id,
                "topology": "chain",
                "round": message_count,
                "message_count": message_count,
                "can_answer": can_answer,
                "discussion_rounds": None,
                "ollama_options": self.ollama_options,
                "agent_name": display_agent_name(speaker),
                "your_symbols": self.cards[speaker],
                "chain_contacts": [display_agent_name(n) for n in self.chain_contacts_by_name.get(speaker, [])],
                "recent_messages": self.recent_messages(speaker_id),
                "preferred_contact": self.preferred_contact(speaker, self.chain_contacts_by_name, self.chain_last_target_by_speaker),
            })
        elif self.topology == "y":
            self.send_json(sock, {
                "type": "your_turn",
                "trial_id": trial_id,
                "topology": "y",
                "round": message_count,
                "message_count": message_count,
                "can_answer": can_answer,
                "discussion_rounds": None,
                "ollama_options": self.ollama_options,
                "agent_name": display_agent_name(speaker),
                "your_symbols": self.cards[speaker],
                "y_contacts": [display_agent_name(n) for n in self.y_contacts_by_name.get(speaker, [])],
                "recent_messages": self.recent_messages(speaker_id),
                "preferred_contact": self.preferred_contact(speaker, self.y_contacts_by_name, self.y_last_target_by_speaker),
            })
        elif self.topology == "wheel":
            self.send_json(sock, {
                "type": "your_turn",
                "trial_id": trial_id,
                "topology": "wheel",
                "round": message_count,
                "message_count": message_count,
                "can_answer": can_answer,
                "discussion_rounds": None,
                "ollama_options": self.ollama_options,
                "agent_name": display_agent_name(speaker),
                "your_symbols": self.cards[speaker],
                "wheel_recipients": [display_agent_name(n) for n in self.wheel_contacts_by_name.get(speaker, [])],
                "recent_messages": self.recent_messages(speaker_id),
                "preferred_recipient": self.preferred_contact(speaker, self.wheel_contacts_by_name, self.wheel_last_target_by_speaker),
            })
        else:
            self.send_json(sock, {
                "type": "your_turn",
                "trial_id": trial_id,
                "topology": "broadcast",
                "round": message_count,
                "message_count": message_count,
                "can_answer": can_answer,
                "discussion_rounds": None,
                "ollama_options": self.ollama_options,
            })

    def route_private_message(
        self,
        topology,
        contacts_by_name,
        last_target_by_speaker,
        contact_label,
        text,
        speaker,
        speaker_id,
        active_socks,
        round_number,
        target,
        raw,
        target_source="",
        original_target="",
    ):
        valid_contacts = contacts_by_name.get(speaker, [])
        original_target = original_target or target or ""
        receiver = internal_agent_name(target) if target else ""
        if receiver not in valid_contacts:
            receiver = internal_agent_name(
                self.preferred_contact(speaker, contacts_by_name, last_target_by_speaker)
            )
            target_source = "server_assigned"
            if receiver not in valid_contacts:
                self.add_event("invalid_route", {
                    "round": round_number,
                    "topology": topology,
                    "sender": display_agent_name(speaker),
                    "target": target,
                    contact_label: [display_agent_name(n) for n in valid_contacts],
                    "message": text,
                    "target_source": target_source,
                    "original_target": original_target,
                })
                return None
        elif not target_source:
            target_source = "agent"
        receiver_sock = self.sock_by_name(active_socks, receiver)
        sent = receiver_sock and self.send_json(receiver_sock, {
            "type": "chat",
            "trial_id": self.active_trial_id,
            "sender": display_agent_name(speaker),
            "text": text,
        })
        if not sent:
            return None
        last_target_by_speaker[speaker] = receiver
        receiver_id = get_agent_id(receiver)
        if receiver_id is not None:
            self.agent_histories.setdefault(receiver_id, []).append({
                "sender": display_agent_name(speaker),
                "text": text,
            })
        message_number = self.record_valid_message(speaker, [receiver])
        return {
            "round": message_number,
            "topology": topology,
            "sender": display_agent_name(speaker),
            "receiver": display_agent_name(receiver),
            contact_label: [display_agent_name(n) for n in valid_contacts],
            "message": text,
            "raw": raw,
            "target_source": target_source,
            "original_target": original_target,
            "elapsed": round(self.elapsed_since_first_message(), 2),
        }

    def route_chat_message(
        self,
        text,
        speaker,
        speaker_id,
        current_sock,
        active_socks,
        round_number,
        target=None,
        raw="",
        target_source="",
        original_target="",
    ):
        if self.topology == "circle":
            valid_neighbors = self.circle_neighbors_by_name.get(speaker, [])
            original_target = original_target or target or ""
            receiver = internal_agent_name(target) if target else target
            if not receiver or receiver not in valid_neighbors:
                receiver = internal_agent_name(self.preferred_circle_neighbor(speaker))
                target_source = "server_assigned"
                if receiver not in valid_neighbors:
                    self.add_event("invalid_route", {
                        "round": round_number,
                        "sender": display_agent_name(speaker),
                        "target": target,
                        "valid_neighbors": [display_agent_name(n) for n in valid_neighbors],
                        "message": text,
                        "target_source": target_source,
                        "original_target": original_target,
                    })
                    return False
            elif not target_source:
                target_source = "agent"
            receiver_sock = self.sock_by_name(active_socks, receiver)
            sent = receiver_sock and self.send_json(receiver_sock, {
                "type": "chat",
                "trial_id": self.active_trial_id,
                "sender": display_agent_name(speaker),
                "text": text,
            })
            if not sent:
                return False
            self.circle_last_target_by_speaker[speaker] = receiver
            receiver_id = get_agent_id(receiver)
            if receiver_id is not None:
                self.agent_histories.setdefault(receiver_id, []).append({
                    "sender": display_agent_name(speaker),
                    "text": text,
                })
            message_number = self.record_valid_message(speaker, [receiver])
            route = {
                "round": message_number,
                "topology": "circle",
                "sender": display_agent_name(speaker),
                "receiver": display_agent_name(receiver),
                "valid_neighbors": [display_agent_name(name) for name in valid_neighbors],
                "message": text,
                "raw": raw,
                "target_source": target_source,
                "original_target": original_target,
                "elapsed": round(self.elapsed_since_first_message(), 2),
            }
        elif self.topology == "chain":
            route = self.route_private_message(
                "chain",
                self.chain_contacts_by_name,
                self.chain_last_target_by_speaker,
                "valid_contacts",
                text,
                speaker,
                speaker_id,
                active_socks,
                round_number,
                target,
                raw,
                target_source,
                original_target,
            )
            if route is None:
                return False
        elif self.topology == "y":
            route = self.route_private_message(
                "y",
                self.y_contacts_by_name,
                self.y_last_target_by_speaker,
                "valid_contacts",
                text,
                speaker,
                speaker_id,
                active_socks,
                round_number,
                target,
                raw,
                target_source,
                original_target,
            )
            if route is None:
                return False
        elif self.topology == "wheel":
            route = self.route_private_message(
                "wheel",
                self.wheel_contacts_by_name,
                self.wheel_last_target_by_speaker,
                "valid_recipients",
                text,
                speaker,
                speaker_id,
                active_socks,
                round_number,
                target,
                raw,
                target_source,
                original_target,
            )
            if route is None:
                return False
        else:
            receivers = [
                self.clients[sock]["name"]
                for sock in active_socks
                if sock != current_sock and sock in self.clients
            ]
            message_number = self.record_valid_message(speaker, receivers)
            self.broadcast(
                {
                    "type": "chat",
                    "trial_id": self.active_trial_id,
                    "sender": display_agent_name(speaker),
                    "text": text,
                },
                exclude=current_sock,
                recipients=active_socks,
            )
            route = {
                "round": message_number,
                "topology": "broadcast",
                "sender": display_agent_name(speaker),
                "receiver": "ALL",
                "valid_recipients": [display_agent_name(name) for name in receivers],
                "message": text,
                "raw": raw,
                "elapsed": round(self.elapsed_since_first_message(), 2),
            }

        with self.lock:
            self.current_route = route
            self.trial_routes.append(dict(route))
        self.add_event("chat", route)
        return True

    def run_experiment(self):
        with self.lock:
            self.trial_requested = False
            self.trial_active = True
            self.trial_counter += 1
            trial_id = self.trial_counter
            self.active_trial_id = trial_id
            trial_started_at = datetime.now(timezone.utc).isoformat()
            trial_started_monotonic = time.monotonic()
            self.cards = {}
            self.common_symbol = None
            self.circle_neighbors_by_name = {}
            self.circle_last_target_by_speaker = {}
            self.chain_contacts_by_name = {}
            self.chain_last_target_by_speaker = {}
            self.y_contacts_by_name = {}
            self.y_last_target_by_speaker = {}
            self.wheel_contacts_by_name = {}
            self.wheel_last_target_by_speaker = {}
            self.agent_histories = {i: [] for i in range(1, self.num_agents + 1)}
            self.unread_agents = set()
            self.scheduler_queue = []
            self.messages_per_agent = {}
            self.message_count = 0
            self.delivery_count = 0
            self.start_time = None
            self.turn_count = 0
            self.round_number = 1
            self.current_route = None
            self.current_speaker = None
            self.trial_routes = []
            self.trial_model_responses = []
            self.trial_paused = False
            self.trial_pause_started_at = None
            self.trial_pause_started_monotonic = None
            self.trial_pause_total_seconds = 0.0
            self.trial_disconnects = []
            max_messages = self.max_messages

        active_socks = self.wait_for_clients(self.num_agents)
        if not active_socks:
            result = {
                "trial_id": trial_id,
                "started_at": trial_started_at,
                "completed_at": datetime.now(timezone.utc).isoformat(),
                "topology": self.topology,
                "num_agents": self.num_agents,
                "result": "stopped",
                "success": False,
                "temperature": self.ollama_options.get("temperature"),
                "ollama_options": self.ollama_options,
                "common_word": self.common_symbol,
                "submitted_answer": None,
                "correct_answer": self.common_symbol,
                "final_answer_speaker": None,
                "final_answer_word": None,
                "submitted_figure_status": "Trial stopped",
                "time_seconds": 0,
                "trial_wall_time_seconds": round(time.monotonic() - trial_started_monotonic, 2),
                "trial_active_time_seconds": round(time.monotonic() - trial_started_monotonic, 2),
                "response_timings": [],
                "completed_generation_count": 0,
                "total_thinking_time_seconds": 0.0,
                "average_thinking_time_seconds": 0.0,
                "total_visible_response_time_seconds": 0.0,
                "average_visible_response_time_seconds": 0.0,
                "total_generation_time_seconds": 0.0,
                "average_generation_time_seconds": 0.0,
                "total_messages": self.message_count,
                "total_deliveries": self.delivery_count,
                "total_turns": self.turn_count,
                "rounds": None,
                "answer_round": None,
                "messages_before_answer": None,
                "max_messages_reached": False,
                "efficiency_explanation": "Trial stopped before all Jetsons were ready.",
                "efficiency_max_messages": max_messages,
                "max_messages_per_trial": max_messages,
                "discussion_rounds": None,
                "stopped": True,
            }
            with self.lock:
                self.results.append(result)
                self.results = self.results[-100:]
                self.trial_active = False
                self.trial_requested = False
                if self.active_trial_id == trial_id:
                    self.active_trial_id = None
                self.stop_requested = False
                self.current_speaker = None
                self.current_route = None
            self.add_event("trial_finished", result)
            return

        with self.lock:
            nicknames = [self.clients[sock]["name"] for sock in active_socks if sock in self.clients]
            self.common_symbol, self.cards, pool_size, figures_per_card = generate_jetson_sets(nicknames)
            self.messages_per_agent = {name: 0 for name in nicknames}
            if self.topology == "circle":
                self.circle_neighbors_by_name = self.build_circle_neighbors(active_socks)
            elif self.topology == "chain":
                self.chain_contacts_by_name = self.build_chain_contacts(active_socks)
            elif self.topology == "y":
                self.y_contacts_by_name = self.build_contact_map(active_socks, get_y_contacts)
            elif self.topology == "wheel":
                self.wheel_contacts_by_name = self.build_contact_map(active_socks, get_wheel_contacts)
            agent_socks = {
                get_agent_id(self.clients[sock]["name"]): sock
                for sock in active_socks
                if sock in self.clients and get_agent_id(self.clients[sock]["name"]) is not None
            }
            sock_agent_ids = {
                sock: get_agent_id(self.clients[sock]["name"])
                for sock in active_socks
                if sock in self.clients
            }
            required_agent_names = list(nicknames)
            socks_by_agent_name = {
                self.clients[sock]["name"]: sock
                for sock in active_socks
                if sock in self.clients
            }

        self.add_event("trial_started", {
            "trial_id": trial_id,
            "topology": self.topology,
            "num_agents": self.num_agents,
            "max_messages": max_messages,
            "ollama_options": self.ollama_options,
            "pool_size": pool_size,
            "figures_per_card": figures_per_card,
            "common_symbol": self.common_symbol,
        })

        self.broadcast({
            "type": "reset_chat_history",
            "trial_id": trial_id,
        }, recipients=active_socks)

        for sock in active_socks:
            with self.lock:
                if sock not in self.clients:
                    continue
                name = self.clients[sock]["name"]
            self.send_json(sock, {
                "type": "experiment_start",
                "trial_id": trial_id,
                "agent_name": display_agent_name(name),
                "your_symbols": self.cards[name],
                "num_agents": self.num_agents,
                "figures_per_card": figures_per_card,
                "pool_size": pool_size,
                "topology": self.topology,
                "discussion_rounds": None,
                "max_messages": max_messages,
                "ollama_options": self.ollama_options,
                "circle_neighbors": [display_agent_name(n) for n in self.circle_neighbors_by_name.get(name, [])],
                "chain_contacts": [display_agent_name(n) for n in self.chain_contacts_by_name.get(name, [])],
                "y_contacts": [display_agent_name(n) for n in self.y_contacts_by_name.get(name, [])],
                "wheel_recipients": [display_agent_name(n) for n in self.wheel_contacts_by_name.get(name, [])],
            })

        answers = {}
        answer_message_count = None
        trial_finished = False
        max_messages_reached = False
        stopped_by_user = False
        scheduler_steps = 0
        response_timings = []
        skip_sock_once = None
        max_scheduler_steps = max_messages * max(self.num_agents, 1) * 4
        while self.running and not trial_finished:
            with self.lock:
                if self.stop_requested:
                    stopped_by_user = True
                    trial_finished = True
                    break
                currently_connected = {
                    info["name"]: sock for sock, info in self.clients.items()
                    if info["name"] in required_agent_names
                }
                missing_required = [
                    name for name in required_agent_names if name not in currently_connected
                ]
                replaced_required = [
                    name for name in required_agent_names
                    if name in currently_connected
                    and currently_connected[name] is not socks_by_agent_name.get(name)
                ]
            if missing_required or replaced_required:
                resumed = self.wait_for_trial_reconnect(
                    required_agent_names,
                    socks_by_agent_name,
                    trial_id,
                )
                if resumed is None:
                    stopped_by_user = True
                    trial_finished = True
                    break
                socks_by_agent_name = resumed
                active_socks = [socks_by_agent_name[name] for name in required_agent_names]
                sock_agent_ids = {
                    sock: get_agent_id(name) for name, sock in socks_by_agent_name.items()
                }
                continue
            socks_by_agent_name = currently_connected
            active_socks = [socks_by_agent_name[name] for name in required_agent_names]
            sock_agent_ids = {
                sock: get_agent_id(name) for name, sock in socks_by_agent_name.items()
            }
            if self.message_count >= max_messages:
                max_messages_reached = True
                trial_finished = True
                break

            if scheduler_steps >= max_scheduler_steps:
                trial_finished = True
                break

            current_sock = self.choose_next_sock(active_socks, exclude=skip_sock_once)
            skip_sock_once = None
            if current_sock is None:
                trial_finished = True
                break

            with self.lock:
                if current_sock not in self.clients:
                    continue
                speaker = self.clients[current_sock]["name"]
                speaker_id = sock_agent_ids.get(current_sock)
                self.current_speaker = display_agent_name(speaker)

            can_answer = self.answer_allowed_now(active_socks)
            self.add_event("turn_started", {
                "message_count": self.message_count,
                "speaker": display_agent_name(speaker),
                "can_answer": can_answer,
            })
            turn_request_started = time.monotonic()
            self.send_turn_request(current_sock, speaker_id, speaker, self.message_count, can_answer)
            while True:
                resp = self.recv_turn_response(
                    current_sock,
                    expected_trial_id=trial_id,
                    required_socks=active_socks,
                    total_timeout=CLIENT_TURN_TIMEOUT_SECONDS,
                )
                if not resp or resp.get("type") != "disconnect":
                    break
                previous_current_sock = current_sock
                resumed = self.wait_for_trial_reconnect(
                    required_agent_names,
                    socks_by_agent_name,
                    trial_id,
                )
                if resumed is None:
                    resp = {"type": "stopped"}
                    break
                socks_by_agent_name = resumed
                active_socks = [socks_by_agent_name[name] for name in required_agent_names]
                sock_agent_ids = {
                    sock: get_agent_id(name) for name, sock in socks_by_agent_name.items()
                }
                current_sock = socks_by_agent_name[speaker]
                speaker_id = sock_agent_ids.get(current_sock)
                if current_sock is not previous_current_sock:
                    self.add_event("turn_retried_after_reconnect", {
                        "trial_id": trial_id,
                        "speaker": display_agent_name(speaker),
                        "message_count": self.message_count,
                    })
                    turn_request_started = time.monotonic()
                    self.send_turn_request(
                        current_sock,
                        speaker_id,
                        speaker,
                        self.message_count,
                        can_answer,
                    )
            with self.lock:
                if self.current_speaker == display_agent_name(speaker):
                    self.current_speaker = None
            response_text = resp.get("text", "") if isinstance(resp, dict) else ""
            server_wait_seconds = round(time.monotonic() - turn_request_started, 6)
            response_timing = {
                "turn": scheduler_steps + 1,
                "message_count_before_response": self.message_count,
                "agent": display_agent_name(speaker),
                "response_type": resp.get("type", "none") if isinstance(resp, dict) else "none",
                "server_wait_time_seconds": server_wait_seconds,
                "request_id": resp.get("request_id") if isinstance(resp, dict) else None,
                "time_to_first_thinking_seconds": resp.get("time_to_first_thinking_seconds") if isinstance(resp, dict) else None,
                "thinking_time_seconds": resp.get("thinking_time_seconds") if isinstance(resp, dict) else None,
                "thinking_stream_time_seconds": resp.get("thinking_stream_time_seconds") if isinstance(resp, dict) else None,
                "thinking_to_response_gap_seconds": resp.get("thinking_to_response_gap_seconds") if isinstance(resp, dict) else None,
                "time_to_first_response_seconds": resp.get("time_to_first_response_seconds") if isinstance(resp, dict) else None,
                "response_time_seconds": resp.get("response_time_seconds") if isinstance(resp, dict) else None,
                "total_generation_time_seconds": resp.get("total_generation_time_seconds") if isinstance(resp, dict) else None,
                "thinking_chars": resp.get("thinking_chars", 0) if isinstance(resp, dict) else 0,
                "response_chars": resp.get("response_chars", 0) if isinstance(resp, dict) else 0,
                "visible_response_tokens": resp.get("visible_response_tokens", 0) if isinstance(resp, dict) else 0,
                "done_reason": resp.get("ollama_done_reason") if isinstance(resp, dict) else None,
                "eval_count": resp.get("ollama_eval_count") if isinstance(resp, dict) else None,
            }
            response_timings.append(response_timing)
            if isinstance(resp, dict) and "ollama_response" in resp:
                self.trial_model_responses.append({
                    "speaker": display_agent_name(speaker),
                    "message_count_before_response": self.message_count,
                    "response_type": resp.get("type", "invalid"),
                    "parser_action": resp.get("parser_action", "invalid"),
                    "ollama_response": str(resp.get("ollama_response", "") or ""),
                    "extracted_response": str(resp.get("extracted_response", "") or ""),
                    "validation_error": resp.get("validation_error", ""),
                    "timing": response_timing,
                })
            scheduler_steps += 1

            with self.lock:
                if self.stop_requested:
                    stopped_by_user = True
                    trial_finished = True
                    break

            if resp and resp.get("type") == "stopped":
                stopped_by_user = True
                trial_finished = True
                break
            if resp is None:
                pass
            elif resp.get("type") == "timeout":
                skip_sock_once = current_sock
                self.add_event("timeout", {"speaker": display_agent_name(speaker)})
            elif resp.get("type") == "ollama_error":
                skip_sock_once = current_sock
                self.add_event("client_ollama_error", {
                    "speaker": display_agent_name(speaker),
                    "error": str(resp.get("error", ""))[:1000],
                    "message": "Infrastructure error was not routed or counted; switching clients.",
                })
            elif resp.get("type") == "invalid":
                self.add_event("invalid_output", {
                    "speaker": display_agent_name(speaker),
                    "reason": resp.get("reason") or "Invalid or empty model output.",
                })
            elif resp.get("type") == "chat":
                text = resp.get("text", "")
                if text:
                    accepted = self.route_chat_message(
                        text,
                        speaker,
                        speaker_id,
                        current_sock,
                        active_socks,
                        self.message_count + 1,
                        target=resp.get("target"),
                        raw=resp.get("raw", ""),
                        target_source=resp.get("target_source", ""),
                        original_target=resp.get("original_target", ""),
                    )
                    if accepted and self.message_count >= max_messages:
                        max_messages_reached = True
                        trial_finished = True
            elif resp.get("type") == "answer":
                raw_word = resp.get("word", resp.get("symbol", resp.get("text", ""))).strip()
                word = normalize_figure_answer(raw_word)
                if not word:
                    self.add_event("invalid_output", {
                        "speaker": display_agent_name(speaker),
                        "reason": f"Invalid answer {raw_word!r}. Use one of: {', '.join(FIGURES)}.",
                    })
                    continue
                if not can_answer and self.topology != "circle":
                    exact_response = str(resp.get("extracted_response", resp.get("raw", "")) or "")
                    accepted = bool(exact_response) and self.route_chat_message(
                        exact_response,
                        speaker,
                        speaker_id,
                        current_sock,
                        active_socks,
                        self.message_count + 1,
                        target=resp.get("target"),
                        raw=resp.get("raw", ""),
                        target_source=resp.get("target_source", ""),
                        original_target=resp.get("original_target", ""),
                    )
                    if accepted and self.message_count >= max_messages:
                        max_messages_reached = True
                        trial_finished = True
                    continue
                answers[speaker] = word
                answer_message_count = self.message_count
                self.add_event("answer", {
                    "message_count": answer_message_count,
                    "speaker": display_agent_name(speaker),
                    "word": word,
                })
                trial_finished = True

            with self.lock:
                self.turn_count += 1
            time.sleep(0.5)

            with self.lock:
                active_socks = [sock for sock in active_socks if sock in self.clients]

        elapsed = self.elapsed_since_first_message()
        trial_wall_time_seconds = max(0.0, time.monotonic() - trial_started_monotonic)
        completed_response_timings = [
            timing for timing in response_timings
            if timing.get("total_generation_time_seconds") is not None
        ]

        def timing_total(field):
            values = []
            for timing in completed_response_timings:
                try:
                    values.append(max(0.0, float(timing.get(field) or 0)))
                except (TypeError, ValueError):
                    continue
            return round(sum(values), 6), values

        total_thinking_time, thinking_values = timing_total("thinking_time_seconds")
        total_visible_response_time, response_values = timing_total("response_time_seconds")
        total_generation_time, generation_values = timing_total("total_generation_time_seconds")
        final_answer_speaker = next(reversed(answers), None) if answers else None
        final_answer_word = answers[final_answer_speaker] if final_answer_speaker else None
        found = bool(final_answer_word) and final_answer_word.strip().lower() == str(self.common_symbol).lower()
        submitted_figure_status = final_answer_word
        if not submitted_figure_status:
            if stopped_by_user:
                submitted_figure_status = "Trial stopped"
            elif max_messages_reached:
                submitted_figure_status = "No figure submitted (message limit reached)"
            else:
                submitted_figure_status = "No figure submitted"
        displayed_messages_per_agent = {
            display_agent_name(name): count
            for name, count in self.messages_per_agent.items()
        }
        displayed_answers = {
            display_agent_name(name): word
            for name, word in answers.items()
        }
        messages_used = answer_message_count if answer_message_count is not None else self.message_count
        if stopped_by_user:
            efficiency_status = "stopped"
            efficiency_explanation = "Trial was stopped manually."
            efficiency_max_messages = max_messages
        else:
            efficiency_status, efficiency_explanation, efficiency_max_messages = evaluate_efficiency(
                found,
                bool(answers),
                messages_used,
                self.num_agents,
                self.topology,
                max_messages,
            )
        result = {
            "trial_id": trial_id,
            "started_at": trial_started_at,
            "completed_at": datetime.now(timezone.utc).isoformat(),
            "topology": self.topology,
            "num_agents": self.num_agents,
            "result": efficiency_status,
            "success": found,
            "temperature": self.ollama_options.get("temperature"),
            "ollama_options": self.ollama_options,
            "common_word": self.common_symbol,
            "answering_agent": display_agent_name(final_answer_speaker) if final_answer_speaker else None,
            "submitted_answer": final_answer_word,
            "submitted_figure_status": submitted_figure_status,
            "correct_answer": self.common_symbol,
            "cards": {
                display_agent_name(name): list(symbols)
                for name, symbols in self.cards.items()
            },
            "is_correct": found,
            "message_count": self.message_count,
            "delivery_count": self.delivery_count,
            "messages_per_agent": displayed_messages_per_agent,
            "answers": displayed_answers,
            "final_answer_speaker": display_agent_name(final_answer_speaker) if final_answer_speaker else None,
            "final_answer_word": final_answer_word,
            "time_seconds": round(elapsed, 2),
            "trial_wall_time_seconds": round(trial_wall_time_seconds, 2),
            "trial_active_time_seconds": round(
                max(0.0, trial_wall_time_seconds - self.trial_pause_total_seconds),
                2,
            ),
            "response_timings": response_timings,
            "model_responses": list(self.trial_model_responses),
            "completed_generation_count": len(completed_response_timings),
            "total_thinking_time_seconds": total_thinking_time,
            "average_thinking_time_seconds": round(
                total_thinking_time / len(thinking_values), 6
            ) if thinking_values else 0.0,
            "total_visible_response_time_seconds": total_visible_response_time,
            "average_visible_response_time_seconds": round(
                total_visible_response_time / len(response_values), 6
            ) if response_values else 0.0,
            "total_generation_time_seconds": total_generation_time,
            "average_generation_time_seconds": round(
                total_generation_time / len(generation_values), 6
            ) if generation_values else 0.0,
            "total_messages": self.message_count,
            "total_deliveries": self.delivery_count,
            "total_turns": self.turn_count,
            "rounds": None,
            "answer_round": None,
            "messages_before_answer": answer_message_count,
            "max_messages_reached": max_messages_reached,
            "efficiency_explanation": efficiency_explanation,
            "efficiency_max_messages": efficiency_max_messages,
            "max_messages_per_trial": max_messages,
            "discussion_rounds": None,
            "stopped": stopped_by_user,
            "interrupted_by_disconnect": False,
            "disconnect_count": len(self.trial_disconnects),
            "disconnect_pause_seconds": round(self.trial_pause_total_seconds, 2),
            "disconnects": list(self.trial_disconnects),
        }

        with self.lock:
            completed_trial_routes = list(self.trial_routes)
        batch_complete, persistence_error = self.persist_auto_batch_trial(result, completed_trial_routes)

        with self.lock:
            self.results.append(result)
            self.results = self.results[-100:]
            self.trial_active = False
            self.trial_requested = False
            self.stop_requested = False
            self.current_speaker = None
            self.current_route = None
            should_continue_auto = self.auto_trials
            should_restart_ollama = (
                should_continue_auto
                and ollama_restart_due(self.auto_batch_completed, self.auto_trial_target)
            )
            if should_restart_ollama:
                self.auto_trial_generation += 1
                ollama_restart_generation = self.auto_trial_generation
                ollama_restart_after_trial = self.auto_batch_completed
            else:
                ollama_restart_generation = None
                ollama_restart_after_trial = None
        self.broadcast({"type": "experiment_end", **result}, recipients=active_socks)
        with self.lock:
            if self.active_trial_id == trial_id:
                self.active_trial_id = None
        self.add_event("trial_finished", result)
        if persistence_error:
            self.add_event("auto_trials_save_failed", {
                "message": persistence_error,
                "batch_id": self.auto_batch_id,
            })
        elif batch_complete:
            self.add_event("auto_trials_completed", {
                "batch_id": self.auto_batch_id,
                "completed": self.auto_batch_completed,
                "target": self.auto_trial_target,
                "report": str(self.auto_batch_dir / "report.md"),
            })
            next_started, study_complete, study_error = self.advance_full_study()
            if study_error:
                self.add_event("full_study_failed", {
                    "study_id": self.full_study_id,
                    "study_kind": self.full_study_kind,
                    "study_label": self.full_study_label,
                    "message": study_error,
                    "directory": str(self.full_study_dir),
                })
            elif study_complete:
                self.add_event("full_study_completed", {
                    "study_id": self.full_study_id,
                    "study_kind": self.full_study_kind,
                    "study_label": self.full_study_label,
                    "topologies": self.full_study_topologies,
                    "completed_batches": self.full_study_completed_batches,
                    "total_batches": len(self.full_study_batches),
                    "total_trials": len(self.full_study_batches) * AUTO_TRIAL_TARGET,
                    "report": str(
                        self.full_study_dir
                        / ("gemma4-50trials-data.txt" if self.full_study_kind == "four_topologies" else "report.md")
                    ),
                })
                self.request_poweroff_all(
                    source=f"{self.full_study_kind or 'automated'}_study_complete",
                    delay=POWER_OFF_DELAY_SECONDS,
                )
            elif next_started:
                self.add_event("full_study_cooling_started", {
                    "study_id": self.full_study_id,
                    "after_batch": self.full_study_index + 1,
                    "pause_kind": self.full_study_cooling_kind,
                    "cooling_until": self.full_study_cooling_until,
                    "cooling_options": self.full_study_cooling_options,
                })
        if should_restart_ollama:
            threading.Thread(
                target=self.run_mid_batch_ollama_restart,
                args=(ollama_restart_generation, ollama_restart_after_trial),
                daemon=True,
            ).start()
        elif should_continue_auto:
            self.schedule_next_auto_trial()


def make_handler(experiment, static_root):
    class DashboardHandler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            print(f"[HTTP] {fmt % args}", flush=True)

        def send_json_response(self, status, payload):
            body = json.dumps(payload).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if self.path == "/api/state":
                self.send_json_response(200, experiment.snapshot())
                return
            if self.path.startswith("/api/events"):
                self.handle_events()
                return
            self.serve_static()

        def do_POST(self):
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length) if length else b"{}"
            try:
                payload = json.loads(raw.decode("utf-8"))
            except json.JSONDecodeError:
                payload = {}

            if self.path == "/api/start":
                ok, message = experiment.start_trial(
                    payload.get("topology", "circle"),
                    payload.get("num_agents", 5),
                    payload.get("discussion_rounds"),
                    payload.get("ollama_options"),
                    payload.get("max_messages"),
                )
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/stop":
                ok, message = experiment.stop_trial()
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/auto-trials":
                ok, message = experiment.set_auto_trials(
                    payload.get("enabled", False),
                    payload.get("topology", "circle"),
                    payload.get("num_agents", 5),
                    payload.get("discussion_rounds"),
                    payload.get("ollama_options"),
                    payload.get("max_messages"),
                )
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/full-study":
                ok, message = experiment.start_full_study(
                    payload.get("ollama_options"),
                    payload.get("cooling_options"),
                    "full",
                )
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/circle-study":
                ok, message = experiment.start_full_study(
                    payload.get("ollama_options"),
                    payload.get("cooling_options"),
                    "circle",
                )
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/y-study":
                ok, message = experiment.start_full_study(
                    payload.get("ollama_options"),
                    payload.get("cooling_options"),
                    "y",
                )
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/wheel-study":
                ok, message = experiment.start_full_study(
                    payload.get("ollama_options"),
                    payload.get("cooling_options"),
                    "wheel",
                )
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/wheel-temperature-1-study":
                ok, message = experiment.start_full_study(
                    payload.get("ollama_options"),
                    payload.get("cooling_options"),
                    "wheel_temperature_1",
                )
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/chain-study":
                ok, message = experiment.start_full_study(
                    payload.get("ollama_options"),
                    payload.get("cooling_options"),
                    "chain",
                )
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/remaining-study":
                ok, message = experiment.start_full_study(
                    payload.get("ollama_options"),
                    payload.get("cooling_options"),
                    "remaining",
                )
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/leavitt-study":
                ok, message = experiment.start_full_study(
                    payload.get("ollama_options"),
                    payload.get("cooling_options"),
                    "leavitt",
                )
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/four-topology-study":
                ok, message = experiment.start_full_study(
                    payload.get("ollama_options"),
                    payload.get("cooling_options"),
                    "four_topologies",
                )
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/check-poweroff":
                ready, readiness = experiment.check_poweroff_readiness(emit_event=True)
                self.send_json_response(200 if ready else 409, {
                    "ok": ready,
                    "message": "All Jetsons are ready for passwordless shutdown." if ready else "Power-off readiness failed.",
                    "readiness": readiness,
                })
                return
            if self.path == "/api/check-ollama-restart":
                ready, readiness = experiment.check_ollama_restart_readiness(emit_event=True)
                self.send_json_response(200 if ready else 409, {
                    "ok": ready,
                    "message": (
                        "All Jetsons can restart Ollama without a password."
                        if ready
                        else "Ollama restart readiness failed."
                    ),
                    "readiness": readiness,
                })
                return
            if self.path == "/api/power-off-jetsons":
                ok, message = experiment.request_poweroff_all(source="manual", delay=3)
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/restart-clients":
                ok, message = experiment.restart_clients()
                self.send_json_response(200 if ok else 409, {"ok": ok, "message": message})
                return
            if self.path == "/api/clear-results":
                with experiment.lock:
                    experiment.results = []
                experiment.add_event("results_cleared", {})
                self.send_json_response(200, {"ok": True})
                return
            self.send_json_response(404, {"ok": False, "message": "Not found"})

        def handle_events(self):
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.end_headers()
            last_id = 0
            while experiment.running:
                with experiment.lock:
                    events = [event for event in experiment.events if event["id"] > last_id]
                    if not events:
                        events = [{
                            "id": experiment.event_id,
                            "time": round(time.time(), 3),
                            "kind": "state",
                            "payload": {},
                            "snapshot": experiment.snapshot_locked(),
                        }]
                try:
                    for event in events:
                        last_id = max(last_id, event["id"])
                        self.wfile.write(f"data: {json.dumps(event)}\n\n".encode("utf-8"))
                    self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError):
                    break
                time.sleep(1)

        def serve_static(self):
            url_path = self.path.split("?", 1)[0].lstrip("/")
            if not url_path:
                url_path = "index.html"
            target = (static_root / url_path).resolve()
            if static_root not in target.parents and target != static_root:
                self.send_error(403)
                return
            if not target.exists() or not target.is_file():
                self.send_error(404)
                return
            content_type = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
            body = target.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
            self.end_headers()
            self.wfile.write(body)

    return DashboardHandler


def main():
    parser = argparse.ArgumentParser(description="Live Leavitt Jetson dashboard")
    parser.add_argument("--http-host", default="127.0.0.1")
    parser.add_argument("--http-port", type=int, default=5173)
    parser.add_argument("--tcp-host", default="0.0.0.0")
    parser.add_argument("--tcp-port", type=int, default=5001)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    experiment = DashboardExperiment(args.tcp_host, args.tcp_port)
    experiment.start_tcp_server()

    server = ThreadingHTTPServer((args.http_host, args.http_port), make_handler(experiment, root))
    print(f"Dashboard: http://{args.http_host}:{args.http_port}", flush=True)
    print(f"Jetsons connect to TCP port {args.tcp_port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        experiment.running = False
        server.shutdown()


if __name__ == "__main__":
    main()
