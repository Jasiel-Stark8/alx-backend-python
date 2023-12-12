#!/usr/bin/env python3
"""Async Basics"""

import asyncio
import random


async def wait_random(max_delay=10):
    """Asynchronous coroutine waits for a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == '__main__':
    asyncio.run(wait_random())
