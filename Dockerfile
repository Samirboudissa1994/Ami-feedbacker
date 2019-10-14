FROM python:3.6-alpine

WORKDIR /ami-feedbacker

VOLUME ./data

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY main.py main.py
COPY ./data/data.sqlite ./data/data.sqlite

COPY boot.sh boot.sh
RUN chmod +x boot.sh

ENV FLASK_APP main.py

EXPOSE 8080
ENTRYPOINT ["./boot.sh"]
