#!/bin/bash
# Start script for local development

set -o errexit

# Install dependencies if needed
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input

# Start development server
python manage.py runserver 0.0.0.0:8000
