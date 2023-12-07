#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of intergers in a mixed list as float"""
    if mxd_lst is None:
        return 0
    return sum(mxd_lst)
