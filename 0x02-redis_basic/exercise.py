#!/usr/bin/env python3
""" Write strings to Redis """
import redis
import uuid
from typing import Union


class Cache():
    """ Caching class """
    def __init__(self):
        """ Intializing method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method that stores a key and value to redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
