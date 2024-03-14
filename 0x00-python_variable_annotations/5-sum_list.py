#!/usr/bin/env python3
"""sum_list function"""


def sum_list(input_list: list[float]) -> float:
    res: float = 0.00
    for i in input_list:
        res = res + i
    return res
