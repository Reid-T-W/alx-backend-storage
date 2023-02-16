#!/usr/bin/env python3
"""
Tracks the number of times a url is called
"""
import requests
import redis
from functools import wraps


def track_url_access_count(method):
    """
    counts the number of times a url is accessed
    """
    @wraps(method)
    def wrapper(*args, **kwds):
        cache = redis.Redis()
        key = f"count:{args[0]}"
        result = method(*args, **kwds)
        cache.expire(key, 10)
        cache.set(key, result)
        # cache.incr(key)
        print(cache.get(key))
        return result
    return wrapper


@track_url_access_count
def get_page(url: str) -> str:
    """
    Retrieves an html page given a url
    """
    html = requests.get(url).text
    return html
