#!/usr/bin/env python3
"""
Helper function for pagination tuple.
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple:
    """A helper function for pagination indices generation

    Args:
        page (int): th page number
        page_size (int): the size of the page

    Returns:
        Tuple: a tuple containing a starting and ending indices of the page
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
