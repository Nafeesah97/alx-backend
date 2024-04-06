#!/usr/bin/python3
"""most recently used cache"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """deletes least recently used cache"""
    def __init__(self):
        """initialization"""
        super().__init__()
        self.cache_data = OrderedDict()


    def _add_node(self, node):
        """Add a node to the front of the linked list"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove a node from the linked list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_front(self, node):
        """Move a node to the front of the linked list"""
        self._remove_node(node)
        self._add_node(node)

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
