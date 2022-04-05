# Django-Docker V2

## Description

This version has the following additional features in the Dockerfile:

- Use a environment called venv and is activate with the line `RUN python3 -m venv /opt/venv`.
- Collect static file with the line `RUN /opt/venv/bin/python3 manage.py collectstatic --noinput`.
- Run app with gunicorn with the line `CMD /opt/venv/bin/gunicorn Cv_Personal.wsgi:application --bind "0.0.0.0:8000"`.



## create image
`docker build --tag django_todov2:latest .`

## create container
`docker run -p 8000:8000 django_todov2:latest`

## To deploy from local with gunicorn
`gunicorn Cv_Personal.wsgi:application`

## TO DO
`settings.DEBUG` is in `True`, in `False` no working inside docker and i think that i should correct it.
