FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY src/main.py /code/main.py
COPY src/controller /code/controller
COPY src/model /code/model
COPY src/service /code/service
COPY src/config /code/config

ENV PYTHONPATH=/code

CMD ["python", "main.py"]