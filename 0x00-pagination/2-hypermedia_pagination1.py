#!/usr/bin/env python3
"""
Implements get_page() in the server class.
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
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
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
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        rng = self.index_range(int(page), int(page_size))
        return self.dataset()[rng[0]: rng[1]]

    def get_hyper(self,
                    page: int = 1,
                    page_size: int = 10) -> Dict[str,
                                            Union[int,
                                                    List[List],
                                                    None]]:
        """a function to return hypermedia page

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): page size. Defaults to 10.

        Returns:
            Dict[str, Union[int, List[List[str]], NoneType]]: returns
                                                    a hypermedia data
        """
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size
        if len(self.dataset()) % page_size != 0:
            total_pages += 1

        prev_page = None
        if page > 1:
            prev_page = page - 1

        next_page = None
        if page < total_pages:
            next_page = page + 1

        res = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': int(total_pages)}
        return res
