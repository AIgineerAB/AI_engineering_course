import streamlit as st
import httpx
from constants import ASSETS_PATH

url = "http://127.0.0.1:8000/api/iris/v1/predict"


def predict_flower(payload):
    with httpx.Client(timeout=10) as client:
        response = client.post(url, json=payload)
        response.raise_for_status()
        return response


st.markdown("# Predict iris flower")

with st.form("iris_data"):
    sepal_length = st.number_input(
        "Sepal length (cm)", min_value=4.01, max_value=8.49, value=6.0
    )
    sepal_width = st.number_input(
        "Sepal width (cm)", min_value=1.81, max_value=4.99, value=2.5, step=0.1
    )
    petal_length = st.number_input(
        "Petal length (cm)", min_value=0.81, max_value=7.49, value=4.5, step=0.1
    )
    petal_width = st.number_input(
        "Petal width (cm)", min_value=0.01, max_value=2.99, value=1.2, step=0.1
    )

    submitted = st.form_submit_button("PREDICT")

# st.markdown(type(petal_width))
if submitted:
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }

    response = predict_flower(payload=payload).json()
    flower = response.get("predicted_flower").casefold()
    st.markdown(f"Predicted flower is {flower}")
    st.image(f"{ASSETS_PATH / flower}.jpg")
