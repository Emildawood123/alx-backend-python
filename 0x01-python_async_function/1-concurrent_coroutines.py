#!/usr/bin/env python3
"""wait n function"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n, max_delay):
    """wait random function"""
    arr = []
    for i in range(0, n):
        await arr.append(wait_random(max_delay))
    return arr
