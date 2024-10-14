#!/usr/bin/env python3
"""File render list of random"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return list of float random numbers"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*tasks)
    return result
