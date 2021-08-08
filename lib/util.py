import logging
import datetime

def _logger_setup(level):
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    return logger

def _get_now_str():
    now = datetime.datetime.now()
    now_str = now.strftime('%Y%m%d%H%M%S')
    return now_str