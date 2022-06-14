FROM python:3.10-slim-buster as base
RUN apt-get update; apt-get install curl -y
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
WORKDIR /todo_app
COPY pyproject.toml /todo_app/pyproject.toml
COPY poetry.lock /todo_app/poetry.lock
RUN poetry install
COPY todo_app ./todo_app

FROM base AS production
EXPOSE 80
ENTRYPOINT poetry run gunicorn -b 0.0.0.0:80 'todo_app.app:create_app()'

FROM base AS development
EXPOSE 5000
ENTRYPOINT poetry run flask run --host 0.0.0.0