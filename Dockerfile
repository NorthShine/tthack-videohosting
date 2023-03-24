FROM python:3.11

WORKDIR /usr/src/app

COPY . .

RUN pip install poetry
RUN poetry install

EXPOSE 80