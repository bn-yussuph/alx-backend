import csv
import math
from typing import List, Tuple


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
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0
        rng = self.index_range(int(page), int(page_size))
        return self.dataset()[rng[0]: rng[1]]

