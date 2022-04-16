FROM python:3.10.4-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app/


RUN apt-get update && \
    apt-get install \
    python3-dev default-libmysqlclient-dev --no-install-recommends --no-install-suggests -y \
    gcc \
    wait-for-it && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove -y && \
    apt-get clean

# Allows docker to cache installed dependencies between builds
COPY /config /config
RUN pip install -r /config/requirements.txt

COPY /app/ .
