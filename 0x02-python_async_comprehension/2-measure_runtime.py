#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Measure the runtime of four parallel async comprehensions"""
    start_time = perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    results = await asyncio.gather(*tasks)
    end_time = perf_counter()
    return end_time - start_time


if __name__ == '__main__':
    async def main():
        total_time = await measure_runtime()
        print(total_time)

    asyncio.run(main())
