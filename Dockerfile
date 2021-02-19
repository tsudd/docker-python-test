FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

CMD ["app.py"]

ENTRYPOINT ["python3"]
