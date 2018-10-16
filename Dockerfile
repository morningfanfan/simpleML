FROM tiangolo/uwsgi-nginx-flask:python3.6
LABEL maintainer="Zhifan Lan <zlan1@ualberta.ca>"

ENV NGINX_WORKER_PROCESSES auto

WORKDIR /app

COPY src /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 80