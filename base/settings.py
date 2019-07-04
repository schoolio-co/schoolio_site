"""
Django settings for base project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from decouple import config, Csv
import django_heroku
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
SECRET_KEY = config('SECRET_KEY')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAYPAL_RECEIVER_EMAIL = 'audrey@schoolio.co'
 
PAYPAL_TEST = False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quiz',
    "ecommerce_app",
    'paypal.standard.ipn',
    'multichoice',
    'true_false',
    "cal",
    'essay',
    "stream_django",
    'preventconcurrentlogins',
]

STREAM_API_KEY = '4emhs9sqfdtv'
STREAM_API_SECRET = 'axa749jt5ybghj747dbqaceqf998a4wf27cewcgp4wzgtn5ctdxvr4bqd6kp6pzm'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'preventconcurrentlogins.middleware.PreventConcurrentLoginsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

ADMINS = [('Audrey', 'audrey@schoolio.co')]
MANAGERS = [('Audrey', 'audrey@schoolio.co')]

ROOT_URLCONF = 'base.urls'

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

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True

MAILER_LIST = ['audrey@schoolio.co']

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'abc'

EMAIL_HOST_PASSWORD = 'Akwenye1'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'webadmin@schoolio.co'


LOGGING = {

'version': 1,

'disable_existing_loggers': True,

'formatters': {

'verbose': {

'format': '%(levelname)s [%(asctime)s] %(module)s %(message)s'

},

},

'handlers': {

'console': {

'level': 'DEBUG',

'class': 'logging.StreamHandler',

'formatter': 'simple'

},

'file': {

'class': 'logging.handlers.RotatingFileHandler',

'formatter': 'verbose',

'filename': '/var/www/logs/ibiddjango.log',

'maxBytes': 1024000,

'backupCount': 3,

},

'mail_admins': {

'level': 'ERROR',

'class': 'django.utils.log.AdminEmailHandler'

}

},

'loggers': {

'django': {

'handlers': ['file', 'console','mail_admins'],

'propagate': True,

'level': 'DEBUG',

},

}

}

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

TIME_INPUT_FORMATS = ['%H:%M:%S',
                        '%H:%M',]

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.


MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

django_heroku.settings(locals())
