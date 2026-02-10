"""
Min-Heap of Size K — Template
"""

import heapq


def kth_largest(nums, k):
    """Find Kth largest element using min-heap of size K."""
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


def k_closest_points(points, k):
    """
    Find K closest points to origin.
    Use max-heap of size K (negate distance to simulate max-heap).
    Keep the K smallest distances.
    """
    heap = []

    for x, y in points:
        dist = -(x * x + y * y)  # negate for max-heap behavior
        heapq.heappush(heap, (dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)

    return [[x, y] for _, x, y in heap]
