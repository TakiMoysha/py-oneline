FROM python:3.12-slim-bookworm as builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

COPY ./src/disearch /app
WORKDIR /app

RUN uv sync

CMD [ 'uv', 'run', 'disearch' ]
