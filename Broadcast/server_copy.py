"""
LEAVITT SERVER - Multi-trial, BROADCASTING, variable Jetson count (2-5)

This file runs the Leavitt experiment server, coordinating Jetson agents
by assigning private figure sets, broadcasting turn-based messages, and 
checking whether they correctly find the shared figure.

"""

import socket
import threading
import json
import sys
import time
import random
import select
import subprocess

FIGURES = [
    "square", "circle", "triangle", "diamond", "cross", "asterisk",
]

MIN_PARTICIPANTS = 2
MAX_PARTICIPANTS = 5
DEFAULT_FIGURES_PER_CARD = 3
MAX_ROUNDS_PER_TRIAL = 10
EFFICIENCY_MAX_ROUNDS_BY_AGENTS = {
    2: 3,
    3: 3,
    4: 4,
    5: 4,
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
    "jetson1": "Agent_1",
    "jetson2": "Agent_2",
    "jetson3": "Agent_3",
    "jetson4": "Agent_4",
    "jetson5": "Agent_5",
}
def generate_jetson_sets(nicknames, seed=None):
    """
    Rules:
    - n in [2, 5]
    - n == 2 (exception): pool=5, each gets 3, exactly 1 common figure
    - n >= 3: pool=n+1, each gets n, exactly 1 figure common to all
      Construction for n>=3: each card omits one distinct non-common figure from pool.
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
        # Exception requested by user: 5 total figures, 3 per Jetson, exactly 1 common.
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

    # n >= 3
    pool_size = n + 1
    if pool_size > len(FIGURES):
        raise ValueError(f"Need {pool_size} figures, but FIGURES only has {len(FIGURES)}.")

    pool = rng.sample(FIGURES, pool_size)
    common_figure = rng.choice(pool)
    non_common = [f for f in pool if f != common_figure]  # exactly n figures
    rng.shuffle(non_common)

    # Each Jetson gets n figures by omitting one distinct non-common figure.
    assignments = {}
    for idx, nickname in enumerate(clean_nicknames):
        omitted = non_common[idx]
        card = [f for f in pool if f != omitted]
        rng.shuffle(card)
        assignments[nickname] = card

    return common_figure, assignments, pool_size, n


def evaluate_efficiency(found, result_status, rounds_used, num_agents):
    max_efficient_rounds = EFFICIENCY_MAX_ROUNDS_BY_AGENTS.get(num_agents, 4)

    if result_status != "correct" or not found:
        return (
            "FAILED",
            "Agents did not correctly identify the common figure.",
            max_efficient_rounds,
        )

    if rounds_used <= max_efficient_rounds:
        return (
            "CORRECT_AND_EFFICIENT",
            f"Agents found the correct figure in {rounds_used} rounds, within the efficiency limit of {max_efficient_rounds} rounds.",
            max_efficient_rounds,
        )

    return (
        "CORRECT_BUT_INEFFICIENT",
        f"Agents found the correct figure, but used {rounds_used} rounds, exceeding the efficiency limit of {max_efficient_rounds} rounds.",
        max_efficient_rounds,
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
    def __init__(self, host, port):
        self.host = host
        self.port = port

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

        self.num_agents = 2
        self.cards = {}
        self.common_symbol = None
        self.answers = {}

        self.start_time = None
        self.end_time = None
        self.message_count = 0
        self.conversation_log = []
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
            print(f"[-] {info.get('name', 'Unknown')} removed ({reason})")

    def _recv(self, sock, timeout=None):
        if timeout:
            sock.settimeout(timeout)
        try:
            buffer = self.recv_buffers.get(sock, b"")

            while b"\n" not in buffer:
                chunk = sock.recv(4096)
                if not chunk:
                    return None
                buffer += chunk

            line, buffer = buffer.split(b"\n", 1)
            self.recv_buffers[sock] = buffer

            return json.loads(line.decode("utf-8"))
        except socket.timeout:
            return {"type": "timeout"}
        except (json.JSONDecodeError, ConnectionResetError, OSError) as e:
            print(f"[RECV ERROR] {e}")
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

    def handle_new_client(self, client_socket, client_address):
        try:
            if not self.accepting_connections:
                self._send(client_socket, {
                    "type": "system",
                    "text": "Server is not accepting clients yet. Wait for operator to start a trial.",
                })
                self._drop_client(client_socket, reason="connections not open")
                return

            self._send(client_socket, {"type": "nickname_request"})
            resp = self._recv(client_socket, timeout=30)
            if not resp or resp.get("type") != "nickname":
                self._drop_client(client_socket, reason="invalid handshake")
                return

            with self.lock:
                hostname = str(resp.get("hostname", "")).strip().lower()
                if not hostname:
                    self._send(client_socket, {"type": "system", "text": "Missing hostname in handshake."})
                    self._drop_client(client_socket, reason="missing hostname")
                    return

                name = HOSTNAME_TO_AGENT.get(hostname)
                if name is None:
                    self._send(client_socket, {"type": "system", "text": f"Unknown hostname '{hostname}'."})
                    self._drop_client(client_socket, reason=f"unknown hostname {hostname}")
                    return

                for info in self.clients.values():
                    if info.get("name") == name:
                        self._send(client_socket, {"type": "system", "text": f"{name} is already connected."})
                        self._drop_client(client_socket, reason=f"duplicate identity {name}")
                        return

                self.clients[client_socket] = {"name": name, "hostname": hostname, "address": client_address}
                self.turn_order.append(client_socket)

            print(f"[+] {name} connected from hostname '{hostname}' at {client_address}")
            self._send(client_socket, {
                "type": "welcome",
                "agent_name": name,
                "hostname": hostname,
                "text": f"Welcome {name} ({hostname}). Waiting for trial start...",
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

    def _wait_for_clients(self, needed):
        print(f"\n[EXP] Waiting for first {needed} connected Jetsons...")
        while self.running:
            with self.lock:
                connected_in_order = []
                for sock in self.turn_order:
                    info = self.clients.get(sock)
                    if not info:
                        continue
                    name = info.get("name", "")
                    if name.startswith("Agent_"):
                        connected_in_order.append((name, sock))

                if len(connected_in_order) >= needed:
                    selected = connected_in_order[:needed]
                    selected.sort(key=lambda x: int(x[0].split("_", 1)[1]))
                    return [sock for _, sock in selected]
            time.sleep(1)

    def _normalize_word(self, text):
        return str(text).strip().lower()

    def run_experiment(self):
        self.stop_current_trial = False
        self.accepting_connections = False
        self.num_agents = self._prompt_num_agents()
        self.required_for_trial = self.num_agents
        self.accepting_connections = True

        active_socks = self._wait_for_clients(self.num_agents)
        self.accepting_connections = False
        time.sleep(1)

        nicknames = []
        with self.lock:
            for sock in active_socks:
                nicknames.append(self.clients[sock]["name"])

        self.common_symbol, self.cards, self.pool_size, self.figures_per_card = generate_jetson_sets(nicknames)
        self.answers = {}
        self.message_count = 0
        self.conversation_log = []
        self.turn_index = 0

        print(f"\n{'=' * 55}")
        print("  EXPERIMENT STARTING")
        print(f"  Jetsons: {self.num_agents}")
        print(f"  Figure pool size: {self.pool_size}")
        print(f"  Figures per card: {self.figures_per_card}")
        print(f"  Common figure: {self.common_symbol}")
        for sock in active_socks:
            name = self.clients[sock]["name"]
            print(f"  {name}'s card: {self.cards[name]}")
        print(f"{'=' * 55}\n")

        for sock in active_socks:
            name = self.clients[sock]["name"]
            self._send(sock, {
                "type": "experiment_start",
                "agent_name": name,
                "your_symbols": self.cards[name],
                "num_agents": self.num_agents,
                "figures_per_card": self.figures_per_card,
                "pool_size": self.pool_size,
            })

        self.start_time = time.time()
        turn_count = 0
        round_number = 1
        trial_finished = False
        stalled = False
        stall_reason = None
        max_rounds_reached = False
        max_rounds_reason = None

        while self.running and not trial_finished:
            if round_number > MAX_ROUNDS_PER_TRIAL:
                max_rounds_reached = True
                max_rounds_reason = f"maximum round limit reached ({MAX_ROUNDS_PER_TRIAL} rounds)"
                print(f"\n[MAX ROUNDS] {max_rounds_reason}")
                trial_finished = True
                break

            if self._poll_stop_command():
                print("\n[MANUAL STOP] Trial stopped by user.")
                trial_finished = True
                break

            round_msg = {"type": "system", "text": f"============= ROUND {round_number} =============="}
            self.broadcast(round_msg, recipients=active_socks)
            print(f"\n============= ROUND {round_number} ==============")

            for current_sock in active_socks:
                with self.lock:
                    if current_sock not in self.clients:
                        continue
                    speaker = self.clients[current_sock]["name"]
                if speaker in self.answers:
                    continue

                self.broadcast(
                    {"type": "system", "text": f"[Waiting for {speaker} to respond]"},
                    exclude=current_sock,
                    recipients=active_socks,
                )

                self._send(current_sock, {"type": "your_turn"})
                print(f"{speaker}'s turn...")

                resp = self._recv_with_manual_stop(current_sock, total_timeout=300, poll_interval=1)
                if resp is None:
                    print(f"[ERROR] {speaker} disconnected.")
                    self._drop_client(current_sock, reason="recv failed/disconnected")
                    continue
                if resp.get("type") == "manual_stop":
                    print("\n[MANUAL STOP] Trial stopped by user.")
                    trial_finished = True
                    break
                if resp.get("type") == "timeout":
                    print(f"[TIMEOUT] {speaker}")
                    turn_count += 1
                    continue

                if resp.get("type") == "chat":
                    text = resp.get("text", "").strip()
                    if text:
                        self.message_count += 1
                        self.conversation_log.append({
                            "round": round_number,
                            "turn": turn_count + 1,
                            "sender": speaker,
                            "text": text,
                            "elapsed": round(time.time() - self.start_time, 2),
                        })
                        self.broadcast(
                            {"type": "chat", "sender": speaker, "text": text},
                            exclude=current_sock,
                            recipients=active_socks,
                        )
                        print(f"[{speaker}] {text}")

                if resp.get("type") == "answer":
                    # Accept explicit word field; keep symbol/text fallback for compatibility.
                    word = resp.get("word", resp.get("symbol", resp.get("text", ""))).strip()
                    self.answers[speaker] = word
                    is_correct = self._normalize_word(word) == self._normalize_word(self.common_symbol)
                    print(f"[ANSWER] {speaker} submitted word: '{word}' (correct={is_correct})")
                    turn_count += 1
                    trial_finished = True
                    break

                if resp.get("type") != "answer":
                    turn_count += 1
                time.sleep(0.5)

            if stalled:
                break
            round_number += 1

            with self.lock:
                alive_active = [sock for sock in active_socks if sock in self.clients]
            active_socks = alive_active
            if len(active_socks) < self.num_agents:
                print("[EXP] Trial stopped because one or more required Jetsons disconnected.")
                break

        self.end_time = time.time()
        elapsed = self.end_time - self.start_time

        found = False
        if self.answers:
            first_answer = next(iter(self.answers.values()))
            found = self._normalize_word(first_answer) == self._normalize_word(self.common_symbol)
        final_answer_speaker = None
        final_answer_word = None
        if self.answers:
            final_answer_speaker, final_answer_word = next(reversed(self.answers.items()))

        result_status = (
            "stopped" if self.stop_current_trial
            else "max_rounds" if max_rounds_reached
            else "stalled" if stalled
            else "correct" if found
            else "incorrect" if self.answers
            else "incomplete"
        )
        rounds_used = max(round_number - 1, 0)
        efficiency_status, efficiency_explanation, efficiency_max_rounds = evaluate_efficiency(
            found,
            result_status,
            rounds_used,
            self.num_agents,
        )

        result = {
            "type": "experiment_end",
            "result": result_status,
            "reason": (
                "trial stopped by user" if self.stop_current_trial
                else max_rounds_reason if max_rounds_reached
                else stall_reason
            ),
            "common_word": self.common_symbol,
            "answers": self.answers,
            "winner": None,
            "final_answer_speaker": final_answer_speaker,
            "final_answer_word": final_answer_word,
            "time_seconds": round(elapsed, 2),
            "total_messages": self.message_count,
            "total_turns": turn_count,
            "rounds": rounds_used,
            "num_agents": self.num_agents,
            "figures_per_card": self.figures_per_card,
            "pool_size": self.pool_size,
            "max_rounds_per_trial": MAX_ROUNDS_PER_TRIAL,
            "max_rounds_reached": max_rounds_reached,
            "efficiency_status": efficiency_status,
            "efficiency_explanation": efficiency_explanation,
            "efficiency_max_rounds": efficiency_max_rounds,
        }

        print(f"\n{'=' * 55}")
        print("  EXPERIMENT COMPLETE")
        if found:
            result_text = "CORRECT"
        elif self.stop_current_trial:
            result_text = "STOPPED"
        elif max_rounds_reached:
            result_text = "MAX_ROUNDS"
        elif stalled:
            result_text = "STALLED"
        elif self.answers:
            result_text = "INCORRECT"
        else:
            result_text = "INCOMPLETE"
        print(f"  Result:         {result_text}")
        if max_rounds_reached and max_rounds_reason:
            print(f"  Reason:         {max_rounds_reason}")
        if stalled and stall_reason:
            print(f"  Reason:         {stall_reason}")
        if final_answer_speaker and final_answer_word:
            verdict = "CORRECT" if found else "WRONG"
            print(f"  Final answer:   {final_answer_speaker} -> '{final_answer_word}' ({verdict})")
        print(f"  Common word:    {self.common_symbol}")
        print(f"  Time:           {elapsed:.2f}s")
        print(f"  Messages sent:  {self.message_count}")
        print(f"  Turns used:     {turn_count}")
        print(f"  Efficiency:     {efficiency_status}")
        print(f"  Eff. reason:    {efficiency_explanation}")
        print(f"  Eff. max rounds:{efficiency_max_rounds}")
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
            print("  Turn mode: round-based")
            print(f"{'=' * 55}\n")

            accept_thread = threading.Thread(target=self._accept_loop, daemon=True)
            accept_thread.start()

            while self.running:
                self.run_experiment()
                while True:
                    choice = input("Continue experiment? (c=continue, r=restart Jetson clients, e=exit): ").strip().lower()
                    if choice in ("c", "continue"):
                        break
                    if choice in ("r", "restart", "reload"):
                        restart_jetson_clients()
                        continue
                    if choice in ("e", "exit"):
                        self.running = False
                        break
                    print("[INPUT] Please type 'c' to continue, 'r' to restart Jetson clients, or 'e' to exit.")

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


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python new_server.py <host> <port>")
        print("Example: python new_server.py 0.0.0.0 5001")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    server = LeavittServer(host=host, port=port)
    server.start()
