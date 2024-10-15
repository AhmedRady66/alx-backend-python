#!/usr/bin/env python3
"""Measure the total runtime of running async_comprehension
four times in parallel"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return runtime of four running async_comprehension in parallel"""
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    elapsed = time.perf_counter() - start
    return elapsed
