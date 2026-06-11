import pandas as pd
import numpy as np

from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load training data only
train_df = pd.read_csv(
    "data/processed/train.csv"
)

# Features and target
X = train_df.drop(
    columns=["yield", "timestamp"]
)

y = train_df["yield"]

print("Feature shape:", X.shape)
print("Target shape:", y.shape)

# Time Series Cross Validation
tscv = TimeSeriesSplit(
    n_splits=5
)

# -----------------------------
# Linear Regression CV
# -----------------------------
print("\n==============================")
print("LINEAR REGRESSION CV")
print("==============================")

lr_maes = []

for fold, (train_idx, val_idx) in enumerate(
    tscv.split(X),
    start=1
):

    X_train = X.iloc[train_idx]
    X_val = X.iloc[val_idx]

    y_train = y.iloc[train_idx]
    y_val = y.iloc[val_idx]

    model = LinearRegression()

    model.fit(
        X_train,
        y_train
    )

    y_pred = model.predict(
        X_val
    )

    mae = mean_absolute_error(
        y_val,
        y_pred
    )

    lr_maes.append(mae)

    print(
        f"Fold {fold} MAE: {mae:.4f}"
    )

print(
    "\nLinear Regression Average MAE:",
    round(np.mean(lr_maes), 4)
)

# -----------------------------
# Random Forest CV
# -----------------------------
print("\n==============================")
print("RANDOM FOREST CV")
print("==============================")

rf_maes = []
rf_train_maes = []

for fold, (train_idx, val_idx) in enumerate(
    tscv.split(X),
    start=1
):

    X_train = X.iloc[train_idx]
    X_val = X.iloc[val_idx]

    y_train = y.iloc[train_idx]
    y_val = y.iloc[val_idx]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    # Validation prediction
    y_pred = model.predict(
        X_val
    )

    val_mae = mean_absolute_error(
        y_val,
        y_pred
    )

    rf_maes.append(val_mae)

    # Training prediction (for overfitting analysis)
    train_pred = model.predict(
        X_train
    )

    train_mae = mean_absolute_error(
        y_train,
        train_pred
    )

    rf_train_maes.append(train_mae)

    print(
        f"Fold {fold} Train MAE: {train_mae:.4f}"
    )

    print(
        f"Fold {fold} Validation MAE: {val_mae:.4f}"
    )

print(
    "\nRandom Forest Average Validation MAE:",
    round(np.mean(rf_maes), 4)
)

print(
    "Random Forest Average Train MAE:",
    round(np.mean(rf_train_maes), 4)
)

# -----------------------------
# Summary
# -----------------------------
print("\n==============================")
print("SUMMARY")
print("==============================")

print(
    "Linear Regression Avg MAE:",
    round(np.mean(lr_maes), 4)
)

print(
    "Random Forest Avg MAE:",
    round(np.mean(rf_maes), 4)
)

if np.mean(rf_maes) < np.mean(lr_maes):
    print(
        "\nRandom Forest performed better in cross-validation."
    )
else:
    print(
        "\nLinear Regression performed better in cross-validation."
    )