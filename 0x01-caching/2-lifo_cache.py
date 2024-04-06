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
        if key is None or item is None:
            return

        # Check if key already exists
        if key in self.cache_data:
            # Move the existing item to the end (update)
            self.cache_data[key] = item
            # Remove and re-add to simulate "most recently used"
            evicted = self.cache_data.pop(key)
            self.cache_data[key] = evicted
        else:
            # Add new item
            self.cache_data[key] = item

        # Check for overflow and discard least recently used (except updated key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key, _ = self.cache_data.popitem()
            if discarded_key != key:  # Don't discard the updated key
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
