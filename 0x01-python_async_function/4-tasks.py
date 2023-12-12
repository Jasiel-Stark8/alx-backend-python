#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple coroutines concurrently and returns a list of their results.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay to pass to the wait_random coroutine.

    Returns:
        List[float]: A list of the delays (floats) from each completed coroutine.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]