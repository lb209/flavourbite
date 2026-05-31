import os
from pathlib import Path
import dj_database_url
import pymysql

pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-secret-key'

DEBUG = True

ALLOWED_HOSTS = ['*']


# ================= INSTALLED APPS =================

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # APP
    'home',

    # API
    'rest_framework',

    # CORS
    'corsheaders',
]


# ================= MIDDLEWARE =================

MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'myproject.urls'


# ================= TEMPLATES =================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'myproject.wsgi.application'


# ================= DATABASE =================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'mydatabase',

        'USER': 'root',

        'PASSWORD': '1234',

        'HOST': 'localhost',

        'PORT': '3306',
    }
}


# ================= PASSWORD =================

AUTH_PASSWORD_VALIDATORS = []


# ================= LANGUAGE =================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# ================= STATIC =================

STATIC_URL = 'static/'


# ================= DEFAULT AUTO FIELD =================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ================= CORS =================

CORS_ALLOW_ALL_ORIGINS = True