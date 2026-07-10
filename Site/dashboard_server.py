import argparse
import json
import mimetypes
import os
import random
import re
import socket
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


FIGURES = ["square", "circle", "triangle", "diamond", "cross", "asterisk"]
MIN_PARTICIPANTS = 2
MAX_PARTICIPANTS = 5
DEFAULT_FIGURES_PER_CARD = 3
MAX_ROUNDS_PER_TRIAL = 10
DEFAULT_MAX_MESSAGES_PER_TRIAL = 50
MIN_MESSAGES_PER_TRIAL = 1
MAX_MESSAGES_PER_TRIAL = 500
CIRCLE_ANSWER_MESSAGE_GATE = 5
EFFICIENCY_MAX_ROUNDS_BY_AGENTS = {2: 3, 3: 3, 4: 4, 5: 4}
CIRCLE_EFFICIENCY_LIMIT_BY_AGENTS = {2: 4, 3: 5, 4: 6, 5: 8}
CIRCLE_HARD_STOP_BY_AGENTS = {2: 6, 3: 7, 4: 8, 5: 10}
VALID_TOPOLOGIES = {"broadcast", "circle", "chain", "y", "wheel"}
FIXED_FIVE_AGENT_TOPOLOGIES = {"circle", "chain", "y", "wheel"}
DEFAULT_OLLAMA_OPTIONS = {
    "temperature": 0.2,
    "top_p": 0.7,
    "repeat_penalty": 1.2,
    "num_predict": 77,
}
JETSON_SSH_USER = "minds_user"
JETSON_HOSTNAMES = [
    "jetson1.local",
    "jetson2.local",
    "jetson3.local",
    "jetson4.local",
    "jetson5.local",
]
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
        1: [5],
        2: [5],
        3: [5],
        4: [5],
        5: [1, 2, 3, 4],
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


def normalize_max_messages(value):
    try:
        messages = int(value)
    except (TypeError, ValueError):
        messages = DEFAULT_MAX_MESSAGES_PER_TRIAL
    return max(MIN_MESSAGES_PER_TRIAL, min(MAX_MESSAGES_PER_TRIAL, messages))


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
        "num_predict": number("num_predict", 1, 300, integer=True),
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


class DashboardExperiment:
    def __init__(self, tcp_host, tcp_port):
        self.tcp_host = tcp_host
        self.tcp_port = tcp_port
        self.clients = {}
        self.turn_order = []
        self.recv_buffers = {}
        self.lock = threading.RLock()
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
        self.auto_max_messages = DEFAULT_MAX_MESSAGES_PER_TRIAL
        self.auto_restart_delay = 2
        self.auto_trial_generation = 0
        self.trial_counter = 0
        self.topology = "circle"
        self.num_agents = 5
        self.discussion_rounds = None
        self.ollama_options = normalize_ollama_options(None)
        self.max_messages = DEFAULT_MAX_MESSAGES_PER_TRIAL
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
        except OSError:
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
        except (json.JSONDecodeError, ConnectionResetError, OSError):
            self.drop_client(sock, "receive failed")
            return None
        finally:
            try:
                sock.settimeout(None)
            except OSError:
                pass

    def recv_turn_response(self, sock, total_timeout=300):
        deadline = time.time() + total_timeout
        while time.time() < deadline:
            with self.lock:
                if self.stop_requested:
                    return {"type": "stopped"}
            resp = self.recv_json(sock, timeout=1)
            if resp and resp.get("type") != "timeout":
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
                "reason": reason,
            })

    def handle_new_client(self, sock, address):
        self.send_json(sock, {"type": "nickname_request"})
        resp = self.recv_json(sock, timeout=30)
        if not resp or resp.get("type") != "nickname":
            self.drop_client(sock, "invalid handshake")
            return

        hostname = normalize_hostname(resp.get("hostname", ""))
        if hostname not in HOSTNAME_TO_AGENT:
            self.send_json(sock, {"type": "system", "text": f"Unknown hostname '{hostname}'."})
            self.drop_client(sock, "unknown hostname")
            return

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

            self.clients[sock] = {"name": hostname, "hostname": hostname, "address": address}
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

    def snapshot_locked(self):
        connected = []
        for info in self.clients.values():
            name = info["name"]
            connected.append({
                "name": display_agent_name(name),
                "hostname": info["hostname"],
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

    def missing_fixed_five_agents_locked(self):
        connected_names = {info["name"] for info in self.clients.values()}
        return [
            f"jetson{number}"
            for number in range(1, MAX_PARTICIPANTS + 1)
            if f"jetson{number}" not in connected_names
        ]

    def start_trial(self, topology, num_agents, discussion_rounds=None, ollama_options=None, max_messages=None):
        with self.lock:
            if self.trial_active or self.trial_requested:
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
            self.max_messages = normalize_max_messages(max_messages)
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
            auto_was_enabled = self.auto_trials
            if not self.trial_active and not self.trial_requested and not auto_was_enabled:
                return False, "No active trial to stop."
            if self.trial_active or self.trial_requested:
                self.stop_requested = True
            self.auto_trials = False
            self.auto_trial_generation += 1
            targets = list(self.clients.keys()) if self.trial_active or self.trial_requested else []
        for sock in targets:
            self.send_json(sock, {"type": "experiment_stop"})
        message = "Trial stop requested. Auto trials disabled." if targets else "Auto trials disabled."
        self.add_event("trial_stop_requested", {"message": message})
        return True, message

    def set_auto_trials(self, enabled, topology=None, num_agents=None, discussion_rounds=None, ollama_options=None, max_messages=None):
        should_start = False
        with self.lock:
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
            self.auto_max_messages = normalize_max_messages(max_messages)
            should_start = self.auto_trials and not self.trial_active and not self.trial_requested
        self.add_event("auto_trials_changed", {"enabled": self.auto_trials})
        if should_start:
            self.schedule_next_auto_trial(delay=0, generation=auto_trial_generation)
        return True, "Auto trials enabled." if self.auto_trials else "Auto trials disabled."

    def restart_clients(self):
        with self.lock:
            if self.trial_active or self.trial_requested:
                return False, "Wait until the current trial is finished before reloading Jetsons."
            old_socks = list(self.clients.keys())
            targets = [
                (normalize_hostname(host), host)
                for host in JETSON_HOSTNAMES
            ]
            self.clients = {}
            self.turn_order = []
            self.recv_buffers = {}
            self.results = []
            self.auto_trials = False
            self.auto_trial_generation += 1
            self.stop_requested = False
            self.trial_active = False
            self.trial_requested = False
            self.trial_counter = 0
            self.topology = "circle"
            self.num_agents = 5
            self.discussion_rounds = None
            self.ollama_options = normalize_ollama_options(None)
            self.max_messages = DEFAULT_MAX_MESSAGES_PER_TRIAL
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
                f"{JETSON_SSH_USER}@{host}",
                f"sudo /usr/bin/systemctl restart {JETSON_CLIENT_SERVICE}",
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
        self.start_trial(topology, num_agents, discussion_rounds, ollama_options, max_messages)

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

    def choose_next_sock(self, active_socks):
        selected_name = None
        with self.lock:
            active_names = [
                self.clients[sock]["name"]
                for sock in active_socks
                if sock in self.clients
            ]
            active_name_set = set(active_names)
            if not self.scheduler_queue:
                self.scheduler_queue = list(active_names)
            else:
                self.scheduler_queue = [
                    name for name in self.scheduler_queue if name in active_name_set
                ]
                for name in active_names:
                    if name not in self.scheduler_queue:
                        self.scheduler_queue.append(name)

            if not self.scheduler_queue:
                return active_socks[0] if active_socks else None

            min_messages = min(
                self.messages_per_agent.get(name, 0)
                for name in active_names
            )
            least_used = {
                name
                for name in active_names
                if self.messages_per_agent.get(name, 0) == min_messages
            }

            for name in list(self.scheduler_queue):
                if name in least_used and name in self.unread_agents:
                    self.scheduler_queue.remove(name)
                    self.scheduler_queue.append(name)
                    self.unread_agents.discard(name)
                    selected_name = name
                    break

            if selected_name is None:
                for name in list(self.scheduler_queue):
                    if name in least_used:
                        self.scheduler_queue.remove(name)
                        self.scheduler_queue.append(name)
                        self.unread_agents.discard(name)
                        selected_name = name
                        break

            if selected_name is None:
                selected_name = self.scheduler_queue.pop(0)
                self.scheduler_queue.append(selected_name)
                self.unread_agents.discard(selected_name)

        if selected_name:
            return self.sock_by_name(active_socks, selected_name)
        return active_socks[0] if active_socks else None

    def record_valid_message(self, speaker, receivers):
        with self.lock:
            if self.start_time is None:
                self.start_time = time.time()
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
                fallback_message_gate = min(CIRCLE_ANSWER_MESSAGE_GATE, max(self.max_messages - 1, 1))
                return bool(active_names) and (
                    all(self.messages_per_agent.get(name, 0) >= 1 for name in active_names)
                    or self.message_count >= fallback_message_gate
                )
            return bool(active_names) and all(
                self.messages_per_agent.get(name, 0) > 0
                for name in active_names
            )

    def elapsed_since_first_message(self):
        with self.lock:
            start_time = self.start_time
        if start_time is None:
            return 0
        return time.time() - start_time

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
        if self.topology == "circle":
            self.send_json(sock, {
                "type": "your_turn",
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
                "topology": "broadcast",
                "round": message_count,
                "message_count": message_count,
                "can_answer": can_answer,
                "discussion_rounds": None,
                "ollama_options": self.ollama_options,
            })

    def route_private_message(self, topology, contacts_by_name, last_target_by_speaker, contact_label, text, speaker, speaker_id, active_socks, round_number, target, raw):
        valid_contacts = contacts_by_name.get(speaker, [])
        receiver = internal_agent_name(target) if target else ""
        target_source = "agent"
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
                })
                return None
        receiver_sock = self.sock_by_name(active_socks, receiver)
        sent = receiver_sock and self.send_json(receiver_sock, {
            "type": "chat",
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
            "message": text,
            "raw": raw,
            "target_source": target_source,
            "elapsed": round(self.elapsed_since_first_message(), 2),
        }

    def route_chat_message(self, text, speaker, speaker_id, current_sock, active_socks, round_number, target=None, raw=""):
        if self.topology == "circle":
            valid_neighbors = self.circle_neighbors_by_name.get(speaker, [])
            receiver = internal_agent_name(target) if target else target
            target_source = "agent"
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
                    })
                    return False
            receiver_sock = self.sock_by_name(active_socks, receiver)
            sent = receiver_sock and self.send_json(receiver_sock, {
                "type": "chat",
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
                "message": text,
                "raw": raw,
                "target_source": target_source,
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
                {"type": "chat", "sender": display_agent_name(speaker), "text": text},
                exclude=current_sock,
                recipients=active_socks,
            )
            route = {
                "round": message_number,
                "topology": "broadcast",
                "sender": display_agent_name(speaker),
                "receiver": "ALL",
                "message": text,
                "raw": raw,
                "elapsed": round(self.elapsed_since_first_message(), 2),
            }

        with self.lock:
            self.current_route = route
        self.add_event("chat", route)
        return True

    def run_experiment(self):
        with self.lock:
            self.trial_requested = False
            self.trial_active = True
            self.trial_counter += 1
            trial_id = self.trial_counter
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
            max_messages = self.max_messages

        active_socks = self.wait_for_clients(self.num_agents)
        if not active_socks:
            result = {
                "trial_id": trial_id,
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

        for sock in active_socks:
            with self.lock:
                if sock not in self.clients:
                    continue
                name = self.clients[sock]["name"]
            self.send_json(sock, {
                "type": "experiment_start",
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
        max_scheduler_steps = max_messages * max(self.num_agents, 1) * 4
        initial_circle_socks = list(active_socks) if self.topology == "circle" else []

        while self.running and not trial_finished:
            with self.lock:
                if self.stop_requested:
                    stopped_by_user = True
                    trial_finished = True
                    break
                active_socks = [sock for sock in active_socks if sock in self.clients]
                initial_circle_socks = [
                    sock
                    for sock in initial_circle_socks
                    if sock in self.clients and sock in active_socks
                ]
            if self.message_count >= max_messages:
                max_messages_reached = True
                trial_finished = True
                break

            if scheduler_steps >= max_scheduler_steps:
                trial_finished = True
                break

            current_sock = (
                initial_circle_socks.pop(0)
                if initial_circle_socks
                else self.choose_next_sock(active_socks)
            )
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
            self.send_turn_request(current_sock, speaker_id, speaker, self.message_count, can_answer)
            resp = self.recv_turn_response(current_sock, total_timeout=300)
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
                self.add_event("timeout", {"speaker": display_agent_name(speaker)})
            elif resp.get("type") == "invalid":
                self.add_event("invalid_output", {"speaker": display_agent_name(speaker)})
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
                if not can_answer:
                    accepted = self.route_chat_message(
                        f"I think the common figure may be {word}.",
                        speaker,
                        speaker_id,
                        current_sock,
                        active_socks,
                        self.message_count + 1,
                        target=resp.get("target"),
                        raw=resp.get("raw", ""),
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
            if len(active_socks) < self.num_agents:
                trial_finished = True

        elapsed = self.elapsed_since_first_message()
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
            "is_correct": found,
            "message_count": self.message_count,
            "delivery_count": self.delivery_count,
            "messages_per_agent": displayed_messages_per_agent,
            "answers": displayed_answers,
            "final_answer_speaker": display_agent_name(final_answer_speaker) if final_answer_speaker else None,
            "final_answer_word": final_answer_word,
            "time_seconds": round(elapsed, 2),
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
        }

        with self.lock:
            self.results.append(result)
            self.results = self.results[-100:]
            self.trial_active = False
            self.trial_requested = False
            self.stop_requested = False
            self.current_speaker = None
            self.current_route = None
            should_continue_auto = self.auto_trials
        self.broadcast({"type": "experiment_end", **result}, recipients=active_socks)
        self.add_event("trial_finished", result)
        if should_continue_auto:
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
