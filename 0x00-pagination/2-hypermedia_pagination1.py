#!/usr/bin/env python3
"""
Added get_hyper() to the server class.
"""
import csv
from types import NoneType
from typing import Dict, List, Tuple, Union


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

    @staticmethod
    def index_range(page, page_size) -> Tuple[int, int]:
        """
        Helper function for pagination tuple.
        """
        end_index = page * page_size
        start_index = end_index - page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page from the dataset

        Args:
            page (int, optional): page required. Defaults to 1.
            page_size (int, optional): page size. Defaults to 10.

        Returns:
            List[List]: a specific page from the dataset
        """
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0
        rng = self.index_range(int(page), int(page_size))
        return self.dataset()[rng[0]: rng[1]]

    def get_hyper(self, page: int = 1,
                    page_size: int = 10) -> Dict[str, Union[int, List[List[str]], NoneType]]:
        """Get a page from the dataset

        Args:
            page (int, optional): page required. Defaults to 1.
            page_size (int, optional): page size. Defaults to 10.

        Returns:
            List[List]: a specific page from the dataset
        """
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0
        rng = self.index_range(int(page), int(page_size))
        data = self.dataset()[rng[0]: rng[1]]
        total_pages = len(self.dataset()) // page_size
        if len(self.dataset()) % page_size != 0:
            total_pages += 1
        prev_page = None
        if page > 1:
            prev_page = page - 1
        next_page = None
        if page < total_pages:
            next_page = page + 1
        res = {'page_size': page_size, 'page': page, 'data': data,
                'next_page': next_page, 'prev_page': prev_page, 'total_pages': total_pages}
        return res
