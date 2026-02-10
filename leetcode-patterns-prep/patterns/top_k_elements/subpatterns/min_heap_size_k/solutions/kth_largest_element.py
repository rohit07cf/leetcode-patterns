"""
Kth Largest Element in an Array (LeetCode 215)

WHY THIS PATTERN: "Kth largest" = textbook min-heap of size K.
The min-heap holds the K largest elements. Its root = Kth largest.

KEY INVARIANT: heap always contains exactly K elements (the K largest seen so far).
When a new element > heap root, it replaces the root.

TIME:  O(N log K) — N pushes, each O(log K)
SPACE: O(K) — heap stores K elements

NOTE: Python also has quickselect via random partition for O(N) average,
but the heap approach is simpler and more commonly expected in interviews.
"""

import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    heap = []  # min-heap of size k

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)  # remove smallest (not in top K)

    return heap[0]  # root = Kth largest


# --- Quick test ---
if __name__ == "__main__":
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))        # 5
    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
