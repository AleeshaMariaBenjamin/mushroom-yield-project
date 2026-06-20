import joblib
import json
import pandas as pd

model = joblib.load("models/champion.joblib")
scaler = joblib.load("models/minmax_scaler.joblib")

with open("models/feature_list.json") as f:
    features = json.load(f)

cases = [
    [15, 50, 300],
    [25, 80, 1000],
    [40, 100, 2000]
]

for temp, hum, co2 in cases:

    interaction = temp * hum

    df = pd.DataFrame({
        "temperature": [temp],
        "humidity": [hum],
        "CO2": [co2],
        "temp_humidity_interaction": [interaction]
    })

    df = df[features]

    print("\nOriginal:")
    print(df)

    scaled = scaler.transform(df)

    print("Scaled:")
    print(scaled)

    pred = model.predict(scaled)

    print("Prediction:", pred[0])