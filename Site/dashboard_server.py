import argparse
import json
import mimetypes
import os
import random
import re
import socket
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
EFFICIENCY_MAX_ROUNDS_BY_AGENTS = {2: 3, 3: 3, 4: 4, 5: 4}
CIRCLE_EFFICIENCY_LIMIT_BY_AGENTS = {2: 4, 3: 5, 4: 6, 5: 8}
CIRCLE_HARD_STOP_BY_AGENTS = {2: 6, 3: 7, 4: 8, 5: 10}
VALID_TOPOLOGIES = {"broadcast", "circle", "chain", "y", "wheel"}
FIXED_FIVE_AGENT_TOPOLOGIES = {"circle", "chain", "y", "wheel"}
DEFAULT_DISCUSSION_ROUNDS = {
    "broadcast": 3,
    "circle": 6,
    "chain": 8,
    "y": 8,
    "wheel": 2,
}
DEFAULT_OLLAMA_OPTIONS = {
    "temperature": 0.2,
    "repeat_penalty": 1.3,
    "num_predict": 70,
}
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


def get_answer_allowed_from_round(topology, num_agents):
    return DEFAULT_DISCUSSION_ROUNDS.get(topology, DEFAULT_DISCUSSION_ROUNDS["broadcast"]) + 1


def get_default_discussion_rounds(topology, num_agents):
    return DEFAULT_DISCUSSION_ROUNDS.get(topology, DEFAULT_DISCUSSION_ROUNDS["broadcast"])


def normalize_discussion_rounds(value, default):
    try:
        rounds = int(value)
    except (TypeError, ValueError):
        rounds = default
    return max(0, rounds)


def normalize_ollama_options(value):
    source = value if isinstance(value, dict) else {}

    def number(name, minimum, maximum, integer=False):
        try:
            selected = float(source.get(name, DEFAULT_OLLAMA_OPTIONS[name]))
        except (TypeError, ValueError):
            selected = DEFAULT_OLLAMA_OPTIONS[name]
        selected = max(minimum, min(maximum, selected))
        return int(round(selected)) if integer else round(selected, 3)

    return {
        "temperature": number("temperature", 0, 2),
        "repeat_penalty": number("repeat_penalty", 0, 3),
        "num_predict": number("num_predict", 1, 300, integer=True),
    }


def evaluate_efficiency(found, has_answer, rounds_used, num_agents, topology):
    max_efficient_rounds = get_efficiency_limit(topology, num_agents)
    if not has_answer:
        return "failed_no_answer", "No answer was submitted before the hard stop.", max_efficient_rounds
    if not found:
        return "failed_wrong_answer", "Agents submitted a wrong answer.", max_efficient_rounds
    if rounds_used <= max_efficient_rounds:
        return (
            "success_efficient",
            f"Agents found the correct figure in {rounds_used} rounds, within the efficiency limit of {max_efficient_rounds} rounds.",
            max_efficient_rounds,
        )
    return (
        "success_slow",
        f"Agents found the correct figure, but used {rounds_used} rounds, after the efficiency limit of {max_efficient_rounds} rounds.",
        max_efficient_rounds,
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
        self.auto_topology = "broadcast"
        self.auto_num_agents = 5
        self.auto_discussion_rounds = get_default_discussion_rounds(self.auto_topology, self.auto_num_agents)
        self.auto_ollama_options = normalize_ollama_options(None)
        self.auto_restart_delay = 2
        self.trial_counter = 0
        self.topology = "broadcast"
        self.num_agents = 5
        self.discussion_rounds = get_default_discussion_rounds(self.topology, self.num_agents)
        self.ollama_options = normalize_ollama_options(None)
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
        self.message_count = 0
        self.turn_count = 0
        self.round_number = 1
        self.current_route = None
        self.current_speaker = None

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
                self.clients.pop(old_sock, None)
                self.recv_buffers.pop(old_sock, None)
                if old_sock in self.turn_order:
                    self.turn_order.remove(old_sock)
                try:
                    old_sock.close()
                except OSError:
                    pass

            self.clients[sock] = {"name": hostname, "hostname": hostname, "address": address}
            self.turn_order.append(sock)

        self.send_json(sock, {
            "type": "welcome",
            "agent_name": display_agent_name(hostname),
            "hostname": hostname,
            "text": f"Welcome {display_agent_name(hostname)} ({hostname}). Waiting for next trial start...",
        })
        self.add_event("client_joined", {"agent": display_agent_name(hostname), "hostname": hostname})

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
            "round": self.round_number,
            "messages": self.message_count,
            "turns": self.turn_count,
            "commonSymbol": self.common_symbol,
            "currentRoute": self.current_route,
            "currentSpeaker": self.current_speaker,
            "results": self.results[-50:],
        }

    def snapshot(self):
        with self.lock:
            return self.snapshot_locked()

    def start_trial(self, topology, num_agents, discussion_rounds=None, ollama_options=None):
        with self.lock:
            if self.trial_active or self.trial_requested:
                return False, "A trial is already running or waiting for Jetsons."
            self.stop_requested = False
            self.topology = topology if topology in VALID_TOPOLOGIES else "broadcast"
            if self.topology in FIXED_FIVE_AGENT_TOPOLOGIES:
                self.num_agents = MAX_PARTICIPANTS
            else:
                self.num_agents = max(MIN_PARTICIPANTS, min(MAX_PARTICIPANTS, int(num_agents)))
            self.discussion_rounds = normalize_discussion_rounds(
                discussion_rounds,
                get_default_discussion_rounds(self.topology, self.num_agents),
            )
            self.ollama_options = normalize_ollama_options(ollama_options)
            self.trial_requested = True
        threading.Thread(target=self.run_experiment, daemon=True).start()
        self.add_event("trial_requested", {
            "topology": self.topology,
            "num_agents": self.num_agents,
            "discussion_rounds": self.discussion_rounds,
            "ollama_options": self.ollama_options,
        })
        return True, "Trial requested."

    def stop_trial(self):
        with self.lock:
            if not self.trial_active and not self.trial_requested:
                return False, "No active trial to stop."
            self.stop_requested = True
            self.auto_trials = False
            targets = list(self.clients.keys())
        for sock in targets:
            self.send_json(sock, {"type": "experiment_stop"})
        self.add_event("trial_stop_requested", {"message": "Trial stop requested."})
        return True, "Trial stop requested."

    def set_auto_trials(self, enabled, topology=None, num_agents=None, discussion_rounds=None, ollama_options=None):
        should_start = False
        with self.lock:
            self.auto_trials = bool(enabled)
            if topology is not None:
                self.auto_topology = topology if topology in VALID_TOPOLOGIES else "broadcast"
            if num_agents is not None:
                if self.auto_topology in FIXED_FIVE_AGENT_TOPOLOGIES:
                    self.auto_num_agents = MAX_PARTICIPANTS
                else:
                    self.auto_num_agents = max(MIN_PARTICIPANTS, min(MAX_PARTICIPANTS, int(num_agents)))
            self.auto_discussion_rounds = normalize_discussion_rounds(
                discussion_rounds,
                get_default_discussion_rounds(self.auto_topology, self.auto_num_agents),
            )
            self.auto_ollama_options = normalize_ollama_options(ollama_options)
            should_start = self.auto_trials and not self.trial_active and not self.trial_requested
        self.add_event("auto_trials_changed", {"enabled": self.auto_trials})
        if should_start:
            self.schedule_next_auto_trial(delay=0)
        return True, "Auto trials enabled." if self.auto_trials else "Auto trials disabled."

    def restart_clients(self):
        with self.lock:
            if self.trial_active or self.trial_requested:
                return False, "Wait until the current trial is finished before reloading Jetsons."
            targets = list(self.clients.keys())
            self.auto_trials = False
        sent_count = 0
        for sock in targets:
            if self.send_json(sock, {"type": "restart_client"}):
                sent_count += 1
        self.add_event("clients_restart_requested", {"count": sent_count})
        return True, f"Reload requested for {sent_count} connected Jetson client{'s' if sent_count != 1 else ''}."

    def schedule_next_auto_trial(self, delay=None):
        threading.Thread(
            target=self.maybe_start_next_auto_trial,
            args=(self.auto_restart_delay if delay is None else delay,),
            daemon=True,
        ).start()

    def maybe_start_next_auto_trial(self, delay):
        if delay > 0:
            time.sleep(delay)
        with self.lock:
            if not self.auto_trials or self.trial_active or self.trial_requested:
                return
            topology = self.auto_topology
            num_agents = self.auto_num_agents
            discussion_rounds = self.auto_discussion_rounds
            ollama_options = self.auto_ollama_options
        self.start_trial(topology, num_agents, discussion_rounds, ollama_options)

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
            self.add_event("waiting", {"selected": len(selected), "needed": needed, "missing": missing})
            if len(selected) >= needed and not missing:
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

    def recent_circle_messages(self, agent_id):
        return list(self.agent_histories.get(agent_id, [])[-5:])

    def recent_messages(self, agent_id):
        return list(self.agent_histories.get(agent_id, [])[-5:])

    def preferred_contact(self, speaker, contacts_by_name, last_target_by_speaker):
        contacts = contacts_by_name.get(speaker, [])
        if not contacts:
            return ""
        last_target = last_target_by_speaker.get(speaker)
        for contact in contacts:
            if contact != last_target:
                return display_agent_name(contact)
        return display_agent_name(contacts[0])

    def preferred_circle_neighbor(self, speaker):
        return self.preferred_contact(
            speaker,
            self.circle_neighbors_by_name,
            self.circle_last_target_by_speaker,
        )

    def send_turn_request(self, sock, speaker_id, speaker, round_number, can_answer):
        if self.topology == "circle":
            self.send_json(sock, {
                "type": "your_turn",
                "topology": "circle",
                "round": round_number,
                "can_answer": can_answer,
                "discussion_rounds": self.discussion_rounds,
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
                "round": round_number,
                "can_answer": can_answer,
                "discussion_rounds": self.discussion_rounds,
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
                "round": round_number,
                "can_answer": can_answer,
                "discussion_rounds": self.discussion_rounds,
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
                "round": round_number,
                "can_answer": can_answer,
                "discussion_rounds": self.discussion_rounds,
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
                "round": round_number,
                "can_answer": can_answer,
                "discussion_rounds": self.discussion_rounds,
                "ollama_options": self.ollama_options,
            })

    def route_private_message(self, topology, contacts_by_name, last_target_by_speaker, contact_label, text, speaker, speaker_id, active_socks, round_number, target, raw):
        valid_contacts = contacts_by_name.get(speaker, [])
        receiver = internal_agent_name(target) if target else ""
        if receiver not in valid_contacts:
            preferred = internal_agent_name(self.preferred_contact(speaker, contacts_by_name, last_target_by_speaker))
            receiver = preferred if preferred in valid_contacts else (valid_contacts[0] if valid_contacts else "")
        if not receiver:
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
        return {
            "round": round_number,
            "topology": topology,
            "sender": display_agent_name(speaker),
            "receiver": display_agent_name(receiver),
            "message": text,
            "raw": raw,
        }

    def route_chat_message(self, text, speaker, speaker_id, current_sock, active_socks, round_number, target=None, raw=""):
        self.message_count += 1
        if self.topology == "circle":
            valid_neighbors = self.circle_neighbors_by_name.get(speaker, [])
            receiver = internal_agent_name(target) if target else target
            if not receiver or receiver not in valid_neighbors:
                self.add_event("invalid_route", {
                    "round": round_number,
                    "sender": display_agent_name(speaker),
                    "target": target,
                    "valid_neighbors": [display_agent_name(n) for n in valid_neighbors],
                    "message": text,
                })
                return
            receiver_sock = self.sock_by_name(active_socks, receiver)
            sent = receiver_sock and self.send_json(receiver_sock, {
                "type": "chat",
                "sender": display_agent_name(speaker),
                "text": text,
            })
            if not sent:
                return
            self.circle_last_target_by_speaker[speaker] = receiver
            receiver_id = get_agent_id(receiver)
            if receiver_id is not None:
                self.agent_histories.setdefault(receiver_id, []).append({
                    "sender": display_agent_name(speaker),
                    "text": text,
                })
            route = {
                "round": round_number,
                "topology": "circle",
                "sender": display_agent_name(speaker),
                "receiver": display_agent_name(receiver),
                "message": text,
                "raw": raw,
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
                return
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
                return
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
                return
        else:
            self.broadcast(
                {"type": "chat", "sender": display_agent_name(speaker), "text": text},
                exclude=current_sock,
                recipients=active_socks,
            )
            route = {
                "round": round_number,
                "topology": "broadcast",
                "sender": display_agent_name(speaker),
                "receiver": "ALL",
                "message": text,
                "raw": raw,
            }

        with self.lock:
            self.current_route = route
        self.add_event("chat", route)

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
            self.message_count = 0
            self.turn_count = 0
            self.round_number = 1
            self.current_route = None
            self.current_speaker = None

        active_socks = self.wait_for_clients(self.num_agents)
        if not active_socks:
            result = {
                "trial_id": trial_id,
                "topology": self.topology,
                "num_agents": self.num_agents,
                "result": "stopped",
                "success": False,
                "common_word": self.common_symbol,
                "final_answer_speaker": None,
                "final_answer_word": None,
                "time_seconds": 0,
                "total_messages": self.message_count,
                "total_turns": self.turn_count,
                "rounds": 0,
                "answer_round": None,
                "max_rounds_reached": False,
                "efficiency_explanation": "Trial stopped before all Jetsons were ready.",
                "efficiency_max_rounds": get_hard_stop_round(self.topology, self.num_agents),
                "discussion_rounds": self.discussion_rounds,
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
            "discussion_rounds": self.discussion_rounds,
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
                "discussion_rounds": self.discussion_rounds,
                "ollama_options": self.ollama_options,
                "circle_neighbors": [display_agent_name(n) for n in self.circle_neighbors_by_name.get(name, [])],
                "chain_contacts": [display_agent_name(n) for n in self.chain_contacts_by_name.get(name, [])],
                "y_contacts": [display_agent_name(n) for n in self.y_contacts_by_name.get(name, [])],
                "wheel_recipients": [display_agent_name(n) for n in self.wheel_contacts_by_name.get(name, [])],
            })

        start_time = time.time()
        answers = {}
        answer_round = None
        hard_stop_round = get_hard_stop_round(self.topology, self.num_agents)
        hard_stop_round = max(hard_stop_round, self.discussion_rounds + 1)
        trial_finished = False
        max_rounds_reached = False
        stopped_by_user = False

        while self.running and not trial_finished:
            with self.lock:
                if self.stop_requested:
                    stopped_by_user = True
                    trial_finished = True
                    break
                self.round_number = self.round_number or 1
                round_number = self.round_number
            if round_number > hard_stop_round:
                max_rounds_reached = True
                trial_finished = True
                break

            self.broadcast({"type": "system", "text": f"===== ROUND {round_number} ====="}, recipients=active_socks)
            self.add_event("round_started", {"round": round_number})

            for current_sock in list(active_socks):
                with self.lock:
                    if self.stop_requested:
                        stopped_by_user = True
                        trial_finished = True
                        break
                    if current_sock not in self.clients:
                        continue
                    speaker = self.clients[current_sock]["name"]
                    speaker_id = sock_agent_ids.get(current_sock)
                    self.current_speaker = display_agent_name(speaker)
                if speaker in answers:
                    continue

                self.broadcast(
                    {"type": "system", "text": f"[Waiting for {display_agent_name(speaker)} to respond]"},
                    exclude=current_sock,
                    recipients=active_socks,
                )
                can_answer = round_number > self.discussion_rounds
                self.add_event("turn_started", {
                    "round": round_number,
                    "speaker": display_agent_name(speaker),
                    "can_answer": can_answer,
                })
                self.send_turn_request(current_sock, speaker_id, speaker, round_number, can_answer)
                resp = self.recv_turn_response(current_sock, total_timeout=300)
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
                    continue
                if resp.get("type") == "timeout":
                    with self.lock:
                        self.turn_count += 1
                    self.add_event("timeout", {"speaker": display_agent_name(speaker), "round": round_number})
                    continue

                if resp.get("type") == "chat":
                    text = resp.get("text", "") or resp.get("raw", "")
                    if text:
                        self.route_chat_message(
                            text,
                            speaker,
                            speaker_id,
                            current_sock,
                            active_socks,
                            round_number,
                            target=resp.get("target"),
                            raw=resp.get("raw", ""),
                        )
                elif resp.get("type") == "answer":
                    word = resp.get("word", resp.get("symbol", resp.get("text", ""))).strip()
                    if can_answer:
                        answers[speaker] = word
                        answer_round = round_number
                        self.add_event("answer", {
                            "round": round_number,
                            "speaker": display_agent_name(speaker),
                            "word": word,
                        })
                        with self.lock:
                            self.turn_count += 1
                        trial_finished = True
                        break
                    self.add_event("early_answer", {
                        "round": round_number,
                        "speaker": display_agent_name(speaker),
                        "word": word,
                    })

                with self.lock:
                    self.turn_count += 1
                time.sleep(0.5)

            with self.lock:
                self.round_number += 1
                active_socks = [sock for sock in active_socks if sock in self.clients]
            if len(active_socks) < self.num_agents:
                trial_finished = True

        elapsed = time.time() - start_time
        final_answer_speaker = next(reversed(answers), None) if answers else None
        final_answer_word = answers[final_answer_speaker] if final_answer_speaker else None
        found = bool(final_answer_word) and final_answer_word.strip().lower() == str(self.common_symbol).lower()
        rounds_used = answer_round if answer_round is not None else max(self.round_number - 1, 0)
        if stopped_by_user:
            efficiency_status = "stopped"
            efficiency_explanation = "Trial was stopped manually."
            efficiency_max_rounds = get_hard_stop_round(self.topology, self.num_agents)
        else:
            efficiency_status, efficiency_explanation, efficiency_max_rounds = evaluate_efficiency(
                found,
                bool(answers),
                rounds_used,
                self.num_agents,
                self.topology,
            )
        result = {
            "trial_id": trial_id,
            "topology": self.topology,
            "num_agents": self.num_agents,
            "result": efficiency_status,
            "success": found,
            "common_word": self.common_symbol,
            "final_answer_speaker": display_agent_name(final_answer_speaker) if final_answer_speaker else None,
            "final_answer_word": final_answer_word,
            "time_seconds": round(elapsed, 2),
            "total_messages": self.message_count,
            "total_turns": self.turn_count,
            "rounds": rounds_used,
            "answer_round": answer_round,
            "max_rounds_reached": max_rounds_reached,
            "efficiency_explanation": efficiency_explanation,
            "efficiency_max_rounds": efficiency_max_rounds,
            "discussion_rounds": self.discussion_rounds,
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
                    payload.get("topology", "broadcast"),
                    payload.get("num_agents", 5),
                    payload.get("discussion_rounds"),
                    payload.get("ollama_options"),
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
                    payload.get("topology", "broadcast"),
                    payload.get("num_agents", 5),
                    payload.get("discussion_rounds"),
                    payload.get("ollama_options"),
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
