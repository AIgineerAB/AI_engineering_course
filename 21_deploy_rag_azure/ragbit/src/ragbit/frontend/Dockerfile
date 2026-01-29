FROM python:3.13-slim

# path inside of the container
WORKDIR /app/frontend

# later in docker compose, we'll use a context that is parent of frontend folder
# then we can send in the frontend folder by writing frontend
COPY frontend .

# installs uv
RUN pip install --no-cache-dir uv

# excluding packages that are marked as dev, e.g. black, ruff, flake8 ...
RUN uv sync --no-dev 

CMD ["sh", "-c", "uv run streamlit run app.py \
    --server.port=${PORT:-8501} \
    --server.address=0.0.0.0"]