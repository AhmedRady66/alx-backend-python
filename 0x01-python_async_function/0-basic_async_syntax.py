#!/usr/bin/env python3
"""File render random numbers between 0 and 10"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Retrun random value between 0 and 1"""
    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num
