#!/usr/bin/env python3
''' complex types - mixed list
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' sums a list of floats and integers. '''

    return float(sum(mxd_lst))
