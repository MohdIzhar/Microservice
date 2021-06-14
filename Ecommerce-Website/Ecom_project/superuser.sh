#!/bin/bash

until nc -z -v -w30 ecomappdb 3306
do
  echo 'Waiting for MySQL...'
  sleep 1
done
echo "MySQL is up and running"

echo "Checking migrations..."
./manage.py makemigrations

echo "Applying migrations..."
./manage.py migrate

echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('izhar', 'izhar@gmail.com', 'izhar')" | python3 manage.py shell

echo "Starting server..."
./manage.py runserver 0.0.0.0:8000
