"""
Two Sum II – Input Array Is Sorted (LeetCode 167)

WHY THIS PATTERN: Sorted array + find a pair = classic opposite-direction two pointers.
Instead of brute-force O(N^2), we exploit sorted order to skip impossible pairs.

KEY INVARIANT: At each step, arr[left] + arr[right] tells us exactly which pointer to move.
- Sum too small → move left right (get a bigger number)
- Sum too big → move right left (get a smaller number)

TIME:  O(N) — each pointer moves at most N times
SPACE: O(1) — no extra data structures
"""

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []  # no solution (problem guarantees one exists)


# --- Quick test ---
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [1, 2]
    print(two_sum([2, 3, 4], 6))         # [1, 3]
    print(two_sum([-1, 0], -1))          # [1, 2]
