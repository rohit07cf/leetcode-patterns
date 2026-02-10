"""
Move Zeroes (LeetCode 283)

WHY THIS PATTERN: "Move all zeroes to end, maintain order" = same-direction two pointers.
The write pointer collects non-zero elements; remaining positions become zero.

KEY INVARIANT: arr[0..write-1] contains all non-zero elements in original order.

TIME:  O(N) — single pass
SPACE: O(1) — in-place
"""

from typing import List


def move_zeroes(nums: List[int]) -> None:
    """Modify nums in-place."""
    write = 0

    # Pass 1: move all non-zero elements to the front
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    # Pass 2: fill the rest with zeroes
    for i in range(write, len(nums)):
        nums[i] = 0


# --- Quick test ---
if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    move_zeroes(arr)
    print(arr)  # [1, 3, 12, 0, 0]

    arr2 = [0, 0, 0]
    move_zeroes(arr2)
    print(arr2)  # [0, 0, 0]
