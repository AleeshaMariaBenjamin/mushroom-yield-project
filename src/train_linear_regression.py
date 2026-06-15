import pandas as pd
import joblib
import json
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
train_df = pd.read_csv(
    "data/processed/train.csv"
)

test_df = pd.read_csv(
    "data/processed/test.csv"
)
scaler = joblib.load(
    "data/processed/minmax_scaler.pkl"
)
train_df["temp_humidity_interaction"] = (
    train_df["temperature"] * train_df["humidity"]
)
test_df["temp_humidity_interaction"] = (
    test_df["temperature"] * test_df["humidity"]
)

features = [
    "temperature",
    "humidity",
    "CO2",
    "temp_humidity_interaction"
]
X_train = train_df[features]
X_test = test_df[features]

y_train = train_df["yield"]
y_test = test_df["yield"]
X_train_scaled = scaler.transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)
model = LinearRegression()

model.fit(
    X_train_scaled,
    y_train
)
train_preds = model.predict(
    X_train_scaled
)
test_preds = model.predict(
    X_test_scaled
)
mae = mean_absolute_error(
    y_test,
    test_preds
)


rmse = np.sqrt(
    mean_squared_error(
        y_test,
        test_preds
    )
)
r2 = r2_score(
    y_test,
    test_preds
)
print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)

print("\nCoefficients:")

for feature, coef in zip(features, model.coef_):
    print(feature, ":", coef)

metrics = {
    "MAE": float(mae),
    "RMSE": float(rmse),
    "R2": float(r2)
}

with open("reports/metrics_linear.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("\nMetrics saved to reports/metrics_linear.json")

joblib.dump(model, "models/linear_regression.joblib")
print("Model saved to models/linear_regression.joblib")