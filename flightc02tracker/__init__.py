"""main module initilazation"""
import logging
import os
import sys

from dotenv import load_dotenv

load_dotenv()

formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

LOG_FILE = "./app.logs"
ENVIRON = os.environ['ENVIRONMENT']

logger = logging.getLogger('app')

match ENVIRON:
    case 'test':
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
    case 'production':
        # heroku only requires stdout
        logger.setLevel(logging.INFO)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    case _:
        logger.setLevel(logging.WARN)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
