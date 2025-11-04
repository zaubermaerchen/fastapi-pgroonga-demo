FROM python:3.13-slim-bookworm AS development

COPY --from=ghcr.io/astral-sh/uv:0.9.6 /uv /uvx /bin/

ENV ENV=development
ENV PYTHONUNBUFFERED=1
ENV UV_PROJECT_ENVIRONMENT=/root/.venv
ENV UV_CACHE_DIR=/root/.cache/uv
ENV UV_LINK_MODE=copy
ENV UV_COMPILE_BYTECODE=1

WORKDIR /app

COPY . /app
RUN uv sync --frozen --no-cache

CMD ["uv", "run", "fastapi", "dev", "--host", "0.0.0.0", "--port", "8000"]
