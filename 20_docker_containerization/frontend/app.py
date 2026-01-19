import streamlit as st
import requests
from pathlib import Path
import os

ASSETS_PATH = Path(__file__).absolute().parents[1] / "assets"
API_URL = os.getenv("API_URL", "http://localhost:8000")


def layout():

    st.markdown("# RAGbit")
    st.markdown("Ask a question about different dwarf rabbits")
    text_input = st.text_input(label="Ask a questions")

    if st.button("Send") and text_input.strip() != "":
        response = requests.post(
            f"{API_URL}/rag/query", json={"prompt": text_input}
        )

        data = response.json()

        st.markdown("## Question:")
        st.markdown(text_input)

        st.markdown("## Answer:")
        st.markdown(data["answer"])

        st.markdown("## Source:")
        st.markdown(data["filepath"])
 
        st.image(ASSETS_PATH / f"{data['filename']}.png")

if __name__ == "__main__":
    layout()
