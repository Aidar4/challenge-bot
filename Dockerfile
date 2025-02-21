FROM python:3.10-slim-buster

# make command
RUN apt-get update \
    && apt-get -y install make

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install pip-tools
COPY Makefile /code/
RUN make install

COPY . /code/