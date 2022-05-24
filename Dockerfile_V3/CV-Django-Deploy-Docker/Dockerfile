# FROM python:3.8.3-slim-buster

# copy your local files to your
# docker container
# COPY . /app
#COPY media/ app/media/

# update your environment to work
# within the folder you copied your 
# files above into
# WORKDIR /app

# set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# /opt: reserved for the installation of add-on application software packages.
# We'll use this to create & store our virtual environment

# Create a virtual environment in /opt
# RUN python3 -m venv /opt/venv

# Install requirments to new virtual environment
# requirements.txt must have gunicorn & django
# RUN apt-get update \
# && apt-get install gcc -y \
# && apt-get clean

# RUN pip install pip --upgrade

# RUN pip install -r requirements.txt

# RUN /opt/venv/bin/pip install pip --upgrade && \
    # /opt/venv/bin/pip install -r requirements.txt

# Collect static files
# RUN /opt/venv/bin/python3 manage.py collectstatic --noinput

# entrypoint.sh will be discussed later.
#CMD ["/opt/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD /opt/venv/bin/gunicorn Cv_Personal.wsgi:application --bind "0.0.0.0:8000"

# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip 
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]