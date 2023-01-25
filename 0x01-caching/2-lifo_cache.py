#!/usr/bin/python3
""" LIFOCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching system using LIFO- Last In First Out.
    """
    def __init__(self):
        """Initializes cache data.
        """
        super().__init__()
        self.last = None

    def put(self, key, item):
        """Add key value data to the cache.
        """
        if key is None or item is None:
            pass

        if key in self.cache_data.keys():
            self.last = key
        
        self.cache_data[key] = item

        if len(self.cache_data) > super().MAX_ITEMS:
            if not self.last:
                del_key = list(self.cache_data.keys())[-2]
                print("Discard: {}".format(del_key))
                del self.cache_data[del_key]
            else:
                print("Discard: {}".format(self.last))
                del self.cache_data[self.last]
                self.last = None

    def get(self, key):
        """ Retrieves key's value.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
