import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import r2_score
test_df = pd.read_csv(
    "data/processed/test.csv"
)

scaler = joblib.load(
    "data/processed/minmax_scaler.pkl"
)

model = joblib.load(
    "models/linear_regression.joblib"
)
features = [
    "temperature",
    "humidity",
    "CO2",
    "temp_humidity_interaction"
]

test_df["temp_humidity_interaction"] = (
    test_df["temperature"] * test_df["humidity"]
)

X_test = test_df[features]

y_test = test_df["yield"]

X_test_scaled = scaler.transform(
    X_test
)
y_pred = model.predict(
    X_test_scaled
)
residuals = y_test - y_pred
plt.figure(figsize=(8,5))

plt.scatter(
    y_pred,
    residuals
)

plt.axhline(
    0,
    linestyle="--"
)

plt.xlabel("Predicted Yield")
plt.ylabel("Residuals")

plt.title(
    "Residuals vs Predicted Yield"
)

plt.savefig(
    "reports/residuals_vs_predicted.png"
)

plt.close()
plt.figure(figsize=(8,5))

plt.scatter(
    test_df["humidity"],
    residuals
)

plt.xlabel("Humidity")
plt.ylabel("Residuals")
plt.title("Residuals vs Humidity")

plt.savefig(
    "reports/residual_vs_humidity_linear.png"
)

plt.close()
r2 = r2_score(
    y_test,
    y_pred
)