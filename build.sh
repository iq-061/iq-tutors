#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
# No models right now, so migrate is optional — safe to keep it:
python manage.py migrate --noinput
python manage.py ensure_superuser