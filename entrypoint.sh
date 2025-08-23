#!/bin/bash

echo "Database is ready. Applying migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py seed_db

echo "Starting the Django development server..."
exec "$@"