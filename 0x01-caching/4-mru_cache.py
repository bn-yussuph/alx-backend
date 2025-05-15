#!/usr/bin/python3
"""MRU Cache Replacement Implementation Class
"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    An implementation of MRU(Most Recently Used) Cache

    Attributes:
        __keys (list): Stores cache keys from least to most accessed
        __rlock (RLock): Lock accessed resources to prevent race condition
    """
    def __init__(self):
        """ Instantiation method, sets instance attributes
        """
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            key_out = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if key_out is not None:
                print('DISCARD: {}'.format(key_out))

    def get(self, key):
        """ Get an item by key
        """
        with self.__rlock:
            value = self.cache_data.get(key, None)
            if key in self.__keys:
                self._balance(key)
        return value

    def _balance(self, key_in):
        """ Removes the earliest item from the cache at MAX size
        """
        key_out = None
        with self.__rlock:
            keysLength = len(self.__keys)
            if key_in not in self.__keys:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    key_out = self.__keys.pop(keysLength - 1)
                    self.cache_data.pop(key_out)
            else:
                self.__keys.remove(key_in)
            self.__keys.insert(keysLength, key_in)
        return key_out
