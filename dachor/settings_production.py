"""
This is the settings file used in production.
First, it imports all default settings, then overrides respective ones.
Secrets are stored in and imported from an additional file, not set under version control.
"""

import dachor.settings_secrets as secrets

# noinspection PyUnresolvedReferences
from dachor.settings import *

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

### EMAILS ###
SEND_MAILS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Addresses of all admins of this instance that will receive mail notifications
ADMIN_MAILS = secrets.MAIL_ADMINS

# Address to send from
SERVER_EMAIL = secrets.MAIL_SERVER_ADDRESS
DEFAULT_FROM_EMAIL = SERVER_EMAIL

# SMTP Server Details
EMAIL_HOST = secrets.MAIL_HOST
EMAIL_PORT = secrets.MAIL_PORT
EMAIL_USE_TLS = secrets.MAIL_USE_TLS
EMAIL_HOST_USER = secrets.MAIL_USER
EMAIL_HOST_PASSWORD = secrets.MAIL_PASSWORD
