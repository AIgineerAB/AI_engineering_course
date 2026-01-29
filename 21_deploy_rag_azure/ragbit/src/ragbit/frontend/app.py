import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000") 

st.markdown("# RAGbit")
st.markdown("RAGbit is good at answering questions about dwarf rabbits")

user_prompt = st.text_input("Ask a question")

if st.button("SEND") and user_prompt.strip() != "":
    response = requests.post(
        f"{API_URL}/rag/query", json={"prompt": user_prompt}
    )

    data = response.json()

    st.write(data)