#!/usr/bin/python3
""" MRUCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A caching system using MRU - Most Recently Used.
    """
    def __init__(self):
        """Initializes cache data.
        """
        super().__init__()
        self.frequency = list(self.cache_data.keys())

    def put(self, key, item):
        """Add key value data to the cache.
        """
        if key is None or item is None:
            pass

        self.cache_data[key] = item

        if len(self.cache_data) > super().MAX_ITEMS:
            del_key = self.frequency[-1]
            print("Discard: {}".format(del_key))
            del self.cache_data[del_key]
            self.frequency.remove(del_key)

        if key in self.frequency:
            self.frequency.remove(key)
            self.frequency.append(key)
        else:
            self.frequency.append(key)

    def get(self, key):
        """ Retrieves key's value.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        self.frequency.remove(key)
        self.frequency.append(key)
        return self.cache_data[key]
