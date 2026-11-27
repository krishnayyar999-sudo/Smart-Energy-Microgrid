# ⚡ Smart Energy Microgrid & Demand Forecasting Engine
**Autonomous Load Prediction & Dynamic Power Distribution System**

**Developed by [Krish Nayyar](https://github.com/krishnayyar999-sudo) (Team Bucephala)** | [LinkedIn](https://www.linkedin.com/in/krish-nayyar-071240420)  
Built for **Hacksphere 3.0 (ATMOS '26) — BITS Pilani, Hyderabad Campus**, powered by **Catalyst by Zoho**.

[![Live App](https://img.shields.io/badge/Live%20Deployment-Zoho%20Catalyst%20Slate-blue)](https://teambucephalas-submi-cnjmgfct.onslate.in)
[![Hackathon](https://img.shields.io/badge/Hackathon-Hacksphere%203.0%20%7C%20BITS%20Pilani-orange)](https://unstop.com/certificate-preview/96b07a81-6583-4d87-a9d7-aaa0dfde8380)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Zoho Catalyst](https://img.shields.io/badge/ML%20%26%20Cloud-Zoho%20Catalyst%20QuickML-green)](https://catalyst.zoho.com/)

---

## 🔗 Live Deployment & Verification
- **Live Dashboard (Zoho Catalyst Slate):** [Launch Smart Energy Microgrid Engine](https://teambucephalas-submi-cnjmgfct.onslate.in)
- **Hackathon Certificate:** [Verify Hacksphere 3.0 Certificate on Unstop](https://unstop.com/certificate-preview/96b07a81-6583-4d87-a9d7-aaa0dfde8380)
- **Team:** Bucephala (`Hacksphere 3.0 — BITS Pilani, Hyderabad Campus`)

---

## 📌 Overview
An autonomous smart microgrid energy management and demand forecasting engine. The system predicts forthcoming electricity loads using machine learning regression and automates real-time power distribution decisions to prevent peak grid stress, overload, and blackouts.

---

## 🔄 Automated Grid Control Logic

| Grid State | Trigger Condition | Automated Control Action |
| :--- | :--- | :--- |
| **`NORMAL_GRID_MODE`** | Predicted demand $\le$ 160 kW (off-peak hours) | Baseline utility grid supply; charges auxiliary battery reserves. |
| **`STORAGE_MODE`** | Evening peak window (18:00–22:00) **OR** demand > 160 kW | Discharges auxiliary battery storage to shave peak load and stabilize frequency. |
| **`CRITICAL_ALERT`** | Predicted demand $\ge$ 200 kW | Triggers emergency load-shedding alerts and isolates non-essential feeders. |

---

## 🛠️ Architecture & Tech Stack
- **ML Training & Endpoint Serving:** Zoho Catalyst QuickML (Regression-based electricity load forecasting)
- **Inference & Control Engine (`predict.py`):** Python telemetry mapping, QuickML endpoint querying, and dynamic grid state switching
- **Edge Deployment & Hosting:** Zoho Catalyst Slate (Live operational status dashboard)

---

## 🚀 Local Setup & Evaluation

1. **Clone this repository:**
   ```bash
   git clone [https://github.com/krishnayyar999-sudo/](https://github.com/krishnayyar999-sudo/)<YOUR-REPO-NAME>.git
   cd <YOUR-REPO-NAME>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the evaluation & inference test suite:**
   ```bash
   python test_eval.py
   ```

---

## 👤 Author
**Krish Nayyar** — Team Bucephala  
B.Tech in Computer Science & Engineering — Guru Nanak Dev University, Amritsar  
- **GitHub:** [github.com/krishnayyar999-sudo](https://github.com/krishnayyar999-sudo)  
- **LinkedIn:** [linkedin.com/in/krish-nayyar-071240420](https://www.linkedin.com/in/krish-nayyar-071240420)
