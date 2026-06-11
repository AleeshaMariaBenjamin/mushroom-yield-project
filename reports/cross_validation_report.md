# Cross Validation Report

## Objective

Evaluate model performance using TimeSeriesSplit cross-validation while preserving the chronological order of the mushroom yield dataset.

---

## Method

TimeSeriesSplit with 5 folds was used to evaluate two models:

1. Linear Regression
2. Random Forest Regressor

Only the training dataset (`train.csv`) was used during cross-validation. The held-out test set was not used.

---

## Linear Regression Results

| Fold | MAE    |
| ---- | ------ |
| 1    | 0.0837 |
| 2    | 0.0797 |
| 3    | 0.0793 |
| 4    | 0.0778 |
| 5    | 0.0768 |

**Average MAE:** 0.0795

---

## Random Forest Results

| Fold | Train MAE | Validation MAE |
| ---- | --------- | -------------- |
| 1    | 0.0255    | 0.0730         |
| 2    | 0.0249    | 0.0597         |
| 3    | 0.0255    | 0.0550         |
| 4    | 0.0233    | 0.0603         |
| 5    | 0.0235    | 0.0572         |

**Average Train MAE:** 0.0245

**Average Validation MAE:** 0.0610

---

## Model Comparison

| Model             | Average MAE |
| ----------------- | ----------- |
| Linear Regression | 0.0795      |
| Random Forest     | 0.0610      |

Random Forest achieved the lower average MAE and therefore demonstrated better predictive performance during cross-validation.

---

## Variance Across Folds

Linear Regression MAE values ranged from 0.0768 to 0.0837.

Random Forest validation MAE values ranged from 0.0550 to 0.0730.

The variation across folds was relatively small for both models, indicating that performance remained reasonably consistent across different time periods in the dataset.

---

## Overfitting Analysis

For Random Forest:

* Average Train MAE = 0.0245
* Average Validation MAE = 0.0610

The training error is considerably lower than the validation error, indicating some degree of overfitting. However, the validation performance remains stable across folds and is still better than Linear Regression. Therefore, the model generalizes reasonably well despite fitting the training data more closely.

---

## Conclusion

TimeSeriesSplit cross-validation confirmed that Random Forest is the stronger model for mushroom yield prediction.

Key findings:

* Random Forest achieved the lowest average MAE (0.0610).
* Linear Regression achieved an average MAE of 0.0795.
* Cross-validation performance was consistent across folds.
* Some overfitting is present in Random Forest, but validation performance remains strong.

Based on both test-set evaluation and cross-validation results, Random Forest is selected as the preferred model for this project.
