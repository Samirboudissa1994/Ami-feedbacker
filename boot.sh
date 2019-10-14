#!/bin/sh
source venv/bin/activate
exec gunicorn -b :8080 --access-logfile - --error-logfile - main:app
