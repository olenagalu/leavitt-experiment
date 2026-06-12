"""
LEAVITT SERVER - Multi-trial, variable Jetson count (2-5)
Based on 3fig_2jet_server.py with minor behavior updates.
"""

import socket
import threading
import json
import sys
import time
import random

FIGURES = [
    "square", "circle", "triangle", "diamond", "cross",
    "asterisk", "star", "heart", "moon", "arrow",
]

MIN_PARTICIPANTS = 2
MAX_PARTICIPANTS = 5
DEFAULT_FIGURES_PER_CARD = 3


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

        self.num_agents = 2
        self.cards = {}
        self.common_symbol = None
        self.answers = {}

        self.start_time = None
        self.end_time = None
        self.message_count = 0
        self.conversation_log = []
        self.max_turns = 30

        self.figures_per_card = DEFAULT_FIGURES_PER_CARD
        self.pool_size = 5

    def _send(self, sock, msg_dict):
        try:
            raw = json.dumps(msg_dict) + "\n"
            sock.sendall(raw.encode("utf-8"))
        except Exception as e:
            print(f"[SEND ERROR] {e}")

    def _recv(self, sock, timeout=None):
        if timeout:
            sock.settimeout(timeout)
        try:
            data = sock.recv(8192)
            if not data:
                return None
            return json.loads(data.decode("utf-8").strip())
        except socket.timeout:
            return {"type": "timeout"}
        except (json.JSONDecodeError, ConnectionResetError, OSError):
            return None
        finally:
            sock.settimeout(None)

    def broadcast(self, msg_dict, exclude=None, recipients=None):
        with self.lock:
            target_socks = recipients if recipients is not None else list(self.clients.keys())
            for sock in list(target_socks):
                if sock != exclude:
                    self._send(sock, msg_dict)

    def handle_new_client(self, client_socket, client_address):
        try:
            self._send(client_socket, {"type": "nickname_request"})
            resp = self._recv(client_socket, timeout=30)
            if not resp or resp.get("type") != "nickname":
                client_socket.close()
                return

            with self.lock:
                assigned_numbers = set()
                for info in self.clients.values():
                    existing = info.get("name", "")
                    if existing.startswith("Agent_"):
                        try:
                            assigned_numbers.add(int(existing.split("_", 1)[1]))
                        except ValueError:
                            pass

                slot = None
                for i in range(1, MAX_PARTICIPANTS + 1):
                    if i not in assigned_numbers:
                        slot = i
                        break

                if slot is None:
                    self._send(client_socket, {"type": "system", "text": "Server is full (max 5 agents)."})
                    client_socket.close()
                    return

                name = f"Agent_{slot}"
                self.clients[client_socket] = {"name": name, "address": client_address}
                self.turn_order.append(client_socket)

            print(f"[+] {name} connected from {client_address}")
            self._send(client_socket, {
                "type": "welcome",
                "text": f"Welcome {name}. Waiting for trial start...",
            })
        except Exception as e:
            print(f"[ERROR] Onboarding: {e}")
            try:
                client_socket.close()
            except OSError:
                pass

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
        print(f"\n[EXP] Waiting for {needed} connected Jetsons...")
        while self.running:
            with self.lock:
                connected = len(self.turn_order)
                if connected >= needed:
                    return list(self.turn_order[:needed])
            time.sleep(1)

    def _normalize_word(self, text):
        return str(text).strip().lower()

    def run_experiment(self):
        self.num_agents = self._prompt_num_agents()

        active_socks = self._wait_for_clients(self.num_agents)
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
                "your_symbols": self.cards[name],
                "num_agents": self.num_agents,
                "figures_per_card": self.figures_per_card,
                "pool_size": self.pool_size,
            })

        self.start_time = time.time()
        turn_count = 0

        while self.running and turn_count < self.max_turns:
            if len(self.answers) >= self.num_agents:
                break

            current_sock = active_socks[self.turn_index % len(active_socks)]
            with self.lock:
                if current_sock not in self.clients:
                    self.turn_index += 1
                    turn_count += 1
                    continue
                speaker = self.clients[current_sock]["name"]

            if speaker in self.answers:
                self.turn_index += 1
                turn_count += 1
                continue

            self.broadcast(
                {"type": "system", "text": f"[Waiting for {speaker} to respond]"},
                exclude=current_sock,
                recipients=active_socks,
            )

            self._send(current_sock, {"type": "your_turn"})
            print(f"[TURN {turn_count + 1}] {speaker}'s turn...")

            resp = self._recv(current_sock, timeout=120)
            if resp is None:
                print(f"[ERROR] {speaker} disconnected.")
                break
            if resp.get("type") == "timeout":
                print(f"[TIMEOUT] {speaker}")
                self.turn_index += 1
                turn_count += 1
                continue

            if resp.get("type") == "chat":
                text = resp.get("text", "").strip()
                if text:
                    self.message_count += 1
                    self.conversation_log.append({
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
                print(f"[ANSWER] {speaker} submitted word: '{word}'")
                self.broadcast(
                    {"type": "system", "text": f"{speaker} has locked in an answer."},
                    exclude=current_sock,
                    recipients=active_socks,
                )

            self.turn_index += 1
            turn_count += 1
            time.sleep(0.5)

        self.end_time = time.time()
        elapsed = self.end_time - self.start_time

        key_word = self._normalize_word(self.common_symbol)
        all_correct = (
            len(self.answers) == self.num_agents
            and all(self._normalize_word(ans) == key_word for ans in self.answers.values())
        )

        result = {
            "type": "experiment_end",
            "result": "correct" if all_correct else "incorrect",
            "common_word": self.common_symbol,
            "answers": self.answers,
            "time_seconds": round(elapsed, 2),
            "total_messages": self.message_count,
            "total_turns": turn_count,
            "num_agents": self.num_agents,
            "figures_per_card": self.figures_per_card,
            "pool_size": self.pool_size,
        }

        print(f"\n{'=' * 55}")
        print("  EXPERIMENT COMPLETE")
        print(f"  Result:         {'CORRECT' if all_correct else 'INCORRECT'}")
        print(f"  Common word:    {self.common_symbol}")
        print(f"  Answers:        {self.answers}")
        print(f"  Time:           {elapsed:.2f}s")
        print(f"  Messages sent:  {self.message_count}")
        print(f"  Turns used:     {turn_count}")
        print(f"{'=' * 55}\n")

        self.broadcast(result, recipients=active_socks)

    def _save_log(self, result):
        # Logging disabled by request.
        return

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(MAX_PARTICIPANTS)

            print(f"\n{'=' * 55}")
            print("  Leavitt Experiment Server")
            print(f"  Listening on {self.host}:{self.port}")
            print(f"  Trial Jetsons range: {MIN_PARTICIPANTS}-{MAX_PARTICIPANTS}")
            print(f"  Max turns per trial: {self.max_turns}")
            print(f"{'=' * 55}\n")

            accept_thread = threading.Thread(target=self._accept_loop, daemon=True)
            accept_thread.start()

            while self.running:
                self.run_experiment()
                while True:
                    choice = input("Continue experiment? (c=continue, e=exit): ").strip().lower()
                    if choice in ("c", "continue"):
                        break
                    if choice in ("e", "exit"):
                        self.running = False
                        break
                    print("[INPUT] Please type 'c' to continue or 'e' to exit.")

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
