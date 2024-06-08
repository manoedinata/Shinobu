# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev

# Copy source code
WORKDIR /app
COPY . /app

# Generate dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
pip3 install poetry
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

EXPOSE 8000
CMD ["/bin/sh", "/app/start.sh"]
