#!/usr/bin/env python3
"""Complex types - list of floats"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """Return sum of list as float"""
    if input_list is None:
        return 0
    return sum(input_list)
