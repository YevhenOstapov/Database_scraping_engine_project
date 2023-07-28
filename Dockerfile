FROM python:3.9.15

RUN apt-get update -y
RUN apt-get install libpq-dev
RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

COPY . .

RUN export PYTHONPATH=/app
