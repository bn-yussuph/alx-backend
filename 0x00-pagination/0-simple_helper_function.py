#!/usr/bin/env python3
"""
Helper function for pagination tuple.
"""
from typing import Tuple

def index_range(page, page_size) -> Tuple:
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)

