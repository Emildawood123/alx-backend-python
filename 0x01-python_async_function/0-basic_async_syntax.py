#!/usr/bin/env python3
"""wait random function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait random function"""
    random_time: float = await randrange(max_delay + 1)
    await asyncio.sleep(random_time)
    return random_time
