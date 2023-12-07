#!/usr/bin/env python3
"""Type Checking"""
from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: float = 2) -> List[int]:
    """
    Refactor Types to get output: 
    {'lst': typing.Tuple, 'factor': <class 'int'>, 'return': typing.List}
    """
    zoomed_in: List[int] = [int(i * factor) for i in lst]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
