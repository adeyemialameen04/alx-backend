#!/usr/bin/env python3
"""This module defines the class `Server` and the function `index_range`"""
import csv
import math
from typing import Dict, List, Tuple, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters
    """
    return (page_size * page - page_size, page_size * page)


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
        """Return the appropriate page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Any]:
        """Return hypermedia dictionary"""
        data = self.get_page(page, page_size)
        _page_size = len(data)
        _page = page  # if data else None
        next_page = page + 1 if self.get_page(page + 1) else None
        prev_page = page - 1 or None
        dataset = []
        if self.__dataset is not None:
            dataset = self.__dataset
        total_pages = math.ceil(len(dataset) / page_size)
        return {
            "page_size": _page_size,
            "page": _page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
