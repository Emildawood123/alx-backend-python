#!/usr/bin/env python3
"""measure_runtime"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """measure_runtime"""
    start: float = time.perf_counter()
    solve = [async_comprehension() for one in range(4)]
    await asyncio.gather(*solve)
    end: float = time.perf_counter()
    return end - start
