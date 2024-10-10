#!/usr/bin/env python3
"""File of Duck typing"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return Duck typing"""
    if lst:
        return lst[0]
    else:
        return None
