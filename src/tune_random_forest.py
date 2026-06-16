import pandas as pd
import numpy as np
import joblib
import json

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# -------------------------------------------------------
# 1. Load data
# -------------------------------------------------------
train_df = pd.read_csv("data/processed/train.csv")
test_df = pd.read_csv("data/processed/test.csv")

# Recreate interaction feature
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
y_train = train_df["yield"]

X_test = test_df[features]
y_test = test_df["yield"]

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

# -------------------------------------------------------
# 2. Define the hyperparameter grid
# -------------------------------------------------------
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 5, 10],
    "min_samples_leaf": [1, 2, 4]
}

# -------------------------------------------------------
# 3. TimeSeriesSplit cross-validator
# -------------------------------------------------------
tscv = TimeSeriesSplit(n_splits=5)

# -------------------------------------------------------
# 4. Grid Search
# -------------------------------------------------------
print("\nRunning Grid Search...")
print("Trying", 3 * 3 * 3, "combinations x 5 folds =", 3*3*3*5, "fits")

base_rf = RandomForestRegressor(random_state=42)

grid_search = GridSearchCV(
    estimator=base_rf,
    param_grid=param_grid,
    cv=tscv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train, y_train)

# -------------------------------------------------------
# 5. Best parameters
# -------------------------------------------------------
print("\n==============================")
print("GRID SEARCH RESULTS")
print("==============================")
print("Best Parameters:", grid_search.best_params_)
print(
    "Best CV MAE:",
    round(-grid_search.best_score_, 4)
)

# -------------------------------------------------------
# 6. Evaluate tuned RF on test set
# -------------------------------------------------------
tuned_rf = grid_search.best_estimator_

y_pred_tuned = tuned_rf.predict(X_test)

tuned_mae = mean_absolute_error(y_test, y_pred_tuned)
tuned_rmse = np.sqrt(mean_squared_error(y_test, y_pred_tuned))
tuned_r2 = r2_score(y_test, y_pred_tuned)

print("\n==============================")
print("TUNED RF — TEST SET METRICS")
print("==============================")
print("MAE :", round(tuned_mae, 4))
print("RMSE:", round(tuned_rmse, 4))
print("R²  :", round(tuned_r2, 4))

# -------------------------------------------------------
# 7. Load existing metrics for comparison
# -------------------------------------------------------
# Linear Regression metrics (from metrics_linear.json)
lr_mae = 0.0823
lr_rmse = 0.1066
lr_r2 = 0.7722

# Default RF metrics (from train_random_forest.py output)
default_rf_mae = 0.0620
default_rf_rmse = 0.0991
default_rf_r2 = 0.8033

print("\n==============================")
print("FULL COMPARISON")
print("==============================")
print(f"{'Model':<25} {'MAE':>8} {'RMSE':>8} {'R²':>8}")
print("-" * 52)
print(f"{'Linear Regression':<25} {lr_mae:>8.4f} {lr_rmse:>8.4f} {lr_r2:>8.4f}")
print(f"{'Default Random Forest':<25} {default_rf_mae:>8.4f} {default_rf_rmse:>8.4f} {default_rf_r2:>8.4f}")
print(f"{'Tuned Random Forest':<25} {tuned_mae:>8.4f} {tuned_rmse:>8.4f} {tuned_r2:>8.4f}")

# -------------------------------------------------------
# 8. Save champion model
# -------------------------------------------------------
# Champion = model with lowest MAE on test set
models = {
    "Linear Regression": (lr_mae, None),
    "Default RF": (default_rf_mae, None),
    "Tuned RF": (tuned_mae, tuned_rf)
}

champion_name = min(models, key=lambda k: models[k][0])
print("\n==============================")
print("CHAMPION MODEL:", champion_name)
print("==============================")

joblib.dump(tuned_rf, "models/champion.joblib")
print("Champion saved to models/champion.joblib")

# -------------------------------------------------------
# 9. Save tuning metrics to JSON
# -------------------------------------------------------
tuning_results = {
    "best_params": grid_search.best_params_,
    "best_cv_mae": round(-grid_search.best_score_, 4),
    "test_metrics": {
        "MAE": round(tuned_mae, 4),
        "RMSE": round(tuned_rmse, 4),
        "R2": round(tuned_r2, 4)
    }
}

with open("reports/tuning_results.json", "w") as f:
    json.dump(tuning_results, f, indent=4)

print("Tuning results saved to reports/tuning_results.json")


import json

features = [
    "temperature",
    "humidity",
    "CO2",
    "temp_humidity_interaction"
]

with open("models/feature_list.json", "w") as f:
    json.dump(features, f)