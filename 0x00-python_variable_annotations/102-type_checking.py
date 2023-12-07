#!/usr/bin/env python3
"""Type Checking"""
from typing import Tuple, Any

def zoom_array(lst: Tuple[Any, ...], factor: Any = 2) -> Tuple[Any, ...]:
    """Refactor to accept [Any, ...]"""
    zoomed_in: Tuple[Any, ...] = tuple(i * factor for i in lst)
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
