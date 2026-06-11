import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Load data
train_df = pd.read_csv(
    "data/processed/train.csv"
)

test_df = pd.read_csv(
    "data/processed/test.csv"
)

# Features and target
X_train = train_df.drop(
    columns=["yield", "timestamp"]
)

y_train = train_df["yield"]

X_test = test_df.drop(
    columns=["yield", "timestamp"]
)

y_test = test_df["yield"]

print("Training data shape:", X_train.shape)
print("Test data shape:", X_test.shape)

# Train model
rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(
    X_train,
    y_train
)

# Predictions
y_pred = rf.predict(
    X_test
)

# Metrics
mae = mean_absolute_error(
    y_test,
    y_pred
)

mse = mean_squared_error(
    y_test,
    y_pred
)

rmse = mse ** 0.5

r2 = r2_score(
    y_test,
    y_pred
)

print("\nRandom Forest Results")
print("---------------------")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)

# Feature importance
importance_df = pd.DataFrame({
    "Feature": X_train.columns,
    "Importance": rf.feature_importances_
})

print("\nFeature Importance")
print("------------------")
print(
    importance_df.sort_values(
        by="Importance",
        ascending=False
    )
)

# Plot feature importance
importance_df = (
    importance_df
    .sort_values(
        by="Importance",
        ascending=True
    )
)

importance_df.plot(
    x="Feature",
    y="Importance",
    kind="barh"
)

plt.tight_layout()

plt.savefig(
    "reports/feature_importance.png"
)

plt.close()

print("\nFeature importance plot saved to:")
print("reports/feature_importance.png")

# Save model
joblib.dump(
    rf,
    "models/random_forest.joblib"
)

print("\nModel saved to:")
print("models/random_forest.joblib")

# Verify saved model
loaded_model = joblib.load(
    "models/random_forest.joblib"
)

print("\nLoaded model type:")
print(type(loaded_model))