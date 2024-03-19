#!/usr/bin/env python3
"""async_comperhension function"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async_comperhension function"""
    res = []
    async for i in async_generator():
        res.append(i)
    return res
