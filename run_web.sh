#!/usr/bin/env bash
cd src/todoapp/

# Migrate Schema
./manage.py migrate

# Run Application
./manage.py runserver 0.0.0.0:8000