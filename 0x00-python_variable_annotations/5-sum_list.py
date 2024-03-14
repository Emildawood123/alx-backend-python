#!/usr/bin/env python3
"""sum_list function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum_list function"""
    res: float = 0.00
    for i in input_list:
        res = res + i
    return res
