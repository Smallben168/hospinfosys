"""
Django settings for hospinfosys project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sq)+nzsyno7f%yng6i8x3@70vy9(8tg!-kr7_-r0k+4pz6at%s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'webroot',
    'hismaxdb',
    'restwebservice',
    'pushnotifications',
    'utilitytools',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hospinfosys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\','/')],
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

WSGI_APPLICATION = 'hospinfosys.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#'HOST': 'localhost', 163.18.22.69',
DATABASES = {
    'default': {
    		'NAME': 'hismax',
    		'ENGINE': 'django.db.backends.mysql',
            'USER': 'orcl',
            'PASSWORD': 'unimaxorcl',
            'HOST': 'localhost',
            'PORT' : '3306',
            'OPTIONS' : {
        		'autocommit':True,
            	},
    	}
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# Ben Add ---未知
#REST_FRAMEWORK = {
    # Use Django's standard 'django.contrib.auth' permissions,
    # or allow read-only access for unauthenticated users.
    #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#    'DEFAULT_PERMISSION_CLASSES':(
#        'rest_framework.permissions.AllowAny',
#    ),
#}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-TW'     #Ben Modify

TIME_ZONE = 'Asia/Taipei'   #Ben Modify

USE_I18N = True

USE_L10N = True

USE_TZ = False              #Ben Modify : default True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

#Ben Add
#STATIC_ROOT = "/var/www/hospinfosys/static/"
#STATIC_ROOT=os.path.join(BASE_DIR, 'collected_static')
STATIC_ROOT=os.path.join(BASE_DIR, 'static')

#STATICFILES_DIRS = [
#    ("js", os.path.join(STATIC_ROOT,'js')),
#    ("css", os.path.join(STATIC_ROOT,'css')),
#    ("images", os.path.join(STATIC_ROOT,'images')),
#    os.path.join(BASE_DIR, "static"),
#    '/var/www/hospinfosys/static',
#]

PUSH_NOTIFICATIONS_SETTINGS = {
    'GCM_API_KEY': 'AIzaSyC89W5Scdl3gLGOQ5fAZFluh1qosscJVek',
}