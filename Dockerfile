
FROM python:3.8-alpine as base

ENV PYTHONUNBUFFERED 1
ENV PATH="/flask/.local/bin:${PATH}"
ARG BUILD_TYPE

RUN apk add --no-cache shadow linux-headers make gcc g++\
    musl-dev libxml2-dev libxslt-dev libffi-dev postgresql-dev 
RUN useradd --user-group --create-home --home-dir /flask --shell /bin/false flask

WORKDIR /flask/src

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY ./docker/backend/flask-entrypoint.sh /flask-entrypoint.sh
RUN chmod 755 /flask-entrypoint.sh

FROM base as build_lxml

# pre-building wheels to reuse them on other stages and keep cached
COPY ./requirements.txt requirements.txt

RUN pip wheel --prefer-binary --wheel-dir=/root/heavy_wheels --find-links=/flask/heavy_wheels -r requirements.txt
