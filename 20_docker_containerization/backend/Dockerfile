FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY knowledge_base knowledge_base
COPY backend/ backend/



WORKDIR /app/backend
# installs directly to system instead of a virtual environment as docker already isolates the environment
# no-dev -> exclude tools such as ruff, black or similar
RUN uv sync --no-dev



CMD ["uv", "run","uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]