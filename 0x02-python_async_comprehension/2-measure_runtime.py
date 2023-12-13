#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    measure_runtime - function execute async_com 4 times
    Arguments:
        nothing
    Returns:
        the total exection time required to complete the task
    """
    start_time = perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    results = await asyncio.gather(*tasks)
    end_time = perf_counter()
    return (end_time - start_time)


if __name__ == '__main__':
    async def main():
        total_time = await measure_runtime()
        print(total_time)

    asyncio.run(main())
