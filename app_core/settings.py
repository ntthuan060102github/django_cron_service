"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import pytz
from pathlib import Path
from decouple import config

ENVIRONMENT = config("APP_ENV", default='local') 

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-pajk1seij+@o=)_zhsg$q$3n#w&%8qnp4t2vjpgnxw$kkalw%f'

DEBUG = ENVIRONMENT != "production"

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'django_app',
    'django_celery_beat'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_app.middlewares.refactor_response.RefactorResponse'
]

ROOT_URLCONF = 'django_app.urls'

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

WSGI_APPLICATION = 'app_core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': config("MYSQL_DATABASE_DB", default="mypt_cron"),
        'USER': config("MYSQL_DATABASE_USER", "root"),
        'PASSWORD': config("MYSQL_DATABASE_PASSWORD", "Thuan123"),
        'HOST': config("MYSQL_DATABASE_HOST", "127.0.0.1"),
        'PORT': config("MYSQL_DATABASE_PORT", "3306"),
    }
}

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

REDIS_HOST = config("CENTRALIZED_SESSION_REDIS_HOST", "127.0.0.1")
REDIS_PORT = config("CENTRALIZED_SESSION_REDIS_PORT", "6379")
REDIS_DATABASE = config("CENTRALIZED_SESSION_REDIS_DATABASE", 1)
REDIS_DATABASE_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DATABASE}'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_DATABASE_URL,
    }
}

SESSION_CACHE_ALIAS = "default"

LANGUAGE_CODE = 'en-us'
PY_TIME_ZONE = pytz.UTC
TIME_ZONE = PY_TIME_ZONE.zone
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = REDIS_DATABASE_URL
CELERY_RESULT_BACKEND = REDIS_DATABASE_URL
CELERY_CACHE_BACKEND = "default"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = "Asia/Ho_Chi_Minh"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_IMPORTS = ["django_app.tasks.cron_tasks", "django_app.tasks.queue_tasks"]