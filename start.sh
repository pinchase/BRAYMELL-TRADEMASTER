#!/bin/bash
# Start script for local development

# Install dependencies if needed
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver 0.0.0.0:8000
