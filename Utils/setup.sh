#!/usr/bin/env bash
# Setup DACHOR website
# execute as Utils/setup.sh

# abort on error, print executed commands
set -ex

# remove old virtualenv
rm -rf venv/

# Setup Python Environment
# Requires: Virtualenv, appropriate Python installation
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade setuptools pip wheel
pip install -r requirements.txt

# Setup database
python manage.py migrate

# Prepare static files and translations
python manage.py collectstatic --noinput
if [ "$1" = "--prod" ]; then
    python manage.py compilemessages
fi

# Create superuser
# Credentials are entered interactively on CLI
python manage.py createsuperuser

deactivate
