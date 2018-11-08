import os
from logging.config import dictConfig

from .alphorn import Alphorn
from .response import Response

LOG_CONF = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'stream': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        'alphorn': {
            'handlers': ['stream'],
            'level': os.getenv('ALPHORN_LOG_LEVEL', 'DEBUG'),
        },
    }
}

dictConfig(LOG_CONF)
