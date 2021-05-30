FROM python:latest

RUN mkdir /code

WORKDIR /code

COPY dockerRepo/ /code

RUN pip3 install -r requirements.txt && chmod +x runserver.sh && apt update && apt install -y netcat
