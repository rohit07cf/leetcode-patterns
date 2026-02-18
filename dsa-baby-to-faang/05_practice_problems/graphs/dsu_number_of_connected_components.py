"""
Problem: Number of Connected Components in Undirected Graph (LeetCode #323)
Pattern: Union Find / DSU (Disjoint Set Union)
Difficulty: Medium

Baby Explanation:
    We have n nodes and a list of edges. We need to count how many separate
    groups (connected components) exist. Think of it like counting friend groups:
    if A knows B and B knows C, they're all in one group. We use Union-Find to
    merge groups and count how many distinct groups remain.

Example:
    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2
    Explanation: Nodes {0,1,2} form one group, nodes {3,4} form another.

Approach:
    1. Initialize each node as its own parent (each node is its own group).
    2. For each edge, union the two nodes (merge their groups).
    3. Use path compression in find() to keep the tree flat and fast.
    4. Use union by rank to keep the tree balanced.
    5. Count how many distinct roots exist - that's our answer.

Time Complexity: O(n + E * alpha(n)) - nearly O(n + E) with path compression
Space Complexity: O(n) - parent and rank arrays
"""


class Solution:
    def countComponents(self, n, edges):
        # Step 1: Each node starts as its own parent
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            # Step 3: Path compression - point directly to root
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            # Step 4: Union by rank - attach smaller tree under bigger
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return  # Already in the same group

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        # Step 2: Union all edges
        for a, b in edges:
            union(a, b)

        # Step 5: Count distinct roots
        return len(set(find(i) for i in range(n)))


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Two components
    assert sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2

    # Test 2: All connected (one component)
    assert sol.countComponents(4, [[0, 1], [1, 2], [2, 3]]) == 1

    # Test 3: No edges (every node is its own component)
    assert sol.countComponents(4, []) == 4

    # Test 4: Edge case - single node
    assert sol.countComponents(1, []) == 1

    # Test 5: Triangle
    assert sol.countComponents(3, [[0, 1], [1, 2], [0, 2]]) == 1

    print("All tests passed!")
