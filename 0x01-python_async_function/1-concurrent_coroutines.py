#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_

    Args:
        n (_type_): _description_
        max_delay (_type_): _description_

    Returns:
        list[float]: _description_
    """
    spawn  = [wait_random(max_delay) for _ in range(n)]
    completed = await asyncio.gather(*spawn)
    return completed
