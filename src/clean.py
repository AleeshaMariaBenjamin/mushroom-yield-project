import pandas as pd

# Load data
df = pd.read_csv("data/interim/01_loaded.csv")
print("\nColumns in dataset:")
print(df.columns)

print("Original Shape:", df.shape)

# Missing values report
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Validity rules
df = df[df["humidity"] >= 0]
df = df[df["humidity"] <= 100]
df = df[df["CO2"] > 0]

# Save cleaned data
df.to_csv("data/processed/02_cleaned.csv", index=False)

print("\nCleaned Shape:", df.shape)

# Cleaning log
with open("cleaning_log.md", "w") as f:
    f.write("# Cleaning Log\n")
    f.write("- Removed duplicate rows\n")
    f.write("- Kept humidity between 0 and 100\n")
    f.write("- Removed rows with CO2 <= 0\n")

print("Cleaning completed.")