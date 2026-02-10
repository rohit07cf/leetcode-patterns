"""
Binary Search on Answer Space — Template
"""

import math
from typing import List


def koko_eating_bananas_style(piles: List[int], h: int) -> int:
    """
    Find minimum eating speed to finish all piles within h hours.
    check(speed) = can Koko finish within h hours at this speed?
    """

    def check(speed):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
        return hours <= h

    lo, hi = 1, max(piles)  # speed range: 1 to max pile

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if check(mid):
            hi = mid        # this speed works, try slower
        else:
            lo = mid + 1    # too slow, need faster

    return lo


def capacity_to_ship_style(weights: List[int], days: int) -> int:
    """
    Find minimum ship capacity to ship all packages within D days.
    check(capacity) = can we ship within D days with this capacity?
    """

    def check(capacity):
        day_count = 1
        current_load = 0
        for w in weights:
            if current_load + w > capacity:
                day_count += 1
                current_load = 0
            current_load += w
        return day_count <= days

    lo = max(weights)       # must at least carry the heaviest package
    hi = sum(weights)       # worst case: ship everything in 1 day

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo
