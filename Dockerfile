FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DD_ENV=dev
ENV DD_SERVICE=app
ENV DD_VERSION=0.1

COPY app /app
COPY requirements.txt /app

RUN python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install pika

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--no-server-header", "--no-access-log"]