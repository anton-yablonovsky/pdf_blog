FROM python:3.11
RUN mkdir backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_PASSWORD
ARG DJANGO_SUPERUSER_EMAIL
ARG DJANGO_USER_USERNAME
ARG DJANGO_USER_PASSWORD
ARG DJANGO_USER_EMAIL

ADD ./ /backend
EXPOSE 8000
WORKDIR /backend/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python3 manage.py migrate --run-syncdb
RUN python3 manage.py makemigrations
# --noinput just use DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_PASSWORD 
# and DJANGO_SUPERUSER_EMAIL env vars for creating a superuser.
RUN python3 manage.py createsuperuser --noinput
