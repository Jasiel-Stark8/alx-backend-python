#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return multiplied arg as float"""
    if multiplier is None:
        return lambda x: x

    def multiplier_function(x: float) -> float:
        """Finally return x * multiplier"""
        return x * multiplier

    return multiplier_function
