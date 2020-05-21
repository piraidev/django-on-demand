"""
Django settings for socialapp project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f3#@hzl^b7f-@r7p7xocth(!+$b-8(^3dqp6*&4*7@bq2-69u-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Adding this silenced system check in order to let django add a varchar field greater than 255 bytes
# This is to allow long tokens (like the linkedin one) to be stored in the Token model/table
SILENCED_SYSTEM_CHECKS = ['mysql.E001']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'request_logging.middleware.LoggingMiddleware',
]

ROOT_URLCONF = 'socialapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'socialapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'socialapp',
        'USER': 'admin',
        'PASSWORD': 'secret',
        'HOST': 'db',
        'PORT': '3306'
    }
}

ASGI_APPLICATION = 'socialapp.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# API Settings

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

# Settings that should be settled locally depending on environment (using local_settings file)
FACEBOOK_ACCESS_TOKEN = '214076775977570|a2b4144e6811caf605a0c2eecde26e20'
LINKEDIN_CLIENT_ID = ''
LINKEDIN_CLIENT_SECRET = ''
LINKEDIN_REDIRECT_URI = ''

# Including all environment (local) settings.
# This import should be kept at the end of this file, to ensure local settings will
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',  # change debug level as appropiate
            'propagate': False,
        },
    },
}
SENDGRID_API_CLIENT_KEY = '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'

#SENDGRID SETTINGS
FROM_EMAIL_ADDRESS = 'no-reply@socialapp.domain'
FROM_NAME = 'Social app dev team'
##SENDGRID TEMPLATES IDS
SENGRID_WELCOME_TEMPLATE_ID = 'd-69e79d9666b64e48964419fc325e616a'
SENGRID_REQUEST_TEMPLATE_ID = 'd-4ed768feac3e46a18efd2afaf1102f29'
SENGRID_NEW_MESSAGE_TEMPLATE_ID = 'd-979aef115e9e49af99461182ef0d6a76'
SENGRID_REQUEST_ACCEPTED_TEMPLATE_ID = 'd-304f035567a64061961d3f820df051a8'
SENGRID_REQUEST_REJECTED_TEMPLATE_ID = 'd-c59ac642e529479892eb2eb3f9e55d75'
SENGRID_REQUEST_CANCELLED_TEMPLATE_ID = 'd-2900fe7cb1964fb5a6e54f11215dc844'
SENGRID_REQUEST_FINISHED_MENTOR_TEMPLATE_ID = 'd-27c97dafdde8447dbf6684b4ac655128'
SENGRID_REQUEST_FINISHED_MENTEE_TEMPLATE_ID = 'd-81ea668f0262488ca6d3d0e678ce719d'
