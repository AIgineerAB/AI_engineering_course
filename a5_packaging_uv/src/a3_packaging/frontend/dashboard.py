import streamlit as st
import pandas as pd
import httpx

data = httpx.get("http://127.0.0.1:8000/taxi/")


df = pd.DataFrame(data.json())


def main():
    st.markdown("# Taxi Prediction Dashboard")

    st.dataframe(df)


if __name__ == "__main__":
    main()
