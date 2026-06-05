import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data
df = pd.read_parquet("data/processed/02_cleaned.parquet")

os.makedirs("reports/figures", exist_ok=True)

# --- 1. Correlation Heatmap ---
plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("reports/figures/correlation_heatmap.png")
plt.close()

# --- 2. Scatter: Humidity vs Yield ---
plt.figure()
plt.scatter(df["humidity"], df["yield"], alpha=0.5)
plt.xlabel("Humidity (%)")
plt.ylabel("Yield (kg)")
plt.title("Humidity vs Yield")
plt.tight_layout()
plt.savefig("reports/figures/humidity_vs_yield.png")
plt.close()

# --- 3. Scatter: Temperature vs Yield ---
plt.figure()
plt.scatter(df["temperature"], df["yield"], alpha=0.5, color="orange")
plt.xlabel("Temperature (°C)")
plt.ylabel("Yield (kg)")
plt.title("Temperature vs Yield")
plt.tight_layout()
plt.savefig("reports/figures/temperature_vs_yield.png")
plt.close()

# --- 4. Scatter: CO2 vs Yield ---
plt.figure()
plt.scatter(df["CO2"], df["yield"], alpha=0.5, color="green")
plt.xlabel("CO2 (ppm)")
plt.ylabel("Yield (kg)")
plt.title("CO2 vs Yield")
plt.tight_layout()
plt.savefig("reports/figures/co2_vs_yield.png")
plt.close()

print("All figures saved to reports/figures/")