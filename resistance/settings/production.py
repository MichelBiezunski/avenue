from .base import *

DEBUG = False
WAGTAILADMINBASE_URL = 'avenue-de-la-resistance.com'
ALLOWED_HOSTS = ['www.avenue-de-la-resistance.com', 'avenue-de-la-resistance.com', '23.239.13.153']

DATABASES['default']['NAME'] = 'resistance_db'

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
