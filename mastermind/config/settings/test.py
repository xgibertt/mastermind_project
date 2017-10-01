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

INSTALLED_APPS += ('django_nose', )

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--cover-erase',
    '--cover-package=game',
]
