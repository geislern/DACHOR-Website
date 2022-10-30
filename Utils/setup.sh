#!/usr/bin/env bash
# Setup DACHOR website
# execute as Utils/check.sh

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
python manage.py compilemessages

# Create superuser
# Credentials are entered interactively on CLI
python manage.py createsuperuser

deactivate
