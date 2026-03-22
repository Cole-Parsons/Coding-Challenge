FROM python:3.10-slim

WORKDIR /app

RUN pip install flask

COPY app/ ./app
COPY certs/ ./certs

EXPOSE 8000

CMD ["python", "app/app.py"]