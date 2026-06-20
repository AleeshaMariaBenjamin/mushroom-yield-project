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


## Run Inference

This project includes a trained champion Random Forest model for mushroom yield prediction.

### Prerequisites

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Project Artifacts

The following files are required for inference:

```text
models/
├── champion.joblib
├── minmax_scaler.joblib
└── feature_list.json
```

### Making a Prediction

Use the `predict_yield()` function from `predict.py`.

Example:

```python
from src.predict import predict_yield

prediction = predict_yield(
    temperature=25,
    humidity=80,
    CO2=1000
)

print(
    f"Predicted Yield: {prediction}"
)
```

### Running the Test Script

Execute:

```bash
python src/test_predict.py
```

Example output:

```text
Predicted Yield: 1.0905799157567575
```

### Verification of Inference Pipeline

The prediction pipeline was verified by comparing outputs from the public inference function (`predict_yield`) with direct model predictions using identical inputs.

Verification result:

```text
Predicted Yield: 1.0905799157567575
Prediction:      1.0905799157567575
```

Both outputs matched exactly, confirming that the inference pipeline loads the model, scaler, and feature list correctly and produces consistent predictions.

### Input Features

The model expects the following inputs:

* Temperature
* Humidity
* CO2

The feature `temp_humidity_interaction` is generated automatically during inference.

### Champion Model

The selected champion model is the tuned Random Forest Regressor obtained through GridSearchCV hyperparameter tuning and evaluated on an untouched test set.


## Streamlit Application

Run the web application:

```bash
streamlit run app.py
```

The application accepts:

* Temperature (°C)
* Humidity (%)
* CO₂ (ppm)

and predicts mushroom yield using the trained Random Forest champion model.

### Example Input

* Temperature = 25°C
* Humidity = 80%
* CO₂ = 1000 ppm

### Example Output

Predicted Yield = 1.09 kg

A screenshot of the application is available in:

```text
reports/streamlit_app.png
```
Test Scenario Table

| Test Case         | Temperature | Humidity | CO₂  | Expected Behavior                                     |
| ----------------- | ----------- | -------- | ---- | ----------------------------------------------------- |
| Normal Conditions | 24          | 80       | 900  | Prediction should be reasonable and positive          |
| High Temperature  | 32          | 80       | 900  | Yield may decrease compared to optimal conditions     |
| Low Humidity      | 24          | 50       | 900  | Prediction should change noticeably                   |
| High CO₂          | 24          | 80       | 1500 | Prediction should increase or vary depending on model |
| Extreme Inputs    | 40          | 20       | 2000 | Prediction still generated without crashing           |
| Boundary Inputs   | 0           | 0        | 0    | Model returns valid numeric output                    |
