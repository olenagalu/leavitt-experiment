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

const state = {
  source: "demo",
  mode: "broadcast",
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
};

const canvas = document.querySelector("#networkCanvas");
const ctx = canvas.getContext("2d");
const agentLayer = document.querySelector("#agentLayer");
const sourceButtons = [...document.querySelectorAll("[data-source]")];
const modeButtons = [...document.querySelectorAll("[data-mode]")];
const agentCount = document.querySelector("#agentCount");
const agentCountValue = document.querySelector("#agentCountValue");
const connectionStatus = document.querySelector("#connectionStatus");
const sourceLabel = document.querySelector("#sourceLabel");
const modeTitle = document.querySelector("#modeTitle");
const modeDescription = document.querySelector("#modeDescription");
const routeText = document.querySelector("#routeText");
const roundMetric = document.querySelector("#roundMetric");
const messageMetric = document.querySelector("#messageMetric");
const symbolMetric = document.querySelector("#symbolMetric");
const eventFeed = document.querySelector("#eventFeed");
const playPause = document.querySelector("#playPause");
const stepButton = document.querySelector("#stepButton");
const clearFeed = document.querySelector("#clearFeed");
const startTrial = document.querySelector("#startTrial");
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
    const liveAgents = connected.length ? connected : fallbackAgents.slice(0, state.agentCount);
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
  const centerX = width / 2;
  const centerY = height / 2 - 16;
  const radius = Math.min(width, height) * (width < 700 ? 0.31 : 0.34);
  const list = visibleAgents();

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

function draw() {
  const rect = canvas.getBoundingClientRect();
  ctx.clearRect(0, 0, rect.width, rect.height);
  const positions = getPositions();
  if (!positions.length) {
    return;
  }

  const offset = (Math.sin(state.pulse) + 1) / 2;
  const active = state.lastRoute
    ? getAgentByName(positions, state.lastRoute.sender) || positions[state.activeIndex % positions.length]
    : positions[state.activeIndex % positions.length];
  const topology = state.source === "live" && state.liveSnapshot ? state.liveSnapshot.topology : state.mode;

  if (topology === "broadcast") {
    positions.forEach((from, index) => {
      positions.forEach((to, targetIndex) => {
        if (index < targetIndex) {
          drawLine(from, to, "#62c6bf", 1.5, 0.18);
        }
      });
    });
    positions.forEach((to) => {
      if (to.name !== active.name) {
        drawLine(active, to, "#62c6bf", 3, 0.84);
        if (state.lastRoute) {
          drawPacket(active, to, "#ef6077", offset);
        }
      }
    });
  } else {
    positions.forEach((from, index) => {
      const to = positions[(index + 1) % positions.length];
      drawLine(from, to, "#f3bd59", 3, 0.66);
    });

    let target = null;
    if (state.lastRoute?.receiver && state.lastRoute.receiver !== "ALL") {
      target = getAgentByName(positions, state.lastRoute.receiver);
    }
    target = target || positions[(positions.indexOf(active) + 1) % positions.length];
    drawLine(active, target, "#ef6077", 4, 0.92);
    if (state.lastRoute) {
      drawPacket(active, target, "#ef6077", offset);
    }
  }
}

function renderAgents() {
  const positions = getPositions();
  const activeName = state.lastRoute?.sender || state.liveSnapshot?.currentSpeaker;
  const receiverName = state.lastRoute?.receiver;

  agentLayer.innerHTML = positions.map((agent) => {
    const classes = [
      "agent-node",
      agent.name === activeName ? "active" : "",
      receiverName === "ALL" || agent.name === receiverName ? "receiver" : "",
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
  const list = visibleAgents();
  if (state.mode === "broadcast") {
    return list.filter((agent) => agent.name !== sender.name);
  }
  const index = list.findIndex((agent) => agent.name === sender.name);
  return [list[(index + 1) % list.length]];
}

function updateCopy() {
  const snapshot = state.liveSnapshot;
  const topology = state.source === "live" && snapshot ? snapshot.topology : state.mode;
  const broadcast = topology === "broadcast";
  const agents = visibleAgents();
  const route = state.lastRoute;

  sourceLabel.textContent = state.source === "live" ? "Live Jetsons" : "Demo animation";
  modeTitle.textContent = broadcast ? "Broadcast mode" : "Circle mode";
  modeDescription.textContent = broadcast
    ? "The server sends each chat message to all selected active Jetsons, matching the console broadcast topology."
    : "The server sends each chat message only to a selected circle neighbor, matching the console circle topology.";

  if (route) {
    routeText.textContent = `${route.sender} -> ${route.receiver}`;
  } else if (state.source === "live") {
    routeText.textContent = snapshot?.trialActive ? "Waiting for next message" : "No live trial running";
  } else {
    const sender = agents[state.activeIndex % agents.length];
    const receivers = getDemoReceivers(sender);
    routeText.textContent = broadcast
      ? `${sender.name} -> ALL`
      : `${sender.name} -> ${receivers.map((agent) => agent.name).join(", ")}`;
  }

  const liveCount = snapshot?.connected?.length || 0;
  connectionStatus.textContent = state.source === "live"
    ? `${liveCount} Jetson${liveCount === 1 ? "" : "s"} connected`
    : "Demo mode";
  agentCountValue.textContent = state.agentCount;
  roundMetric.textContent = snapshot?.round ?? state.round;
  messageMetric.textContent = snapshot?.messages ?? state.messageCount;
  symbolMetric.textContent = snapshot?.commonSymbol || (state.messageCount >= Math.max(3, state.agentCount) ? "circle" : "?");
  startTrial.disabled = state.source !== "live" || Boolean(snapshot?.trialActive || snapshot?.trialRequested);
  renderResults(snapshot?.results || []);
}

function addEvent(kind, title, text, topology = state.mode) {
  const item = document.createElement("li");
  item.className = [
    topology === "circle" ? "circle-event" : "",
    kind === "system" ? "system-event" : "",
  ].filter(Boolean).join(" ");
  item.innerHTML = `<strong>${escapeHtml(title)}</strong><span>${escapeHtml(text)}</span>`;
  eventFeed.prepend(item);

  while (eventFeed.children.length > 14) {
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

  state.lastRoute = { sender: sender.name, receiver: receiverText, topology: state.mode, message: text };
  state.messageCount += 1;
  state.round = Math.floor((state.messageCount - 1) / state.agentCount) + 1;
  addEvent("chat", `${sender.name} -> ${receiverText}`, text, state.mode);
  state.activeIndex = (state.activeIndex + 1) % state.agentCount;

  updateCopy();
  renderAgents();
  draw();
}

function setMode(mode) {
  state.mode = mode;
  if (state.source === "demo") {
    resetDemo();
  }
  modeButtons.forEach((button) => {
    const active = button.dataset.mode === mode;
    button.classList.toggle("active", active);
    button.setAttribute("aria-selected", String(active));
  });
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
}

function connectLive() {
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
    connectionStatus.textContent = "Live server offline";
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
  try {
    const response = await fetch("/api/state");
    state.liveSnapshot = await response.json();
    updateCopy();
    renderAgents();
    draw();
  } catch {
    connectionStatus.textContent = "Live server offline";
  }
}

function handleLiveEvent(event) {
  const payload = event.payload || {};
  if (event.kind === "chat") {
    state.lastRoute = payload;
    addEvent("chat", `${payload.sender} -> ${payload.receiver}`, payload.message || "", payload.topology);
  } else if (event.kind === "trial_started") {
    state.lastRoute = null;
    eventFeed.innerHTML = "";
    addEvent("system", "Trial started", `${payload.num_agents} Jetsons in ${payload.topology} mode.`, payload.topology);
  } else if (event.kind === "turn_started") {
    addEvent("system", "Turn", `${payload.speaker} is responding in round ${payload.round}.`, state.liveSnapshot?.topology);
  } else if (event.kind === "answer") {
    addEvent("system", "Answer submitted", `${payload.speaker} answered ${payload.word}.`, state.liveSnapshot?.topology);
  } else if (event.kind === "trial_finished") {
    addEvent("system", "Trial finished", `${payload.result}. Answer: ${payload.final_answer_word || "none"}.`, payload.topology);
  } else if (event.kind === "client_joined") {
    addEvent("system", "Jetson connected", `${payload.agent} (${payload.hostname})`, state.liveSnapshot?.topology);
  } else if (event.kind === "client_left") {
    addEvent("system", "Jetson disconnected", `${payload.agent} (${payload.reason})`, state.liveSnapshot?.topology);
  } else if (event.kind === "waiting") {
    if (payload.missing?.length) {
      addEvent("system", "Waiting for Jetsons", `Selected ${payload.selected}/${payload.needed}. Missing ${payload.missing.join(", ")}.`, state.liveSnapshot?.topology);
    }
  }
}

function renderResults(results) {
  if (!results.length) {
    resultsBody.innerHTML = `<tr><td colspan="5">No live trials yet.</td></tr>`;
    return;
  }
  resultsBody.innerHTML = [...results].reverse().map((result) => {
    const resultClass = result.success ? "result-good" : "result-bad";
    return `
      <tr>
        <td>${result.trial_id}</td>
        <td>${escapeHtml(result.topology)}</td>
        <td><span class="${resultClass}">${escapeHtml(result.result)}</span></td>
        <td>${result.rounds ?? "-"}</td>
        <td>${result.time_seconds ?? "-"}s</td>
      </tr>
    `;
  }).join("");
}

async function requestStartTrial() {
  try {
    const response = await fetch("/api/start", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topology: state.mode, num_agents: state.agentCount }),
    });
    const payload = await response.json();
    addEvent(response.ok ? "system" : "error", response.ok ? "Live trial requested" : "Could not start trial", payload.message || "", state.mode);
    fetchState();
  } catch {
    addEvent("system", "Live server offline", "Start dashboard_server.py, then reload this page.", state.mode);
  }
}

async function requestClearResults() {
  try {
    await fetch("/api/clear-results", { method: "POST" });
    renderResults([]);
  } catch {
    renderResults([]);
  }
}

function animate() {
  state.pulse += state.playing || state.source === "live" ? 0.045 : 0.015;
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

sourceButtons.forEach((button) => {
  button.addEventListener("click", () => setSource(button.dataset.source));
});

modeButtons.forEach((button) => {
  button.addEventListener("click", () => setMode(button.dataset.mode));
});

agentCount.addEventListener("input", () => {
  state.agentCount = Number(agentCount.value);
  if (state.source === "demo") {
    resetDemo();
  }
  updateCopy();
  renderAgents();
  draw();
});

playPause.addEventListener("click", () => {
  state.playing = !state.playing;
  playPause.classList.toggle("playing", !state.playing);
  playPause.setAttribute("aria-label", state.playing ? "Pause animation" : "Play animation");
  playPause.setAttribute("title", state.playing ? "Pause animation" : "Play animation");
});

stepButton.addEventListener("click", demoStep);
clearFeed.addEventListener("click", () => {
  eventFeed.innerHTML = "";
});
startTrial.addEventListener("click", requestStartTrial);
clearResults.addEventListener("click", requestClearResults);

setInterval(() => {
  if (state.source === "demo" && state.playing) {
    demoStep();
  }
}, 2200);

window.addEventListener("resize", resizeCanvas);
resizeCanvas();
setMode("broadcast");
setSource("demo");
demoStep();
animate();
