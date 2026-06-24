1. Problem Statement & Data Description

Goal: Predict mushroom yield using polyhouse sensor readings.
Inputs:
Temperature
Humidity
CO₂
Target:
Mushroom Yield (kg)
Dataset source and number of records.

2. Data Cleaning & EDA Highlights

Removed missing values.
Checked data quality.
Created interaction feature:
Temperature × Humidity
Performed exploratory analysis.
Observed relationships between environmental conditions and yield.

3. Modeling & Evaluation

Temporal train-test split used.
Models trained:
Linear Regression
Random Forest Regressor
Metrics:
MAE
RMSE
R² Score
Champion model selected based on performance.

4. Deployment & Monitoring
Streamlit application developed.
Public deployment URL.
User inputs collected through sliders.
Prediction logging strategy.
Retraining triggers documented.


5. Limitations

Small dataset.
Limited environmental features.
Model may not generalize to all farms.
Requires periodic retraining.

6. Future Work

Add additional sensor features.
Real-time IoT integration.
Automatic retraining pipeline.
Cloud database for prediction logs.

7. Conclusion

Successfully built an end-to-end ML pipeline.
Completed data preparation, modeling, evaluation, deployment, and monitoring.

Live Application:https://aleeshamariabenjamin-mushroom-yield-project-app-ozckve.streamlit.app/