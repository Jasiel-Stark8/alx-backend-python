#!/usr/bin/env python3
"""Measure the runtime"""

import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of the wait_n coroutine.

    Args:
        n (int): The number of concurrent coroutines to run.
        max_delay (int): The maximum delay to pass to each coroutine.

    Returns:
        float: The total execution time.
    """
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()

    total_time = end_time - start_time
    average_time  = total_time / n
    return average_time
