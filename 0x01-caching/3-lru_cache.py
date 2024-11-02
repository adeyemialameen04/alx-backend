#!/usr/bin/env python3
"""
This module defines a class `LRUCache` that implements LRU cache replacement
policy
"""

from base_caching import BaseCaching
from typing import Any


class LRUCache(BaseCaching):
    """Implement LRU caching"""

    def __init__(self):
        super().__init__()
        self.tracker = list(self.cache_data.keys())

    def put(self, key: Any, item: Any):
        """
        Assign to the dictionary `self.cache_data` the `item` value for the
        key `key`
        """
        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS:
                self.cache_data.pop(self.tracker[0])
                lru = self.tracker.pop(0)
                if key != lru:
                    print("DISCARD:", lru)
            self.cache_data.update({key: item})
            self.tracker.append(key)

    def get(self, key: Any) -> Any:
        """Return the value in `self.cache_data` linked to `key`"""
        item = self.cache_data.get(key)
        if item:
            mru = self.tracker.pop(self.tracker.index(key))
            self.tracker.append(mru)
        return item
