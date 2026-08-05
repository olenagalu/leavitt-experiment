"""
LEAVITT SERVER - Multi-trial, selectable broadcast, circle, chain, Y, or wheel topology.

Runs the experiment server, coordinating Jetson agents by assigning private
figure sets, routing turn-based messages, and checking whether they correctly
find the shared figure.
"""

import socket
import threading
import json
import sys
import time
import random
import select
import subprocess
import re

DEBUG = False

FIGURES = [
    "square", "circle", "triangle", "diamond", "cross", "asterisk",
]

MIN_PARTICIPANTS = 2
MAX_PARTICIPANTS = 5
FIXED_FIVE_JETSON_TOPOLOGIES = {"circle", "chain", "y", "wheel"}
DEFAULT_FIGURES_PER_CARD = 3
MAX_ROUNDS_PER_TRIAL = 10
MAX_MESSAGES_PER_TRIAL = 50
CIRCLE_MAX_MESSAGES_PER_TRIAL = 40
EFFICIENCY_MAX_ROUNDS_BY_AGENTS = {
    2: 3,
    3: 3,
    4: 4,
    5: 4,
}
CIRCLE_EFFICIENCY_LIMIT_BY_AGENTS = {
    2: 4,
    3: 5,
    4: 6,
    5: 8,
}
CIRCLE_HARD_STOP_BY_AGENTS = {
    2: 6,
    3: 7,
    4: 8,
    5: 10,
}
DEFAULT_CIRCLE_DISCUSSION_ROUNDS = 5
DEFAULT_CHAIN_DISCUSSION_ROUNDS = 8
DEFAULT_Y_DISCUSSION_ROUNDS = 8
DEFAULT_WHEEL_DISCUSSION_ROUNDS = 2
DEFAULT_BROADCAST_DISCUSSION_ROUNDS = 3
RECENT_MESSAGE_LIMIT = 15
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
AGENT_TO_HOSTNAME = {agent: hostname for hostname, agent in HOSTNAME_TO_AGENT.items()}


def internal_to_display(name):
    return HOSTNAME_TO_AGENT.get(normalize_hostname(name), str(name))


def display_to_internal(name):
    text = str(name).strip()
    match = re.fullmatch(r"agent\s*(\d+)", text, flags=re.IGNORECASE)
    if match:
        return f"jetson{int(match.group(1))}"
    return normalize_hostname(text)


def display_agent_name(name):
    return internal_to_display(name)


def internal_agent_name(name):
    return display_to_internal(name)


def normalize_figure_answer(value):
    text = str(value or "").strip().lower()
    text = re.sub(r"^[^a-z]+|[^a-z]+$", "", text)
    return text if text in FIGURES else ""


def extract_figure_answer(value):
    text = str(value or "")
    exact = normalize_figure_answer(text)
    if exact:
        return exact

    patterns = [
        r"\b(?:final\s+answer|answer|common\s+figure|shared\s+figure|common\s+symbol)\s*(?:is|:|should\s+be|may\s+be|might\s+be)\s+([a-z]+)\b",
        r"\b(?:submit|choose)\s+(?:ANSWER\s*:?\s*)?([a-z]+)\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            figure = normalize_figure_answer(match.group(1))
            if figure:
                return figure

    mentioned = [
        figure
        for figure in FIGURES
        if re.search(rf"\b{re.escape(figure)}\b", text, flags=re.IGNORECASE)
    ]
    return mentioned[0] if len(mentioned) == 1 else ""


def normalize_hostname(hostname):
    return str(hostname).strip().lower().split(".", 1)[0]


def get_jetson_number(name):
    match = re.search(r"jetson\s*(\d+)", normalize_hostname(name))
    if not match:
        return None
    return int(match.group(1))


def jetson_number_from_hostname(hostname):
    return get_jetson_number(hostname)


def get_agent_id(name):
    match = re.search(r"(\d+)", str(name))
    if not match:
        return None
    return int(match.group(1))


def get_circle_neighbors(agent_id, num_agents):
    left = agent_id - 1
    right = agent_id + 1

    if left < 1:
        left = num_agents

    if right > num_agents:
        right = 1

    return [left, right]


def get_chain_contacts(agent_id, num_agents):
    contacts = []
    if agent_id > 1:
        contacts.append(agent_id - 1)
    if agent_id < num_agents:
        contacts.append(agent_id + 1)
    return contacts


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
    if topology == "y":
        return "Y-shape"
    if topology == "wheel":
        return "wheel"
    return str(topology)


def topology_requires_all_jetsons(topology):
    return topology in FIXED_FIVE_JETSON_TOPOLOGIES


def generate_jetson_sets(nicknames, seed=None):
    """
    Rules:
    - n in [2, 5]
    - n == 2: pool=5, each gets 3, exactly 1 common figure
    - n >= 3: pool=n+1, each gets n, exactly 1 figure common to all
      Construction for n>=3: each card omits one distinct non-common figure.
    """
    if not isinstance(nicknames, list):
        raise TypeError("nicknames must be a list of strings.")

    clean_nicknames = [n.strip() for n in nicknames]
    if any(not n for n in clean_nicknames):
        raise ValueError("All nicknames must be non-empty.")
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

        assignments = {}
        assignments[clean_nicknames[0]] = [common_figure, others[0], others[1]]
        assignments[clean_nicknames[1]] = [common_figure, others[2], others[3]]
        rng.shuffle(assignments[clean_nicknames[0]])
        rng.shuffle(assignments[clean_nicknames[1]])
        return common_figure, assignments, 5, 3

    pool_size = n + 1
    if pool_size > len(FIGURES):
        raise ValueError(f"Need {pool_size} figures, but FIGURES only has {len(FIGURES)}.")

    pool = rng.sample(FIGURES, pool_size)
    common_figure = rng.choice(pool)
    non_common = [f for f in pool if f != common_figure]
    rng.shuffle(non_common)

    assignments = {}
    for idx, nickname in enumerate(clean_nicknames):
        omitted = non_common[idx]
        card = [f for f in pool if f != omitted]
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
    if topology in ("chain", "y", "wheel"):
        return MAX_ROUNDS_PER_TRIAL
    return MAX_ROUNDS_PER_TRIAL


def get_answer_allowed_from_round(topology, num_agents):
    if topology == "circle":
        return DEFAULT_CIRCLE_DISCUSSION_ROUNDS + 1
    if topology == "chain":
        return DEFAULT_CHAIN_DISCUSSION_ROUNDS + 1
    if topology == "y":
        return DEFAULT_Y_DISCUSSION_ROUNDS + 1
    if topology == "wheel":
        return DEFAULT_WHEEL_DISCUSSION_ROUNDS + 1
    return 4


def get_default_discussion_rounds(topology):
    if topology == "circle":
        return DEFAULT_CIRCLE_DISCUSSION_ROUNDS
    if topology == "chain":
        return DEFAULT_CHAIN_DISCUSSION_ROUNDS
    if topology == "y":
        return DEFAULT_Y_DISCUSSION_ROUNDS
    if topology == "wheel":
        return DEFAULT_WHEEL_DISCUSSION_ROUNDS
    return DEFAULT_BROADCAST_DISCUSSION_ROUNDS


def normalize_discussion_rounds(value, default=DEFAULT_CIRCLE_DISCUSSION_ROUNDS):
    try:
        rounds = int(value)
    except (TypeError, ValueError):
        rounds = default
    return max(0, rounds)


def answer_gate_message_count(topology, server):
    if topology == "circle":
        return 0
    if topology == "chain":
        return server.chain_discussion_rounds
    if topology == "y":
        return server.y_discussion_rounds
    if topology == "wheel":
        return server.wheel_discussion_rounds
    return server.broadcast_discussion_rounds


def max_messages_for_topology(topology):
    return CIRCLE_MAX_MESSAGES_PER_TRIAL if topology == "circle" else MAX_MESSAGES_PER_TRIAL


def evaluate_efficiency(found, has_answer, messages_used, num_agents, topology, max_messages):
    max_efficient_messages = max_messages

    if not has_answer:
        return (
            "failed_no_answer",
            "No answer was submitted before the hard stop.",
            max_efficient_messages,
        )

    if not found:
        return (
            "failed_wrong_answer",
            "Agents submitted a wrong answer.",
            max_efficient_messages,
        )

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


def restart_jetson_clients():
    for host in JETSON_HOSTNAMES:
        cmd = [
            "ssh",
            f"{JETSON_SSH_USER}@{host}",
            f"sudo /usr/bin/systemctl restart {JETSON_CLIENT_SERVICE}",
        ]

        print(f"[RESTART] Restarting client on {host}...")
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=20,
            )

            if result.returncode == 0:
                print(f"[RESTART] {host}: OK")
            else:
                print(f"[RESTART] {host}: FAILED")
                if result.stderr:
                    print(result.stderr.strip())

        except subprocess.TimeoutExpired:
            print(f"[RESTART] {host}: TIMEOUT")
        except Exception as e:
            print(f"[RESTART] {host}: ERROR: {e}")


class LeavittServer:
    def __init__(self, host, port, topology):
        self.host = host
        self.port = port
        self.topology = topology

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.clients = {}
        self.turn_order = []
        self.turn_index = 0
        self.lock = threading.Lock()
        self.running = True
        self.accepting_connections = False
        self.required_for_trial = 0
        self.stop_current_trial = False
        self.trial_id = 0

        self.num_agents = 2
        self.cards = {}
        self.common_symbol = None
        self.answers = {}
        self.circle_neighbors_by_name = {}
        self.circle_last_target_by_speaker = {}
        self.broadcast_discussion_rounds = normalize_discussion_rounds(
            None,
            DEFAULT_BROADCAST_DISCUSSION_ROUNDS,
        )
        self.circle_discussion_rounds = normalize_discussion_rounds(None)
        self.chain_contacts_by_name = {}
        self.chain_last_target_by_speaker = {}
        self.chain_discussion_rounds = normalize_discussion_rounds(None, DEFAULT_CHAIN_DISCUSSION_ROUNDS)
        self.y_contacts_by_name = {}
        self.y_last_target_by_speaker = {}
        self.y_discussion_rounds = normalize_discussion_rounds(None, DEFAULT_Y_DISCUSSION_ROUNDS)
        self.wheel_contacts_by_name = {}
        self.wheel_last_target_by_speaker = {}
        self.wheel_discussion_rounds = normalize_discussion_rounds(None, DEFAULT_WHEEL_DISCUSSION_ROUNDS)

        self.start_time = None
        self.end_time = None
        self.message_count = 0
        self.delivery_count = 0
        self.conversation_log = []
        self.agent_histories = {}
        self.unread_agents = set()
        self.scheduler_queue = []
        self.messages_per_agent = {}
        self.recv_buffers = {}

        self.figures_per_card = DEFAULT_FIGURES_PER_CARD
        self.pool_size = 5

    def _send(self, sock, msg_dict):
        try:
            raw = json.dumps(msg_dict) + "\n"
            sock.sendall(raw.encode("utf-8"))
            return True
        except Exception as e:
            print(f"[SEND ERROR] {e}")
            self._drop_client(sock, reason=f"send failed: {e}")
            return False

    def _drop_client(self, sock, reason="disconnected"):
        removed = False
        with self.lock:
            info = self.clients.pop(sock, None)
            self.recv_buffers.pop(sock, None)
            removed = info is not None
            if sock in self.turn_order:
                self.turn_order.remove(sock)
        if removed:
            try:
                sock.close()
            except OSError:
                pass
        if info:
            print(f"[-] {display_agent_name(info.get('name', 'Unknown'))} removed ({reason})")

    def _recv(self, sock, timeout=None):
        if timeout:
            sock.settimeout(timeout)
        try:
            buffer = self.recv_buffers.get(sock, b"")

            while b"\n" not in buffer:
                chunk = sock.recv(4096)
                if not chunk:
                    self._drop_client(sock, reason="recv failed/disconnected")
                    return None
                buffer += chunk

            line, buffer = buffer.split(b"\n", 1)
            self.recv_buffers[sock] = buffer

            return json.loads(line.decode("utf-8"))
        except socket.timeout:
            return {"type": "timeout"}
        except (json.JSONDecodeError, ConnectionResetError, OSError) as e:
            print(f"[RECV ERROR] {e}")
            self._drop_client(sock, reason=f"recv failed: {e}")
            return None
        finally:
            try:
                sock.settimeout(None)
            except OSError:
                pass

    def _poll_stop_command(self):
        """
        Non-blocking terminal poll for manual stop command during a running trial.
        Returns True if user typed 's'.
        """
        try:
            ready, _, _ = select.select([sys.stdin], [], [], 0)
        except (ValueError, OSError):
            return False

        if not ready:
            return False

        cmd = sys.stdin.readline().strip().lower()
        if cmd == "s":
            self.stop_current_trial = True
            return True
        return False

    def _recv_with_manual_stop(self, sock, total_timeout=300, poll_interval=1):
        """
        Receive JSON with periodic checks for manual stop command.
        Returns dict/None compatible with _recv().
        """
        deadline = time.time() + total_timeout
        while self.running:
            if self._poll_stop_command():
                return {"type": "manual_stop"}

            remaining = deadline - time.time()
            if remaining <= 0:
                return {"type": "timeout"}

            step = min(poll_interval, max(0.1, remaining))
            resp = self._recv(sock, timeout=step)
            if resp is None:
                return None
            if resp.get("type") == "timeout":
                continue
            return resp

        return None

    def broadcast(self, msg_dict, exclude=None, recipients=None):
        with self.lock:
            target_socks = recipients if recipients is not None else list(self.clients.keys())
        for sock in list(target_socks):
            if sock != exclude:
                self._send(sock, msg_dict)

    def _send_to_agent_ids(self, msg_dict, agent_ids, agent_socks):
        for agent_id in agent_ids:
            sock = agent_socks.get(agent_id)
            if sock:
                self._send(sock, msg_dict)

    def _recent_circle_messages(self, agent_id):
        return list(self.agent_histories.get(agent_id, [])[-RECENT_MESSAGE_LIMIT:])

    def _recent_chain_messages(self, agent_id):
        return list(self.agent_histories.get(agent_id, [])[-RECENT_MESSAGE_LIMIT:])

    def _recent_y_messages(self, agent_id):
        return list(self.agent_histories.get(agent_id, [])[-RECENT_MESSAGE_LIMIT:])

    def _recent_wheel_messages(self, agent_id):
        return list(self.agent_histories.get(agent_id, [])[-RECENT_MESSAGE_LIMIT:])

    def _reset_agent_histories(self):
        for agent_id in list(self.agent_histories):
            self.agent_histories[agent_id] = []

    def _random_contact(self, speaker, contacts, last_target_by_speaker):
        if not contacts:
            return ""
        last_target = last_target_by_speaker.get(speaker)
        choices = [contact for contact in contacts if contact != last_target] or list(contacts)
        return display_agent_name(random.choice(choices))

    def _preferred_circle_neighbor(self, speaker):
        neighbors = self.circle_neighbors_by_name.get(speaker, [])
        if not neighbors:
            return ""
        last_target = self.circle_last_target_by_speaker.get(speaker)
        if last_target in neighbors and len(neighbors) > 1:
            next_index = (neighbors.index(last_target) + 1) % len(neighbors)
            return display_agent_name(neighbors[next_index])
        return display_agent_name(neighbors[0])

    def _preferred_chain_contact(self, speaker):
        return self._random_contact(
            speaker,
            self.chain_contacts_by_name.get(speaker, []),
            self.chain_last_target_by_speaker,
        )

    def _preferred_y_contact(self, speaker):
        return self._random_contact(
            speaker,
            self.y_contacts_by_name.get(speaker, []),
            self.y_last_target_by_speaker,
        )

    def _preferred_wheel_contact(self, speaker):
        return self._random_contact(
            speaker,
            self.wheel_contacts_by_name.get(speaker, []),
            self.wheel_last_target_by_speaker,
        )

    def handle_new_client(self, client_socket, client_address):
        try:
            self._send(client_socket, {"type": "nickname_request"})
            resp = self._recv(client_socket, timeout=30)
            if not resp or resp.get("type") != "nickname":
                self._drop_client(client_socket, reason="invalid handshake")
                return

            old_sock = None
            with self.lock:
                hostname = normalize_hostname(resp.get("hostname", ""))
                if not hostname:
                    self._send(client_socket, {"type": "system", "text": "Missing hostname in handshake."})
                    self._drop_client(client_socket, reason="missing hostname")
                    return

                if hostname not in HOSTNAME_TO_AGENT:
                    self._send(client_socket, {"type": "system", "text": f"Unknown hostname '{hostname}'."})
                    self._drop_client(client_socket, reason=f"unknown hostname {hostname}")
                    return
                name = hostname

                for sock, info in list(self.clients.items()):
                    if info.get("name") == name:
                        old_sock = sock
                        break

                if old_sock is not None:
                    self.clients.pop(old_sock, None)
                    self.recv_buffers.pop(old_sock, None)
                    if old_sock in self.turn_order:
                        self.turn_order.remove(old_sock)
                    try:
                        old_sock.close()
                    except OSError:
                        pass

                self.clients[client_socket] = {
                    "name": name,
                    "hostname": hostname,
                    "address": client_address,
                }
                self.turn_order.append(client_socket)

            self._send(client_socket, {
                "type": "welcome",
                "agent_name": display_agent_name(name),
                "hostname": hostname,
                "text": f"Welcome {display_agent_name(name)} ({hostname}). Waiting for next trial start...",
            })
        except Exception as e:
            print(f"[ERROR] Onboarding: {e}")
            self._drop_client(client_socket, reason=f"onboarding exception: {e}")

    def _prompt_num_agents(self):
        while True:
            raw = input(f"Enter number of Jetsons for next trial ({MIN_PARTICIPANTS}-{MAX_PARTICIPANTS}): ").strip()
            try:
                n = int(raw)
            except ValueError:
                print("[INPUT] Please enter a number.")
                continue
            if MIN_PARTICIPANTS <= n <= MAX_PARTICIPANTS:
                return n
            print(f"[INPUT] Please enter a value between {MIN_PARTICIPANTS} and {MAX_PARTICIPANTS}.")

    def _prompt_discussion_rounds(self):
        default = get_default_discussion_rounds(self.topology)
        while True:
            raw = input(f"Set number of discussion rounds (default {default}): ").strip()
            if raw == "":
                return default
            try:
                rounds = int(raw)
            except ValueError:
                print("[INPUT] Please enter a non-negative integer, or press Enter for the default.")
                continue
            if rounds >= 0:
                return normalize_discussion_rounds(rounds, default)
            print("[INPUT] Please enter a non-negative integer, or press Enter for the default.")

    def _print_connection_summary(self, selected_socks=None, needed=None, missing_names=None):
        with self.lock:
            selected_socks = selected_socks or []
            missing_names = missing_names or []

            if needed is None:
                alive = [sock for sock in self.turn_order if sock in self.clients]
                print(f"[CONNECTED] {len(alive)} Jetson(s) currently connected:")
                display_socks = alive
            else:
                print(f"[CONNECTED] {len(selected_socks)}/{needed} selected:")
                display_socks = selected_socks

            for index, sock in enumerate(display_socks, start=1):
                info = self.clients.get(sock)
                if not info:
                    continue
                name = info.get("name", "Unknown")
                hostname = normalize_hostname(info.get("hostname", "unknown"))
                marker = ""
                if selected_socks is not None and sock in selected_socks:
                    marker = "  SELECTED"
                print(f"  {index}. {display_agent_name(name)} ({hostname}){marker}")
            if missing_names:
                missing_display = ", ".join(display_agent_name(name) for name in missing_names)
                print(f"[WAITING FOR] {missing_display}")

    def _wait_for_clients(self, needed):
        print(f"\n[EXP] Waiting for {needed} connected Jetsons...")
        last_display_state = None
        while self.running:
            should_print = False
            done = False
            with self.lock:
                if topology_requires_all_jetsons(self.topology):
                    required = {}
                    for sock in list(self.turn_order):
                        info = self.clients.get(sock)
                        if not info:
                            continue
                        jetson_number = jetson_number_from_hostname(info.get("name", ""))
                        if jetson_number is None or not (1 <= jetson_number <= needed):
                            continue
                        required.setdefault(jetson_number, sock)

                    selected = [
                        required[number]
                        for number in range(1, needed + 1)
                        if number in required
                    ]
                    missing_names = [
                        f"jetson{number}"
                        for number in range(1, needed + 1)
                        if number not in required
                    ]
                else:
                    alive = [
                        sock for sock in list(self.turn_order)
                        if sock in self.clients
                    ]
                    selected = alive[:needed]
                    missing_names = []

                selected_names = tuple(
                    self.clients[sock]["name"]
                    for sock in selected
                    if sock in self.clients
                )
                display_state = (selected_names, tuple(missing_names))

                if display_state != last_display_state:
                    should_print = True
                    last_display_state = display_state

                if len(selected) >= needed and not missing_names:
                    done = True
            if should_print:
                self._print_connection_summary(
                    selected_socks=selected,
                    needed=needed,
                    missing_names=missing_names,
                )
            if done:
                return selected
            time.sleep(1)
        return []

    def _normalize_word(self, text):
        return str(text).strip().lower()

    def _agent_maps(self, active_socks):
        agent_socks = {}
        sock_agent_ids = {}
        with self.lock:
            for sock in active_socks:
                agent_id = get_agent_id(self.clients[sock]["name"])
                if agent_id is not None:
                    agent_socks[agent_id] = sock
                    sock_agent_ids[sock] = agent_id
        return agent_socks, sock_agent_ids

    def _active_agent_names(self, active_socks):
        with self.lock:
            return [
                self.clients[sock]["name"]
                for sock in active_socks
                if sock in self.clients
            ]

    def _missing_required_jetsons(self, active_socks):
        if not topology_requires_all_jetsons(self.topology):
            return []

        with self.lock:
            connected_numbers = {
                jetson_number_from_hostname(self.clients[sock]["name"])
                for sock in active_socks
                if sock in self.clients
            }

        return [
            f"jetson{number}"
            for number in range(1, MAX_PARTICIPANTS + 1)
            if number not in connected_numbers
        ]

    def _circle_agent_order(self, active_socks):
        names = self._active_agent_names(active_socks)
        return sorted(names, key=lambda name: (get_jetson_number(name) or 999, name))

    def _build_circle_neighbors(self, active_socks):
        ordered_names = self._circle_agent_order(active_socks)
        neighbors_by_name = {}
        total = len(ordered_names)
        for index, name in enumerate(ordered_names):
            if total <= 1:
                neighbors = []
            else:
                previous_name = ordered_names[(index - 1) % total]
                next_name = ordered_names[(index + 1) % total]
                neighbors = list(dict.fromkeys([previous_name, next_name]))
            neighbors_by_name[name] = neighbors
        return neighbors_by_name

    def _build_chain_contacts(self, active_socks):
        ordered_names = self._circle_agent_order(active_socks)
        contacts_by_name = {}
        total = len(ordered_names)
        for index, name in enumerate(ordered_names):
            contacts = []
            if index > 0:
                contacts.append(ordered_names[index - 1])
            if index < total - 1:
                contacts.append(ordered_names[index + 1])
            contacts_by_name[name] = contacts
        return contacts_by_name

    def _build_y_contacts(self, active_socks):
        active_names = set(self._active_agent_names(active_socks))
        contacts_by_name = {}
        for name in active_names:
            agent_id = get_agent_id(name)
            contacts_by_name[name] = [
                f"jetson{contact_id}"
                for contact_id in get_y_contacts(agent_id)
                if f"jetson{contact_id}" in active_names
            ]
        return contacts_by_name

    def _build_wheel_contacts(self, active_socks):
        active_names = set(self._active_agent_names(active_socks))
        contacts_by_name = {}
        for name in active_names:
            agent_id = get_agent_id(name)
            contacts_by_name[name] = [
                f"jetson{contact_id}"
                for contact_id in get_wheel_contacts(agent_id)
                if f"jetson{contact_id}" in active_names
            ]
        return contacts_by_name

    def _sock_by_name(self, active_socks, name):
        with self.lock:
            for sock in active_socks:
                info = self.clients.get(sock)
                if info and info.get("name") == name:
                    return sock
        return None

    def _choose_next_sock(self, active_socks):
        candidates = [sock for sock in active_socks if sock in self.clients]
        return random.choice(candidates) if candidates else None

    def _record_valid_message(self, speaker, receivers):
        if self.start_time is None:
            self.start_time = time.time()
        self.message_count += 1
        self.delivery_count += len(receivers)
        self.messages_per_agent[speaker] = self.messages_per_agent.get(speaker, 0) + 1
        for receiver in receivers:
            if receiver and receiver != speaker:
                self.unread_agents.add(receiver)
        return self.message_count

    def _elapsed_since_first_message(self):
        if self.start_time is None:
            return 0
        end_time = self.end_time if self.end_time is not None else time.time()
        return end_time - self.start_time

    def _send_turn_request(self, sock, speaker_id, speaker, round_number, can_answer, reset_chat_history=False):
        message_count = self.message_count
        answer_allowed_after = answer_gate_message_count(self.topology, self)
        if self.topology == "circle":
            self._send(sock, {
                "type": "your_turn",
                "trial_id": self.trial_id,
                "topology": "circle",
                "round": message_count,
                "message_count": message_count,
                "can_answer": can_answer,
                "reset_chat_history": reset_chat_history,
                "discussion_rounds": answer_allowed_after,
                "agent_name": display_agent_name(speaker),
                "your_symbols": self.cards[speaker],
                "circle_neighbors": [
                    display_agent_name(neighbor)
                    for neighbor in self.circle_neighbors_by_name.get(speaker, [])
                ],
                "recent_messages": self._recent_circle_messages(speaker_id),
                "preferred_neighbor": self._preferred_circle_neighbor(speaker),
            })
        elif self.topology == "chain":
            self._send(sock, {
                "type": "your_turn",
                "trial_id": self.trial_id,
                "topology": "chain",
                "round": message_count,
                "message_count": message_count,
                "can_answer": can_answer,
                "reset_chat_history": reset_chat_history,
                "discussion_rounds": answer_allowed_after,
                "agent_name": display_agent_name(speaker),
                "your_symbols": self.cards[speaker],
                "chain_contacts": [
                    display_agent_name(contact)
                    for contact in self.chain_contacts_by_name.get(speaker, [])
                ],
                "recent_messages": self._recent_chain_messages(speaker_id),
                "preferred_contact": self._preferred_chain_contact(speaker),
            })
        elif self.topology == "y":
            self._send(sock, {
                "type": "your_turn",
                "trial_id": self.trial_id,
                "topology": "y",
                "round": message_count,
                "message_count": message_count,
                "can_answer": can_answer,
                "reset_chat_history": reset_chat_history,
                "discussion_rounds": answer_allowed_after,
                "agent_name": display_agent_name(speaker),
                "your_symbols": self.cards[speaker],
                "y_contacts": [
                    display_agent_name(contact)
                    for contact in self.y_contacts_by_name.get(speaker, [])
                ],
                "recent_messages": self._recent_y_messages(speaker_id),
                "preferred_contact": self._preferred_y_contact(speaker),
            })
        elif self.topology == "wheel":
            self._send(sock, {
                "type": "your_turn",
                "trial_id": self.trial_id,
                "topology": "wheel",
                "round": message_count,
                "message_count": message_count,
                "can_answer": can_answer,
                "reset_chat_history": reset_chat_history,
                "discussion_rounds": answer_allowed_after,
                "agent_name": display_agent_name(speaker),
                "your_symbols": self.cards[speaker],
                "wheel_recipients": [
                    display_agent_name(contact)
                    for contact in self.wheel_contacts_by_name.get(speaker, [])
                ],
                "recent_messages": self._recent_wheel_messages(speaker_id),
                "preferred_recipient": self._preferred_wheel_contact(speaker),
            })
        else:
            self._send(sock, {
                "type": "your_turn",
                "trial_id": self.trial_id,
                "round": message_count,
                "message_count": message_count,
                "can_answer": can_answer,
                "reset_chat_history": reset_chat_history,
                "discussion_rounds": answer_allowed_after,
            })

    def route_chat_message(
        self,
        text,
        speaker,
        speaker_id,
        current_sock,
        active_socks,
        agent_socks,
        round_number,
        turn_number,
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
                if not valid_neighbors:
                    print(f"{display_agent_name(speaker)}: no valid target, skipped.")
                    self.conversation_log.append({
                        "round": round_number,
                        "topology": "circle",
                        "sender": display_agent_name(speaker),
                        "receiver": None,
                        "valid_neighbors": [display_agent_name(name) for name in valid_neighbors],
                        "raw": raw,
                        "message": text,
                        "target_source": target_source,
                        "original_target": original_target,
                    })
                    return False
                receiver = internal_agent_name(self._preferred_circle_neighbor(speaker))
                target_source = "server_assigned"
                print(
                    f"{display_agent_name(speaker)}: invalid target {target!r}; "
                    f"defaulted to {display_agent_name(receiver)}."
                )
            elif not target_source:
                target_source = "agent"

            receiver_sock = self._sock_by_name(active_socks, receiver)
            if receiver_sock and self._send(receiver_sock, {
                "type": "chat",
                "trial_id": self.trial_id,
                "sender": display_agent_name(speaker),
                "text": text,
            }):
                self.circle_last_target_by_speaker[speaker] = receiver
            else:
                print(f"{display_agent_name(speaker)}: invalid target, skipped.")
                self.conversation_log.append({
                    "round": round_number,
                    "topology": "circle",
                    "sender": display_agent_name(speaker),
                    "receiver": display_agent_name(receiver),
                    "valid_neighbors": [display_agent_name(name) for name in valid_neighbors],
                    "raw": raw,
                    "message": text,
                    "target_source": target_source,
                    "original_target": original_target,
                })
                return False

            receiver_id = get_agent_id(receiver)
            if receiver_id is not None:
                self.agent_histories.setdefault(receiver_id, []).append({
                    "sender": display_agent_name(speaker),
                    "text": text,
                })
            if speaker_id is not None:
                self.agent_histories.setdefault(speaker_id, []).append({
                    "sender": display_agent_name(speaker),
                    "text": f"To {display_agent_name(receiver)}: {text}",
                })
            message_number = self._record_valid_message(speaker, [receiver])

            self.conversation_log.append({
                "round": message_number,
                "topology": "circle",
                "sender": display_agent_name(speaker),
                "receiver": display_agent_name(receiver),
                "valid_neighbors": [display_agent_name(name) for name in valid_neighbors],
                "raw": raw,
                "message": text,
                "target_source": target_source,
                "original_target": original_target,
                "elapsed": round(self._elapsed_since_first_message(), 2),
            })

            if receiver_sock:
                print(f"{display_agent_name(speaker)} -> {display_agent_name(receiver)}: {text}")
        elif self.topology == "chain":
            valid_contacts = self.chain_contacts_by_name.get(speaker, [])
            original_target = original_target or target or ""
            receiver = internal_agent_name(target) if target else ""
            routing_note = ""

            if not valid_contacts:
                self.conversation_log.append({
                    "round": round_number,
                    "topology": "chain",
                    "sender": display_agent_name(speaker),
                    "receiver": None,
                    "valid_contacts": [display_agent_name(name) for name in valid_contacts],
                    "raw": raw,
                    "message": text,
                    "target_source": target_source,
                    "routing_note": "No valid chain contacts available. Message skipped.",
                    "original_target": original_target,
                })
                print(f"[CHAIN ROUTE] {display_agent_name(speaker)} has no valid contacts. Message skipped.")
                return False

            if target_source == "client_default" and receiver in valid_contacts:
                routing_note = (
                    f"{display_agent_name(speaker)} did not provide a valid target. "
                    f"Client defaulted to {display_agent_name(receiver)}."
                )
            elif receiver in valid_contacts:
                routing_note = f"{display_agent_name(speaker)} chose {display_agent_name(receiver)}."
            else:
                receiver = internal_agent_name(self._preferred_chain_contact(speaker))
                routing_note = (
                    f"{display_agent_name(speaker)} did not provide a valid target. "
                    f"Server defaulted to {display_agent_name(receiver)}."
                )

            receiver_sock = self._sock_by_name(active_socks, receiver)
            if receiver_sock and self._send(receiver_sock, {
                "type": "chat",
                "trial_id": self.trial_id,
                "sender": display_agent_name(speaker),
                "text": text,
            }):
                self.chain_last_target_by_speaker[speaker] = receiver
            else:
                print(f"{display_agent_name(speaker)}: invalid target, skipped.")
                self.conversation_log.append({
                    "round": round_number,
                    "topology": "chain",
                    "sender": display_agent_name(speaker),
                    "receiver": display_agent_name(receiver),
                    "valid_contacts": [display_agent_name(name) for name in valid_contacts],
                    "raw": raw,
                    "message": text,
                    "target_source": target_source,
                    "routing_note": routing_note,
                    "original_target": original_target,
                })
                return False

            receiver_id = get_agent_id(receiver)
            if receiver_id is not None:
                self.agent_histories.setdefault(receiver_id, []).append({
                    "sender": display_agent_name(speaker),
                    "text": text,
                })
            message_number = self._record_valid_message(speaker, [receiver])

            display_message = f"{display_agent_name(speaker)} -> {display_agent_name(receiver)}: {text}"
            self.conversation_log.append({
                "round": message_number,
                "topology": "chain",
                "sender": display_agent_name(speaker),
                "receiver": display_agent_name(receiver),
                "valid_contacts": [display_agent_name(name) for name in valid_contacts],
                "raw": raw,
                "message": text,
                "target_source": target_source,
                "routing_note": routing_note,
                "original_target": original_target,
                "display": display_message,
                "elapsed": round(self._elapsed_since_first_message(), 2),
            })

            if receiver_sock:
                print(f"[CHAIN ROUTE] {routing_note}")
                print(display_message)
        elif self.topology == "y":
            valid_contacts = self.y_contacts_by_name.get(speaker, [])
            original_target = original_target or target or ""
            receiver = internal_agent_name(target) if target else ""
            routing_note = ""

            if not valid_contacts:
                self.conversation_log.append({
                    "round": round_number,
                    "topology": "y",
                    "sender": display_agent_name(speaker),
                    "receiver": None,
                    "valid_contacts": [display_agent_name(name) for name in valid_contacts],
                    "raw": raw,
                    "message": text,
                    "target_source": target_source,
                    "routing_note": "No valid Y contacts available. Message skipped.",
                    "original_target": original_target,
                })
                print(f"[Y ROUTE] {display_agent_name(speaker)} has no valid contacts. Message skipped.")
                return False

            if target_source == "client_default" and receiver in valid_contacts:
                routing_note = (
                    f"{display_agent_name(speaker)} did not provide a valid target. "
                    f"Client defaulted to {display_agent_name(receiver)}."
                )
            elif receiver in valid_contacts:
                routing_note = f"{display_agent_name(speaker)} chose {display_agent_name(receiver)}."
            else:
                receiver = internal_agent_name(self._preferred_y_contact(speaker))
                routing_note = (
                    f"{display_agent_name(speaker)} did not provide a valid target. "
                    f"Server defaulted to {display_agent_name(receiver)}."
                )

            receiver_sock = self._sock_by_name(active_socks, receiver)
            if receiver_sock and self._send(receiver_sock, {
                "type": "chat",
                "trial_id": self.trial_id,
                "sender": display_agent_name(speaker),
                "text": text,
            }):
                self.y_last_target_by_speaker[speaker] = receiver
            else:
                print(f"{display_agent_name(speaker)}: invalid target, skipped.")
                self.conversation_log.append({
                    "round": round_number,
                    "topology": "y",
                    "sender": display_agent_name(speaker),
                    "receiver": display_agent_name(receiver),
                    "valid_contacts": [display_agent_name(name) for name in valid_contacts],
                    "raw": raw,
                    "message": text,
                    "target_source": target_source,
                    "routing_note": routing_note,
                    "original_target": original_target,
                })
                return False

            receiver_id = get_agent_id(receiver)
            if receiver_id is not None:
                self.agent_histories.setdefault(receiver_id, []).append({
                    "sender": display_agent_name(speaker),
                    "text": text,
                })
            message_number = self._record_valid_message(speaker, [receiver])

            display_message = f"{display_agent_name(speaker)} -> {display_agent_name(receiver)}: {text}"
            self.conversation_log.append({
                "round": message_number,
                "topology": "y",
                "sender": display_agent_name(speaker),
                "receiver": display_agent_name(receiver),
                "valid_contacts": [display_agent_name(name) for name in valid_contacts],
                "raw": raw,
                "message": text,
                "target_source": target_source,
                "routing_note": routing_note,
                "original_target": original_target,
                "display": display_message,
                "elapsed": round(self._elapsed_since_first_message(), 2),
            })

            if receiver_sock:
                print(f"[Y ROUTE] {routing_note}")
                print(display_message)
        elif self.topology == "wheel":
            valid_contacts = self.wheel_contacts_by_name.get(speaker, [])
            original_target = original_target or target or ""
            receiver = internal_agent_name(target) if target else ""
            routing_note = ""

            if not valid_contacts:
                self.conversation_log.append({
                    "round": round_number,
                    "topology": "wheel",
                    "sender": display_agent_name(speaker),
                    "receiver": None,
                    "valid_recipients": [display_agent_name(name) for name in valid_contacts],
                    "raw": raw,
                    "message": text,
                    "target_source": target_source,
                    "routing_note": "No valid wheel recipients available. Message skipped.",
                    "original_target": original_target,
                })
                print(f"[WHEEL ROUTE] {display_agent_name(speaker)} has no valid recipients. Message skipped.")
                return False

            if target_source == "client_default" and receiver in valid_contacts:
                routing_note = (
                    f"{display_agent_name(speaker)} did not provide a valid target. "
                    f"Client defaulted to {display_agent_name(receiver)}."
                )
            elif receiver in valid_contacts:
                routing_note = f"{display_agent_name(speaker)} chose {display_agent_name(receiver)}."
            else:
                receiver = internal_agent_name(self._preferred_wheel_contact(speaker))
                routing_note = (
                    f"{display_agent_name(speaker)} did not provide a valid target. "
                    f"Server defaulted to {display_agent_name(receiver)}."
                )

            receiver_sock = self._sock_by_name(active_socks, receiver)
            if receiver_sock and self._send(receiver_sock, {
                "type": "chat",
                "trial_id": self.trial_id,
                "sender": display_agent_name(speaker),
                "text": text,
            }):
                self.wheel_last_target_by_speaker[speaker] = receiver
            else:
                print(f"{display_agent_name(speaker)}: invalid target, skipped.")
                self.conversation_log.append({
                    "round": round_number,
                    "topology": "wheel",
                    "sender": display_agent_name(speaker),
                    "receiver": display_agent_name(receiver),
                    "valid_recipients": [display_agent_name(name) for name in valid_contacts],
                    "raw": raw,
                    "message": text,
                    "target_source": target_source,
                    "routing_note": routing_note,
                    "original_target": original_target,
                })
                return False

            receiver_id = get_agent_id(receiver)
            if receiver_id is not None:
                self.agent_histories.setdefault(receiver_id, []).append({
                    "sender": display_agent_name(speaker),
                    "text": text,
                })
            message_number = self._record_valid_message(speaker, [receiver])

            display_message = f"{display_agent_name(speaker)} -> {display_agent_name(receiver)}: {text}"
            self.conversation_log.append({
                "round": message_number,
                "topology": "wheel",
                "sender": display_agent_name(speaker),
                "receiver": display_agent_name(receiver),
                "valid_recipients": [display_agent_name(name) for name in valid_contacts],
                "raw": raw,
                "message": text,
                "target_source": target_source,
                "routing_note": routing_note,
                "original_target": original_target,
                "display": display_message,
                "elapsed": round(self._elapsed_since_first_message(), 2),
            })

            if receiver_sock:
                print(f"[WHEEL ROUTE] {routing_note}")
                print(display_message)
        else:
            receivers = [
                self.clients[sock]["name"]
                for sock in active_socks
                if sock != current_sock and sock in self.clients
            ]
            message_number = self._record_valid_message(speaker, receivers)
            self.conversation_log.append({
                "round": message_number,
                "topology": "broadcast",
                "sender": display_agent_name(speaker),
                "receiver": "ALL",
                "raw": raw,
                "message": text,
                "elapsed": round(self._elapsed_since_first_message(), 2),
            })
            self.broadcast(
                {
                    "type": "chat",
                    "trial_id": self.trial_id,
                    "sender": display_agent_name(speaker),
                    "text": text,
                },
                exclude=current_sock,
                recipients=active_socks,
            )
            print(f"{display_agent_name(speaker)} -> ALL: {text}")
        return True

    def run_experiment(self):
        self.stop_current_trial = False
        self.accepting_connections = False
        self.trial_id += 1
        current_trial_id = self.trial_id
        if topology_requires_all_jetsons(self.topology):
            self.num_agents = MAX_PARTICIPANTS
            print(f"[START] {display_topology_name(self.topology)} mode requires all {MAX_PARTICIPANTS} Jetsons.")
        else:
            self.num_agents = self._prompt_num_agents()
        max_messages_per_trial = max_messages_for_topology(self.topology)
        print(f"[START] Trial limit: {max_messages_per_trial} total messages.")
        self.required_for_trial = self.num_agents
        self.accepting_connections = True

        active_socks = self._wait_for_clients(self.num_agents)
        self.accepting_connections = False
        time.sleep(1)
        missing_required = self._missing_required_jetsons(active_socks)
        if missing_required:
            missing_display = ", ".join(display_agent_name(name) for name in missing_required)
            print(f"[START BLOCKED] Cannot start {display_topology_name(self.topology)} round. Missing: {missing_display}.")
            return

        nicknames = []
        with self.lock:
            for sock in active_socks:
                nicknames.append(self.clients[sock]["name"])

        self.common_symbol, self.cards, self.pool_size, self.figures_per_card = generate_jetson_sets(nicknames)
        self.answers = {}
        self.message_count = 0
        self.delivery_count = 0
        self.conversation_log = []
        self.agent_histories = {agent_id: [] for agent_id in range(1, self.num_agents + 1)}
        self.unread_agents = set()
        self.scheduler_queue = []
        self.messages_per_agent = {
            name: 0
            for name in nicknames
        }
        self.circle_last_target_by_speaker = {}
        self.chain_last_target_by_speaker = {}
        self.y_last_target_by_speaker = {}
        self.wheel_last_target_by_speaker = {}
        self.circle_neighbors_by_name = (
            self._build_circle_neighbors(active_socks)
            if self.topology == "circle"
            else {}
        )
        self.chain_contacts_by_name = (
            self._build_chain_contacts(active_socks)
            if self.topology == "chain"
            else {}
        )
        self.y_contacts_by_name = (
            self._build_y_contacts(active_socks)
            if self.topology == "y"
            else {}
        )
        self.wheel_contacts_by_name = (
            self._build_wheel_contacts(active_socks)
            if self.topology == "wheel"
            else {}
        )
        self.turn_index = 0
        agent_socks, sock_agent_ids = self._agent_maps(active_socks)
        selected_internal_order = [
            self.clients[sock]["name"]
            for sock in active_socks
            if sock in self.clients
        ]

        print(f"\n{'=' * 55}")
        print("  EXPERIMENT STARTING")
        print(f"  Communication topology: {display_topology_name(self.topology)}")
        print(f"  Jetsons: {self.num_agents}")
        print(f"  Figure pool size: {self.pool_size}")
        print(f"  Figures per card: {self.figures_per_card}")
        print(f"  Common figure: {self.common_symbol}")
        for sock in active_socks:
            name = self.clients[sock]["name"]
            print(f"  {display_agent_name(name)}'s card: {self.cards[name]}")
        if self.topology == "circle":
            print("  Circle neighbors:")
            for name in selected_internal_order:
                neighbors = self.circle_neighbors_by_name.get(name, [])
                display_neighbors = ", ".join(display_agent_name(neighbor) for neighbor in neighbors)
                print(f"  {display_agent_name(name)}: {display_neighbors}")
        if self.topology == "chain":
            print("  Chain contacts:")
            for name in selected_internal_order:
                contacts = self.chain_contacts_by_name.get(name, [])
                display_contacts = ", ".join(display_agent_name(contact) for contact in contacts)
                print(f"  {display_agent_name(name)}: {display_contacts}")
        if self.topology == "y":
            print("  Y-shape contacts:")
            for name in selected_internal_order:
                contacts = self.y_contacts_by_name.get(name, [])
                display_contacts = ", ".join(display_agent_name(contact) for contact in contacts)
                print(f"  {display_agent_name(name)}: {display_contacts}")
        if self.topology == "wheel":
            print("  Wheel recipients:")
            for name in selected_internal_order:
                contacts = self.wheel_contacts_by_name.get(name, [])
                display_contacts = ", ".join(display_agent_name(contact) for contact in contacts)
                print(f"  {display_agent_name(name)}: {display_contacts}")
        if DEBUG:
            print(f"  Selected internal order: {', '.join(selected_internal_order)}")
        print(f"{'=' * 55}\n")

        self.broadcast({
            "type": "reset_chat_history",
            "trial_id": current_trial_id,
        }, recipients=active_socks)

        for sock in active_socks:
            name = self.clients[sock]["name"]
            self._send(sock, {
                "type": "experiment_start",
                "trial_id": current_trial_id,
                "agent_name": display_agent_name(name),
                "your_symbols": self.cards[name],
                "num_agents": self.num_agents,
                "figures_per_card": self.figures_per_card,
                "pool_size": self.pool_size,
                "topology": self.topology,
                "discussion_rounds": None,
                "max_messages": max_messages_per_trial,
                "circle_neighbors": [
                    display_agent_name(neighbor)
                    for neighbor in self.circle_neighbors_by_name.get(name, [])
                ],
                "chain_contacts": [
                    display_agent_name(contact)
                    for contact in self.chain_contacts_by_name.get(name, [])
                ],
                "y_contacts": [
                    display_agent_name(contact)
                    for contact in self.y_contacts_by_name.get(name, [])
                ],
                "wheel_recipients": [
                    display_agent_name(contact)
                    for contact in self.wheel_contacts_by_name.get(name, [])
                ],
            })

        self.start_time = None
        turn_count = 0
        answer_message_count = None
        trial_finished = False
        stalled = False
        stall_reason = None
        max_messages_reached = False
        max_messages_reason = None
        scheduler_steps = 0
        idle_steps = 0
        max_scheduler_steps = max_messages_per_trial * max(self.num_agents, 1) * 4
        while self.running and not trial_finished:
            with self.lock:
                active_socks = [sock for sock in active_socks if sock in self.clients]
            missing_required = self._missing_required_jetsons(active_socks)
            if missing_required:
                missing_display = ", ".join(display_agent_name(name) for name in missing_required)
                stalled = True
                stall_reason = f"required Jetsons disconnected or missing: {missing_display}"
                print(f"[EXP] Trial stopped before next turn. Missing: {missing_display}.")
                break

            if self.message_count >= max_messages_per_trial:
                max_messages_reached = True
                max_messages_reason = f"maximum message limit reached ({max_messages_per_trial} messages)"
                print(f"\n[MAX MESSAGES] {max_messages_reason}")
                trial_finished = True
                break

            if self._poll_stop_command():
                print("\n[MANUAL STOP] Trial stopped by user.")
                trial_finished = True
                break

            if scheduler_steps >= max_scheduler_steps:
                stalled = True
                stall_reason = "scheduler stopped after too many invalid/timeout steps without an answer"
                print(f"\n[STALLED] {stall_reason}")
                break

            current_sock = self._choose_next_sock(active_socks)
            if current_sock is None:
                stalled = True
                stall_reason = "no active agents available"
                break

            with self.lock:
                if current_sock not in self.clients:
                    continue
                speaker = self.clients[current_sock]["name"]
                speaker_id = sock_agent_ids.get(current_sock)

            reset_chat_history = False
            if reset_chat_history:
                self._reset_agent_histories()
                self.broadcast({
                    "type": "reset_chat_history",
                    "trial_id": current_trial_id,
                }, recipients=active_socks)
                print("[ROUND] Round ended. Resetting agent chat histories.")

            can_answer = self.message_count >= answer_gate_message_count(self.topology, self)
            self._send_turn_request(
                current_sock,
                speaker_id,
                speaker,
                self.message_count,
                can_answer,
                reset_chat_history=reset_chat_history,
            )
            print(
                f"[SCHEDULER] Requesting output from {display_agent_name(speaker)} "
                f"at message_count={self.message_count}; can_answer={can_answer}."
            )

            before_messages = self.message_count
            resp = self._recv_with_manual_stop(current_sock, total_timeout=300, poll_interval=1)
            scheduler_steps += 1
            if resp is None:
                print(f"[ERROR] {display_agent_name(speaker)} disconnected.")
                self._drop_client(current_sock, reason="recv failed/disconnected")
            elif resp.get("type") == "manual_stop":
                print("\n[MANUAL STOP] Trial stopped by user.")
                trial_finished = True
            elif resp.get("type") == "timeout":
                print(f"[TIMEOUT] {display_agent_name(speaker)}")
            elif resp.get("trial_id") != current_trial_id:
                print(
                    f"[STALE RESPONSE IGNORED] {display_agent_name(speaker)} sent "
                    f"trial_id={resp.get('trial_id')!r}; expected {current_trial_id}."
                )
            elif resp.get("type") == "invalid":
                print(f"{display_agent_name(speaker)}: invalid output, skipped.")
            elif resp.get("type") == "chat":
                text = resp.get("text", "")
                raw = resp.get("raw", "")
                target = resp.get("target")
                target_source = resp.get("target_source", "")
                original_target = resp.get("original_target", "")
                if text:
                    accepted = self.route_chat_message(
                        text,
                        speaker,
                        speaker_id,
                        current_sock,
                        active_socks,
                        agent_socks,
                        self.message_count + 1,
                        turn_count + 1,
                        target=target,
                        raw=raw,
                        target_source=target_source,
                        original_target=original_target,
                    )
                    if accepted and self.message_count >= max_messages_per_trial:
                        max_messages_reached = True
                        max_messages_reason = f"maximum message limit reached ({max_messages_per_trial} messages)"
                        print(f"\n[MAX MESSAGES] {max_messages_reason}")
                        trial_finished = True
                else:
                    print(f"{display_agent_name(speaker)}: empty MESSAGE, skipped.")
            elif resp.get("type") == "answer":
                raw_word = resp.get("word", resp.get("symbol", resp.get("text", ""))).strip()
                word = extract_figure_answer(raw_word)
                if not word:
                    print(
                        f"{display_agent_name(speaker)}: invalid answer {raw_word!r}, skipped. "
                        f"Use one of: {', '.join(FIGURES)}."
                    )
                    continue
                raw = resp.get("raw", "")
                answer_message_count = self.message_count
                self.answers[speaker] = word
                is_correct = self._normalize_word(word) == self._normalize_word(self.common_symbol)
                print(f"{display_agent_name(speaker)} ANSWER: {word}")
                if DEBUG and raw:
                    print(f"[ANSWER RAW] {raw}")
                trial_finished = True
            else:
                print(f"{display_agent_name(speaker)}: invalid output, skipped.")

            turn_count += 1
            idle_steps = 0 if self.message_count > before_messages else idle_steps + 1
            time.sleep(0.5)

            with self.lock:
                alive_active = [sock for sock in active_socks if sock in self.clients]
            active_socks = alive_active
            agent_socks = {
                sock_agent_ids[sock]: sock
                for sock in active_socks
                if sock in sock_agent_ids
            }
            if len(active_socks) < self.num_agents:
                print("[EXP] Trial stopped because one or more required Jetsons disconnected.")
                break

        self.end_time = time.time()
        elapsed = self._elapsed_since_first_message()

        found = False
        if self.answers:
            first_answer = next(iter(self.answers.values()))
            found = self._normalize_word(first_answer) == self._normalize_word(self.common_symbol)
        final_answer_speaker = None
        final_answer_word = None
        if self.answers:
            final_answer_speaker, final_answer_word = next(reversed(self.answers.items()))
        submitted_figure_status = final_answer_word
        if not submitted_figure_status:
            if self.stop_current_trial:
                submitted_figure_status = "Trial stopped"
            elif max_messages_reached:
                submitted_figure_status = "No figure submitted (message limit reached)"
            else:
                submitted_figure_status = "No figure submitted"
        displayed_answers = {
            display_agent_name(name): word
            for name, word in self.answers.items()
        }
        displayed_messages_per_agent = {
            display_agent_name(name): count
            for name, count in self.messages_per_agent.items()
        }

        messages_used = answer_message_count if answer_message_count is not None else self.message_count
        efficiency_status, efficiency_explanation, efficiency_max_rounds = evaluate_efficiency(
            found,
            bool(self.answers),
            messages_used,
            self.num_agents,
            self.topology,
            max_messages_per_trial,
        )
        result_status = efficiency_status

        result = {
            "type": "experiment_end",
            "trial_id": current_trial_id,
            "result": result_status,
            "reason": (
                "trial stopped by user" if self.stop_current_trial
                else max_messages_reason if max_messages_reached
                else stall_reason
            ),
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
            "winner": None,
            "final_answer_speaker": display_agent_name(final_answer_speaker) if final_answer_speaker else None,
            "final_answer_word": final_answer_word,
            "time_seconds": round(elapsed, 2),
            "total_messages": self.message_count,
            "total_deliveries": self.delivery_count,
            "total_turns": turn_count,
            "conversation_log": self.conversation_log,
            "rounds": None,
            "answer_round": None,
            "rounds_before_answer": None,
            "messages_before_answer": answer_message_count,
            "num_agents": self.num_agents,
            "figures_per_card": self.figures_per_card,
            "pool_size": self.pool_size,
            "max_messages_per_trial": max_messages_per_trial,
            "max_messages_reached": max_messages_reached,
            "efficiency_status": efficiency_status,
            "efficiency_explanation": efficiency_explanation,
            "efficiency_max_messages": efficiency_max_rounds,
            "topology": self.topology,
            "discussion_rounds": None,
        }

        print(f"\n{'=' * 55}")
        print("  EXPERIMENT COMPLETE")
        if result_status == "success_efficient":
            result_text = "SUCCESS_EFFICIENT"
        elif result_status == "success_slow":
            result_text = "SUCCESS_SLOW"
        elif self.stop_current_trial:
            result_text = "STOPPED"
        elif max_messages_reached:
            result_text = "FAILED_NO_ANSWER"
        elif stalled:
            result_text = "STALLED"
        elif self.answers:
            result_text = "FAILED_WRONG_ANSWER"
        else:
            result_text = "FAILED_NO_ANSWER"
        print(f"  Result:         {result_text}")
        if max_messages_reached and max_messages_reason:
            print(f"  Reason:         {max_messages_reason}")
        if stalled and stall_reason:
            print(f"  Reason:         {stall_reason}")
        if final_answer_speaker and final_answer_word:
            verdict = "CORRECT" if found else "WRONG"
            print(f"  Final answer:   {display_agent_name(final_answer_speaker)} -> '{final_answer_word}' ({verdict})")
        if answer_message_count is not None:
            print(f"  Answer msg #:   {answer_message_count}")
        else:
            print("  Answer msg #:   None")
        print(f"  Common word:    {self.common_symbol}")
        print(f"  Time:           {elapsed:.2f}s")
        print(f"  Messages sent:  {self.message_count}")
        print(f"  Deliveries:     {self.delivery_count}")
        print(f"  Turns used:     {turn_count}")
        print(f"  Efficiency:     {efficiency_status}")
        print(f"  Eff. reason:    {efficiency_explanation}")
        print(f"  Max messages:   {efficiency_max_rounds}")
        print(f"{'=' * 55}\n")

        self.broadcast(result, recipients=active_socks)

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(MAX_PARTICIPANTS)

            print(f"\n{'=' * 55}")
            print("  Leavitt Experiment Server")
            print(f"  Listening on {self.host}:{self.port}")
            print(f"  Trial Jetsons range: {MIN_PARTICIPANTS}-{MAX_PARTICIPANTS}")
            print(f"  Topology: {display_topology_name(self.topology)}")
            print("  Trial mode: message-count based")
            print(f"{'=' * 55}\n")

            accept_thread = threading.Thread(target=self._accept_loop, daemon=True)
            accept_thread.start()

            while self.running:
                self.run_experiment()
                while True:
                    choice = input("Continue experiment? (c=continue, r=restart Jetson clients, m=change mode, e=exit): ").strip().lower()
                    if choice in ("c", "continue"):
                        break
                    if choice in ("r", "restart", "reload"):
                        restart_jetson_clients()
                        continue
                    if choice in ("m", "mode", "change"):
                        self.topology = prompt_topology()
                        print(f"[MODE] Topology changed to: {display_topology_name(self.topology)}")
                        break
                    if choice in ("e", "exit"):
                        self.running = False
                        break
                    print("[INPUT] Please type 'c' to continue, 'r' to restart Jetson clients, 'm' to change mode, or 'e' to exit.")

        except KeyboardInterrupt:
            print("\n[SERVER] Shutting down...")
        except OSError as e:
            print(f"[SERVER ERROR] {e}")
        finally:
            self.running = False
            for sock in list(self.clients.keys()):
                try:
                    sock.close()
                except OSError:
                    pass
            self.server_socket.close()
            print("[SERVER] Closed.")

    def _accept_loop(self):
        while self.running:
            try:
                client_socket, addr = self.server_socket.accept()
                threading.Thread(
                    target=self.handle_new_client,
                    args=(client_socket, addr),
                    daemon=True,
                ).start()
            except OSError:
                break


def prompt_topology():
    while True:
        choice = input("Select topology (b=broadcast, c=circle, h=chain, y=y-shape, w=wheel): ").strip().lower()
        if choice in ("b", "broadcast"):
            return "broadcast"
        if choice in ("c", "circle"):
            return "circle"
        if choice in ("h", "chain"):
            return "chain"
        if choice in ("y", "y-shape", "yshape"):
            return "y"
        if choice in ("w", "wheel"):
            return "wheel"
        print("[INPUT] Please type 'b' for broadcast, 'c' for circle, 'h' for chain, 'y' for y-shape, or 'w' for wheel.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python server.py <host> <port>")
        print("Example: python server.py 0.0.0.0 5001")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    topology = prompt_topology()

    server = LeavittServer(host=host, port=port, topology=topology)
    server.start()
