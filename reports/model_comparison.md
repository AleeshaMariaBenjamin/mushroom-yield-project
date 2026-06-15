# Model Comparison

## Performance Metrics

### Cross-Validation + Test Metrics

| Model | CV MAE | Test MAE | Test RMSE | Test R² |
|---|---|---|---|---|
| Linear Regression | 0.0795 | 0.0823 | 0.1066 | 0.7722 |
| Random Forest (Default) | 0.0610 | 0.0620 | 0.0991 | 0.8033 |
| Random Forest (Tuned) | 0.0598 | 0.0610 | 0.0965 | 0.8135 |

## Feature Importance (Random Forest)

| Feature | Importance |
|---|---|
| Temperature | 0.691 |
| Humidity | 0.169 |
| CO₂ | 0.140 |

## Linear Regression Coefficients

| Feature | Coefficient |
|---|---|
| Temperature | 0.2679 |
| Humidity | -0.3829 |
| CO₂ | 0.2813 |

## Analysis

All three models were trained on the same dataset and evaluated on the same unseen test set.

- Linear Regression achieved R² = 0.7722, meaning it explains 77% of yield variation. It serves as the baseline.
- Default Random Forest improved on this with R² = 0.8033 and MAE = 0.0620, capturing non-linear relationships between sensor readings and yield.
- Tuned Random Forest (best params: n_estimators=50, max_depth=5, min_samples_leaf=1) achieved the best results with R² = 0.8135 and MAE = 0.0610.

Temperature is the most influential feature at 69.1% importance, which aligns with the biological sensitivity of mushrooms to temperature.

## Champion Model

**Tuned Random Forest** is selected as the champion model.

It achieved the lowest MAE (0.0610) and highest R² (0.8135) on the unseen test set. It was selected through GridSearchCV with TimeSeriesSplit (5 folds), testing 27 hyperparameter combinations — making the selection evidence-based rather than arbitrary.

The best hyperparameters found were:
- `n_estimators`: 50
- `max_depth`: 5
- `min_samples_leaf`: 1

Saved to: `models/champion.joblib`

## Limitations

1. The model was trained only on the available sensor ranges for temperature, humidity, and CO2. Predictions may be unreliable when sensor values fall outside the observed training range.
2. The dataset may not fully capture seasonal variations in mushroom growth.
3. The model does not account for other factors such as substrate quality, disease occurrence, or farm management practices.
4. Performance was evaluated on a single historical test period and may vary on future data.

## Evaluation Procedure

All models were evaluated on the same unseen test set created during a chronological 80/20 train-test split. No model tuning or training was performed on the test data. Cross-validation was performed using TimeSeriesSplit to respect the time-ordered nature of the sensor data.