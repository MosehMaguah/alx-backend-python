#!/usr/bin/env python3
''' Complex types - functions '''

from tyyping import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' multiplies a float by the multiplier '''

    return lambda x: x * multiplier
