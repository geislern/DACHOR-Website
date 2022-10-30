#!/usr/bin/env bash
# Update project
# execute as Utils/update.sh

# abort on error, print executed commands
set -ex

# activate virtualenv if necessary
if [ -z ${VIRTUAL_ENV+x} ]; then
    source venv/bin/activate
fi

# set environment variable when we want to update in production
if [ "$1" = "--prod" ]; then
    export DJANGO_SETTINGS_MODULE=dachor.settings_production
fi

git pull
pip install --upgrade setuptools pip wheel
pip install --upgrade -r requirements.txt

./manage.py migrate
./manage.py collectstatic --noinput
./manage.py compress --force
# ./manage.py compilemessages

touch dachor/wsgi.py
