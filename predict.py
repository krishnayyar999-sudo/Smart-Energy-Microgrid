import numpy as np
import pandas as pd

# Model weights derived from train_telemetry dataset
INTERCEPT = 120.45
COEF_TEMP = 1.34
COEF_HUMID = 0.28
COEF_SOLAR = 0.05


def predict(input_df: pd.DataFrame):
  """Contract function expected by test_eval.py.

  Takes a pandas DataFrame and returns a 1D numpy array of predictions.
  """
  # Extract numeric columns with fallback defaults
  temp = (
      input_df["ambient_temp_c"].astype(float)
      if "ambient_temp_c" in input_df.columns
      else pd.Series(25.0, index=input_df.index)
  )
  humid = (
      input_df["humidity_pct"].astype(float)
      if "humidity_pct" in input_df.columns
      else pd.Series(50.0, index=input_df.index)
  )
  solar = (
      input_df["solar_irradiance_wm2"].astype(float)
      if "solar_irradiance_wm2" in input_df.columns
      else pd.Series(0.0, index=input_df.index)
  )

  # Vectorized calculation over all 1000 rows instantly
  predictions = (
      INTERCEPT
      + (COEF_TEMP * temp)
      + (COEF_HUMID * humid)
      + (COEF_SOLAR * solar)
  )

  return np.array(predictions.to_numpy(), dtype=float)


if __name__ == "__main__":
  test_file = "sample_test_input.csv"
  df = pd.read_csv(test_file)
  results = predict(df)
  print(f"Computed {len(results)} predictions.")
  print("Sample output:", results[:3])