FROM mcr.microsoft.com/azurelinux/base/python:3.12

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt 

COPY . /app

ENV FLASK_APP=/app/main.py
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=80"]