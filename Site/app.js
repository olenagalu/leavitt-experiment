const fallbackAgents = [
  { id: 1, name: "Agent1", hostname: "jetson1", symbols: ["square", "circle", "cross"], color: "#4098d0" },
  { id: 2, name: "Agent2", hostname: "jetson2", symbols: ["circle", "diamond", "asterisk"], color: "#62c6bf" },
  { id: 3, name: "Agent3", hostname: "jetson3", symbols: ["circle", "triangle", "cross"], color: "#ef6077" },
  { id: 4, name: "Agent4", hostname: "jetson4", symbols: ["circle", "square", "diamond"], color: "#ad70b3" },
  { id: 5, name: "Agent5", hostname: "jetson5", symbols: ["circle", "triangle", "asterisk"], color: "#f3bd59" },
];

const symbolMarks = {
  square: "□",
  circle: "○",
  triangle: "△",
  diamond: "◇",
  cross: "×",
  asterisk: "*",
};

const demoMessages = [
  "I have circle, square, and cross.",
  "Circle overlaps with my list.",
  "Passing circle forward as the strongest candidate.",
  "I can confirm circle.",
  "Final answer should be circle.",
];

const topologyMeta = {
  broadcast: {
    label: "Broadcast mode",
    description: "The server sends each chat message to all selected active Jetsons, matching the console broadcast topology.",
  },
  circle: {
    label: "Circle mode",
    description: "Each Jetson sends private messages only to its two circle neighbors.",
    fixedAgents: 5,
  },
  chain: {
    label: "Chain mode",
    description: "Jetsons communicate along a line: Agent1 through Agent5, with only adjacent contacts.",
    fixedAgents: 5,
  },
  y: {
    label: "Y topology",
    description: "Agent3 is the junction, Agent4 bridges to Agent5, and endpoints can only use their branch contact.",
    fixedAgents: 5,
  },
  wheel: {
    label: "Wheel mode",
    description: "Agent5 is the central hub. Other Jetsons send through Agent5.",
    fixedAgents: 5,
  },
};

const topologyLinks = {
  circle: [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]],
  chain: [[1, 2], [2, 3], [3, 4], [4, 5]],
  y: [[1, 3], [2, 3], [3, 4], [4, 5]],
  wheel: [[1, 5], [2, 5], [3, 5], [4, 5]],
};

const defaultOllamaOptions = {
  temperature: 0.2,
  top_p: 0.7,
  repeat_penalty: 1.2,
  num_predict: 77,
};
const defaultMaxMessages = 50;

const state = {
  source: "live",
  mode: "circle",
  agentCount: 5,
  agents: fallbackAgents,
  activeIndex: 0,
  messageCount: 0,
  round: 1,
  playing: true,
  pulse: 0,
  lastRoute: null,
  liveConnected: false,
  liveSnapshot: null,
  eventSource: null,
  autoTrials: false,
  ollamaOptions: { ...defaultOllamaOptions },
  maxMessages: defaultMaxMessages,
  chatHistories: {},
};

const canvas = document.querySelector("#networkCanvas");
const ctx = canvas.getContext("2d");
const networkStage = document.querySelector(".network-stage");
const stageOverlayText = document.querySelector("#stageOverlayText");
const agentLayer = document.querySelector("#agentLayer");
const sourceButtons = [...document.querySelectorAll("[data-source]")];
const modeButtons = [...document.querySelectorAll("[data-mode]")];
const agentCount = document.querySelector("#agentCount");
const agentCountGroup = agentCount.closest(".control-group");
const agentCountValue = document.querySelector("#agentCountValue");
const ollamaTemperature = document.querySelector("#ollamaTemperature");
const ollamaTopP = document.querySelector("#ollamaTopP");
const ollamaRepeatPenalty = document.querySelector("#ollamaRepeatPenalty");
const ollamaNumPredict = document.querySelector("#ollamaNumPredict");
const maxMessages = document.querySelector("#maxMessages");
const connectionStatus = document.querySelector("#connectionStatus");
const statusPill = document.querySelector(".status-pill");
const sourceLabel = document.querySelector("#sourceLabel");
const modeTitle = document.querySelector("#modeTitle");
const modeDescription = document.querySelector("#modeDescription");
const routeText = document.querySelector("#routeText");
const currentMessageText = document.querySelector("#currentMessageText");
const chatPanel = document.querySelector("#chatPanel");
const chatGrid = document.querySelector("#chatGrid");
const messageMetric = document.querySelector("#messageMetric");
const symbolMetric = document.querySelector("#symbolMetric");
const eventFeed = document.querySelector("#eventFeed");
const eventFeedResizeHandle = document.querySelector("#eventFeedResizeHandle");
const workspace = document.querySelector(".workspace");
const stageColumn = document.querySelector(".stage-column");
const infoPanel = document.querySelector("#infoPanel");
const panelResizeHandle = document.querySelector("#panelResizeHandle");
const stageResizeHandle = document.querySelector("#stageResizeHandle");
const playPause = document.querySelector("#playPause");
const stepButton = document.querySelector("#stepButton");
const clearFeed = document.querySelector("#clearFeed");
const startTrial = document.querySelector("#startTrial");
const stopTrial = document.querySelector("#stopTrial");
const autoTrials = document.querySelector("#autoTrials");
const restartClients = document.querySelector("#restartClients");
const clearResults = document.querySelector("#clearResults");
const resultsBody = document.querySelector("#resultsBody");
const demoControls = document.querySelector(".demo-controls");
const liveControls = document.querySelector(".live-controls");

function agentId(agent) {
  const match = String(agent.name || "").match(/\d+/);
  return match ? Number(match[0]) : 999;
}

function visibleAgents() {
  if (state.source === "live" && state.liveSnapshot) {
    const connected = state.liveSnapshot.connected || [];
    const fallbackCount = state.liveSnapshot.numAgents || state.agentCount;
    const liveAgents = connected.length ? connected : fallbackAgents.slice(0, fallbackCount);
    return liveAgents.map((agent, index) => ({
      ...fallbackAgents[index],
      ...agent,
      id: agentId(agent),
      color: fallbackAgents[index]?.color || "#62c6bf",
      symbols: agent.symbols?.length ? agent.symbols : [],
    })).sort((a, b) => agentId(a) - agentId(b));
  }
  return fallbackAgents.slice(0, state.agentCount);
}

function resizeCanvas() {
  const rect = canvas.getBoundingClientRect();
  const scale = window.devicePixelRatio || 1;
  canvas.width = Math.round(rect.width * scale);
  canvas.height = Math.round(rect.height * scale);
  ctx.setTransform(scale, 0, 0, scale, 0, 0);
  draw();
  renderAgents();
}

function getPositions() {
  const rect = canvas.getBoundingClientRect();
  const width = rect.width;
  const height = rect.height;
  const snapshotLocked = Boolean(state.liveSnapshot?.trialActive || state.liveSnapshot?.trialRequested);
  const topology = state.source === "live" && snapshotLocked ? state.liveSnapshot.topology : state.mode;
  const list = visibleAgents();
  if (["chain", "y", "wheel"].includes(topology)) {
    const layouts = {
      chain: {
        1: [0.13, 0.5],
        2: [0.31, 0.5],
        3: [0.5, 0.5],
        4: [0.69, 0.5],
        5: [0.87, 0.5],
      },
      y: {
        1: [0.27, 0.25],
        2: [0.27, 0.75],
        3: [0.5, 0.5],
        4: [0.69, 0.5],
        5: [0.87, 0.5],
      },
      wheel: {
        1: [0.28, 0.24],
        2: [0.28, 0.76],
        3: [0.72, 0.24],
        4: [0.72, 0.76],
        5: [0.5, 0.5],
      },
    };
    return list.map((agent) => {
      const [xRatio, yRatio] = layouts[topology][agent.id] || [0.5, 0.5];
      return { ...agent, x: width * xRatio, y: height * yRatio };
    });
  }
  const centerX = width / 2;
  const centerY = height / 2 - 16;
  const radius = Math.min(width, height) * (width < 700 ? 0.31 : 0.34);

  return list.map((agent, index) => {
    const angle = -Math.PI / 2 + (index / Math.max(list.length, 1)) * Math.PI * 2;
    return {
      ...agent,
      x: centerX + Math.cos(angle) * radius,
      y: centerY + Math.sin(angle) * radius,
    };
  });
}

function drawLine(from, to, color, width = 2, alpha = 1) {
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.strokeStyle = color;
  ctx.lineWidth = width;
  ctx.lineCap = "round";
  ctx.beginPath();
  ctx.moveTo(from.x, from.y);
  ctx.lineTo(to.x, to.y);
  ctx.stroke();
  ctx.restore();
}

function drawPacket(from, to, color, offset) {
  const x = from.x + (to.x - from.x) * offset;
  const y = from.y + (to.y - from.y) * offset;
  ctx.save();
  ctx.fillStyle = color;
  ctx.shadowColor = color;
  ctx.shadowBlur = 18;
  ctx.beginPath();
  ctx.arc(x, y, 7, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
}

function getAgentByName(positions, name) {
  return positions.find((agent) => agent.name === name);
}

function getAgentById(positions, id) {
  return positions.find((agent) => agent.id === id);
}

function drawTopologyLinks(positions, topology) {
  const links = topologyLinks[topology] || [];
  links.forEach(([fromId, toId]) => {
    const from = getAgentById(positions, fromId);
    const to = getAgentById(positions, toId);
    if (from && to) {
      drawLine(from, to, topology === "circle" ? "#f3bd59" : "#62c6bf", 3, 0.66);
    }
  });
}

function receiverNames(route, positions) {
  if (!route?.receiver || route.receiver === "ALL") {
    return positions.filter((agent) => agent.name !== route?.sender).map((agent) => agent.name);
  }
  return String(route.receiver)
    .split(",")
    .map((name) => name.trim())
    .filter(Boolean);
}

function shortestPathNames(fromName, toName, positions, topology) {
  if (topology === "broadcast") {
    return [fromName, toName];
  }

  const byId = new Map(positions.map((agent) => [agent.id, agent.name]));
  const byName = new Map(positions.map((agent) => [agent.name, agent.id]));
  const startId = byName.get(fromName);
  const targetId = byName.get(toName);
  const links = topologyLinks[topology] || [];

  if (!startId || !targetId || !links.length) {
    return [fromName, toName];
  }

  const graph = new Map(positions.map((agent) => [agent.id, []]));
  links.forEach(([fromId, toId]) => {
    if (graph.has(fromId) && graph.has(toId)) {
      graph.get(fromId).push(toId);
      graph.get(toId).push(fromId);
    }
  });

  const queue = [[startId]];
  const seen = new Set([startId]);
  while (queue.length) {
    const path = queue.shift();
    const last = path[path.length - 1];
    if (last === targetId) {
      return path.map((id) => byId.get(id)).filter(Boolean);
    }
    (graph.get(last) || []).forEach((nextId) => {
      if (!seen.has(nextId)) {
        seen.add(nextId);
        queue.push([...path, nextId]);
      }
    });
  }

  return [fromName, toName];
}

function drawPacketPath(path, color, offset) {
  if (path.length < 2) {
    return;
  }

  const segments = [];
  let totalLength = 0;
  for (let index = 0; index < path.length - 1; index += 1) {
    const from = path[index];
    const to = path[index + 1];
    const length = Math.hypot(to.x - from.x, to.y - from.y);
    totalLength += length;
    segments.push({ from, to, length });
  }

  let distance = offset * totalLength;
  for (const segment of segments) {
    if (distance <= segment.length || segment === segments[segments.length - 1]) {
      const segmentOffset = segment.length ? distance / segment.length : 0;
      drawPacket(segment.from, segment.to, color, Math.max(0, Math.min(1, segmentOffset)));
      return;
    }
    distance -= segment.length;
  }
}

function draw() {
  const rect = canvas.getBoundingClientRect();
  ctx.clearRect(0, 0, rect.width, rect.height);
  const positions = getPositions();
  if (!positions.length) {
    return;
  }

  const offset = state.pulse;
  const active = state.lastRoute
    ? getAgentByName(positions, state.lastRoute.sender) || positions[state.activeIndex % positions.length]
    : positions[state.activeIndex % positions.length];
  const snapshotLocked = Boolean(state.liveSnapshot?.trialActive || state.liveSnapshot?.trialRequested);
  const topology = state.source === "live" && snapshotLocked ? state.liveSnapshot.topology : state.mode;

  if (topology === "broadcast") {
    positions.forEach((from, index) => {
      positions.forEach((to, targetIndex) => {
        if (index < targetIndex) {
          drawLine(from, to, "#62c6bf", 1.5, 0.18);
        }
      });
    });
    const targetNames = state.lastRoute
      ? receiverNames(state.lastRoute, positions)
      : positions.filter((agent) => agent.name !== active.name).map((agent) => agent.name);
    targetNames
      .map((name) => getAgentByName(positions, name))
      .filter(Boolean)
      .forEach((to) => {
      if (to.name !== active.name) {
        drawLine(active, to, "#62c6bf", 3, 0.84);
        if (state.lastRoute) {
          drawPacket(active, to, "#ef6077", offset);
        }
      }
    });
    return;
  }

  drawTopologyLinks(positions, topology);
  const receivers = state.lastRoute
    ? receiverNames(state.lastRoute, positions)
    : getTopologyReceivers(active, topology).map((agent) => agent.name);
  const targets = receivers
    .map((name) => getAgentByName(positions, name))
    .filter(Boolean);
  const fallbackTarget = positions[(positions.indexOf(active) + 1) % positions.length];
  (targets.length ? targets : [fallbackTarget]).forEach((target) => {
    if (!target || target.name === active.name) {
      return;
    }
    const path = shortestPathNames(active.name, target.name, positions, topology)
      .map((name) => getAgentByName(positions, name))
      .filter(Boolean);
    for (let index = 0; index < path.length - 1; index += 1) {
      drawLine(path[index], path[index + 1], "#ef6077", 4, 0.92);
    }
    if (state.lastRoute) {
      drawPacketPath(path, "#ef6077", offset);
    }
  });
}

function getTopologyReceivers(sender, mode = state.mode) {
  const list = visibleAgents();
  if (mode === "broadcast") {
    return list.filter((agent) => agent.name !== sender.name);
  }
  if (mode === "circle") {
    const index = list.findIndex((agent) => agent.name === sender.name);
    return [list[(index + 1) % list.length]].filter(Boolean);
  }
  const links = topologyLinks[mode] || [];
  const contactIds = links
    .filter(([from, to]) => from === sender.id || to === sender.id)
    .map(([from, to]) => (from === sender.id ? to : from));
  return contactIds.map((id) => list.find((agent) => agent.id === id)).filter(Boolean);
}

function renderAgents() {
  const positions = getPositions();
  const activeName = state.lastRoute?.sender || state.liveSnapshot?.currentSpeaker;
  const receiverSet = new Set(state.lastRoute ? receiverNames(state.lastRoute, positions) : []);

  agentLayer.innerHTML = positions.map((agent) => {
    const classes = [
      "agent-node",
      agent.name === activeName ? "sender" : "",
      receiverSet.has(agent.name) ? "receiver" : "",
    ].filter(Boolean).join(" ");

    const symbols = (agent.symbols || []).length
      ? agent.symbols.map((symbol) => `<span class="symbol" title="${symbol}">${symbolMarks[symbol] || "?"}</span>`).join("")
      : `<span class="symbol" title="hidden">?</span>`;
    const note = agent.name === activeName ? "speaking now" : agent.hostname || "waiting";

    return `
      <article class="${classes}" style="left:${agent.x}px; top:${agent.y}px">
        <div class="agent-name">
          <span>${escapeHtml(agent.name)}</span>
          <i class="chip" style="background:${agent.color}"></i>
        </div>
        <div class="symbols">${symbols}</div>
        <div class="agent-note">${escapeHtml(note)}</div>
      </article>
    `;
  }).join("");
}

function getDemoReceivers(sender) {
  return getTopologyReceivers(sender);
}

function colorForAgent(name) {
  const id = agentId({ name });
  return fallbackAgents.find((agent) => agent.id === id)?.color || "#62c6bf";
}

function parseReceiverList(route, agents) {
  if (!route?.receiver || route.receiver === "ALL") {
    return agents.filter((agent) => agent.name !== route?.sender).map((agent) => agent.name);
  }
  return String(route.receiver).split(",").map((name) => name.trim()).filter(Boolean);
}

function routeLabel(route) {
  const sender = route?.sender || "?";
  const receiver = route?.receiver || route?.target || "?";
  return `${sender} -> ${receiver}`;
}

function resetChatHistories() {
  state.chatHistories = {};
  visibleAgents().forEach((agent) => {
    state.chatHistories[agent.name] = [];
  });
}

function recordChat(route) {
  const agents = visibleAgents();
  const viewers = new Set([route.sender, ...parseReceiverList(route, agents)]);
  viewers.forEach((name) => {
    if (!state.chatHistories[name]) {
      state.chatHistories[name] = [];
    }
    state.chatHistories[name].push({
      sender: route.sender,
      receiver: route.receiver,
      message: route.message || "",
      round: route.round,
    });
    state.chatHistories[name] = state.chatHistories[name].slice(-8);
  });
}

function renderChats(topology) {
  if (topology === "broadcast") {
    chatPanel.hidden = true;
    chatGrid.innerHTML = "";
    return;
  }
  chatPanel.hidden = false;
  const agents = visibleAgents();
  chatGrid.innerHTML = agents.map((agent) => {
    const history = state.chatHistories[agent.name] || [];
    const rows = history.length
      ? history.map((entry) => {
        return `<p><b>${escapeHtml(routeLabel(entry))}:</b> ${escapeHtml(entry.message)}</p>`;
      }).join("")
      : `<p>No private messages yet.</p>`;
    return `
      <article class="chat-card" style="--agent-color:${agent.color}">
        <strong>${escapeHtml(agent.name)} sees</strong>
        ${rows}
      </article>
    `;
  }).join("");
}

function syncModeButtons(activeTopology) {
  modeButtons.forEach((button) => {
    const active = button.dataset.mode === activeTopology;
    button.classList.toggle("active", active);
    button.setAttribute("aria-selected", String(active));
  });
}

function updateCopy() {
  const snapshot = state.liveSnapshot;
  const trialLocked = Boolean(snapshot?.trialActive || snapshot?.trialRequested);
  const topology = state.source === "live" && trialLocked ? snapshot.topology : state.mode;
  const meta = topologyMeta[topology] || topologyMeta.broadcast;
  const agents = visibleAgents();
  const route = state.lastRoute;
  const neededAgents = topologyMeta[topology]?.fixedAgents || state.agentCount;
  const connectedAgents = snapshot?.connected?.length || 0;
  const waitingForAgents = state.source === "live" && connectedAgents < neededAgents;

  sourceLabel.textContent = state.source === "live" ? "Live Jetsons" : "Demo animation";
  modeTitle.textContent = meta.label;
  modeDescription.textContent = `SLM stands for small language model: a compact AI model running locally on each Jetson to read messages and choose a response. ${meta.description}`;
  syncModeButtons(topology);

  if (route) {
    const label = routeLabel(route);
    routeText.textContent = label;
    currentMessageText.innerHTML = route.message
      ? `<span class="message-sender">${escapeHtml(label)}:</span> <span class="message-body">${escapeHtml(route.message)}</span>`
      : "No message text.";
  } else if (state.source === "live") {
    routeText.textContent = waitingForAgents
      ? "Waiting for all agents to connect..."
      : (snapshot?.trialActive ? "Waiting for next message" : "No live trial running");
    currentMessageText.innerHTML = snapshot?.trialActive ? "Waiting for next message..." : "No message yet.";
  } else {
    const sender = agents[state.activeIndex % agents.length];
    const receivers = getDemoReceivers(sender);
    routeText.textContent = topology === "broadcast"
      ? `${sender.name} -> ALL`
      : `${sender.name} -> ${receivers.map((agent) => agent.name).join(", ")}`;
    currentMessageText.innerHTML = "No message yet.";
  }

  const liveCount = snapshot?.connected?.length || 0;
  if (state.liveConnected || snapshot) {
    connectionStatus.textContent = `${liveCount} Jetson${liveCount === 1 ? "" : "s"} connected`;
    statusPill.classList.toggle("connected", liveCount >= 5);
    statusPill.classList.toggle("partial", liveCount < 5);
    statusPill.classList.toggle("offline", false);
  } else if (window.location.protocol === "file:") {
    connectionStatus.textContent = "Open http://server:5173";
    statusPill.classList.toggle("connected", false);
    statusPill.classList.toggle("partial", false);
    statusPill.classList.toggle("offline", true);
  } else {
    connectionStatus.textContent = "Live server offline";
    statusPill.classList.toggle("connected", false);
    statusPill.classList.toggle("partial", false);
    statusPill.classList.toggle("offline", true);
  }
  agentCountValue.textContent = state.agentCount;
  messageMetric.textContent = snapshot?.messages ?? state.messageCount;
  symbolMetric.textContent = snapshot?.commonSymbol || (state.messageCount >= Math.max(3, state.agentCount) ? "circle" : "?");
  agentCountGroup.hidden = topology !== "broadcast";
  const fixedFiveMode = ["circle", "chain", "y", "wheel"].includes(topology);
  const lacksRequiredJetsons = state.source === "live" && fixedFiveMode && liveCount < 5;
  renderChats(topology);
  modeButtons.forEach((button) => {
    button.disabled = trialLocked;
  });
  agentCount.disabled = trialLocked;
  ollamaTemperature.disabled = trialLocked;
  ollamaTopP.disabled = trialLocked;
  ollamaRepeatPenalty.disabled = trialLocked;
  ollamaNumPredict.disabled = trialLocked;
  maxMessages.disabled = trialLocked;
  if (trialLocked && snapshot?.maxMessages) {
    maxMessages.value = String(snapshot.maxMessages);
    state.maxMessages = snapshot.maxMessages;
  }
  startTrial.disabled = state.source !== "live" || trialLocked || lacksRequiredJetsons;
  startTrial.title = lacksRequiredJetsons ? "Circle, chain, Y, and wheel require all 5 Jetsons connected." : "";
  stopTrial.disabled = state.source !== "live" || !trialLocked;
  restartClients.disabled = state.source !== "live" || trialLocked;
  clearFeed.disabled = trialLocked;
  clearResults.disabled = trialLocked;
  autoTrials.setAttribute("aria-pressed", String(Boolean(snapshot?.autoTrials || state.autoTrials)));
  autoTrials.textContent = snapshot?.autoTrials || state.autoTrials ? "Stop auto" : "Auto trials";
  autoTrials.disabled = trialLocked;
  updateStageOverlay(snapshot);
  renderResults(snapshot?.results || []);
}

function updateStageOverlay(snapshot) {
  const trialRunning = Boolean(snapshot?.trialActive || snapshot?.trialRequested);
  const latestResult = snapshot?.results?.length ? snapshot.results[snapshot.results.length - 1] : null;

  if (trialRunning) {
    networkStage.classList.remove("is-blurred");
    stageOverlayText.textContent = "";
    return;
  }

  networkStage.classList.add("is-blurred");
  if (!latestResult) {
    stageOverlayText.textContent = "Start Trial";
  } else if (latestResult.stopped || latestResult.result === "stopped") {
    stageOverlayText.textContent = "Trial Ended (Stopped)";
  } else {
    stageOverlayText.textContent = latestResult.success ? "Trial Ended (Success)" : "Trial Ended (Fail)";
  }
}

function insertFeedItem(item) {
  eventFeed.prepend(item);
}

function addEvent(kind, title, text, topology = state.mode, sender = null) {
  const item = document.createElement("li");
  item.className = [
    topology !== "broadcast" ? "circle-event" : "",
    kind === "system" ? "system-event" : "",
  ].filter(Boolean).join(" ");
  if (sender) {
    item.style.setProperty("--event-color", colorForAgent(sender));
  }
  item.innerHTML = `<strong>${escapeHtml(title)}</strong><span>${escapeHtml(text)}</span>`;
  insertFeedItem(item);
  eventFeed.scrollTop = 0;

  while (eventFeed.children.length > 80) {
    eventFeed.lastElementChild.remove();
  }
}

function demoStep() {
  if (state.source !== "demo") {
    return;
  }
  const list = visibleAgents();
  const sender = list[state.activeIndex % list.length];
  const receivers = getDemoReceivers(sender);
  const receiverText = state.mode === "broadcast" ? "ALL" : receivers.map((agent) => agent.name).join(", ");
  const text = demoMessages[state.messageCount % demoMessages.length];

  state.lastRoute = { sender: sender.name, receiver: receiverText, topology: state.mode, message: text, round: state.round };
  state.pulse = 0;
  state.messageCount += 1;
  state.round = Math.floor((state.messageCount - 1) / state.agentCount) + 1;
  state.lastRoute.round = state.round;
  recordChat(state.lastRoute);
  addEvent("chat", routeLabel(state.lastRoute), text, state.mode, sender.name);
  state.activeIndex = (state.activeIndex + 1) % state.agentCount;

  updateCopy();
  renderAgents();
  draw();
}

function setMode(mode) {
  if (state.liveSnapshot?.trialActive || state.liveSnapshot?.trialRequested) {
    return;
  }
  state.mode = mode;
  if (topologyMeta[mode]?.fixedAgents) {
    state.agentCount = topologyMeta[mode].fixedAgents;
    agentCount.value = String(state.agentCount);
  }
  if (state.source === "demo") {
    resetDemo();
  }
  resetChatHistories();
  syncModeButtons(mode);
  updateCopy();
  renderAgents();
  draw();
}

function setSource(source) {
  state.source = source;
  sourceButtons.forEach((button) => {
    const active = button.dataset.source === source;
    button.classList.toggle("active", active);
    button.setAttribute("aria-selected", String(active));
  });
  demoControls.hidden = source !== "demo";
  liveControls.hidden = source !== "live";
  eventFeed.innerHTML = "";
  resetChatHistories();
  state.lastRoute = null;

  if (source === "live") {
    connectLive();
    fetchState();
  } else {
    resetDemo();
  }
  updateCopy();
  renderAgents();
  draw();
}

function resetDemo() {
  state.activeIndex = 0;
  state.messageCount = 0;
  state.round = 1;
  state.lastRoute = null;
  eventFeed.innerHTML = "";
  resetChatHistories();
}

function connectLive() {
  if (window.location.protocol === "file:") {
    state.liveConnected = false;
    updateCopy();
    return;
  }
  if (state.eventSource) {
    return;
  }
  const events = new EventSource("/api/events");
  state.eventSource = events;
  events.onopen = () => {
    state.liveConnected = true;
    updateCopy();
  };
  events.onerror = () => {
    state.liveConnected = false;
    updateCopy();
  };
  events.onmessage = (message) => {
    const event = JSON.parse(message.data);
    state.liveSnapshot = event.snapshot;
    handleLiveEvent(event);
    updateCopy();
    renderAgents();
    draw();
  };
}

async function fetchState() {
  if (window.location.protocol === "file:") {
    state.liveConnected = false;
    updateCopy();
    return;
  }
  try {
    const response = await fetch("/api/state");
    state.liveSnapshot = await response.json();
    updateCopy();
    renderAgents();
    draw();
  } catch {
    state.liveConnected = false;
    updateCopy();
  }
}

function handleLiveEvent(event) {
  const payload = event.payload || {};
  if (event.kind === "chat") {
    state.lastRoute = payload;
    state.pulse = 0;
    recordChat(payload);
    addEvent("chat", routeLabel(payload), payload.message || "", payload.topology, payload.sender);
  } else if (event.kind === "trial_started") {
    state.lastRoute = null;
    eventFeed.innerHTML = "";
    resetChatHistories();
  } else if (event.kind === "turn_started") {
    return;
  } else if (event.kind === "answer") {
    addEvent("system", `${payload.speaker} answered`, payload.word || "", state.mode, payload.speaker);
  } else if (event.kind === "invalid_output") {
    addEvent("error", `${payload.speaker} output skipped`, payload.reason || "Invalid format.", state.mode, payload.speaker);
  } else if (event.kind === "invalid_route") {
    const target = payload.target ? `Invalid target: ${payload.target}` : "Missing or invalid target";
    addEvent("error", `${payload.sender} message skipped`, target, payload.topology || state.mode, payload.sender);
  } else if (event.kind === "timeout") {
    addEvent("error", `${payload.speaker} timed out`, "No response received.", state.mode, payload.speaker);
  } else if (event.kind === "trial_finished") {
    return;
  } else if (event.kind === "client_joined") {
    const label = payload.reloaded ? "reconnected after reload" : "connected";
    addEvent("system", `${payload.agent} ${label}`, payload.hostname || "", state.mode, payload.agent);
  } else if (event.kind === "client_left") {
    addEvent("error", `${payload.agent} disconnected`, payload.reason || "", state.mode, payload.agent);
  } else if (event.kind === "waiting") {
    const missing = payload.missing?.length ? ` Missing: ${payload.missing.join(", ")}` : "";
    addEvent("system", "Waiting for Jetsons", `${payload.selected}/${payload.needed} connected.${missing}`, state.mode);
  } else if (event.kind === "server") {
    addEvent("system", "Server", payload.message || "", state.mode);
  } else if (event.kind === "clients_reload_started") {
    const agents = payload.agents?.length ? payload.agents.join(", ") : "none";
    addEvent("system", "Reload started", `${payload.count || 0} connected Jetson(s): ${agents}`, state.mode);
  } else if (event.kind === "client_reload_requested") {
    addEvent("system", `${payload.agent} reload requested`, payload.hostname || "", state.mode, payload.agent);
  } else if (event.kind === "client_reload_command_sent") {
    addEvent("system", `${payload.agent} reload command sent`, "Waiting for disconnect and reconnect.", state.mode, payload.agent);
  } else if (event.kind === "client_reload_command_failed") {
    const reason = payload.reason ? `${payload.hostname || ""}: ${payload.reason}` : (payload.hostname || "");
    addEvent("error", `${payload.agent} reload command failed`, reason, state.mode, payload.agent);
  } else if (event.kind === "clients_reload_commands_finished") {
    const pending = payload.pending?.length ? ` Waiting for: ${payload.pending.join(", ")}` : " No reconnects pending.";
    addEvent("system", "Reload commands done", `${payload.sent}/${payload.requested} sent.${pending}`, state.mode);
  } else if (event.kind === "client_reload_completed") {
    const pending = payload.pending?.length ? `Still waiting for: ${payload.pending.join(", ")}` : "No agents pending.";
    addEvent("system", `${payload.agent} reload complete`, pending, state.mode, payload.agent);
  } else if (event.kind === "clients_reload_finished") {
    addEvent("system", "Reload complete", payload.message || "", state.mode);
  }
}

function renderResults(results) {
  const activeTopology = state.source === "live" && (state.liveSnapshot?.trialActive || state.liveSnapshot?.trialRequested)
    ? state.liveSnapshot.topology
    : state.mode;
  const topology = topologyMeta[activeTopology]?.label || activeTopology || "-";
  const topologyRow = `<tr><td><strong>Topology</strong></td><td colspan="6">${escapeHtml(topology)}</td></tr>`;

  if (!results.length) {
    resultsBody.innerHTML = `${topologyRow}<tr><td colspan="7">No live trials yet.</td></tr>`;
    return;
  }
  const resultRows = [...results].reverse().map((result) => {
    const resultClass = result.success ? "result-good" : "result-bad";
    const resultText = result.success ? "Success" : "Fail";
    const submittedFigure = resultSubmittedFigureText(result);
    const correctFigure = resultCorrectFigureText(result);
    return `
      <tr>
        <td>${result.trial_id ?? "-"}</td>
        <td><span class="${resultClass}">${resultText}</span></td>
        <td>${escapeHtml(submittedFigure)}</td>
        <td>${escapeHtml(correctFigure)}</td>
        <td>${result.temperature ?? result.ollama_options?.temperature ?? "-"}</td>
        <td>${result.total_messages ?? "-"}</td>
        <td>${result.time_seconds ?? "-"}s</td>
      </tr>
    `;
  }).join("");
  resultsBody.innerHTML = `${topologyRow}${resultRows}`;
}

function resultSubmittedFigureText(result) {
  const submitted = result.submitted_answer
    || result.final_answer_word
    || latestAnswerValue(result.answers);
  if (submitted) {
    return figureDisplayText(submitted);
  }
  if (result.submitted_figure_status) {
    return result.submitted_figure_status;
  }
  if (result.stopped || result.result === "stopped") {
    return "Trial stopped";
  }
  if (result.max_messages_reached) {
    return "No figure submitted (message limit reached)";
  }
  return "No figure submitted";
}

function resultCorrectFigureText(result) {
  const correct = result.correct_answer
    || result.common_word
    || result.commonSymbol;
  return correct ? figureDisplayText(correct) : "-";
}

function latestAnswerValue(answers) {
  if (!answers || typeof answers !== "object") {
    return "";
  }
  const values = Object.values(answers).filter(Boolean);
  return values.length ? values[values.length - 1] : "";
}

function figureDisplayText(value) {
  return String(value ?? "").trim();
}

function numberFromInput(input, fallback, min, max, integer = false) {
  const value = Number(input.value);
  const nextValue = Number.isFinite(value) ? Math.max(min, Math.min(max, value)) : fallback;
  const normalized = integer ? Math.round(nextValue) : Number(nextValue.toFixed(3));
  input.value = String(normalized);
  return normalized;
}

function getOllamaOptions() {
  state.ollamaOptions = {
    temperature: numberFromInput(ollamaTemperature, defaultOllamaOptions.temperature, 0, 2),
    top_p: numberFromInput(ollamaTopP, defaultOllamaOptions.top_p, 0, 1),
    repeat_penalty: numberFromInput(ollamaRepeatPenalty, defaultOllamaOptions.repeat_penalty, 0, 3),
    num_predict: numberFromInput(ollamaNumPredict, defaultOllamaOptions.num_predict, 1, 300, true),
  };
  return state.ollamaOptions;
}

function getMaxMessages() {
  state.maxMessages = numberFromInput(maxMessages, defaultMaxMessages, 1, 500, true);
  return state.maxMessages;
}

async function requestStartTrial() {
  if (state.liveSnapshot?.trialActive || state.liveSnapshot?.trialRequested) {
    return;
  }
  const fixedFiveMode = ["circle", "chain", "y", "wheel"].includes(state.mode);
  const liveCount = state.liveSnapshot?.connected?.length || 0;
  if (fixedFiveMode && liveCount < 5) {
    addEvent("error", "Could not start trial", "Circle, chain, Y, and wheel require all 5 Jetsons connected.", state.mode);
    return;
  }
  try {
    const response = await fetch("/api/start", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        topology: state.mode,
        num_agents: state.agentCount,
        ollama_options: getOllamaOptions(),
        max_messages: getMaxMessages(),
      }),
    });
    const payload = await response.json();
    addEvent(response.ok ? "system" : "error", response.ok ? "Live trial requested" : "Could not start trial", payload.message || "", state.mode);
    fetchState();
  } catch {
    addEvent("system", "Live server offline", "Start dashboard_server.py, then reload this page.", state.mode);
  }
}

async function requestStopTrial() {
  state.autoTrials = false;
  updateCopy();
  try {
    const response = await fetch("/api/stop", { method: "POST" });
    const payload = await response.json();
    addEvent(response.ok ? "system" : "error", response.ok ? "Stop trial" : "Could not stop trial", payload.message || "", state.mode);
    fetchState();
  } catch {
    addEvent("system", "Live server offline", "Start dashboard_server.py, then reload this page.", state.mode);
  }
}

async function requestAutoTrials() {
  if ((state.liveSnapshot?.trialActive || state.liveSnapshot?.trialRequested) && !(state.liveSnapshot?.autoTrials || state.autoTrials)) {
    return;
  }
  const nextEnabled = !(state.liveSnapshot?.autoTrials || state.autoTrials);
  state.autoTrials = nextEnabled;
  updateCopy();
  try {
    const response = await fetch("/api/auto-trials", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        enabled: nextEnabled,
        topology: state.mode,
        num_agents: state.agentCount,
        ollama_options: getOllamaOptions(),
        max_messages: getMaxMessages(),
      }),
    });
    const payload = await response.json();
    if (!response.ok) {
      state.autoTrials = false;
    }
    addEvent(response.ok ? "system" : "error", nextEnabled ? "Auto trials" : "Auto stopped", payload.message || "", state.mode);
    fetchState();
  } catch {
    state.autoTrials = false;
    updateCopy();
    addEvent("system", "Live server offline", "Start dashboard_server.py, then reload this page.", state.mode);
  }
}

async function requestRestartClients() {
  if (state.liveSnapshot?.trialActive || state.liveSnapshot?.trialRequested) {
    return;
  }
  eventFeed.innerHTML = "";
  resetChatHistories();
  state.lastRoute = null;
  state.messageCount = 0;
  state.round = 1;
  try {
    const response = await fetch("/api/restart-clients", { method: "POST" });
    const payload = await response.json();
    addEvent(response.ok ? "system" : "error", "Restart fresh", payload.message || "", state.mode);
    fetchState();
  } catch {
    addEvent("system", "Live server offline", "Start dashboard_server.py, then reload this page.", state.mode);
  }
}

async function requestClearResults() {
  if (state.liveSnapshot?.trialActive || state.liveSnapshot?.trialRequested) {
    return;
  }
  try {
    await fetch("/api/clear-results", { method: "POST" });
    renderResults([]);
  } catch {
    renderResults([]);
  }
}

function animate() {
  const speed = state.playing || state.source === "live" ? 0.018 : 0.006;
  state.pulse = (state.pulse + speed) % 1;
  draw();
  requestAnimationFrame(animate);
}

function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#039;",
  })[char]);
}

function startPanelResize(event) {
  event.preventDefault();
  const startX = event.clientX;
  const startWidth = infoPanel.getBoundingClientRect().width;

  function resize(moveEvent) {
    const nextWidth = Math.max(340, Math.min(760, startWidth - (moveEvent.clientX - startX)));
    workspace.style.setProperty("--info-width", `${Math.round(nextWidth)}px`);
    resizeCanvas();
  }

  function stopResize() {
    window.removeEventListener("pointermove", resize);
    window.removeEventListener("pointerup", stopResize);
  }

  window.addEventListener("pointermove", resize);
  window.addEventListener("pointerup", stopResize);
}

function startStageResize(event) {
  event.preventDefault();
  const startY = event.clientY;
  const startHeight = networkStage.getBoundingClientRect().height;

  function resize(moveEvent) {
    const availableHeight = stageColumn.getBoundingClientRect().height;
    const maxHeight = Math.max(260, availableHeight - 88);
    const nextHeight = Math.max(240, Math.min(maxHeight, startHeight + (moveEvent.clientY - startY)));
    stageColumn.style.setProperty("--stage-height", `${Math.round(nextHeight)}px`);
    resizeCanvas();
  }

  function stopResize() {
    window.removeEventListener("pointermove", resize);
    window.removeEventListener("pointerup", stopResize);
  }

  window.addEventListener("pointermove", resize);
  window.addEventListener("pointerup", stopResize);
}

function startEventFeedResize(event) {
  event.preventDefault();
  const startY = event.clientY;
  const startHeight = eventFeed.getBoundingClientRect().height;

  function resize(moveEvent) {
    const maxHeight = Math.max(420, window.innerHeight * 1.5);
    const nextHeight = Math.max(120, Math.min(maxHeight, startHeight + (moveEvent.clientY - startY)));
    eventFeed.style.setProperty("--event-feed-height", `${Math.round(nextHeight)}px`);
  }

  function stopResize() {
    window.removeEventListener("pointermove", resize);
    window.removeEventListener("pointerup", stopResize);
  }

  window.addEventListener("pointermove", resize);
  window.addEventListener("pointerup", stopResize);
}

sourceButtons.forEach((button) => {
  button.addEventListener("click", () => setSource(button.dataset.source));
});

modeButtons.forEach((button) => {
  button.addEventListener("click", () => setMode(button.dataset.mode));
});

agentCount.addEventListener("input", () => {
  if (state.liveSnapshot?.trialActive || state.liveSnapshot?.trialRequested) {
    return;
  }
  state.agentCount = Number(agentCount.value);
  if (state.source === "demo") {
    resetDemo();
  }
  updateCopy();
  renderAgents();
  draw();
});

[ollamaTemperature, ollamaTopP, ollamaRepeatPenalty, ollamaNumPredict].forEach((input) => {
  input.addEventListener("input", () => {
    if (state.liveSnapshot?.trialActive || state.liveSnapshot?.trialRequested) {
      return;
    }
    getOllamaOptions();
  });
});

maxMessages.addEventListener("input", () => {
  if (state.liveSnapshot?.trialActive || state.liveSnapshot?.trialRequested) {
    return;
  }
  getMaxMessages();
});

playPause.addEventListener("click", () => {
  state.playing = !state.playing;
  playPause.classList.toggle("playing", !state.playing);
  playPause.setAttribute("aria-label", state.playing ? "Pause animation" : "Play animation");
  playPause.setAttribute("title", state.playing ? "Pause animation" : "Play animation");
});

stepButton.addEventListener("click", demoStep);
clearFeed.addEventListener("click", () => {
  if (state.liveSnapshot?.trialActive || state.liveSnapshot?.trialRequested) {
    return;
  }
  eventFeed.innerHTML = "";
  resetChatHistories();
});
panelResizeHandle.addEventListener("pointerdown", startPanelResize);
stageResizeHandle.addEventListener("pointerdown", startStageResize);
eventFeedResizeHandle.addEventListener("pointerdown", startEventFeedResize);
startTrial.addEventListener("click", requestStartTrial);
stopTrial.addEventListener("click", requestStopTrial);
autoTrials.addEventListener("click", requestAutoTrials);
restartClients.addEventListener("click", requestRestartClients);
clearResults.addEventListener("click", requestClearResults);

setInterval(() => {
  if (state.source === "demo" && state.playing) {
    demoStep();
  }
}, 2200);

window.addEventListener("resize", resizeCanvas);
resizeCanvas();
setMode("circle");
setSource("live");
animate();
