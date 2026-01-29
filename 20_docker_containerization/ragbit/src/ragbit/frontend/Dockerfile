FROM python:3.13-slim

WORKDIR /app

COPY frontend frontend
COPY assets assets

RUN pip install --no-cache-dir uv 

WORKDIR /app/frontend

RUN uv sync --no-dev

CMD ["uv", "run", "streamlit", "run","app.py", "--server.port=8501", "--server.address=0.0.0.0"]
