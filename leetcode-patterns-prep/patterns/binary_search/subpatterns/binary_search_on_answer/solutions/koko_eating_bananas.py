"""
Koko Eating Bananas (LeetCode 875)

WHY THIS PATTERN: "Minimum speed to finish within h hours" = binary search on answer space.
The answer (speed) is monotonic: if speed=x works, speed=x+1 also works.
So we binary search for the MINIMUM speed that works.

KEY INVARIANT:
- check(speed) = True means Koko can finish within h hours at this speed
- If check(speed) is True, check(speed+1) is also True → monotonic
- We want the leftmost True → binary search finds it

TIME:  O(N * log(max(piles))) — log(max) binary search steps, N per check
SPACE: O(1)
"""

import math
from typing import List


def min_eating_speed(piles: List[int], h: int) -> int:
    def check(speed):
        """Can Koko eat all piles within h hours at this speed?"""
        hours_needed = 0
        for pile in piles:
            hours_needed += math.ceil(pile / speed)
        return hours_needed <= h

    # Answer space: speed can be 1 (slowest) to max(piles) (fastest needed)
    lo, hi = 1, max(piles)

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if check(mid):
            hi = mid        # this speed works, try slower
        else:
            lo = mid + 1    # too slow, need faster

    return lo


# --- Quick test ---
if __name__ == "__main__":
    print(min_eating_speed([3, 6, 7, 11], 8))    # 4
    print(min_eating_speed([30, 11, 23, 4, 20], 5))  # 30
    print(min_eating_speed([30, 11, 23, 4, 20], 6))  # 23
