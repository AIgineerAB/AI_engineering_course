FROM python:3.13-slim

WORKDIR /app/frontend

COPY frontend .
COPY assets /app/assets

RUN pip install --no-cache-dir uv
RUN uv sync --no-dev



CMD ["uv", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
