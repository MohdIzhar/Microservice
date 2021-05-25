#!/bin/bash

echo "Checking migrations..."
./manage.py makemigrations
sleep 5
echo "Applying migrations..."
./manage.py migrate
sleep 5
echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('izhar', 'izhar@gmail.com', 'izhar')" | python3 manage.py shell

sleep 5
echo "Starting server..."
./manage.py runserver 0.0.0.0:8000
