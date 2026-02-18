"""
Problem: Network Delay Time (LeetCode #743)
Pattern: Dijkstra's Algorithm
Difficulty: Medium

Baby Explanation:
    We have a network of n nodes and weighted directed edges. We send a signal
    from a starting node and want to know how long it takes to reach ALL nodes.
    We use Dijkstra's algorithm to find the shortest path to every node, then
    return the maximum of those times. If any node is unreachable, return -1.

Example:
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2
    Explanation: From node 2: reach 1 in 1, reach 3 in 1, reach 4 in 2. Max = 2.

Approach:
    1. Build an adjacency list from the edge list.
    2. Use a min-heap (priority queue) starting from node k with distance 0.
    3. Pop the closest unvisited node, record its distance.
    4. Push all its neighbors with updated distances into the heap.
    5. If all nodes are visited, return the max distance. Otherwise return -1.

Time Complexity: O(E log V) - each edge processed once, heap operations are log V
Space Complexity: O(V + E) - adjacency list and heap
"""

import heapq


class Solution:
    def networkDelayTime(self, times, n, k):
        # Step 1: Build adjacency list {source: [(cost, dest), ...]}
        graph = [[] for _ in range(n + 1)]  # 1-indexed nodes
        for src, dst, cost in times:
            graph[src].append((cost, dst))

        # Step 2: Min-heap with (distance, node), start from k
        heap = [(0, k)]
        dist = {}  # node -> shortest distance from k

        # Step 3: Process nodes in order of shortest distance
        while heap:
            d, node = heapq.heappop(heap)

            # Skip if we already found a shorter path to this node
            if node in dist:
                continue

            # Record the shortest distance to this node
            dist[node] = d

            # Step 4: Push neighbors with updated distances
            for cost, neighbor in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (d + cost, neighbor))

        # Step 5: Check if all nodes are reachable
        if len(dist) == n:
            return max(dist.values())
        return -1


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: All nodes reachable
    times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    assert sol.networkDelayTime(times1, 4, 2) == 2

    # Test 2: Not all nodes reachable
    assert sol.networkDelayTime([[1, 2, 1]], 2, 2) == -1

    # Test 3: Single node
    assert sol.networkDelayTime([], 1, 1) == 0

    # Test 4: Two paths, pick shorter
    times4 = [[1, 2, 5], [1, 3, 1], [3, 2, 1]]
    assert sol.networkDelayTime(times4, 3, 1) == 2  # 1->3->2 costs 2, not 1->2 costs 5

    print("All tests passed!")
