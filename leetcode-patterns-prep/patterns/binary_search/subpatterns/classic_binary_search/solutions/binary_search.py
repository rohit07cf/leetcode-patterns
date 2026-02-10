"""
Binary Search (LeetCode 704)

WHY THIS PATTERN: Sorted array + find target = the textbook binary search.
This is the foundation for every other binary search variant.

KEY INVARIANT: target (if it exists) is always within arr[left..right].
Each step eliminates half the search space.

TIME:  O(log N) — halve the search space each step
SPACE: O(1) — just three pointers
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1     # target is in the right half
        else:
            right = mid - 1    # target is in the left half

    return -1  # not found


# --- Quick test ---
if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))   # 4
    print(search([-1, 0, 3, 5, 9, 12], 2))    # -1
    print(search([5], 5))                       # 0
