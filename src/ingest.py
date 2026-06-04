import pandas as pd

df = pd.read_csv(
    "data/raw/polyhouse_sensors.csv",
    parse_dates=["timestamp"]
)

print(df.shape)
print(df.dtypes)
print(df.head())

df.to_csv(
    "data/interim/01_loaded.csv",
    index=False
)

print("Snapshot saved successfully!")