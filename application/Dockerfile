FROM tiangolo/meinheld-gunicorn:python3.7-alpine3.8
LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"
RUN pip install flask
COPY ./app /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
