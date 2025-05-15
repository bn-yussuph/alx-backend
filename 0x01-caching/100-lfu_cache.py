#!/usr/bin/python3
"""LFU Cache Replacement Implementation Class
"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    An implementaion of LFUCache(Least frequently used)

    Attributes:
        __stats (list): A dictionary of cache keys for access count
        __rlock (RLock): Lock accessed resources to prevent race condition
    """
    def __init__(self):
        """ Instantiation method, sets instance attributes
        """
        super().__init__()
        self.__stats = {}
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
            if key in self.__stats:
                self.__stats[key] += 1
        return value

    def _balance(self, key_in):
        """ Removes the earliest item from the cache at MAX size
        """
        key_out = None
        with self.__rlock:
            if key_in not in self.__stats:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    key_out = min(self.__stats, key=self.__stats.get)
                    self.cache_data.pop(key_out)
                    self.__stats.pop(key_out)
            self.__stats[key_in] = self.__stats.get(key_in, 0) + 1
        return key_out
