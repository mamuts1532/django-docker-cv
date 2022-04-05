# Django-Docker V1

## create image
docker build --tag django_todov2:latest .

## create container
docker run -p 8000:8000 django_todov2:latest

## To deploy from local with gunicorn
gunicorn Cv_Personal.wsgi:application

## TO DO
settings.DEBUG is in True, in False no working inside docker and i think that i should correct it.
