# Smart Energy Microgrid & Demand Forecasting Engine
**Team:** Bucephala | **Event:** HackSphere 3.0

## 🌐 Live Catalyst Deployment
- **Live App URL:** [https://teambucephalas-submi-cnjmgfct.onslate.in](https://teambucephalas-submi-cnjmgfct.onslate.in)
- **Deployment Platform:** Zoho Catalyst Slate

---

## ⚡ Overview
An autonomous smart microgrid energy management and demand forecasting engine. The system predicts forthcoming electricity loads using machine learning regression and automates power distribution decisions to avoid peak grid stress and blackouts.

## 🛠️ Architecture & Tech Stack
- **Zoho Catalyst QuickML:** Model training and endpoint serving for energy load forecasting.
- **Python Inference (`predict.py`):** Telemetry mapping, model querying, and dynamic grid mode switching.
- **Zoho Catalyst Slate:** Cloud edge deployment hosting the project status dashboard.

## 🔄 Grid Control Logic
- `NORMAL_GRID_MODE`: Baseline grid operation (demand $\le$ 160 kW during off-peak hours).
- `STORAGE_MODE`: Discharges auxiliary battery storage during evening peak hours (18:00–22:00) or high demand (>160 kW).
- `CRITICAL_ALERT`: Triggers emergency shedding alerts if demand reaches or exceeds 200 kW.

## 🚀 Local Evaluation
```bash
pip install -r requirements.txt
python test_eval.py
