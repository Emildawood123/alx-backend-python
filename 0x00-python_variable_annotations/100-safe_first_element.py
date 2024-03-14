#!/usr/bin/env python3
"""safe_first_element function"""
from typing import Union, Sequence, Any, NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """safe_first_element function"""
    if lst:
        return lst[0]
    else:
        return None
