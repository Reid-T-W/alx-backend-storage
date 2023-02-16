#!/usr/bin/env python3
""" Write strings to Redis """
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Makes track of the calles made by a function """
    inputs = []
    outputs = []

    @wraps(method)
    def wrapper(*args, **kwds):
        """Wrapper Function"""
        self = args[0]
        self._redis.rpush(method.__qualname__+":inputs", str(args[1]))
        output = method(*args, **kwds)
        self._redis.rpush(method.__qualname__+":outputs", output)
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    Decorator function that tracks the number of
    times the store method of cache class is called
    """
    @wraps(method)
    def wrapper(*args, **kwds):
        """Wrapper function"""
        self = args[0]
        self.__qualname__ = method.__qualname__
        key = self.__qualname__
        self._redis.incr(key)
        return method(*args, **kwds)
    return wrapper


class Cache():
    """ Caching class """
    def __init__(self):
        """ Intializing method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method that stores a key and value to redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get_str(self, key: str) -> str:
        """Convert byte to string"""
        return(self._redis.get(key).decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Convert byte to int"""
        return(int(self._redis.get(key), 10))

    def get(self, key: str, fn: Callable = None) -> \
            Union[str, bytes, int, float, None]:
        """
        Modified get inorder to convert the values
        to their original types
        """
        # Handling the case where key does not exist
        # the default behaviour of get is conserved
        if not self._redis.exists(key):
            return self._redis.get(key)
        else:
            if fn == int:
                return(self.get_int(key))
            elif fn is None:
                return(self._redis.get(key))
            else:
                return(self.get_str(key))
