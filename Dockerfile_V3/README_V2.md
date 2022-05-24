# Django-Docker V2

## Description

This versión is deployed using Docker compose and dockerized a database to conecction with Django App:

- The docker-compose.yml file is created with necessary configuration.  

## Create image and container
`docker-compose up -d --build`

## View logs
`docker-compose logs -f`
## TO DO
`settings.DEBUG` is in `True`, in `False` no working inside docker and i think that i should correct it.
