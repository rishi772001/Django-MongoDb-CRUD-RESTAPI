FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /main
WORKDIR /main
COPY . /main/
RUN pip install -r requirements.txt