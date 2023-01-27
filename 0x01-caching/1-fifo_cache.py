#!/usr/bin/python3
""" FIFOCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A caching system using FIFO- First In First Out.
    """
    def __init__(self):
        """Initializes cache data.
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Add key value data to the cache.
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                del_key = list(self.cache_data.keys())[0]
                print("Discard: {}".format(del_key))
                del self.cache_data[del_key]

    def get(self, key):
        """ Retrieves key's value.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
