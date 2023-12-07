#!/usr/bin/env python3
"""More involved type annotations"""
from typing import Mapping, Any, Optional


def safely_get_value(dct: Mapping, key: Any, default: Optional[Any] = Optional[None]) -> Optional[Any]:
    """Add type annotations to function"""
    if key in dct:
        return dct[key]
    else:
        return default
