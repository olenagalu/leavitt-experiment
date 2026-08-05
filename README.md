# Replicating Bavelas-Leavitt Experiment with SLMs

This project replicates the Bavelas-Leavitt communication experiment using autonomous agents powered by locally hosted **Gemma 3 4B** language models. Instead of human participants exchanging information through different communication networks, the agents run with Ollama on **NVIDIA Jetson Nano Developer Kit units** and communicate through a TCP server on a local network.

Each trial gives agents private figure lists with exactly one figure shared by all participating agents. Agents communicate only with others allowed by the selected topology, compare received information with their own lists, and submit a final answer when they identify the common figure.

The project studies how communication structure affects:
* Success rate
* Number of messages
* Time required to reach an answer
* Agent coordination
* Information flow

Broadcast trials can use 2-5 agents. The circle, chain, Y, and wheel topologies are configured for five Jetson agents.

The models run locally and do not require internet access during the experiment.

## Public Demo

[Open the interactive Leavitt Experiment demo](https://minds-leavitt-demo.netlify.app/)

The public demo reproduces the current dashboard with simulated Jetson agents, topology-based message routing, conversations, and trial results. It does not connect to the private Jetson network or expose live experiment data.

## Supported Topologies

* 🌐 **Broadcast** - every agent can communicate with every other agent.
* ⭕ **Circle** - each agent communicates with two adjacent agents.
* ⛓️ **Chain** - agents communicate through a linear network.
* 🔀 **Y Structure** - agents communicate through a branching structure.
* 🎡 **Wheel** - one central agent communicates with all other agents.

Each topology restricts how information can move between agents, allowing their efficiency and accuracy to be compared.

## Project Structure

The experiment is implemented as a local multi-agent system. A Python dashboard server coordinates trials, assigns private figure lists, routes messages according to the selected topology, and records trial results. Each Jetson runs a client connected to the server over TCP. The client sends prompts to a locally hosted Gemma 3 4B model through Ollama and returns the generated message or final answer to the server.

```text
Private figure lists
        ↓
Gemma 3 4B agents on Jetsons
        ↓
Jetson client
        ↓
TCP experiment server
        ↓
Topology-based message routing
        ↓
Dashboard, results, and statistics
```

```text
Coordination_LLM/
├── Main/
│   ├── client.py
│   ├── circle_client.py
│   ├── chain_client.py
│   ├── y_client.py
│   ├── wheel_client.py
│   └── shared_features_client.py
│
├── Site/
│   ├── dashboard_server.py
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   └── minds-logo.png
│
├── notes.txt
└── README.md
```

### `Main/`

Contains the Jetson client entry point, topology-specific client logic, and shared prompt helpers.

`Main/client.py` is the main client file executed on each Jetson. It connects to the TCP server, receives trial instructions, calls the local Gemma 3 4B model through Ollama, and sends messages or final answers back to the server.

`shared_features_client.py` contains shared prompt sections used by the private-message topology clients. It defines common prompt content such as the experiment setup, agent state, recent message history, answer rules, and output format. This helps control what information agents see and how their responses are structured.

`circle_client.py`, `chain_client.py`, `y_client.py`, and `wheel_client.py` add topology-specific prompts and helper code for each communication structure.

### `Site/`

Contains the live dashboard and experiment server.

`Site/dashboard_server.py` serves the web interface and manages TCP communication with the Jetsons.

### `notes.txt`

Contains short setup and operating notes for the local experiment environment.

The system is designed to run on a local network without requiring internet access during trials.

## Metrics Collected

The experiment records:

* Trial number
* Selected topology
* Correct common figure
* Agent answers
* Success or failure
* Total messages
* Trial duration
* Temperature
