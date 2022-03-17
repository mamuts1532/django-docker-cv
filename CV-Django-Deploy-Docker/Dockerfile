# # pull the official base image
# FROM python:3.8.3-alpine

# # set work directory
# WORKDIR /usr/src/app

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # install dependencies
# RUN apk update && apk add python3-dev gcc libc-dev
# RUN apk add -u zlib-dev 
# RUN python -m pip install --upgrade pip 
# COPY ./requirements.txt /usr/src/app
# RUN pip install -r requirements.txt

# # copy project
# COPY . /usr/src/app

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



####################################################################

FROM python:3.8.3-slim

# copy your local files to your
# docker container
COPY . /app

# update your environment to work
# within the folder you copied your 
# files above into
WORKDIR /app

# /opt: reserved for the installation of add-on application software packages.
# We'll use this to create & store our virtual environment

# Create a virtual environment in /opt
RUN python3 -m venv /opt/venv

# Install requirments to new virtual environment
# requirements.txt must have gunicorn & django
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

RUN /opt/venv/bin/pip install pip --upgrade

RUN /opt/venv/bin/pip install -r requirements.txt

#RUN /opt/venv/bin/pip install -r requirements.txt &&

# entrypoint.sh will be discussed later.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]