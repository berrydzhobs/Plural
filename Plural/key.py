from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!o5-pk4a(pew_is@ad2me3^r7r_t*m_$ow$$jc&)8o4qqn(cq)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['5739-105-178-43-199.ngrok.io', '127.0.0.1']

SITE_ID = 1


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Application definition



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    #
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # 
    'django_summernote',
    #
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.apple',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    #
    'django_htmx',
    #
    #My Applications
    'Setting.apps.SettingConfig',
    'Content.apps.ContentConfig',
    'Main.apps.MainConfig',
    'Startqt.apps.StartqtConfig',
    'Profile.apps.ProfileConfig',
    'Discover.apps.DiscoverConfig',
    'Feed.apps.FeedConfig',
    'Document.apps.DocumentConfig',
    #External Applications
    'Graph.apps.GraphConfig',
    'Search.apps.SearchConfig',
    'django_cleanup.apps.CleanupConfig',
]


# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'APP_ID': '702978201296377',
        'APP_SECRET': '12a6765d3a6e53eb075806c90b7389e4',
        'SCOPE': ['Plural@gmail.com', 'public_profile'],
    },
    }

ACCOUNT_FORMS = {
    'signup': 'Plural.forms.CustomSignupForm',
}


ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_USERNAME_REQUIRED = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # ... other middleware ...
    'Main.middleware.CheckMainMiddleware',
    # ... end other middleware ...
]

ROOT_URLCONF = 'Plural.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Plural.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LOCALE_PATHS = [
   os.path.join(BASE_DIR, 'locale')
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_DIRS =(str(BASE_DIR.joinpath('static')),)

STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATIC_URL = '/static/'


MEDIA_URL = '/media/'

MEDIA_ROOT = str(BASE_DIR.joinpath('media'))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
LOGIN_REDIRECT_URL = 'Startqt'
LOGIN_URL = 'account_login'

CKEDITOR_CONFIGS = {
    'default':{
    'toolbar':'full',
    'width':'100%',
    'height':'100%',
    },
}
#DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
