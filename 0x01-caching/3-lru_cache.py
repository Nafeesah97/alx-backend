#!/usr/bin/python3
"""least recently used cache"""
from base_caching import BaseCaching


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(BaseCaching):
    """deletes least recently used cache"""
    def __init__(self):
        """initialization"""
        super().__init__()
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

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
        """ Add an item in the cache
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = item
            self._move_to_front(node)
        else:
            if len(self.cache) == self.MAX_ITEMS:
                print("DISCARD: {}".format(self.tail.prev.key))
                del self.cache[self.tail.prev.key]
                self._remove_node(self.tail.prev)
            new_node = Node(key, item)
            self.cache[key] = new_node
            self._add_node(new_node)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        else:
            return None