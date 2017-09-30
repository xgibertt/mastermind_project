"""Test settings"""
from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mastermind_test',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}