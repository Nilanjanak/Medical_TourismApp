# MedicalTourismApp

start this project on local server

    python -m venv .venv

    pip -r requirements.txt

    python manage.py migrate

    python manage.py collectstatic


    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

    celery -A config worker -l info

    celery -A config flower   
