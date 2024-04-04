#!/usr/bin/python3
"""lifo cache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Defines a fifo caching system with a limit"""

    def __init__(self):
        """initialization"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            max = self.MAX_ITEMS
            if len(self.cache_data) >= max:
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
