# Smart Energy Microgrid & Demand Forecasting Engine
**HackSphere 3.0 Submission**

## Architecture Overview
- **Data Ingestion & Training:** Historical telemetry (`train_telemetry.csv`) trained using Zoho Catalyst QuickML (Random Forest Regressor).
- **Inference Pipeline:** Preprocessed telemetry inputs (`ambient_temp_c`, `humidity_pct`, `solar_irradiance_wm2`) routed through QuickML endpoints for demand forecasting.
- **Smart Switching Rules:** 
  - `NORMAL_GRID_MODE`: Baseline grid operation.
  - `STORAGE_MODE`: Peak hours (18:00 - 22:00) or high demand (>160 kW).
  - `CRITICAL_ALERT`: Overload threshold exceeded (>=200 kW).

## Local Verification
1. Activate virtual environment:
   ```bash
   .\.venv\Scripts\Activate.ps1