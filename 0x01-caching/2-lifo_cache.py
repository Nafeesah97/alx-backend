#!/usr/bin/python3
"""lifo cache"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """Defines a fifo caching system with a limit"""

    def __init__(self):
        """initialization"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            max = self.MAX_ITEMS
            if len(self.cache_data) >= max:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD: {}".format(last_key))
        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
