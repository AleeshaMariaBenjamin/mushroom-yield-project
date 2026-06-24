import streamlit as st
import joblib
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from datetime import datetime

st.set_page_config(
    page_title="Mushroom Yield Predictor",
    page_icon="🍄"
)


@st.cache_resource
def load_artifacts():

    try:

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

    except FileNotFoundError:

        st.error(
            "Model files not found. Please restore the model artifacts."
        )

        st.stop()


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
        "temp_humidity_interaction": [
            interaction
        ]
    })

    data = data[features]

    prediction = model.predict(
        data
    )

    return float(
        prediction[0]
    )

# =====================
# APP UI
# =====================

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

# =====================
# INPUTS
# =====================

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

# =====================
# WARNINGS
# =====================

if temperature > 35:

    st.warning(
        "Temperature is unusually high."
    )

if humidity < 60:

    st.warning(
        "Humidity is below recommended range."
    )

if CO2 > 1800:

    st.warning(
        "CO₂ level is unusually high."
    )

# =====================
# PREDICTION
# =====================

if st.button("Predict Yield"):

    prediction = predict_yield(
        temperature,
        humidity,
        CO2
    )

    # logging code AFTER prediction exists

    os.makedirs(
        "logs",
        exist_ok=True
    )

    log_file = "logs/predictions.csv"

    file_exists = os.path.isfile(
        log_file
    )

    with open(
        log_file,
        "a",
        newline=""
    ) as f:

        writer = csv.writer(f)

        if not file_exists:

            writer.writerow([
                "timestamp",
                "temperature",
                "humidity",
                "CO2",
                "prediction"
            ])

        writer.writerow([
            datetime.now(),
            temperature,
            humidity,
            CO2,
            prediction
        ])

    st.metric(
        label="Predicted Yield",
        value=f"{prediction:.2f} kg"
    )       

    st.write(
        f"Inputs → Temperature: {temperature}°C | Humidity: {humidity}% | CO₂: {CO2} ppm"
    )

    st.metric(
        label="Predicted Yield",
        value=f"{prediction:.2f} kg"
    )

    # =====================
    # SENSITIVITY CHART
    # =====================

    temps = np.arange(
        15,
        41
    )

    predictions = []

    for t in temps:

        pred = predict_yield(
            t,
            humidity,
            CO2
        )

        predictions.append(
            pred
        )

    fig, ax = plt.subplots()

    ax.plot(
        temps,
        predictions
    )

    ax.set_xlabel(
        "Temperature (°C)"
    )

    ax.set_ylabel(
        "Predicted Yield (kg)"
    )

    ax.set_title(
        "Yield Sensitivity to Temperature"
    )

    st.pyplot(
        fig
    )

# =====================
# CHART EXPLANATION
# =====================

with st.expander(
    "About the Sensitivity Chart"
):

    st.write("""
This chart shows how predicted yield
changes as temperature changes while
humidity and CO₂ remain fixed.
""")

# =====================
# MODEL INFORMATION
# =====================

with st.expander(
    "Model Information"
):

    st.write(
        "Model: Random Forest Regressor"
    )

    st.write(
        "Version: v1.0"
    )

    st.write(
        "Features Used:"
    )

    st.write([
        "Temperature",
        "Humidity",
        "CO₂",
        "Temperature × Humidity"
    ])

    st.write(
        "Champion model selected using GridSearchCV."
    )