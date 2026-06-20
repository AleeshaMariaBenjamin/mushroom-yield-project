# Monitoring Plan

## Sample Prediction Log

| Timestamp  | Temperature | Humidity | CO2  | Predicted Yield |
| ---------- | ----------- | -------- | ---- | --------------- |
| 2026-06-20 | 25          | 80       | 1000 | 1.09 kg         |
| 2026-06-20 | 30          | 85       | 1200 | 1.15 kg         |

## Monitoring Strategy

The application should record incoming sensor values and model predictions for future analysis.

Important fields:

* Temperature
* Humidity
* CO2
* Predicted Yield
* Timestamp

## Retraining Triggers

Retraining should be considered when:

1. New production data becomes available.
2. Prediction performance decreases.
3. Environmental conditions change significantly.
4. Monthly model review indicates drift.
5. New sensors or features are added.

## Model Artifacts

Artifacts used by the application:

* models/champion.joblib
* models/minmax_scaler.joblib
* models/feature_list.json

These files are committed to the repository and loaded during application startup.
