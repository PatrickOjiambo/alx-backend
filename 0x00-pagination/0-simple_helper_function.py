#!/usr/bin/env python3
"""
Task 0 file
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Taks 0 function
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return (start_index, end_index)
