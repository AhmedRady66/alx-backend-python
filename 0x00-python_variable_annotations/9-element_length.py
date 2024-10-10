#!/usr/bin/env python3
"""File of Duck typing"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return Duck typing"""
    return [(i, len(i)) for i in lst]
