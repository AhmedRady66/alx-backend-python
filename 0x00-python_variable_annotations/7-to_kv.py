#!/usr/bin/env python3
"""File of tuple str and float"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuble of str and number"""
    return (k, float(v ** 2))
