#!/usr/bin/env python3
"""Async Comprehensions"""

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Yield Async Comprehension"""
    return [i async for i in async_generator()]


if __name__ == '__main__':
    async def main():
        await i in async_comprehension()
        print(results)

    asyncio.run(main())
