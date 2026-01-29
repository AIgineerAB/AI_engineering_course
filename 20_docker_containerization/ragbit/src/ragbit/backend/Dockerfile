FROM python:3.13-slim

WORKDIR /app

COPY knowledge_base knowledge_base
COPY backend backend

RUN pip install --no-cache-dir uv 

WORKDIR /app/backend

RUN uv sync --no-dev

CMD ["uv", "run", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
