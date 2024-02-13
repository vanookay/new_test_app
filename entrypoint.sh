#!/usr/bin/env bash
app() {
  echo "Start migrate command..."
  python manage.py migrate --no-color --traceback
  time python3.10 manage.py runserver
}
