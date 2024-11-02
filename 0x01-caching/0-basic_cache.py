#!/usr/bin/env python3
"""Basic dictionary for caching"""

from base_caching import BaseCaching
from typing import Any


class BasicCache(BaseCaching):
    """Class modelling a basic caching system"""
    def put(self, key: Any, item: Any):
        """
        Assign to the dictionary `self.cache_data` the item `value` for the
        key `key`
        """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key: Any) -> Any:
        """Return the value in `self.cache_data` linked to `key`"""
        return self.cache_data.get(key)
