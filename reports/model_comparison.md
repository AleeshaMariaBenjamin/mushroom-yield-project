# Model Comparison

## Performance Metrics

| Model             | MAE    | RMSE   | R²     |
| ----------------- | ------ | ------ | ------ |
| Linear Regression | 0.0823 | 0.1066 | 0.7722 |
| Random Forest     | 0.0620 | 0.0991 | 0.8033 |

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
