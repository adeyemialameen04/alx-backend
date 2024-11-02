#!/usr/bin/env python3
"""
This module defines a class `LIFOCache` that implements LIFO cache replacemen
policy
"""

from base_caching import BaseCaching
from typing import Any


class LIFOCache(BaseCaching):
    """Implement LIFO caching"""

    def put(self, key: Any, item: Any):
        """
        Assign to the dictionary `self.cache_data` the item `value` for the
        key `key`
        """
        if key and item:
            if len(
                    self.cache_data
            ) >= BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():
                to_pop = list(self.cache_data.keys())[-1]
                self.cache_data.pop(to_pop)
                print("DISCARD:", to_pop)
            self.cache_data.update({key: item})

    def get(self, key: Any) -> Any:
        """Return the value in `self.cache_data` linked to `key`"""
        if key:
            return self.cache_data.get(key)
        return None
