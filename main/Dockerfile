FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN apk add --update --no-cache mariadb-dev
RUN apk add --update --no-cache --virtual .tmp-build-devs \
    build-base gcc python3-dev musl-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-devs

COPY . /app

RUN adduser -D user
USER user