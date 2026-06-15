import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load test data
test_df = pd.read_csv("data/processed/test.csv")

# Create interaction feature
test_df["temp_humidity_interaction"] = (
    test_df["temperature"] * test_df["humidity"]
)

# Features used during training
features = [
    "temperature",
    "humidity",
    "CO2",
    "temp_humidity_interaction"
]

# Split into X and y
X_test = test_df[features]
y_test = test_df["yield"]

# Load tuned Random Forest model
model = joblib.load(
    "models/random_forest_tuned.pkl"
)

# Make predictions
predictions = model.predict(X_test)

# Check sample counts
print("Test samples:", len(y_test))
print("Predictions:", len(predictions))

# Predicted vs Actual plot
plt.figure(figsize=(8, 6))

plt.scatter(
    y_test,
    predictions,
    alpha=0.7
)

# Perfect prediction reference line
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--',
    linewidth=2,
    label="Perfect Prediction"
)

plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("Predicted vs Actual Yield")
plt.legend()
plt.grid(True)

# Save plot
plt.savefig(
    "reports/predicted_vs_actual.png",
    bbox_inches="tight"
)



