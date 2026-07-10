"""
LEAVITT SERVER - Feb. 14th - 16th , 2026 
"""

# libraries
import socket # TCP socket constructor, 
import threading # thread constructor, start(), lock() -> easy thread management
import json # serialize data to send over socket + make log -> .dumps(dict), .loads(string), .dump(dict, file)
import sys # handle command line arguments -> sys.argv, sys.exit(1)
import time # for time() and sleep()
import random # for shuffle(list)

# global? or is this like a #define?
#SYMBOL_POOL = list("@#$%&*+!=?~^<>{}[]|/\\:;")

FIGURES = ["square", "circle", "triangle", "diamond", "cross", "asterisk"]  # max 6 total

MIN_PARTICIPANTS = 2 # exactly 2 Jetsons
MAX_PARTICIPANTS = 2 # exactly 2 Jetsons
DEFAULT_FIGURES_PER_CARD = 3 # for now, each Jetson gets only 3 figures

def generate_jetson_sets(nicknames, figures_per_card=DEFAULT_FIGURES_PER_CARD, seed=None):
    """
    Give each Jetson exactly `figures_per_card` figures.
    For the 2-Jetson version, there is exactly ONE common figure.

    Example with 3 figures per Jetson:
        Jetson1: [common, unique1, unique2]
        Jetson2: [common, unique3, unique4]
    """
    if not isinstance(nicknames, list):
        raise TypeError("nicknames must be a list of strings.")

    clean_nicknames = [n.strip() for n in nicknames]

    if any(not n for n in clean_nicknames):
        raise ValueError("All nicknames must be non-empty.")

    if len(set(clean_nicknames)) != len(clean_nicknames):
        raise ValueError("Nicknames must be unique.")

    num_jetsons = len(clean_nicknames)
    if not (MIN_PARTICIPANTS <= num_jetsons <= MAX_PARTICIPANTS):
        raise ValueError(
            f"num_jetsons must be between {MIN_PARTICIPANTS} and {MAX_PARTICIPANTS}."
        )

    if figures_per_card < 2:
        raise ValueError("figures_per_card must be at least 2.")

    # Need 1 common figure + unique distractors for every Jetson.
    # For 2 Jetsons and 3 figures each: 1 + 2*(3 - 1) = 5 figures needed.
    total_figure_count = 1 + num_jetsons * (figures_per_card - 1)
    if total_figure_count > len(FIGURES):
        raise ValueError(
            f"Need {total_figure_count} figures, but FIGURES only has {len(FIGURES)}."
        )

    rng = random.Random(seed)
    pool = rng.sample(FIGURES, total_figure_count)

    # This is the only figure shared by all Jetsons.
    common_figure = rng.choice(pool)
    other_figures = [f for f in pool if f != common_figure]
    rng.shuffle(other_figures)

    assignments = {}
    index = 0

    for nickname in clean_nicknames:
        my_distractors = other_figures[index:index + figures_per_card - 1]
        index += figures_per_card - 1

        jetson_figures = [common_figure] + my_distractors
        rng.shuffle(jetson_figures)
        assignments[nickname] = jetson_figures

    return common_figure, assignments


# server class	
class LeavittServer: # note: self = this
	
	# constructor
	def __init__(self, host, port, figures_per_card=DEFAULT_FIGURES_PER_CARD):
		
		####################################################################################################################
		###### MEMBER DATA ######
		
		# save parameter args to object
		self.host = host
		self.port = port
		self.figures_per_card = figures_per_card
		
		# make socket = IPv4 (AF_INET), TCP (SOCK_STREAM)
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		# allow port re-use, w/o this if we kill server and restart quickly OS will hold port for timeout period
		self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		# dictionary, here the C++ equivalent is std::unordered_map, lets us look up agent's name + addr. given socket
		# so... key = socket ID, values = agent name, agent addr. 
		# filled in later
		self.clients = {}
		
		# list -> just a dynamic array, used to keep sockets in turn sequences -> filled in during experiment
		self.turn_order = []
		
		# tracks whose turn it is -> using a round-robin architecture for server, one agent talks at a time
		self.turn_index = 0
		
		# c++ equivalent = std::mutex, protects client/server order from race conditions
		self.lock = threading.Lock()
		
		# simple bool, tracks whether server is on/off
		self.running = True

		# number of agents in experiment
		self.num_agents = 2
		
		# dict, nickname -> list of figures, filled by generate_jetson_sets
		self.cards = {}
		
		# ANSWER KEY -> filled in later
		self.common_symbol = None
		
		# dict, agent name = key, agent answer = value
		self.answers = {}
		
		# time-stamp start of experimen -> filled in later
		self.start_time = None
		
		# time-stamp end of experiment -> filled in later
		self.end_time = None
		
		# message counter, counts all chat messages sent during experiment
		self.message_count = 0
		
		# list of every message, converted to JSON at the end
		self.conversation_log = []
		
		# safety limit -> in case AI agents start going crazy and hearing voices in their heads...
		self.max_turns = 30

		####################################################################################################################

	######### _send and _recv are equivalent to C++ PRIVATE FUNCTIONS ######### -> ONLY SERVER FUNCS WILL CALL THESE 
	
	# send one JSON message to one CLIENT
	def _send(self, sock, msg_dict): # note: try, except = try - catch block from C/C++
		
		try:
			
			raw = json.dumps(msg_dict) + "\n" # call JSON library function dumps() to 
			
			sock.sendall(raw.encode("utf-8")) # convert string to bytes, send all of these .sendall is very important here, see sock lib docs
		
		except Exception as e:
			
			print(f"[SEND ERROR] {e}") # if we run into trouble with either json.dumps() or sock.sendall(), print what went wrong
										# {e} will print the exception that was caught 

	# receive one JSON message from one CLIENT
	
	def _recv(self, sock, timeout=None):
		
		if timeout: # handle timeout 
			
			sock.settimeout(timeout)
		
		try: 
			
			data = sock.recv(8192) # read up to 8192 bytes. why 8192? because....
			
			if not data:
				
				return None
			
			return json.loads(data.decode("utf-8").strip()) # 
		
		except socket.timeout:
			
			return {"type": "timeout"}
		
		except (json.JSONDecodeError, ConnectionResetError, OSError):
			
			return None
		
		finally:
			
			sock.settimeout(None)

	######### END PRIVATE FUNCTIONS #########
	
	# send a message to ALL connected clients, optionally skip one (the sender)
	# exclude = the socket we DON'T want to send to (so agent doesn't receive its own message)
	def broadcast(self, msg_dict, exclude=None):
		
		# grab mutex -> no other thread can touch self.clients while we iterate
		with self.lock:
			
			# list() makes a copy of keys so we can safely iterate even if a client disconnects mid-loop
			for sock in list(self.clients.keys()):
				
				# send to everyone except the excluded socket
				if sock != exclude:
					self._send(sock, msg_dict)

	########################################## CLIENT MANAGEMENT ##########################################
	
	# called when a new client (jetson) connects -> runs in its own thread
	# does the nickname handshake, registers client in our data structures
	def handle_new_client(self, client_socket, client_address):
		
		try:
			# ask the client for its name -> sends JSON: {"type": "nickname_request"}
			self._send(client_socket, {"type": "nickname_request"})
			
			# wait up to 30 sec for client to respond with its name
			resp = self._recv(client_socket, timeout=30)
			
			# if no response OR response isn't a nickname message -> reject and close
			if not resp or resp.get("type") != "nickname":
				client_socket.close()
				return

			# .get("name", default) -> like accessing a map with a fallback value
			# if client didn't send a name, use "Agent_<port_number>" as default
			name = resp.get("name", f"Agent_{client_address[1]}")

			# grab mutex -> modifying shared data structures
			with self.lock:
				# register this client -> store name + address, keyed by socket
				self.clients[client_socket] = {"name": name, "address": client_address}
				# add to turn order list so they get a turn in the experiment
				self.turn_order.append(client_socket)

			print(f"[+] {name} connected from {client_address}")
			
			# tell the client they're in
			self._send(client_socket, {
				"type": "welcome",
				"text": f"Welcome {name}. Waiting for all agents to connect...",
			})

		except Exception as e:
			print(f"[ERROR] Onboarding: {e}")
			# if anything goes wrong, clean up the socket
			try:
				client_socket.close()
			except OSError:
				pass

	########################################## EXPERIMENT LOGIC ##########################################
	
	# main experiment loop -> waits for agents, deals cards, manages turns, grades answers
	def run_experiment(self):
		
		print(f"\n[EXP] Waiting for {self.num_agents} agents to connect...")

		# busy-wait until enough agents have connected
		# checks every 1 second -> like polling in C with sleep(1)
		while self.running:
			with self.lock:
				if len(self.clients) >= self.num_agents:
					break
			time.sleep(1)

		# small delay so all clients are settled and ready
		time.sleep(2)

		# build nickname list in turn order
		nicknames = [self.clients[sock]["name"] for sock in self.turn_order]

		# generate figure sets -> get back common figure + dict of {nickname: [figures]}
		self.common_symbol, self.cards = generate_jetson_sets(nicknames, figures_per_card=self.figures_per_card)

		# print experiment info to server console (agents can't see this)
		print(f"\n{'=' * 55}")
		print(f"  EXPERIMENT STARTING")
		print(f"  Common figure: {self.common_symbol}")
		for sock in self.turn_order:
			name = self.clients[sock]["name"]
			print(f"  {name}'s card: {self.cards[name]}")
		print(f"{'=' * 55}\n")

		# send each agent ONLY their own card -> they don't see each other's
		for sock in self.turn_order:
			name = self.clients[sock]["name"]
			self._send(sock, {
				"type": "experiment_start",
				"your_symbols": self.cards[name],
				"num_agents": self.num_agents,
			})

		# start the clock
		self.start_time = time.time()
		turn_count = 0

		############ TURN LOOP -> round-robin, one agent talks at a time ############
		
		while self.running and turn_count < self.max_turns:
			
			# check if both agents have submitted answers -> if so, we're done
			with self.lock:
				if len(self.answers) >= self.num_agents:
					break

			# modulo (%) wraps around -> turn_index 0,1,2,3... maps to agent 0,1,0,1...
			current_sock = self.turn_order[self.turn_index % len(self.turn_order)]
			
			# look up speaker's name from the clients dict
			speaker = self.clients[current_sock]["name"]

			# if this agent already submitted an answer, skip their turn
			# "in" keyword checks if key exists in dict -> like map.find(key) != map.end()
			if speaker in self.answers:
				self.turn_index += 1
				turn_count += 1
				continue

			# tell the OTHER agent who we're waiting on
			self.broadcast(
				{"type": "system", "text": f"[Waiting for {speaker} to respond]"},
				exclude=current_sock,
			)

			# tell THIS agent it's their turn -> triggers the AI model on the jetson
			self._send(current_sock, {"type": "your_turn"})
			print(f"[TURN {turn_count + 1}] {speaker}'s turn...")

			# wait up to 120 sec for response -> model inference can be slow on jetson
			resp = self._recv(current_sock, timeout=120)

			# None = client disconnected -> bail out
			if resp is None:
				print(f"[ERROR] {speaker} disconnected.")
				break

			# agent took too long -> skip their turn
			if resp.get("type") == "timeout":
				print(f"[TIMEOUT] {speaker}")
				self.turn_index += 1
				turn_count += 1
				continue

			# ---- handle CHAT message -> agent is sharing info / discussing ----
			if resp.get("type") == "chat":
				text = resp.get("text", "").strip() # .strip() removes whitespace from edges
				if text:
					self.message_count += 1
					# log this message with turn number, who sent it, what they said, time elapsed
					self.conversation_log.append({
						"turn": turn_count + 1,
						"sender": speaker,
						"text": text,
						"elapsed": round(time.time() - self.start_time, 2),
					})
					# forward the message to the other agent (not back to sender)
					self.broadcast(
						{"type": "chat", "sender": speaker, "text": text},
						exclude=current_sock,
					)
					print(f"[{speaker}] {text}")

			# ---- handle ANSWER submission -> agent thinks they know the common symbol ----
			if resp.get("type") == "answer":
				symbol = resp.get("symbol", "").strip()
				# store in answers dict -> agent_name: symbol_they_guessed
				self.answers[speaker] = symbol
				print(f"[ANSWER] {speaker} submitted: '{symbol}'")
				# let the other agent know someone locked in
				self.broadcast(
					{"type": "system", "text": f"{speaker} has locked in an answer."},
					exclude=current_sock,
				)

			# next turn
			self.turn_index += 1
			turn_count += 1
			time.sleep(0.5) # small delay between turns for readability

		############ END TURN LOOP ############

		# ---- grade the answers ----
		self.end_time = time.time()
		elapsed = self.end_time - self.start_time

		# all() returns True if every element is True -> like looping and checking each one
		# .values() gets all values from dict -> the symbols each agent submitted
		all_correct = (
			len(self.answers) == self.num_agents
			and all(ans == self.common_symbol for ans in self.answers.values())
		)

		# build result dict -> sent to all agents + saved to log
		# "correct" if all_correct else "incorrect" -> ternary operator, like: all_correct ? "correct" : "incorrect"
		result = {
			"type": "experiment_end",
			"result": "correct" if all_correct else "incorrect",
			"common_symbol": self.common_symbol,
			"answers": self.answers,
			"time_seconds": round(elapsed, 2),
			"total_messages": self.message_count,
			"total_turns": turn_count,
		}

		# print results to server console
		print(f"\n{'=' * 55}")
		print(f"  EXPERIMENT COMPLETE")
		print(f"  Result:         {'CORRECT' if all_correct else 'INCORRECT'}")
		print(f"  Common symbol:  {self.common_symbol}")
		print(f"  Answers:        {self.answers}")
		print(f"  Time:           {elapsed:.2f}s")
		print(f"  Messages sent:  {self.message_count}")
		print(f"  Turns used:     {turn_count}")
		print(f"{'=' * 55}\n")

		# send results to all agents so they know the outcome
		self.broadcast(result)
		
		# save full conversation log to JSON file
		self._save_log(result)

	########################################## LOGGING ##########################################
	
	# private -> saves the full experiment data to a JSON file
	def _save_log(self, result):
		
		# build the complete log dict
		log = {
			"experiment": "leavitt_common_symbol",
			"num_agents": self.num_agents,
			"figures_per_card": self.figures_per_card,
			"common_symbol": self.common_symbol,
			# cards is already a dict of {nickname: [figures]} from generate_jetson_sets
			"cards": self.cards,
			"result": result,
			"conversation": self.conversation_log,
		}
		
		# filename includes unix timestamp so each run gets a unique file
		filename = f"leavitt_log_{int(time.time())}.json"
		
		# open file for writing -> "with" auto-closes the file when block ends (like RAII in C++)
		with open(filename, "w") as f:
			# json.dump() writes dict directly to file, indent=2 makes it human-readable
			json.dump(log, f, indent=2)
		
		print(f"[LOG] Saved to {filename}")

	########################################## SERVER START + ACCEPT LOOP ##########################################
	
	# main entry point -> binds socket, starts listening, kicks off the experiment
	def start(self):
		
		try:
			# bind to host:port -> like bind() in C
			self.server_socket.bind((self.host, self.port))
			
			# start listening for connections, queue up to 5 pending connections
			self.server_socket.listen(2)

			print(f"\n{'=' * 55}")
			print(f"  Leavitt Experiment Server")
			print(f"  Listening on {self.host}:{self.port}")
			print(f"  Waiting for {self.num_agents} agents...")
			print(f"  Figures per card: {self.figures_per_card}")
			print(f"  Max turns: {self.max_turns}")
			print(f"{'=' * 55}\n")

			# spawn a daemon thread that loops forever accepting new connections
			# daemon=True -> thread dies automatically when main program exits
			accept_thread = threading.Thread(target=self._accept_loop, daemon=True)
			accept_thread.start()

			# run the experiment in the MAIN thread (blocking)
			self.run_experiment()

		# Ctrl+C handler -> clean shutdown
		except KeyboardInterrupt:
			print("\n[SERVER] Shutting down...")
		
		except OSError as e:
			print(f"[SERVER ERROR] {e}")
		
		# finally ALWAYS runs -> cleanup, close all sockets no matter what happened
		finally:
			self.running = False
			# close every client socket
			for sock in list(self.clients.keys()):
				try:
					sock.close()
				except OSError:
					pass
			# close the server socket itself
			self.server_socket.close()
			print("[SERVER] Closed.")

	# private -> runs in its own thread, loops forever accepting new client connections
	# each new client gets its own thread via handle_new_client
	def _accept_loop(self):
		
		while self.running:
			try:
				# blocks here until a client connects -> returns (new_socket, address)
				client_socket, addr = self.server_socket.accept()
				
				# spawn a new thread to handle the handshake for this client
				# so accept_loop can immediately go back to waiting for more connections
				threading.Thread(
					target=self.handle_new_client,
					args=(client_socket, addr),
					daemon=True,
				).start()
			
			# OSError = server socket was closed -> time to stop
			except OSError:
				break


########################################## COMMAND LINE ENTRY POINT ##########################################

# __name__ == "__main__" -> only runs if this file is executed directly (not imported)
# equivalent to: int main(int argc, char* argv[])
if __name__ == "__main__":
	
	# need at least 3 args: script name, host, port
	if len(sys.argv) < 3:
		print("Usage: python leavitt_server.py <host> <port> [figures_per_card]")
		print("Example: python leavitt_server_2jetsons.py 0.0.0.0 5001 5")
		sys.exit(1)

	host = sys.argv[1] # first arg = host (e.g., "0.0.0.0")
	port = int(sys.argv[2]) # second arg = port, cast string to int

	# third arg is optional -> figures per card, defaults to 5
	fpc = int(sys.argv[3]) if len(sys.argv) >= 4 else DEFAULT_FIGURES_PER_CARD

	# create server object and start it
	server = LeavittServer(host=host, port=port, figures_per_card=fpc)
	server.start()