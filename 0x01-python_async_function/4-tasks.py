#!/usr/bin/env python3
"""Tasks function"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Tasks function"""
    arr: List[float] = []
    for i in range(0, n):
        val = wait_random(max_delay)
        arr.append(await val)
    return arr
