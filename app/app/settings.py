# app/settings.py
# Application settings required

from os.path import dirname, join


DEBUG=True
TEMPLATE_DEBUG = True

# Location of app directory
ROOT_URLCONF = 'app.urls'
BASE_DIR     = dirname(dirname(__file__))
DOC_DIR      = BASE_DIR+'/user_doc'
   
# Login
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

# App startup
SECRET_KEY = 's!qs5!9(bhkv7#hn#172zm_*l#m)j(8lv1gj)#84p$9+^&amp;bn9e'


# Shim to run application from Apache
WSGI_APPLICATION = 'app.wsgi.application'


# Static server
STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = (  BASE_DIR+'/static', )
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'doc',
    #'task',
    'util',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

 
# Loading templates
TEMPLATE_DIRS = (
    BASE_DIR+"/templates",
)


from db import DATABASES
