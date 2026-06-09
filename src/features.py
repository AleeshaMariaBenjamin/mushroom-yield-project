import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

df = pd.read_parquet("data/processed/02_cleaned.parquet")

print(df.columns)

features = ["temperature", "humidity", "CO2"]
df["temp_humidity_interaction"] = (
    df["temperature"] * df["humidity"]
)
features.append("temp_humidity_interaction")
X = df[features]
y = df["yield"]
print(X.isna().sum())
print(y.isna().sum())
scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(
    X_scaled,
    columns=features
)
print(X_scaled.min())
print(X_scaled.max())
joblib.dump(
    scaler,
    "models/minmax_scaler.joblib"
)
X_scaled.to_parquet(
    "data/processed/features.parquet"
)
print("X shape:", X.shape)
print("y shape:", y.shape)