FROM python:3.9

WORKDIR /code

COPY . /code


RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000