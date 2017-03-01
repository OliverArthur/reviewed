#!/usr/bin/env bash

set -e

echo "Doing 'pip install'..."
# Install python dependencies
pip3 install -r requirements.txt
echo

# Start the server
echo "Starting the server..."
python manage.py runserver -h 0.0.0.0 -p 5000

exec "$@"
