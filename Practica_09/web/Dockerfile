FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN pip3 install supervisor

RUN mkdir /web
COPY . /web
COPY gunicorn.ini /etc/supervisor.d/

WORKDIR /web
RUN pip3 install -r requirements.txt
