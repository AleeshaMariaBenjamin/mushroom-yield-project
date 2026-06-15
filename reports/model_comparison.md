# Model Comparison

## Performance Metrics

| Model             | MAE    | RMSE   | R²     |
| ----------------- | ------ | ------ | ------ |
| Linear Regression | 0.0823 | 0.1066 | 0.7722 |
| Random Forest     | 0.0620 | 0.0991 | 0.8033 |
|randomforest(tuned)|0.0610  |0.0965  | 0.8135 |
| Model | Test MAE |
|---------|---------|
| Linear Regression | 0.0823|
| Random Forest (Default) | 0.0620 |
| Random Forest (Tuned) | 0.0618 |

## Feature Importance (Random Forest)

| Feature     | Importance |
| ----------- | ---------- |
| Temperature | 0.691      |
| Humidity    | 0.169      |
| CO₂         | 0.140      |

## Linear Regression Coefficients

| Feature     | Coefficient |
| ----------- | ----------- |
| Temperature | 0.2679      |
| Humidity    | -0.3829     |
| CO₂         | 0.2813      |

## Analysis

The Random Forest model achieved better performance than the Linear Regression baseline across all evaluation metrics.

* MAE decreased from 0.0823 to 0.0620.
* RMSE decreased from 0.1066 to 0.0991.
* R² increased from 0.7722 to 0.8033.

These results indicate that Random Forest captures the relationships between environmental variables and mushroom yield more effectively than Linear Regression.

Feature importance analysis shows that temperature is the most influential feature, contributing approximately 69.1% of the model's predictive power.

## Conclusion

Random Forest outperformed Linear Regression on the test dataset. The reduction in prediction error and improvement in R² score justify the added complexity of the Random Forest model. Therefore, Random Forest is selected as the preferred model for mushroom yield prediction.

| Model | Test MAE |
|---------|---------|
| Linear Regression | 0.0823|
| Random Forest (Default) | 0.0620 |
| Random Forest (Tuned) | 0.0618 |

## Champion Model

The Tuned Random Forest Regressor was selected as the champion model because it achieved the lowest Mean Absolute Error (MAE) on the untouched test dataset. The model demonstrated better predictive accuracy than both the Linear Regression model and the default Random Forest model. Therefore, it was chosen as the final model for mushroom yield prediction.

## Limitations

1. The model was trained only on the available sensor ranges for temperature, humidity, and CO2. Predictions may be unreliable when sensor values fall outside the observed training range.

2. The dataset may not fully capture seasonal variations in mushroom growth. Changes in weather, climate, or production cycles could affect model performance.

3. The model relies only on the provided sensor measurements and does not account for other factors such as substrate quality, disease occurrence, or farm management practices.

4. Performance was evaluated on a single historical test period and may vary when deployed on future data.

## Evaluation Procedure

All models were evaluated using the same untouched test dataset created during the chronological train-test split. No model tuning or training was performed on the test data. This ensured a fair comparison between models.
