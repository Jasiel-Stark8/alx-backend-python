#!/usr/bin/env python3
"""Async Basics"""

import asyncio
import random


async def wait_random(max_delay=10):
    delay = await random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return float(delay)


if __name__ == '__main__':
    result = asyncio.run(wait_random())
    print(f'{result}')
