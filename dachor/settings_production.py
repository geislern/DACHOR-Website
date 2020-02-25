"""
This is the settings file used in production.
First, it imports all default settings, then overrides respective ones.
Secrets are stored in and imported from an additional file, not set under version control.
"""

import dachor.settings_secrets as secrets

# noinspection PyUnresolvedReferences
from AKPlanning.settings import *

### SECURITY ###

DEBUG = False

ALLOWED_HOSTS = secrets.HOSTS

SECRET_KEY = secrets.SECRET_KEY

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

### DATABASE ###

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': secrets.DB_NAME,
        'USER': secrets.DB_USER,
        'PASSWORD': secrets.DB_PASSWORD,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

# TODO: caching
