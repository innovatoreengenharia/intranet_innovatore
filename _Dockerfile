FROM python:3.11-slim AS env_base

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for building python deps
        build-essential \
        # libpq-dev and python-dev are needed to install psycopg2
        libpq-dev \
        # python-dev is no longer available since Debian 11
        python-dev-is-python3

RUN python -m venv /venv

COPY ./ /code/

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /code

RUN . /venv/bin/activate && pip install -r requirements.txt

COPY /venv /venv

ENV PATH="/venv/bin:${PATH}"

EXPOSE 8001