# Data Cleaning Log

## Dataset Information
- Source: Polyhouse sensor data
- Input: data/interim/01_loaded.csv
- Output: data/processed/02_cleaned.parquet

## Missing Value Handling
- Filled missing temperature values with column mean
- Filled missing humidity values with column mean
- Filled missing CO2 values with column mean

## Data Validation Rules
- Removed duplicate rows
- Kept humidity between 0 and 100
- Removed rows where CO2 <= 0

## Output
- Original rows: 500
- Final clean rows: 500
- Saved to data/processed/02_cleaned.parquet
