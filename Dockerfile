FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /code 

WORKDIR /code 

COPY ./Ecom_project/requirements.txt /code/requirements.txt
COPY ./Ecom_project /code

RUN pip3 install -r requirements.txt \
 && chmod +x superuser.sh && apt update && apt install -y netcat

