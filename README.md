# ARAMS | Adaptive Resource Allocation Management System

ARAMS is a professional, web-based simulation and demonstration platform for an Operating Systems concept: **Adaptive Resource Allocation in Multiprogramming Environments**. 

It monitors simulated live CPU and memory pressure, predicts resource contention, and reallocates resources proactively before system performance drops.

## 🚀 Features

- **Continuous Telemetry:** Live system monitoring captures pressure trends and keeps allocation decisions grounded in current state.
- **Predictive Adaptation:** Forecasting logic anticipates saturation before it becomes a bottleneck and triggers proactive balancing.
- **Operational Resilience:** Priority-aware scheduling keeps essential workloads responsive even during high-demand conditions.
- **Live Interactive Demo:** Real-time dashboard powered by **Socket.IO** and **Chart.js**, visualizing CPU/Memory meters, process states, and AI-driven insights.
- **AI Integration:** Uses OpenAI's API to analyze live multiprogramming metrics and provide intelligent reallocation recommendations.

## 🛠️ Technology Stack

- **Backend:** Node.js, Express.js
- **Real-Time Communication:** Socket.IO
- **Frontend:** HTML5, CSS3 (Modern Glassmorphism & Animations), Vanilla JavaScript
- **Data Visualization:** Chart.js
- **AI Analytics:** OpenAI API

## 💻 Running Locally

### Prerequisites
- [Node.js](https://nodejs.org/) installed (v16 or higher recommended).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BandiPranayKumar/os-project.git
   cd os-project
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

4. **View the app:**
   Open your browser and navigate to `http://localhost:3001`

## ☁️ Deployment

This project is configured to be easily deployed on platform-as-a-service providers like **Render**.

### Deploying to Render
1. Create a new **Web Service** on Render.
2. Connect this GitHub repository.
3. Keep the "Root Directory" empty.
4. Set the Build Command to `npm install`.
5. Set the Start Command to `npm start`.
6. Select the **Free** instance type and click Deploy!

*(Note: Render automatically injects the `PORT` environment variable, which `server.js` is already configured to accept.)*

## 📁 Project Structure

```text
/
├── public/                 # Frontend static assets (HTML, CSS, JS)
│   ├── index.html          # Landing Page
│   ├── demo.html           # Live Simulator Dashboard
│   ├── system.html         # Architecture explanation
│   ├── style.css           # Styling with variables & animations
│   └── script.js           # Client-side logic & Socket.IO events
├── server.js               # Express server & backend API
├── package.json            # Node.js dependencies
└── README.md               # Project documentation
```

## 📜 License
ISC License
