from .base import *
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

WAGTAILADMINBASE_URL = 'localhost:8000'
BASE_URL = 'localhost:8000'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']
# STATIC_ROOT = os.path.join(BASE_DIR, 'localhost_static')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'localhost_media')
STATIC_ROOT = 'https://avenue-de-la-resistance.com/static/'
# STATIC_URL = 'https://avenue-de-la-resistance.com/static'
# STATIC_URL = '/static/'
STATIC_URL = STATIC_ROOT

#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = 'https://avenue-de-la-resistance.com/'
MEDIA_URL = os.path.join(MEDIA_ROOT, 'media/')



DATABASES['default']['NAME'] = 'resistance_db'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'watched_file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/django/resistance.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['watched_file', ],
            'level': 'INFO',
            'propagate': True,
        }
    }
}
