#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """Return complext agr types as tuple"""
    if k is None or v is None:
        return ('', 0)
    return (k, v**2)
