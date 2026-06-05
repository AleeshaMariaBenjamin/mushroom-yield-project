import pandas as pd

df = pd.read_parquet("data/processed/02_cleaned.parquet")

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nSummary Statistics")
print(df.describe())

print("\nDate Range")

if "timestamp" in df.columns:
    print("Start:", df["timestamp"].min())
    print("End:", df["timestamp"].max())