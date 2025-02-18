# ========== Base stage ========== 
FROM python:3.10 AS base

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.6.1 /uv /uvx /bin/

COPY pyproject.toml uv.lock README.md ./

RUN uv sync

ENV PATH="/app/.venv/bin:$PATH"

FROM base AS dev

ENV APP_ENV="dev"

COPY . /app/

EXPOSE 5050

CMD ["sh", "./bin/start_wsgi.sh"]

FROM base AS prod

ENV  APP_END="prod"

COPY /config/ /app/config/
COPY /bin/ /app/bin/
COPY /pps/ /app/pps/

EXPOSE 5050

CMD ["sh", "./bin/start_wsgi.sh"]

