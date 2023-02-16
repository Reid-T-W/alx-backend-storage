#!/usr/bin/env python3
"""
Tracks the number of times a url is called
"""
import requests
import redis


def get_page(url: str) -> str:
    """
    Retrieves an html page given a url
    """
    cache = redis.Redis()
    key = f"count:{url}"
    result = requests.get(url).text
    # cache.setex(key, 10, result)
    cache.incr(key)
    print(cache.get(key))
    return result
