from functools import wraps
from time import time


def http_request_timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        run_time = time() - start_time
        return result, run_time

    return wrapper
