#!/usr/bin/env python3
"""More involved type annotations"""
from typing import Mapping, Any, Optional, TypeVar, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Optional[T] = None) -> Union[Any, T]:
    """Add type annotations to function"""
    if key in dct:
        return dct[key]
    return default
