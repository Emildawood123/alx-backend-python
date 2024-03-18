#!/usr/bin/env python3
"""wait n function"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait random function"""
    arr: List[float] = []
    for i in range(0, n):
        val = wait_random(max_delay)
        arr.append(await val)
    return arr
