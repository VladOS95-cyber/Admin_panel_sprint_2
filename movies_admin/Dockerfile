FROM python:3.9

EXPOSE 8000

WORKDIR /code

COPY requirements.txt /code

RUN pip install --upgrade pip --no-cache-dir && \
    pip install -r /code/requirements.txt

COPY . /code

CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000