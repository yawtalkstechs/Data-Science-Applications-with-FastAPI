FROM tiangolo/uvicorn-gunicorn:python3.11.1-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_MODULE project.app:app

COPY requirements.txt /app

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./ /app