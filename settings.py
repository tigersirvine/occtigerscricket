# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os
'''
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.mysql',
        'ENGINE':'google.appengine.ext.django.backends.rdbms',
        'HOST': '/cloudsql/occtigerscricket:cricekt',
        #use this if you want to connect locally to cloud database
        #'HOST' : '173.194.253.3',
        'INSTANCE': 'occtigerscricket:cricket',
        #'NAME' : 'mysql',
        'USER': 'root',
        'PASSWORD' : 'root',
        
    }
}
'''
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
#if True:
    DATABASES = {
    'default': {
        'ENGINE':'google.appengine.ext.django.backends.rdbms',
        'HOST': '/cloudsql/occtigerscricket:cricekt',
        'INSTANCE': 'occtigerscricket:cricket',
        'NAME': 'mysql',
        'USER': 'root',        
        #'PASSWORD' : 'root',
    }
    }
elif os.getenv('SETTINGS_MODE') == 'prod':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            #'ENGINE':'google.appengine.ext.django.backends.rdbms',
            #'HOST': '/cloudsql/occtigerscricket:cricekt',
        #use this if you want to connect locally to cloud database
            'HOST' : '173.194.253.3',
            'INSTANCE': 'occtigerscricket:cricket',
            'NAME' : 'mysql',
            'USER': 'root',
            'PASSWORD' : 'root',
           }
        }   
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            #'ENGINE':'google.appengine.ext.django.backends.rdbms',
            #'HOST': '/cloudsql/occtigerscricket:cricekt',
        #use this if you want to connect locally to cloud database
            'HOST' : 'localhost',
            #'INSTANCE': 'occtigerscricket:cricket',
            'NAME' : 'cricekt',
            'USER': 'root',
            'PASSWORD' : 'root',
           }
        }   
    # Running in development, so use a local MySQL database.
    
# Activate django-dbindexer for the default database
#DATABASES['native'] = DATABASES['default']
#DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'djangotoolbox',
    'autoload',
    'dbindexer',
    'django.contrib.staticfiles',
    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
    'mainapp',
)

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)
ROOT_PATH = os.path.dirname(__file__)


# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

MEDIA_ROOT = ROOT_PATH + '/media/'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
#ADMIN_MEDIA_PREFIX = '/django/contrib/admin/static/admin/'


TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'
