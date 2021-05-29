"""
Django settings for estateSite project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='foobar')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)


# ALLOWED_HOSTS = ['akezurel.pythonanywhere.com', '127.0.0.1']
# ALLOWED_HOSTS=[]
ALLOWED_HOSTS = config('ALLOWED_HOSTS',default='localhost,127.0.0.1,akezurel.pythonanywhere.com,kamolthip.herokuapp.com').split(',')


# Application definition

INSTALLED_APPS = [
    'estate.apps.EstateConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_google_maps',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'estateSite.urls'

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
                'django.template.context_processors.request',
            ],
        },
    },
]

LOGIN_REDIRECT_URL = 'estate:index'

WSGI_APPLICATION = 'estateSite.wsgi.application'

# Database

if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': {
            dj_database_url.config(default=os.environ['DATABASE_URL'])
        }
    }
else:
    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.sqlite3',
            'ENGINE': config('DATABASE_ENGINE',default='django.db.backends.sqlite3'),

            # 'NAME': BASE_DIR / 'db.sqlite3',
            'NAME': config('DATABASE_NAME',default='db.sqlite3'),
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3')

            'USER': config('DATABASE_USER',default='user'),
            'PASSWORD': config('DATABASE_PWD',default='password'),
            # 'HOST': config('DATABASE_HOST',default='localhost'),
            'HOST': config('DATABASE_HOST',default='kamolthip.herokuapp.com'),
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }

# Password validation

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

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = config('TIME_ZONE',default='Asia/Bangkok')
TIME_ZONE='Asia/Bangkok'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_ROOT = "/home/akezurel/real-estate-rental/estate/static/"
# STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'

MEDIA_URL = '/images/'
# MEDIA_ROOT = "/home/akezurel/real-estate-rental/images/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'images')


AUTH_USER_MODEL = 'estate.CustomUser'

GOOGLE_MAPS_API_KEY = config('GOOGLE_MAPS_API_KEY', default='AIzaSyCO5k3BaMnHoLBabkndpqf2LFUFHOfTP5Q')

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = 'none'

LOGIN_REDIRECT_URL = 'estate:index'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'access_type': 'online'}
    },
}

ACCOUNT_FORMS = {
    'signup': 'estate.forms.custom_form.CustomSignupForm',
}

#Email -> gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Nananda.estate@gmail.com'
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='password')
EMAIL_USE_TLS = True