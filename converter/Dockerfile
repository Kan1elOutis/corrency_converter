FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt-get update

RUN pip freeze > requirements.txt

RUN pip install -r requirements.txt