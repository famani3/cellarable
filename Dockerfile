
FROM python:3.9-alpine as base

ENV PYTHONUNBUFFERED 1
ENV PATH="/flask/.local/bin:${PATH}"
ARG BUILD_TYPE

RUN apk add --no-cache shadow linux-headers make  postgresql-dev
RUN useradd --user-group --create-home --home-dir /flask --shell /bin/false flask

WORKDIR /flask/src

RUN /usr/local/bin/python -m pip install --upgrade pip

FROM base as build_lxml

# pre-building wheels to reuse them on other stages and keep cached
COPY ./requirements.txt requirements.txt

RUN mkdir /flask/heavy_wheels
RUN pip  install -r requirements.txt 
ENTRYPOINT [ "entrypoint.sh" ]

