import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

df = pd.read_parquet(
    "data/processed/02_cleaned.parquet"
)
print(df.columns)
df["timestamp"] = pd.to_datetime(
    df["timestamp"]
)
df = df.sort_values("timestamp")
print(df["timestamp"].head())
print(df["timestamp"].tail())
split_idx = int(len(df) * 0.8)

train_df = df.iloc[:split_idx]

test_df = df.iloc[split_idx:]
print("Train size:", len(train_df))
print("Test size:", len(test_df))

print("Train starts:",
      train_df["timestamp"].min())

print("Train ends:",
      train_df["timestamp"].max())

print("Test starts:",
      test_df["timestamp"].min())

print("Test ends:",
      test_df["timestamp"].max())
assert (
    train_df["timestamp"].max()
    <
    test_df["timestamp"].min()
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
scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)
X_test_scaled = scaler.transform(
    X_test
)
train_df.to_csv(
    "data/processed/train.csv",
    index=False
)
test_df.to_csv(
    "data/processed/test.csv",
    index=False
)
joblib.dump(
    scaler,
    "data/processed/minmax_scaler.pkl"
)
print("Chronological split complete")
print("Train CSV saved")
print("Test CSV saved")
print("Scaler saved")