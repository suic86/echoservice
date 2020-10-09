#!/bin/sh

gunicorn --worker-class=gthread --bind 0.0.0.0:8080 wsgi:app