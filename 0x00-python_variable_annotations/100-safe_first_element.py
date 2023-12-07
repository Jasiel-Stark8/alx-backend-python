#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""
from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Corrected duck-typed annotations"""
    return lst[0] if lst else None
