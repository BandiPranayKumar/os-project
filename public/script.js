class ARAMSApp {
  constructor() {
    this.socket = null;
    this.chart = null;
    this.currentMode = "normal";
    this.init();
  }

  init() {
    this.injectGravityField();
    this.setupNavigation();
    this.setupReveals();
    this.setupCounters();
    this.setupForm();
    this.setupRealtime();
    this.setupModeButtons();
    this.setupInsightGenerator();
  }

  injectGravityField() {
    const field = document.createElement("div");
    field.className = "gravity-field";

    for (let index = 0; index < 16; index += 1) {
      const orb = document.createElement("span");
      const size = 40 + Math.random() * 140;
      orb.className = "gravity-orb";
      orb.style.width = `${size}px`;
      orb.style.height = `${size}px`;
      orb.style.left = `${Math.random() * 100}%`;
      orb.style.top = `${20 + Math.random() * 90}%`;
      orb.style.animationDuration = `${12 + Math.random() * 18}s`;
      orb.style.animationDelay = `${Math.random() * -20}s`;
      field.appendChild(orb);
    }

    document.body.prepend(field);
  }

  setupNavigation() {
    const page = document.body.dataset.page;
    const navLinks = document.querySelectorAll(".nav-link");
    navLinks.forEach((link) => {
      const href = link.getAttribute("href");
      const isHome = page === "home" && href === "index.html";
      if ((href && href.includes(page)) || isHome) {
        link.classList.add("is-active");
      }
    });

    const toggle = document.querySelector(".menu-toggle");
    const panel = document.querySelector(".nav-panel");

    if (toggle && panel) {
      toggle.addEventListener("click", () => {
        const expanded = toggle.getAttribute("aria-expanded") === "true";
        toggle.setAttribute("aria-expanded", String(!expanded));
        panel.classList.toggle("is-open");
      });
    }
  }

  setupReveals() {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
          }
        });
      },
      { threshold: 0.18 }
    );

    document.querySelectorAll(".reveal").forEach((item) => observer.observe(item));
  }

  setupCounters() {
    const counters = document.querySelectorAll("[data-counter]");
    const animate = (entry) => {
      const target = Number(entry.dataset.counter);
      const hasDecimal = String(target).includes(".");
      const duration = 1400;
      const start = performance.now();

      const step = (now) => {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const value = target * eased;
        entry.textContent = hasDecimal ? value.toFixed(1) : Math.round(value);
        if (progress < 1) {
          requestAnimationFrame(step);
        }
      };

      requestAnimationFrame(step);
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting && !entry.target.dataset.animated) {
          entry.target.dataset.animated = "true";
          animate(entry.target);
        }
      });
    });

    counters.forEach((counter) => observer.observe(counter));
  }

  setupForm() {
    const form = document.getElementById("contactForm");
    const feedback = document.getElementById("formFeedback");

    if (!form || !feedback) {
      return;
    }

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      feedback.textContent = "Sending...";
      await new Promise((resolve) => setTimeout(resolve, 900));
      form.reset();
      feedback.textContent = "Message submitted successfully.";
    });
  }

  setupRealtime() {
    if (!document.getElementById("performanceChart") && !document.getElementById("cpu-meter")) {
      return;
    }

    const socketScript = document.createElement("script");
    socketScript.src = "/socket.io/socket.io.js";
    socketScript.onload = () => {
      this.socket = io();
      this.socket.on("systemUpdate", (data) => {
        this.renderRealtime(data);
      });
    };
    document.head.appendChild(socketScript);

    if (document.getElementById("performanceChart")) {
      this.fetchChart();
    }
  }

  setupModeButtons() {
    const buttons = document.querySelectorAll(".mode-btn");
    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        buttons.forEach((item) => item.classList.remove("active"));
        button.classList.add("active");
        this.currentMode = button.dataset.mode;
        if (this.socket) {
          this.socket.emit("demoMode", this.currentMode);
        }
        this.fetchChart();
      });
    });
  }

  setupInsightGenerator() {
    const button = document.getElementById("generateInsightBtn");
    const input = document.getElementById("apiKeyInput");
    const feedback = document.getElementById("insightFeedback");

    if (!button || !input || !feedback) {
      return;
    }

    button.addEventListener("click", async () => {
      const apiKey = input.value.trim();

      if (!apiKey) {
        feedback.textContent = "Enter your OpenAI API key first.";
        return;
      }

      feedback.textContent = "Generating insight...";
      button.disabled = true;

      try {
        const response = await fetch("/api/ai-insights", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ apiKey })
        });
        const rawText = await response.text();
        let data = {};

        if (rawText.trim()) {
          try {
            data = JSON.parse(rawText);
          } catch (parseError) {
            throw new Error("Server returned an invalid response. Make sure the app is running from localhost.");
          }
        }

        if (!response.ok) {
          throw new Error(data.detail || data.error || "Insight request failed.");
        }

        if (!data.insight) {
          throw new Error("No AI insight was returned by the server.");
        }

        this.setText("insightSummary", data.insight.summary);
        this.setText("insightRisk", data.insight.primaryRisk);
        this.setText("insightAction", data.insight.recommendedAction);
        this.setText("insightImpact", data.insight.expectedImpact);
        feedback.textContent = "AI insight generated successfully.";
      } catch (error) {
        feedback.textContent = error.message || "Unable to generate insight right now.";
      } finally {
        button.disabled = false;
      }
    });
  }

  renderRealtime(data) {
    this.setWidth("cpu-meter", data.cpu.usage);
    this.setWidth("memory-meter", data.memory.usage);
    this.setWidth("demo-cpu", data.cpu.usage);
    this.setWidth("demo-memory", data.memory.usage);
    this.setWidth("efficiency-meter", data.metrics.efficiency);
    this.setText("cpu-value", `${Math.round(data.cpu.usage)}%`);
    this.setText("memory-value", `${Math.round(data.memory.usage)}%`);
    this.setText("efficiency-value", `${data.metrics.efficiency}%`);
    this.setText("process-count", String(data.processes.length));
    this.setText("throughput", String(data.metrics.throughput));
    this.setText("adaptations", String(data.metrics.adaptations));

    const tbody = document.getElementById("process-table-body");
    if (tbody) {
      tbody.innerHTML = data.processes
        .map(
          (process) => `
            <tr>
              <td>${process.id}</td>
              <td>${process.name}</td>
              <td>${process.cpu}%</td>
              <td>${process.memory} MB</td>
              <td><span class="priority-chip ${process.priority.toLowerCase()}">${process.priority}</span></td>
              <td><span class="status-chip ${process.status.toLowerCase()}">${process.status}</span></td>
            </tr>
          `
        )
        .join("");
    }
  }

  async fetchChart() {
    const canvas = document.getElementById("performanceChart");
    if (!canvas || typeof Chart === "undefined") {
      return;
    }

    const response = await fetch("/api/performance");
    const data = await response.json();

    const chartData = {
      labels: data.cpuHistory.map((item) => item.time),
      datasets: [
        {
          label: "CPU usage",
          data: data.cpuHistory.map((item) => item.value),
          borderColor: "#57c7ff",
          backgroundColor: "rgba(87, 199, 255, 0.14)",
          fill: true,
          tension: 0.35
        },
        {
          label: "Memory usage",
          data: data.memoryHistory.map((item) => item.value),
          borderColor: "#ffd166",
          backgroundColor: "rgba(255, 209, 102, 0.12)",
          fill: true,
          tension: 0.35
        }
      ]
    };

    if (this.chart) {
      this.chart.data = chartData;
      this.chart.update();
      return;
    }

    this.chart = new Chart(canvas, {
      type: "line",
      data: chartData,
      options: {
        maintainAspectRatio: false,
        plugins: {
          legend: {
            labels: {
              color: "#eef4ff"
            }
          }
        },
        scales: {
          x: {
            ticks: { color: "#9fb0cf" },
            grid: { color: "rgba(255,255,255,0.06)" }
          },
          y: {
            beginAtZero: true,
            max: 100,
            ticks: { color: "#9fb0cf" },
            grid: { color: "rgba(255,255,255,0.06)" }
          }
        }
      }
    });
  }

  setWidth(id, value) {
    const element = document.getElementById(id);
    if (element) {
      element.style.width = `${value}%`;
    }
  }

  setText(id, value) {
    const element = document.getElementById(id);
    if (element) {
      element.textContent = value;
    }
  }
}

document.addEventListener("DOMContentLoaded", () => {
  new ARAMSApp();
});
