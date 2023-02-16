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
    cache.incr(key)
    cache.setex("result", 10, result)
    return result
