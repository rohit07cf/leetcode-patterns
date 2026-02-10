"""
Top K Elements — Master Template
Python's heapq is a min-heap. Negate values for max-heap behavior.
"""

import heapq
from collections import Counter


# ─── KTH LARGEST (MIN-HEAP OF SIZE K) ─────────────────────────────
def kth_largest(nums, k):
    """
    Use when: find Kth largest element.
    Key: min-heap of size K. Root = Kth largest.
    """
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # evict smallest (not in top K)

    return heap[0]  # root = Kth largest


# ─── KTH SMALLEST (MAX-HEAP OF SIZE K, NEGATED) ───────────────────
def kth_smallest(nums, k):
    """
    Use when: find Kth smallest element.
    Key: max-heap of size K (negate values). Root = Kth smallest (negated).
    """
    heap = []

    for num in nums:
        heapq.heappush(heap, -num)  # negate for max-heap
        if len(heap) > k:
            heapq.heappop(heap)     # evict largest (not in bottom K)

    return -heap[0]  # negate back


# ─── TOP K FREQUENT ───────────────────────────────────────────────
def top_k_frequent(nums, k):
    """
    Use when: find K most frequent elements.
    Alternative: bucket sort for O(N) solution.
    """
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
