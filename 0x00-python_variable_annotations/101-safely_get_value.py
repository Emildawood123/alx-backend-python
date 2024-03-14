#!/usr/bin/env python3
"""safely_get_value function"""
from typing import Mapping, Any, Union, TypeVar

tV = TypeVar("T", bound=Any)
abbr = Union[tV, None]
abbr2 = Union[Any, tV]


def safely_get_value(dct: Mapping, key: Any, default: abbr = None) -> abbr2:
    if key in dct:
        return dct[key]
    else:
        return default
