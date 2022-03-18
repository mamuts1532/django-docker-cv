# Django-Docker V1

# create image
docker build --tag django_todo:latest .

# create container
docker run -p 8000:8000 django_todo:latest

# To deploy from local with gunicorn
gunicorn Cv_Personal.wsgi:application
