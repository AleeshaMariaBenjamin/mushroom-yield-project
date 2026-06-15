import pandas as pd
import joblib
import json
import time

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.metrics import mean_absolute_error

train_df = pd.read_csv("data/processed/train.csv")
test_df = pd.read_csv("data/processed/test.csv")
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

tscv = TimeSeriesSplit(n_splits=5)

param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [5, 10, None],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2]
}

rf = RandomForestRegressor(
    random_state=42
)

start_time = time.time()

grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=tscv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1
)
grid_search.fit(
    X_train,
    y_train
)

end_time = time.time()

runtime = end_time - start_time

print(f"Runtime: {runtime:.2f} seconds")

best_params = grid_search.best_params_

print(best_params)

best_model = grid_search.best_estimator_
predictions = best_model.predict(
    X_test
)

mae = mean_absolute_error(
    y_test,
    predictions
)

print("Test MAE:", mae)

joblib.dump(
    best_model,
    "models/random_forest_tuned.pkl"
)

with open(
    "models/best_params.json",
    "w"
) as f:
    json.dump(
        best_params,
        f,
        indent=4
    )