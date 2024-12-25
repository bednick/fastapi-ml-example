# docker build -t fastapi-ml-example .
# docker run -p 8080:8080 --rm -it fastapi-ml-example

FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

RUN uv run ml_model_dump.py

FROM python:3.11-slim-bookworm

WORKDIR /app

COPY --from=builder /app /app
ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "fastapi_ml_example.asgi:app", "--host", "0.0.0.0", "--port", "8080",  "--proxy-headers"]
