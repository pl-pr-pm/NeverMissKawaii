import logging
import datetime
import re
from functools import wraps
import time

def _logger_setup(level):
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    return logger

def _get_now_str():
    now = datetime.datetime.now()
    now_str = now.strftime('%Y%m%d%H%M%S')
    return now_str


"複数のパターンにワードが一致した場合Trueを返却、そうでなければFalseを返却"
def _match_word(patterns, word):
    for pattern in patterns:
        repattern = re.compile(pattern)
        result = repattern.search(word)
        if result:
            return True
    return False

'''関数の実行時間を計測'''
def _time_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f'{func.__name__} took {elapsed} s')
        return result
    return wrapper