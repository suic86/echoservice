#!/bin/sh

# Script for running the echoservice app with gunicorn.

gunicorn wsgi:app \
    --worker-class=gthread \
    --bind 0.0.0.0:8080 \
    --log-level=info \
    --access-logfile access.log \
    --error-logfile gunicorn.log