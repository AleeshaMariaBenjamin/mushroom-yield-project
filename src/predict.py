import joblib
import json
import pandas as pd


model = joblib.load(
    "models/champion.joblib"
)

scaler = joblib.load(
    "models/minmax_scaler.joblib"
)

with open(
    "models/feature_list.json"
) as f:
    features = json.load(f)


def predict_yield(
    temperature,
    humidity,
    CO2
):

    temp_humidity_interaction = (
        temperature * humidity
    )

    data = pd.DataFrame({
        "temperature": [temperature],
        "humidity": [humidity],
        "CO2": [CO2],
        "temp_humidity_interaction":
            [temp_humidity_interaction]
    })

    data = data[features]

    data_scaled = scaler.transform(
        data
    )

    prediction = model.predict(
        data_scaled
    )

    return float(prediction[0])