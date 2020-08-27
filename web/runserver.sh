#!/bin/sh

/etc/init.d/cron start

gunicorn --log-level info --log-file=/gunicorn.log --workers 4 --name app -b 0.0.0.0:8000 --reload run:app

python create_users.py
#gunicorn --log-level info --log-file=/gunicorn.log  --name app -b 0.0.0.0:8000 run:app
#command: gunicorn --log-level info --log-file=/gunicorn.log  --name app -b 0.0.0.0:8000 run:app
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    echo "PostgreSQL started"
fi


exec "$@"
