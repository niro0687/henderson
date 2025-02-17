"""
Django settings for nikemall project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-one1xd!tms523&-ae^uqnp!lyjs9=2fj#bxrph9b+jshb%*2ho'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "192.168.43.1"]

SPECIAL_USER_USERNAME = "special0687nikemall.id"
SPECIAL_USER_EMAIL = "specialuser@nikemall.com"
SPECIAL_USER_PASSWORD = "niro.ni.0687"
SPECIAL_USER_TRANSACTION_PASSWORD = "niro0687"
SPECIAL_USER_FIRST_NAME = "Special"
SPECIAL_USER_LAST_NAME = "User"
SPECIAL_USER_FIRST_NAME = "Special"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.middleware.midd.WebAccessMiddleware',
    'app.middleware.midd.NikeMallUserGetMiddleware',
    'app.middleware.midd.PostDataMiddleware',
    'app.middleware.midd.UserLoginMiddleware',
    'django.middleware.http.ConditionalGetMiddleware'
]

ROOT_URLCONF = 'nikemall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'nikemall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
    	'NAME': 'default',
        'ENGINE': "django.db.backends.sqlite3",
    }
}

DATABASE_ROUTERS = ["app.router.authRouter.AuthRouter", "app.router.otherRouter.OtherRouter"]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = "media"
MEDIA_URL = "/media/"

STATICFILES_DIR = (
    os.path.join(BASE_DIR, "static"),
)


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = "/login/null/"

RECHARGE_CODE = "THP1qGXjTUy319nRo32vE9S7GhkvAYmBfA"

NETWORK_ALLOWED = ["TRC-20", "Airtel Money", "Orange Money", "MVola", "PayPal","Payeer"]

MAX_WITHDRAW_METHOD = 3

MAX_LOGIN_LIMIT = 30

MADAGASCAR_TIMEZONE = "Indian/Antananarivo"

PARIS_TIMEZONE = "Europe/Paris"

REUNION_TIMEZONE = "Indian/Reunion"


NIRO_FIRST_NAME = "HENDERSON"
NIRO_LAST_NAME = "Niro"
NIRO_USERNAME = "niro.off"
NIRO_EMAIL = "niro.admin@nikemall.com"
NIRO_PASSWORD = "niro.NI.0687"