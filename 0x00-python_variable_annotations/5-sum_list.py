#!/usr/bin/env python3
"""Complex types - list of floats"""


def sum_list(input_list: list[float]) -> float:
    """Retunr sum of list as float"""
    total: float = 0.0
    for i in input_list:
        total += i
    return total
