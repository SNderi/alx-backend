#!/usr/bin/python3
""" LFUCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A caching system using MRU - Most Recently Used.
    """
    def __init__(self):
        """Initializes cache data.
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """Add key value data to the cache.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > super().MAX_ITEMS:
            del_key = min(self.frequency, key=self.frequency.get)
            print("Discard: {}".format(del_key))
            del self.cache_data[del_key]
            del self.frequency[del_key]

        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

    def get(self, key):
        """ Retrieves key's value.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        return self.cache_data[key]
