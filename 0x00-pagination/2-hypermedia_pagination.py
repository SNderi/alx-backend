#!/usr/bin/env python3
""" Module to create pagination parameters. """

from typing import Tuple, List, Dict
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
        """Initializes the data."""
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

        start, end = index_range(page, page_size)
        data = self.dataset()

        try:
            data_set = data[start:end]
        except IndexError:
            data_set = []
        return data_set

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary of the metadata for the data returned
        by get_page.
        """
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size + 1
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page + 1 <= total_pages else None
        if page < 1:
            prev_page = None
        if data == []:
            next_page = None

        return {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
            }
