#!/usr/bin/env python3
"""Type Checking"""
from typing import Tuple, List, Union

def zoom_array(lst: List[int], factor: Union[int, float] = 2) -> List[int]:
    """
    Refactor Types to get output: 
    {'lst': typing.Tuple, 'factor': <class 'int'>, 'return': typing.List}
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(int(factor))
        ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
