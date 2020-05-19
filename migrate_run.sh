#!/bin/bash

set -e

host="$1"

while ! mysqladmin ping -h"$DB_HOST" --silent; do
    sleep 5
    echo "database not ready"
done

echo "database ready"
python3 manage.py migrate
daphne -b 0.0.0.0 -p 8001 asgi:application &
python3 manage.py runserver 0.0.0.0:8000

