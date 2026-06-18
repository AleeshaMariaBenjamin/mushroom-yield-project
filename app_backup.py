import streamlit as st
import joblib
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@st.cache_resource
def load_artifacts():

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

    return model, scaler, features

def predict_yield(
    temperature,
    humidity,
    CO2
):

    model, scaler, features = (
        load_artifacts()
    )

    interaction = (
        temperature * humidity
    )

    data = pd.DataFrame({
        "temperature": [temperature],
        "humidity": [humidity],
        "CO2": [CO2],
        "temp_humidity_interaction":
            [interaction]
    })

    data = data[features]

    scaled = scaler.transform(
        data
    )

    prediction = model.predict(
        scaled
    )

    return float(
        prediction[0]
    )

st.title(
    "🍄 Mushroom Yield Predictor"
)

st.markdown("""
### How to Use

1. Select sensor readings.
2. Click Predict Yield.
3. View the predicted mushroom yield.

The model estimates yield based on
polyhouse environmental conditions.
""")

st.write(
    "Predict mushroom yield from polyhouse sensor readings."
)
col1, col2 = st.columns(2)

with col1:

    temperature = st.slider(
        "Temperature (°C)",
        15,
        40,
        25
    )

    humidity = st.slider(
        "Humidity (%)",
        50,
        100,
        80
    )

with col2:

    CO2 = st.slider(
        "CO₂ (ppm)",
        300,
        2000,
        1000
    )
if st.button("Predict Yield"):
    prediction = predict_yield(
        temperature,
        humidity,
        CO2
    )

    st.metric(
        label="Predicted Yield",
        value=f"{prediction:.2f} kg"
    )