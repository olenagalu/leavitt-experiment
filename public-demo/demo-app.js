const agents = [
  { id: 1, name: "Agent1", hostname: "slm-1", symbols: ["square", "circle", "cross"], color: "#4098d0" },
  { id: 2, name: "Agent2", hostname: "slm-2", symbols: ["circle", "diamond", "asterisk"], color: "#62c6bf" },
  { id: 3, name: "Agent3", hostname: "slm-3", symbols: ["circle", "triangle", "cross"], color: "#ef6077" },
  { id: 4, name: "Agent4", hostname: "slm-4", symbols: ["circle", "square", "diamond"], color: "#ad70b3" },
  { id: 5, name: "Agent5", hostname: "slm-5", symbols: ["circle", "triangle", "asterisk"], color: "#f3bd59" },
];

const symbolMarks = {
  square: "□",
  circle: "○",
  triangle: "△",
  diamond: "◇",
  cross: "×",
  asterisk: "*",
};

const topologyMeta = {
  broadcast: {
    label: "Broadcast mode",
    description: "The server sends each chat message to all selected active SLMs.",
    defaultDiscussionRounds: 3,
  },
  circle: {
    label: "Circle mode",
    description: "Each SLM sends private messages only to its two circle neighbors.",
    defaultDiscussionRounds: 6,
    fixedAgents: 5,
  },
  chain: {
    label: "Chain mode",
    description: "SLMs communicate along a line: Agent1 through Agent5, with only adjacent contacts.",
    defaultDiscussionRounds: 8,
    fixedAgents: 5,
  },
  y: {
    label: "Y topology",
    description: "Agent3 is the junction, Agent4 bridges to Agent5, and endpoints only use their branch contact.",
    defaultDiscussionRounds: 8,
    fixedAgents: 5,
  },
  wheel: {
    label: "Wheel mode",
    description: "Agent3 is the central hub. Other SLMs send through Agent3.",
    defaultDiscussionRounds: 2,
    fixedAgents: 5,
  },
};

const topologyLinks = {
  circle: [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]],
  chain: [[1, 2], [2, 3], [3, 4], [4, 5]],
  y: [[1, 3], [2, 3], [3, 4], [4, 5]],
  wheel: [[1, 3], [2, 3], [3, 4], [3, 5]],
};

const demoScript = [
  "I have circle, square, and cross.",
  "Circle appears on my card too.",
  "I do not have square, but circle is shared.",
  "I can confirm circle with my symbols.",
  "Final answer should be circle.",
];

const canvas = document.querySelector("#networkCanvas");
const ctx = canvas.getContext("2d");
const networkStage = document.querySelector(".network-stage");
const stageOverlayText = document.querySelector("#stageOverlayText");
const agentLayer = document.querySelector("#agentLayer");
const modeButtons = [...document.querySelectorAll("[data-mode]")];
const agentCount = document.querySelector("#agentCount");
const agentCountValue = document.querySelector("#agentCountValue");
const discussionRounds = document.querySelector("#discussionRounds");
const ollamaTemperature = document.querySelector("#ollamaTemperature");
const ollamaRepeatPenalty = document.querySelector("#ollamaRepeatPenalty");
const ollamaNumPredict = document.querySelector("#ollamaNumPredict");
const connectionStatus = document.querySelector("#connectionStatus");
const statusPill = document.querySelector(".status-pill");
const sourceLabel = document.querySelector("#sourceLabel");
const modeTitle = document.querySelector("#modeTitle");
const modeDescription = document.querySelector("#modeDescription");
const routeText = document.querySelector("#routeText");
const currentMessageText = document.querySelector("#currentMessageText");
const chatPanel = document.querySelector("#chatPanel");
const chatGrid = document.querySelector("#chatGrid");
const roundMetric = document.querySelector("#roundMetric");
const messageMetric = document.querySelector("#messageMetric");
const symbolMetric = document.querySelector("#symbolMetric");
const eventFeed = document.querySelector("#eventFeed");
const workspace = document.querySelector(".workspace");
const stageColumn = document.querySelector(".stage-column");
const infoPanel = document.querySelector("#infoPanel");
const panelResizeHandle = document.querySelector("#panelResizeHandle");
const stageResizeHandle = document.querySelector("#stageResizeHandle");
const startTrialButton = document.querySelector("#startTrial");
const stopTrialButton = document.querySelector("#stopTrial");
const autoTrials = document.querySelector("#autoTrials");
const restartClients = document.querySelector("#restartClients");
const clearFeed = document.querySelector("#clearFeed");
const clearResults = document.querySelector("#clearResults");
const resultsBody = document.querySelector("#resultsBody");
const liveControls = document.querySelector(".live-controls");
const agentCountGroup = agentCount.closest(".control-group");

const state = {
  mode: "broadcast",
  agentCount: 5,
  discussionRounds: topologyMeta.broadcast.defaultDiscussionRounds,
  running: false,
  auto: false,
  autoTimer: null,
  trialId: 0,
  step: 0,
  round: 1,
  messages: 0,
  pulse: 0,
  lastRoute: null,
  timer: null,
  results: [],
  resultModes: [],
  lastFeedRound: null,
  chatHistories: {},
};

function visibleAgents() {
  return agents.slice(0, state.agentCount);
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
  const list = visibleAgents();
  if (["chain", "y", "wheel"].includes(state.mode)) {
    const layouts = {
      chain: { 1: [0.13, 0.5], 2: [0.31, 0.5], 3: [0.5, 0.5], 4: [0.69, 0.5], 5: [0.87, 0.5] },
      y: { 1: [0.27, 0.25], 2: [0.27, 0.75], 3: [0.5, 0.5], 4: [0.69, 0.5], 5: [0.87, 0.5] },
      wheel: { 1: [0.28, 0.24], 2: [0.28, 0.76], 3: [0.5, 0.5], 4: [0.72, 0.76], 5: [0.72, 0.24] },
    };
    return list.map((agent) => {
      const [xRatio, yRatio] = layouts[state.mode][agent.id] || [0.5, 0.5];
      return { ...agent, x: width * xRatio, y: height * yRatio };
    });
  }

  const centerX = width / 2;
  const centerY = height / 2 - 16;
  const radius = Math.min(width, height) * (width < 700 ? 0.31 : 0.34);
  return list.map((agent, index) => {
    const angle = -Math.PI / 2 + (index / Math.max(list.length, 1)) * Math.PI * 2;
    return { ...agent, x: centerX + Math.cos(angle) * radius, y: centerY + Math.sin(angle) * radius };
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

function byName(positions, name) {
  return positions.find((agent) => agent.name === name);
}

function byId(positions, id) {
  return positions.find((agent) => agent.id === id);
}

function receiversFor(sender) {
  const list = visibleAgents();
  if (state.mode === "broadcast") {
    return list.filter((agent) => agent.name !== sender.name);
  }
  if (state.mode === "circle") {
    const index = list.findIndex((agent) => agent.id === sender.id);
    return [list[(index + 1) % list.length]].filter(Boolean);
  }
  const links = topologyLinks[state.mode] || [];
  const ids = links
    .filter(([from, to]) => from === sender.id || to === sender.id)
    .map(([from, to]) => (from === sender.id ? to : from));
  return ids.map((id) => list.find((agent) => agent.id === id)).filter(Boolean);
}

function drawTopology(positions) {
  if (state.mode === "broadcast") {
    positions.forEach((from, index) => {
      positions.forEach((to, targetIndex) => {
        if (index < targetIndex) {
          drawLine(from, to, "#62c6bf", 1.5, 0.18);
        }
      });
    });
    return;
  }

  (topologyLinks[state.mode] || []).forEach(([fromId, toId]) => {
    const from = byId(positions, fromId);
    const to = byId(positions, toId);
    if (from && to) {
      drawLine(from, to, state.mode === "circle" ? "#f3bd59" : "#62c6bf", 3, 0.66);
    }
  });
}

function draw() {
  const rect = canvas.getBoundingClientRect();
  ctx.clearRect(0, 0, rect.width, rect.height);
  const positions = getPositions();
  if (!positions.length) return;

  drawTopology(positions);
  const offset = state.pulse;
  if (!state.lastRoute) return;

  const sender = byName(positions, state.lastRoute.sender);
  const receiverNames = state.lastRoute.receiver === "ALL"
    ? positions.filter((agent) => agent.name !== state.lastRoute.sender).map((agent) => agent.name)
    : state.lastRoute.receiver.split(",").map((name) => name.trim());

  receiverNames.forEach((receiverName) => {
    const receiver = byName(positions, receiverName);
    if (!sender || !receiver) return;
    drawLine(sender, receiver, "#ef6077", 4, 0.92);
    drawPacket(sender, receiver, "#ef6077", offset);
  });
}

function renderAgents() {
  const positions = getPositions();
  const receiverSet = new Set(
    state.lastRoute?.receiver === "ALL"
      ? positions.filter((agent) => agent.name !== state.lastRoute.sender).map((agent) => agent.name)
      : (state.lastRoute?.receiver || "").split(",").map((name) => name.trim()).filter(Boolean),
  );
  agentLayer.innerHTML = positions.map((agent) => {
    const classes = [
      "agent-node",
      state.lastRoute?.sender === agent.name ? "sender" : "",
      receiverSet.has(agent.name) ? "receiver" : "",
    ].filter(Boolean).join(" ");
    const symbols = agent.symbols.map((symbol) => `<span class="symbol" title="${symbol}">${symbolMarks[symbol]}</span>`).join("");
    const note = state.lastRoute?.sender === agent.name ? "speaking now" : agent.hostname;
    return `
      <article class="${classes}" style="left:${agent.x}px; top:${agent.y}px">
        <div class="agent-name"><span>${agent.name}</span><i class="chip" style="background:${agent.color}"></i></div>
        <div class="symbols">${symbols}</div>
        <div class="agent-note">${note}</div>
      </article>
    `;
  }).join("");
}

function colorForAgent(name) {
  return agents.find((agent) => agent.name === name)?.color || "#62c6bf";
}

function parseReceiverList(route, list = visibleAgents()) {
  if (!route?.receiver || route.receiver === "ALL") {
    return list.filter((agent) => agent.name !== route?.sender).map((agent) => agent.name);
  }
  return String(route.receiver).split(",").map((name) => name.trim()).filter(Boolean);
}

function resetChatHistories() {
  state.chatHistories = {};
  visibleAgents().forEach((agent) => {
    state.chatHistories[agent.name] = [];
  });
}

function recordChat(route) {
  const viewers = new Set([route.sender, ...parseReceiverList(route)]);
  viewers.forEach((name) => {
    if (!state.chatHistories[name]) {
      state.chatHistories[name] = [];
    }
    state.chatHistories[name].push({
      sender: route.sender,
      message: route.message || "",
      round: route.round,
    });
    state.chatHistories[name] = state.chatHistories[name].slice(-8);
  });
}

function renderChats() {
  if (state.mode === "broadcast") {
    chatPanel.hidden = true;
    chatGrid.innerHTML = "";
    return;
  }
  chatPanel.hidden = false;
  chatGrid.innerHTML = visibleAgents().map((agent) => {
    const history = state.chatHistories[agent.name] || [];
    const rows = history.length
      ? history.map((entry) => `<p><b>${escapeHtml(entry.sender)}:</b> ${escapeHtml(entry.message)}</p>`).join("")
      : `<p>No private messages yet.</p>`;
    return `
      <article class="chat-card" style="--agent-color:${agent.color}">
        <strong>${escapeHtml(agent.name)} sees</strong>
        ${rows}
      </article>
    `;
  }).join("");
}

function addRoundHeader(round) {
  if (!round || state.lastFeedRound === round) {
    return;
  }
  state.lastFeedRound = round;
  const header = document.createElement("li");
  header.className = "round-header";
  header.textContent = `Round ${round}`;
  eventFeed.prepend(header);
}

function insertFeedItem(item) {
  const first = eventFeed.firstElementChild;
  if (first?.classList.contains("round-header")) {
    eventFeed.insertBefore(item, first.nextSibling);
  } else {
    eventFeed.prepend(item);
  }
}

function addEvent(kind, title, text, round = null, sender = null) {
  if (kind === "chat") {
    addRoundHeader(round);
  }
  const item = document.createElement("li");
  item.className = [state.mode !== "broadcast" ? "circle-event" : "", kind === "system" ? "system-event" : ""].filter(Boolean).join(" ");
  if (sender) {
    item.style.setProperty("--event-color", colorForAgent(sender));
  }
  item.innerHTML = `<strong>${escapeHtml(title)}</strong><span>${escapeHtml(text)}</span>`;
  insertFeedItem(item);
  eventFeed.scrollTop = 0;
  while (eventFeed.children.length > 18) {
    eventFeed.lastElementChild.remove();
  }
}

function setLocked(locked) {
  modeButtons.forEach((button) => { button.disabled = locked; });
  agentCount.disabled = locked;
  discussionRounds.disabled = locked;
  ollamaTemperature.disabled = locked;
  ollamaRepeatPenalty.disabled = locked;
  ollamaNumPredict.disabled = locked;
  startTrialButton.disabled = locked;
  stopTrialButton.disabled = !locked;
  autoTrials.disabled = locked;
  restartClients.disabled = locked;
  clearFeed.disabled = locked;
  clearResults.disabled = locked;
}

function modeDetailText(meta) {
  return `SLM stands for small language model: a compact AI model that can run locally and exchange short messages. ${meta.description}`;
}

function syncCopy() {
  const meta = topologyMeta[state.mode];
  sourceLabel.textContent = "Static demo";
  modeTitle.textContent = meta.label;
  modeDescription.textContent = modeDetailText(meta);
  agentCountValue.textContent = state.agentCount;
  agentCountGroup.hidden = state.mode !== "broadcast";
  renderChats();
  roundMetric.textContent = state.round;
  messageMetric.textContent = state.messages;
  symbolMetric.textContent = state.messages ? "circle" : "?";
  autoTrials.setAttribute("aria-pressed", String(state.auto));
  autoTrials.textContent = state.auto ? "Stop auto" : "Auto trials";
  modeButtons.forEach((button) => {
    const active = button.dataset.mode === state.mode;
    button.classList.toggle("active", active);
    button.setAttribute("aria-selected", String(active));
  });
}

function showOverlay(text) {
  networkStage.classList.add("is-blurred");
  stageOverlayText.textContent = text;
}

function hideOverlay() {
  networkStage.classList.remove("is-blurred");
  stageOverlayText.textContent = "";
}

function renderResults() {
  rememberResultMode(state.mode);
  if (!state.results.length) {
    resultsBody.innerHTML = `${renderResultModeRow(state.mode)}<tr><td colspan="7">No demo trials yet.</td></tr>`;
    return;
  }
  resultsBody.innerHTML = renderResultSections();
}

function rememberResultMode(mode) {
  if (!mode) {
    return;
  }
  state.resultModes = [
    mode,
    ...state.resultModes.filter((savedMode) => savedMode !== mode),
  ];
}

function renderResultSections() {
  const modes = [
    state.mode,
    ...state.resultModes,
    ...state.results.map((result) => result.mode),
  ].filter(Boolean);
  const orderedModes = [...new Set(modes)];
  return orderedModes.map((mode) => {
    const modeResults = state.results.filter((result) => result.mode === mode);
    if (!modeResults.length) {
      return mode === state.mode ? renderResultModeRow(mode) : "";
    }
    const resultRows = [...modeResults].reverse().map((result, index) => {
      const trial = modeResults.length - index;
      return `
        <tr>
          <td>${trial}</td>
          <td>${escapeHtml(result.mode)}</td>
          <td><span class="${result.success ? "result-good" : "result-bad"}">${result.success ? "success" : "stopped"}</span></td>
          <td>circle</td>
          <td><span class="${result.success ? "answer-correct" : "answer-wrong"}">${escapeHtml(result.answer)}</span></td>
          <td>${result.rounds}</td>
          <td>${result.seconds}s</td>
        </tr>
      `;
    }).join("");
    return `${renderResultModeRow(mode)}${resultRows}`;
  }).join("");
}

function renderResultModeRow(mode) {
  const label = topologyMeta[mode]?.label || mode || "-";
  return `<tr><td><strong>Topology</strong></td><td colspan="6">${escapeHtml(label)}</td></tr>`;
}

function setMode(mode) {
  if (state.running) return;
  state.mode = mode;
  if (topologyMeta[mode].fixedAgents) {
    state.agentCount = 5;
    agentCount.value = "5";
  }
  state.discussionRounds = topologyMeta[mode].defaultDiscussionRounds;
  discussionRounds.value = String(state.discussionRounds);
  state.lastRoute = null;
  resetChatHistories();
  syncCopy();
  renderResults();
  renderAgents();
  draw();
}

function startDemoTrial() {
  if (state.running) return;
  window.clearTimeout(state.autoTimer);
  state.autoTimer = null;
  state.running = true;
  state.trialId += 1;
  state.step = 0;
  state.round = 1;
  state.messages = 0;
  state.lastRoute = null;
  eventFeed.innerHTML = "";
  state.lastFeedRound = null;
  resetChatHistories();
  setLocked(true);
  hideOverlay();
  syncCopy();
  runStep();
  state.timer = window.setInterval(runStep, 1500);
}

function finishTrial(success, answer = "circle", stopped = false) {
  window.clearInterval(state.timer);
  state.timer = null;
  state.running = false;
  setLocked(false);
  const result = {
    trial: state.trialId,
    mode: state.mode,
    success,
    answer,
    stopped,
    rounds: state.round,
    seconds: Math.max(2, state.messages * 1.5).toFixed(1),
  };
  state.results.push(result);
  renderResults();
  showOverlay(stopped ? "Trial Ended (Stopped)" : (success ? "Trial Ended (Success)" : "Trial Ended (Fail)"));
  if (state.auto && success) {
    state.autoTimer = window.setTimeout(startDemoTrial, 1800);
  }
}

function stopDemoTrial() {
  if (!state.running) return;
  state.auto = false;
  window.clearTimeout(state.autoTimer);
  state.autoTimer = null;
  finishTrial(false, "none", true);
}

function resetDemo() {
  window.clearInterval(state.timer);
  window.clearTimeout(state.autoTimer);
  state.timer = null;
  state.autoTimer = null;
  state.running = false;
  state.auto = false;
  state.step = 0;
  state.round = 1;
  state.messages = 0;
  state.lastRoute = null;
  eventFeed.innerHTML = "";
  state.lastFeedRound = null;
  resetChatHistories();
  routeText.textContent = "Agent1 -> ALL";
  currentMessageText.textContent = "No message yet.";
  setLocked(false);
  showOverlay("Start Trial");
  syncCopy();
  renderAgents();
  draw();
}

function runStep() {
  if (!state.running) return;
  const list = visibleAgents();
  const sender = list[state.step % list.length];
  const receivers = receiversFor(sender);
  const receiverText = state.mode === "broadcast" ? "ALL" : receivers.map((agent) => agent.name).join(", ");
  const text = demoScript[state.step % demoScript.length];
  state.lastRoute = { sender: sender.name, receiver: receiverText, message: text };
  state.pulse = 0;
  state.messages += 1;
  state.round = Math.floor((state.messages - 1) / Math.max(1, state.agentCount)) + 1;
  state.lastRoute.round = state.round;
  recordChat(state.lastRoute);
  routeText.textContent = `${sender.name} -> ${receiverText}`;
  currentMessageText.innerHTML = `<span class="message-sender">${sender.name}:</span> <span class="message-body">${escapeHtml(text)}</span>`;
  addEvent("chat", `${sender.name} -> ${receiverText}`, text, state.round, sender.name);
  state.step += 1;
  syncCopy();
  renderAgents();
  draw();

  const targetMessages = Math.max(5, Math.min(14, state.discussionRounds + 4));
  if (state.messages >= targetMessages) {
    finishTrial(true);
  }
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

modeButtons.forEach((button) => {
  button.addEventListener("click", () => setMode(button.dataset.mode));
});

agentCount.addEventListener("input", () => {
  if (state.running) return;
  state.agentCount = Number(agentCount.value);
  syncCopy();
  renderAgents();
  draw();
});

discussionRounds.addEventListener("input", () => {
  if (state.running) return;
  const nextValue = Number(discussionRounds.value);
  state.discussionRounds = Number.isFinite(nextValue) ? Math.max(0, Math.min(20, Math.floor(nextValue))) : topologyMeta[state.mode].defaultDiscussionRounds;
  discussionRounds.value = String(state.discussionRounds);
});

startTrialButton.addEventListener("click", startDemoTrial);
stopTrialButton.addEventListener("click", stopDemoTrial);
autoTrials.addEventListener("click", () => {
  if (state.running) return;
  state.auto = !state.auto;
  if (!state.auto) {
    window.clearTimeout(state.autoTimer);
    state.autoTimer = null;
  }
  syncCopy();
  if (state.auto) startDemoTrial();
});
restartClients.addEventListener("click", resetDemo);
clearFeed.addEventListener("click", () => {
  if (!state.running) {
    eventFeed.innerHTML = "";
    state.lastFeedRound = null;
    resetChatHistories();
    renderChats();
  }
});
clearResults.addEventListener("click", () => {
  if (!state.running) {
    state.results = [];
    state.resultModes = [];
    renderResults();
  }
});
panelResizeHandle.addEventListener("pointerdown", startPanelResize);
stageResizeHandle.addEventListener("pointerdown", startStageResize);

function animate() {
  state.pulse = (state.pulse + 0.018) % 1;
  draw();
  requestAnimationFrame(animate);
}

liveControls.hidden = false;
restartClients.disabled = false;
connectionStatus.textContent = "Demo mode";
statusPill.classList.add("connected");
showOverlay("Start Trial");
syncCopy();
renderResults();
resizeCanvas();
window.addEventListener("resize", resizeCanvas);
animate();
