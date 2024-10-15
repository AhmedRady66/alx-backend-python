#!/usr/bin/env python3
"""File to reneder number numbers"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Return a random numbers between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
