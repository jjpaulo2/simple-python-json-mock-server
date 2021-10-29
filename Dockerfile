FROM python:3.8-alpine
LABEL author="João Paulo Carvalho <jjpaulo2@protonmail.com>"

USER root

COPY ./mock_server /srv/mock_server
COPY ./requirements.txt /srv

ENV PYTHONPATH=/srv
EXPOSE 5000

RUN pip install -r /srv/requirements.txt --upgrade

WORKDIR /srv
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "mock_server.wsgi:flask_app"]