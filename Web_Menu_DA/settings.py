import os
from pathlib import Path

"""Next 2 string need for correct work knox Authentication"""
from datetime import timedelta
from rest_framework.settings import api_settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-$pso2)*$i!8k#k_y^6j_31c@6@fv66+5)m1@0o3p3ii#p*use3')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

HOST = os.environ.get('HOST_NAME', 'http://127.0.0.1:8000')
ALLOWED_HOSTS = [
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # libraries
    'rest_framework',
    'django_filters',
    'phonenumber_field',
    'knox',

    # applications
    'company',
    'location',
    'registration',
    'address',
    'image',
    'product',
    'menu',

    # 'client',
    # 'manager',
    # 'owner',
]

AUTH_USER_MODEL = 'registration.WebMenuUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Web_Menu_DA.urls'

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

WSGI_APPLICATION = 'Web_Menu_DA.wsgi.application'

"""If we wont to work with DB from local machine and from docker at the same time we must:
1. make personal .env file for docker / docker-compose or directly write environment data in docker / docker-compose
2. we do not need an .env file with data for the local machine. Django does not read this data
3. the data for ENGINE, NAME, USER must be specified directly
4. data for HOST must be specified with reference to the internal .env file in the dock
5. data for PORT must be specified with reference to the internal .env file in the dock. Also, if we changed the
 standard output port (5432), we must specify the new one as an alternative for connection"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", 'Postgres_Web_Menu_DA'),
        "USER": os.environ.get("POSTGRES_USER", 'postgres'),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", 'K@i160486'),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT", "5433"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# email
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.ukr.net')
EMAIL_PORT = 2525
EMAIL_USE_SSL = True

REST_KNOX = {
    'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
    'AUTH_TOKEN_CHARACTER_LENGTH': 64,
    'TOKEN_TTL': timedelta(hours=24),
    'USER_SERIALIZER': 'registration.serializers.WebMenuUserSerializer',  # displays all data in the view
    'TOKEN_LIMIT_PER_USER': 2,
    'AUTO_REFRESH': True,
    'MIN_REFRESH_INTERVAL': 360,
    'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT,
}
