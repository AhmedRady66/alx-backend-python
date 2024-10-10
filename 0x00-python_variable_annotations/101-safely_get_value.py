#!/usr/bin/env python3
"""File of safely_get_value"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """Return values, add type annotations to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
