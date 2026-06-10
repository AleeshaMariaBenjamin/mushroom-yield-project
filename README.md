\# Environment Setup



1\. Installed Python 3.10

2\. Created virtual environment (venv)

3\. Installed pandas, numpy, matplotlib, scikit-learn and jupyter

4\. Ran test.py successfully

# Mushroom Yield Project

## Problem Statement

Predict mushroom yield using environmental sensor data such as temperature, humidity, and CO2.

## Project Structure

mushroom-yield-project/
│
├── data/
├── models/
├── notebooks/
├── src/
│   └── smoke_test.py
├── requirements.txt
├── .gitignore
└── README.md

## Setup

1. Create virtual environment
2. Activate virtual environment
3. Install requirements

```bash
pip install -r requirements.txt
  

  
## Dataset Columns

- timestamp: Date and time of sensor reading
- temperature: Temperature inside the polyhouse (°C)
- humidity: Relative humidity (%)
- CO2: Carbon dioxide concentration (ppm)
- yield: Mushroom yield harvested


## Features

- temperature: Polyhouse temperature (°C)
- humidity: Relative humidity (%)
- co2: Carbon dioxide concentration (ppm)
- temp_humidity_interaction: Temperature × Humidity interaction feature
Chronological Train-Test Split

The dataset was sorted by timestamp before splitting. An 80/20 chronological split was performed to prevent future information leakage.

Training Period:
2025-01-01 06:00:00 to 2025-01-17 21:00:00

Testing Period:
2025-01-17 22:00:00 to 2025-01-22 01:00:00

Training Rows: 400
Testing Rows: 100

MinMaxScaler was fitted only on the training data and then applied to the test data using the same scaling parameters. The train dataset, test dataset, and scaler object were saved under data/processed for reproducibility.


Target:
- yield: Mushroom yield harvested (kg)

## Author

Aleesha Benjamin