import pandas as pd

# Load data
df = pd.read_csv("data/interim/01_loaded.csv")
print("Columns in dataset:")
print(df.columns.tolist())
print("Rows in dataset:", len(df))
print("Original Shape:", df.shape)

# Step 1 - Handle missing values
print("\nMissing Values Before:")
print(df.isnull().sum())

df["temperature"] = df["temperature"].fillna(df["temperature"].mean())
df["humidity"] = df["humidity"].fillna(df["humidity"].mean())
df["CO2"] = df["CO2"].fillna(df["CO2"].mean())

print("\nMissing Values After:")
print(df.isnull().sum())

# Step 2 - Remove duplicates
before_dup = len(df)
df = df.drop_duplicates()
after_dup = len(df)
print(f"\nDuplicates removed: {before_dup - after_dup}")


# Step 3 - Validity rules
before_filter = len(df)
df = df[df["humidity"] >= 0]
df = df[df["humidity"] <= 100]
df = df[df["CO2"] > 0]
after_filter = len(df)
print(f"Rows removed by validity rules: {before_filter - after_filter}")

print("\nCleaned Shape:", df.shape)

# Step 4 - Save cleaned data
df.to_parquet("data/processed/02_cleaned.parquet", index=False)
print("Saved to data/processed/02_cleaned.parquet")

# Step 5 - Write cleaning log
with open("cleaning_log.md", "w") as f:
    f.write("# Data Cleaning Log\n\n")

    f.write("## Dataset Information\n")
    f.write("- Source: Polyhouse sensor data\n")
    f.write("- Input: data/interim/01_loaded.csv\n")
    f.write("- Output: data/processed/02_cleaned.parquet\n\n")

    f.write("## Missing Value Handling\n")
    f.write("- Filled missing temperature values with column mean\n")
    f.write("- Filled missing humidity values with column mean\n")
    f.write("- Filled missing CO2 values with column mean\n\n")

    f.write("## Data Validation Rules\n")
    f.write("- Removed duplicate rows\n")
    f.write("- Kept humidity between 0 and 100\n")
    f.write("- Removed rows where CO2 <= 0\n\n")

    f.write("## Output\n")
    f.write(f"- Original rows: {before_dup}\n")
    f.write(f"- Final clean rows: {after_filter}\n")
    f.write("- Saved to data/processed/02_cleaned.parquet\n")

print("Cleaning completed.")
