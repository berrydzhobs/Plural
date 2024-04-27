from pathlib import Path
from .key import *
from .mail import *
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG

ALLOWED_HOSTS = ALLOWED_HOSTS

SITE_ID = SITE_ID


AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS


# Application definition



INSTALLED_APPS = INSTALLED_APPS


# Provider specific settings
SOCIALACCOUNT_PROVIDERS = SOCIALACCOUNT_PROVIDERS

ACCOUNT_FORMS = ACCOUNT_FORMS


ACCOUNT_AUTHENTICATION_METHOD = ACCOUNT_AUTHENTICATION_METHOD
ACCOUNT_EMAIL_REQUIRED = ACCOUNT_EMAIL_REQUIRED
ACCOUNT_USERNAME_REQUIRED = ACCOUNT_USERNAME_REQUIRED



MIDDLEWARE = MIDDLEWARE

ROOT_URLCONF = ROOT_URLCONF

TEMPLATES = TEMPLATES

WSGI_APPLICATION = WSGI_APPLICATION


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = DATABASES


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = AUTH_PASSWORD_VALIDATORS

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LOCALE_PATHS = LOCALE_PATHS


LANGUAGE_CODE = LANGUAGE_CODE

TIME_ZONE = TIME_ZONE

USE_I18N = USE_I18N

USE_L10N = USE_L10N

USE_TZ = USE_TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_DIRS = STATICFILES_DIRS

STATIC_ROOT = STATIC_ROOT
STATIC_ROOT = STATIC_ROOT
STATICFILES_STORAGE = STATICFILES_STORAGE 

STATIC_URL = STATIC_URL


MEDIA_URL = MEDIA_URL

MEDIA_ROOT = MEDIA_ROOT
MEDIA_ROOT = MEDIA_ROOT
LOGIN_REDIRECT_URL = LOGIN_REDIRECT_URL
LOGIN_URL = LOGIN_URL





EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = EMAIL_HOST
EMAIL_PORT = EMAIL_PORT
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD

CKEDITOR_CONFIGS = CKEDITOR_CONFIGS

#DEFAULT PRIMARY KEY

DEFAULT_AUTO_FIELD = DEFAULT_AUTO_FIELD