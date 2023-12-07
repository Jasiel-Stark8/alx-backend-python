#!/usr/bin/env python3
"""More involved type annotations"""
from typing import Mapping, Any, Optional, TypeVar


T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Optional[T] = None) -> Optional[T]:
    """Add type annotations to function"""
    if key in dct:
        return dct[key]
    else:
        return default
