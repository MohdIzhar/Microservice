#!/bin/sh

echo "Checking migrations..."
python3 manage.py makemigrations
echo "Applying migrations..."
python3 manage.py migrate
echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')" | python3 manage.py shell

echo "Starting server..."
python3 manage.py runserver 0.0.0.0:8000