#!/usr/bin/env python3
"""sum_mixed_list function"""
from typing import List, Union

Num = Union[int, float]


def sum_mixed_list(mxd_lst: List[Num]) -> float:
    """sum_mixed_list function"""
    return sum(mxd_lst)
