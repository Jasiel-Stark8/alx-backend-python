#!/usr/bin/env python3
"""Async Generator"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield a random integer after every 1 seconds of sleep within a range"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == '__main__':
    async def main():
        result = []
        async for value in async_generator():
            result.append(value)
        print(result)

    asyncio.run(main())
