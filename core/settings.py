# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

import os
from decouple import config
from unipath import Path
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = Path(__file__).parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False)

# load production server from .env
ALLOWED_HOSTS = ['*']

# 'localhost', '127.0.0.1', config('SERVER', default='127.0.0.1'), 

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Enable the inner app 
    'api',
    'lms_app',
    'user',
    'phonenumber_field',
    'rest_framework',
    'rest_framework.authtoken',
    'cities_light',
    # 'storages',
    'fcm_django',
    'corsheaders',
    'crispy_forms',
    'django_select2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"   # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(BASE_DIR, "core/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]




WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sbr',
#         'USER': 'admin',
#         'PASSWORD': 'e961c4cc50b74025879392eeb68f8681261202b025ea584c',
#         'HOST': '127.0.0.1',
#         'PORT': '',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES',character_set_connection=utf8,collation_connection=utf8_unicode_ci"
#         }
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'dblms.sqlite'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sbr',
        'USER': 'shabeer',
        'PASSWORD': '7K*52Ck7E-apT?pq6EZ7CCS&B7vAt',
        'HOST': 'localhost',

    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'sbrdb',
#         'USER': 'shabeer',
#         'PASSWORD': '7K*52Ck7E-apT?pq6EZ7CCS&B7vAt',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'database-1',
#         'USER': 'admin',
#         'PASSWORD': 'FpBesS8FRTJGA7qeuev4WLmP3',
#         'HOST': 'database-1.c87jt2nj0lma.us-east-2.rds.amazonaws.com',
#         'PORT': '3306',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sbr',
#         'USER': 'admin',
#         'PASSWORD': 'FpBesS8FRTJGA7qeuev4WLmP3',
#         'HOST': 'database-1.c87jt2nj0lma.us-east-2.rds.amazonaws.com',
#         'PORT': '3306',
#     }
# }



#nothing
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'user.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'DEFAULT_AUTHENTICATION_CLASSES': (
        #     'rest_framework.authentication.TokenAuthentication',
        # ),
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}


FCM_DJANGO_SETTINGS = {
        "FCM_SERVER_KEY": "AAAAMmDy9Aw:APA91bHClA1aMAxJNRChRZtFxmPaK1okQRjguMofrUPMNviLp76_hTwfBK6O6JbuA1b-aaY5DWmbqgPeOzGPqwJUSL5niSJhG2TlgiUoz2yVPOdewbvJiIGGazan6wUdOxJsV-3mI5_h",
}


CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# CACHES = {
#             "default": {
#                 "BACKEND": "django_redis.cache.RedisCache",
#                 "LOCATION": "redis://127.0.0.1:6379/1",
#                 "OPTIONS": {
#                     "CLIENT_CLASS": "django_redis.client.DefaultClient",
#                 }
#             },
#             'select2': {
#                 "BACKEND": "django_redis.cache.RedisCache",
#                 "LOCATION": "redis://127.0.0.1:6379/2",
#                 "OPTIONS": {
#                     "CLIENT_CLASS": "django_redis.client.DefaultClient",
#                 }
#             }
#         }


# Tell select2 which cache configuration to use:
# SELECT2_CACHE_BACKEND = "select2"

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'core/static'),
)


MEDIA_URL= "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'media_root')
#############################################################
#############################################################




# AWS_ACCESS_KEY_ID = 'AKIAUGL6LDKVBY2AK6E2'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'sbr-bucket'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'
# AWS_DEFAULT_ACL = None


# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DEFAULT_FILE_STORAGE = 'core.storage_backends.MediaStorage' 



