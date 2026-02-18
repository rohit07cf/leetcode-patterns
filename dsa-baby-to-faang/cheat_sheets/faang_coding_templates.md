# FAANG Coding Templates

> Every template you need. Clean Python. Copy, adapt, conquer.

---

## 1. Binary Search — Exact Match

```python
# Use when: sorted array, find exact target. O(log n)
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

## 2. Binary Search — Lower Bound (First >= target)

```python
# Use when: find insertion point or first element >= target. O(log n)
def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

## 3. Binary Search — Upper Bound (First > target)

```python
# Use when: find first element strictly greater than target. O(log n)
def upper_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

---

## 4. Two Pointers — Opposite Direction

```python
# Use when: sorted array, pair sum, palindrome check. O(n)
def two_pointers_opposite(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []
```

## 5. Two Pointers — Same Direction (Fast & Slow)

```python
# Use when: remove duplicates, partition, linked list cycle. O(n)
def remove_duplicates(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

---

## 6. Sliding Window — Fixed Size

```python
# Use when: max sum of subarray of size k. O(n)
def fixed_window(nums, k):
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]    # slide: add right, remove left
        best = max(best, window_sum)
    return best
```

## 7. Sliding Window — Variable Size

```python
# Use when: smallest subarray with sum >= target, longest substring without repeats. O(n)
def variable_window(s):
    left = 0
    window = {}                               # track window contents
    best = 0
    for right in range(len(s)):
        window[s[right]] = window.get(s[right], 0) + 1   # expand
        while not is_valid(window):                        # shrink if invalid
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        best = max(best, right - left + 1)                # update answer
    return best
```

---

## 8. BFS — Graph

```python
# Use when: shortest path (unweighted), level-order traversal. O(V + E)
from collections import deque

def bfs_graph(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
```

## 9. BFS — Grid

```python
# Use when: shortest path in grid, nearest object. O(rows * cols)
from collections import deque

def bfs_grid(grid, sr, sc):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(sr, sc, 0)])
    visited = {(sr, sc)}
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        nr, nc = sr + dr, sc + dc
    # (full version in grid loop below)
    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] != 0:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
```

## 10. BFS — Tree (Level Order)

```python
# Use when: level-order traversal, right side view, zigzag. O(n)
from collections import deque

def bfs_tree(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

---

## 11. DFS — Graph (Recursive)

```python
# Use when: connected components, cycle detection, all paths. O(V + E)
def dfs_graph(graph, node, visited):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs_graph(graph, nei, visited)
```

## 12. DFS — Grid

```python
# Use when: flood fill, island count, connected region. O(rows * cols)
def dfs_grid(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or grid[r][c] == 0:
        return
    visited.add((r, c))
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        dfs_grid(grid, r + dr, c + dc, visited)
```

## 13. Tree DFS — Preorder, Inorder, Postorder

```python
# Preorder: process node, then children. Use when: serialize, copy tree.
def preorder(node):
    if not node: return
    process(node.val)
    preorder(node.left)
    preorder(node.right)

# Inorder: left, process, right. Use when: BST sorted order.
def inorder(node):
    if not node: return
    inorder(node.left)
    process(node.val)
    inorder(node.right)

# Postorder: children first, then node. Use when: delete, calculate height.
def postorder(node):
    if not node: return
    postorder(node.left)
    postorder(node.right)
    process(node.val)
```

---

## 14. Topological Sort (Kahn's BFS)

```python
# Use when: task ordering, course schedule, dependency resolution. O(V + E)
from collections import deque, defaultdict

def topo_sort(n, edges):
    graph = defaultdict(list)
    in_deg = [0] * n
    for u, v in edges:
        graph[u].append(v)
        in_deg[v] += 1
    queue = deque(i for i in range(n) if in_deg[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph[node]:
            in_deg[nei] -= 1
            if in_deg[nei] == 0:
                queue.append(nei)
    return order if len(order) == n else []
```

## 15. Union Find

```python
# Use when: connected components, redundant edges, accounts merge. O(alpha(n))
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        return True
```

## 16. Dijkstra's Algorithm

```python
# Use when: shortest path with non-negative weights. O((V+E) log V)
import heapq

def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```

---

## 17. Monotonic Stack

```python
# Use when: next greater/smaller element, histogram area, stock span. O(n)
def next_greater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []                              # stores indices
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
```

---

## 18. 1D DP

```python
# Use when: climbing stairs, house robber, coin change. O(n)
def dp_1d(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]                         # base case
    for i in range(1, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])  # recurrence
    return dp[-1]
```

## 19. 2D DP

```python
# Use when: two strings (LCS, edit distance), grid paths. O(m * n)
def dp_2d(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

## 20. 0/1 Knapsack

```python
# Use when: subset with weight limit, partition equal subset sum. O(n * W)
def knapsack(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):     # backwards for 0/1
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]
```

---

## 21. Linked List Reversal

```python
# Use when: reverse linked list, reverse portion, palindrome list. O(n)
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

---

## Quick Reference Summary

| # | Template | Time | When to Use |
|---|----------|------|-------------|
| 1 | Binary Search (exact) | O(log n) | Find target in sorted array |
| 2 | Binary Search (lower bound) | O(log n) | First element >= target |
| 3 | Binary Search (upper bound) | O(log n) | First element > target |
| 4 | Two Pointers (opposite) | O(n) | Pair sum, palindrome |
| 5 | Two Pointers (same dir) | O(n) | Remove duplicates, partition |
| 6 | Sliding Window (fixed) | O(n) | Max/min of window size k |
| 7 | Sliding Window (variable) | O(n) | Longest/shortest valid window |
| 8 | BFS (graph) | O(V+E) | Shortest unweighted path |
| 9 | BFS (grid) | O(r*c) | Shortest path in matrix |
| 10 | BFS (tree) | O(n) | Level-order traversal |
| 11 | DFS (graph) | O(V+E) | Components, cycles, paths |
| 12 | DFS (grid) | O(r*c) | Islands, flood fill |
| 13 | Tree DFS | O(n) | Traversal, height, paths |
| 14 | Topological Sort | O(V+E) | Dependency ordering |
| 15 | Union Find | O(a(n)) | Connected components |
| 16 | Dijkstra | O((V+E)logV) | Weighted shortest path |
| 17 | Monotonic Stack | O(n) | Next greater/smaller |
| 18 | 1D DP | O(n) | Sequence optimization |
| 19 | 2D DP | O(m*n) | Two-sequence / grid problems |
| 20 | 0/1 Knapsack | O(n*W) | Subset selection with limit |
| 21 | Linked List Reversal | O(n) | Reverse list/portion |

**These 21 templates cover 90% of FAANG interview problems. Know them cold.**
