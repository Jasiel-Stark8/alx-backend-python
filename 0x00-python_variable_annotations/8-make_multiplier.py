#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return multiplied arg as float"""
    if multiplier is None:
        raise ValueError('Multiplier must be a float')
    return lambda x: x * multiplier
