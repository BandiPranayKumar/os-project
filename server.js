const express = require("express");
const http = require("http");
const https = require("https");
const path = require("path");
const cors = require("cors");
const os = require("os");
const { Server } = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"]
  }
});

const publicDir = path.join(__dirname, "public");
const pages = [
  "index.html",
  "features.html",
  "system.html",
  "demo.html",
  "about.html",
  "contact.html"
];

app.use(cors());
app.use(express.json());
app.use(express.static(publicDir));

const systemData = {
  cpu: { usage: 42, cores: os.cpus().length, load: 0.58 },
  memory: {
    total: Math.round(os.totalmem() / 1024 / 1024 / 1024),
    used: 0,
    usage: 0
  },
  processes: [
    { id: "P1", name: "Priority Scheduler", cpu: 24, memory: 128, priority: "CRITICAL", status: "RUNNING" },
    { id: "P2", name: "ML Predictor", cpu: 18, memory: 96, priority: "HIGH", status: "RUNNING" },
    { id: "P3", name: "Telemetry Agent", cpu: 11, memory: 64, priority: "NORMAL", status: "IDLE" },
    { id: "P4", name: "Recovery Service", cpu: 8, memory: 48, priority: "NORMAL", status: "WAITING" }
  ],
  metrics: {
    adaptations: 127,
    throughput: 1.24,
    latency: 42,
    efficiency: 98.2,
    incidentsPrevented: 31
  },
  mode: "normal"
};

function clamp(value, min, max) {
  return Math.max(min, Math.min(max, value));
}

function randomDelta(range) {
  return (Math.random() - 0.5) * range;
}

function applyModeProfile() {
  const profiles = {
    normal: { cpu: 42, memory: 48, throughput: 1.24, latency: 42, efficiency: 98.2 },
    stress: { cpu: 84, memory: 76, throughput: 1.81, latency: 73, efficiency: 92.1 },
    priority: { cpu: 61, memory: 58, throughput: 1.53, latency: 34, efficiency: 97.4 }
  };

  const profile = profiles[systemData.mode] || profiles.normal;

  systemData.cpu.usage = clamp(profile.cpu + randomDelta(8), 18, 96);
  systemData.memory.usage = clamp(profile.memory + randomDelta(10), 22, 92);
  systemData.memory.used = Math.round(systemData.memory.total * (systemData.memory.usage / 100));
  systemData.cpu.load = Number((systemData.cpu.usage / 100).toFixed(2));
  systemData.metrics.throughput = Number((profile.throughput + randomDelta(0.15)).toFixed(2));
  systemData.metrics.latency = Math.round(clamp(profile.latency + randomDelta(10), 20, 95));
  systemData.metrics.efficiency = Number(clamp(profile.efficiency + randomDelta(1.8), 90, 99.8).toFixed(1));
  systemData.metrics.adaptations += Math.random() > 0.72 ? 1 : 0;
  systemData.metrics.incidentsPrevented += Math.random() > 0.9 ? 1 : 0;

  systemData.processes = systemData.processes.map((process, index) => {
    const cpuWeight = systemData.mode === "stress" ? 1.35 : systemData.mode === "priority" && index < 2 ? 1.25 : 1;
    const memoryWeight = systemData.mode === "stress" ? 1.2 : 1;
    const statuses = ["RUNNING", "WAITING", "IDLE"];
    const statusIndex = Math.floor(Math.random() * statuses.length);

    return {
      ...process,
      cpu: Number(clamp(process.cpu * cpuWeight + randomDelta(8), 2, 94).toFixed(1)),
      memory: Math.round(clamp(process.memory * memoryWeight + randomDelta(16), 24, 256)),
      status: statuses[statusIndex],
      priority:
        systemData.mode === "priority" && index === 0
          ? "CRITICAL"
          : systemData.mode === "stress" && index === 1
            ? "HIGH"
            : process.priority
    };
  });
}

function buildPerformanceHistory(baseline, amplitude) {
  return Array.from({ length: 30 }, (_, index) => ({
    time: `${index + 1}s`,
    value: Number(clamp(baseline + Math.sin(index / 3) * amplitude + randomDelta(5), 15, 98).toFixed(1))
  }));
}

function callOpenAI(apiKey, payload) {
  return new Promise((resolve, reject) => {
    const requestBody = JSON.stringify(payload);

    const request = https.request(
      {
        hostname: "api.openai.com",
        path: "/v1/responses",
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Content-Length": Buffer.byteLength(requestBody),
          Authorization: `Bearer ${apiKey}`
        }
      },
      (response) => {
        let body = "";

        response.on("data", (chunk) => {
          body += chunk;
        });

        response.on("end", () => {
          if (response.statusCode < 200 || response.statusCode >= 300) {
            reject(new Error(`OpenAI request failed with status ${response.statusCode}: ${body}`));
            return;
          }

          try {
            resolve(JSON.parse(body));
          } catch (error) {
            reject(error);
          }
        });
      }
    );

    request.on("error", reject);
    request.write(requestBody);
    request.end();
  });
}

function extractResponseText(result) {
  if (!result || !Array.isArray(result.output)) {
    return "";
  }

  return result.output
    .filter((item) => item.type === "message" && Array.isArray(item.content))
    .flatMap((item) => item.content)
    .filter((content) => content.type === "output_text" && typeof content.text === "string")
    .map((content) => content.text)
    .join("");
}

io.on("connection", (socket) => {
  socket.emit("systemUpdate", systemData);

  socket.on("demoMode", (mode) => {
    if (["normal", "stress", "priority"].includes(mode)) {
      systemData.mode = mode;
      applyModeProfile();
      io.emit("systemUpdate", systemData);
    }
  });
});

setInterval(() => {
  applyModeProfile();
  io.emit("systemUpdate", systemData);
}, 1400);

app.get("/api/system", (req, res) => {
  res.json(systemData);
});

app.get("/api/performance", (req, res) => {
  const cpuBaseline = systemData.mode === "stress" ? 76 : systemData.mode === "priority" ? 58 : 44;
  const memoryBaseline = systemData.mode === "stress" ? 71 : systemData.mode === "priority" ? 55 : 46;

  res.json({
    cpuHistory: buildPerformanceHistory(cpuBaseline, 12),
    memoryHistory: buildPerformanceHistory(memoryBaseline, 10)
  });
});

app.post("/api/adapt", (req, res) => {
  const target = req.body?.target || "P1";
  const response = {
    success: true,
    adaptation: {
      action: "REALLOCATE",
      target,
      cpuDelta: Number(randomDelta(14).toFixed(1)),
      memoryDelta: Math.round(randomDelta(48)),
      timestamp: new Date().toISOString(),
      confidence: Number((0.9 + Math.random() * 0.09).toFixed(2))
    }
  };

  systemData.metrics.adaptations += 1;
  res.json(response);
});

app.get("/api/system-info", (req, res) => {
  res.json({
    platform: os.platform(),
    arch: os.arch(),
    cpus: os.cpus().length,
    totalMemory: `${Math.round(os.totalmem() / 1024 / 1024 / 1024)} GB`,
    uptime: `${Math.round(os.uptime() / 60)} minutes`,
    nodeVersion: process.version
  });
});

app.get("/api/ml-predict", (req, res) => {
  res.json({
    nextCpuPeak: Math.round(clamp(systemData.cpu.usage + 11, 20, 99)),
    memoryDemand: Math.round(clamp(systemData.memory.usage + 8, 25, 99)),
    recommendation: "INCREASE_PRIORITY_FOR_P1",
    confidence: 0.94
  });
});

app.post("/api/ai-insights", async (req, res) => {
  const apiKey = req.body?.apiKey?.trim();

  if (!apiKey) {
    res.status(400).json({ error: "Missing OpenAI API key." });
    return;
  }

  const prompt = `
You are an operating-systems optimization assistant for a project called ARAMS.
Analyze the following live multiprogramming metrics and respond as compact JSON with keys:
"summary", "primaryRisk", "recommendedAction", "expectedImpact".
Keep each value under 35 words and focus on CPU and memory reallocation advice.

Metrics:
${JSON.stringify(systemData, null, 2)}
  `.trim();

  try {
    const result = await callOpenAI(apiKey, {
      model: "gpt-4.1-mini",
      input: [
        {
          role: "system",
          content: [
            {
              type: "input_text",
              text: "You are an operating-systems optimization assistant for a project called ARAMS."
            }
          ]
        },
        {
          role: "user",
          content: [
            {
              type: "input_text",
              text: prompt
            }
          ]
        }
      ],
      text: {
        format: {
          type: "json_schema",
          name: "resource_insight",
          strict: true,
          schema: {
            type: "object",
            additionalProperties: false,
            properties: {
              summary: { type: "string" },
              primaryRisk: { type: "string" },
              recommendedAction: { type: "string" },
              expectedImpact: { type: "string" }
            },
            required: ["summary", "primaryRisk", "recommendedAction", "expectedImpact"]
          }
        }
      }
    });

    const outputText = extractResponseText(result);

    if (!outputText) {
      throw new Error("OpenAI returned an empty response.");
    }

    const insight = JSON.parse(outputText);
    res.json({ insight });
  } catch (error) {
    res.status(500).json({
      error: "Unable to generate AI insight right now.",
      detail: error.message
    });
  }
});

app.get("/", (req, res) => {
  res.sendFile(path.join(publicDir, "index.html"));
});

pages.forEach((page) => {
  app.get(`/${page}`, (req, res) => {
    res.sendFile(path.join(publicDir, page));
  });
});

app.get("/health", (req, res) => {
  res.json({ status: "healthy", timestamp: new Date().toISOString() });
});

app.use((req, res) => {
  res.status(404).json({ error: "Page not found" });
});

app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({ error: "Unexpected server error" });
});

const PORT = process.env.PORT || 3001;

applyModeProfile();

server.listen(PORT, () => {
  console.log(`ARAMS Professional site running at http://localhost:${PORT}`);
});
