#!/usr/bin/python3
""" BasicCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A caching system.
    """
    def put(self, key, item):
        """Assigns value to dictionary.
        """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieves key's value.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
