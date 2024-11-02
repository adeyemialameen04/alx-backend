#!/usr/bin/python3

""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()
        self.freq_counter = {}  # Keeps track of the frequency of each key

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item  # Update item
                self.freq_counter[key] += 1  # Increment frequency
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # Find keys with the minimum frequency
                    min_freq = min(self.freq_counter.values())
                    keys_to_discard = [
                        k for k, v in self.freq_counter.items()
                        if v == min_freq]
                    # If multiple items have the same minimum frequency, use
                    # LRU
                    if len(keys_to_discard) > 1:
                        lru_key = min(
                            self.freq_counter,
                            key=lambda k: self.freq_counter[k])
                        keys_to_discard = [lru_key]
                    # Discard the keys
                    for k in keys_to_discard:
                        del self.cache_data[k]
                        del self.freq_counter[k]
                        print("DISCARD: {}".format(k))
                self.cache_data[key] = item
                self.freq_counter[key] = 1

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            if key in self.cache_data:
                self.freq_counter[key] += 1
                return self.cache_data[key]
            else:
                return None
