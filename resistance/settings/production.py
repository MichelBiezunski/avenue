from .base import *

DEBUG = False
WAGTAILADMINBASE_URL = 'web.avenue-de-la-resistance.com'
ALLOWED_HOSTS = ['https://web.avenue-de-la-resistance.com', '23.239.13.153', 'localhost']

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
