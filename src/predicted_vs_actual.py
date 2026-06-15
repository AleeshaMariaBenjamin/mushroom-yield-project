import pandas as pd
import joblib
import matplotlib.pyplot as plt

test_df = pd.read_csv("data/processed/test.csv")

test_df["temp_humidity_interaction"] = (
    test_df["temperature"] * test_df["humidity"]
)

features = [
    "temperature",
    "humidity",
    "CO2",
    "temp_humidity_interaction"
]

X_test = test_df[features]
y_test = test_df["yield"]

model = joblib.load(
    "models/random_forest_tuned.pkl"
)

predictions = model.predict(X_test)

plt.figure(figsize=(8,6))
plt.scatter(y_test, predictions)

plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("Predicted vs Actual Yield")

plt.savefig(
    "reports/predicted_vs_actual.png"
)

