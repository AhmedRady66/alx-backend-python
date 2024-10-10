#!/usr/bin/env python3
"""File find length of list"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return length of list"""
    return [(i, len(i)) for i in lst]
