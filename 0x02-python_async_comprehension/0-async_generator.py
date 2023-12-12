#!/usr/bin/env python3
"""Async Generator"""

import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    for i in range(10):
        await asyncio.sleep(1)
        yield i


async def main():
    async for value in async_generator():
        print(value)


if __name__ == '__main__':
    asyncio.run(main())
