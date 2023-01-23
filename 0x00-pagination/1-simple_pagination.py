#!/usr/bin/env python3
""" Module to create pagination parameters. """

from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    """ Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    return (start_index, start_index + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ It takes to int arguments and returns a list of rows. """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        pages = index_range(page, page_size)
        data = self.dataset()

        if pages[1] > len(data):
            return []
        else:
            return data[pages[0]:pages[1]]
