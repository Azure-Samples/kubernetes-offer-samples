FROM alpine:latest

RUN apk add --no-cache py-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT FLASK_APP=/app/main.py flask run --host=0.0.0.0 --port=80