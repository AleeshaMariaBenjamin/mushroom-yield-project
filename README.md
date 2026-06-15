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

Model                MAE     RMSE     R²
------------------------------------------
Linear Regression    
Random Forest   


Feature Importance Interpretation

CO2 was the most important feature for
predicting mushroom yield.

Humidity was the second most important
feature.

Temperature had the lowest influence.


Conclusion

Random Forest was compared with
Linear Regression.

The model achieved a lower error and
higher R² score, indicating better
prediction performance.

Therefore Random Forest is the preferred
model for this dataset.

## Champion Model

The Tuned Random Forest Regressor was selected as the champion model because it achieved the lowest Mean Absolute Error (MAE) on the untouched test dataset. The model demonstrated better predictive accuracy than both the Linear Regression model and the default Random Forest model. Therefore, it was chosen as the final model for mushroom yield prediction.
