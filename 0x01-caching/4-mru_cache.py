#!/usr/bin/env python3
"""
This module defines a class `MRUCache` that implements MRU cache replacemen
policy
"""

from base_caching import BaseCaching
from typing import Any


class MRUCache(BaseCaching):
    """Implement MRU caching"""

    def __init__(self):
        super().__init__()
        self.tracker = list(self.cache_data.items())

    def put(self, key: Any, item: Any):
        """
        Assign to the dictionary `self.cache_data` the `item` value for the
        key `key`
        """
        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS:
                self.cache_data.pop(self.tracker[-1][0])
                mru = self.tracker.pop()[0]
                if key != mru:
                    print("DISCARD:", mru)
            self.cache_data.update({key: item})
            self.tracker.append((key, item))

    def get(self, key: Any) -> Any:
        """Return the value in `self.cache_data` linked to `key`"""
        item = self.cache_data.get(key)
        if item:
            mru = self.tracker.pop(self.tracker.index((key, item)))
            self.tracker.append(mru)
        return item
