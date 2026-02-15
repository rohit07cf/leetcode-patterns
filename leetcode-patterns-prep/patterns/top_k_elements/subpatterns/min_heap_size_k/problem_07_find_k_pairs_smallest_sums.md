# Find K Pairs with Smallest Sums

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Min Heap of Size K
**Link:** https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given two sorted arrays `nums1` and `nums2`, and an integer `k`, return the `k` pairs `(u, v)` with the **smallest sums**, where `u` is from `nums1` and `v` is from `nums2`.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums1.length, nums2.length <= 10^5`, `1 <= k <= min(nums1.length * nums2.length, 10^4)`, arrays are sorted ascending.
- **Edge cases?** `k = 1` (just the pair of both first elements); one array has 1 element; `k` equals total pairs.
- **Expected output?** A list of k pairs `[u, v]`.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Generate all pairs, sort by sum, return the first k.
- **Time:** O(m * n * log(m * n))
- **Space:** O(m * n)

### 4. Optimized Approach

- 💡 **Core Insight:** Since both arrays are sorted, the smallest sum is `nums1[0] + nums2[0]`. The next smallest must include either `nums1[1] + nums2[0]` or `nums1[0] + nums2[1]`. Use a **min heap** to explore pairs in order of sum, starting from `(0, 0)` and expanding indices. Only push `(i, j+1)` from each popped `(i, j)`, and push `(i+1, 0)` only when `j == 0` to avoid duplicates.
- **Time:** O(k log k)
- **Space:** O(k)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| All pairs + sort | O(mn log(mn)) | O(mn) | Impractical for large arrays |
| Min Heap exploration | O(k log k) | O(k) | **Optimal — only explores k candidates** |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Seed the heap with `(nums1[0] + nums2[0], 0, 0)`.
- Pop the smallest sum pair. Add it to result.
- Push the "right neighbor" `(i, j+1)` — always valid to explore.
- Push the "down neighbor" `(i+1, j)` — but **only when `j == 0`** to prevent duplicate entries.
- Repeat k times.

```python
import heapq

def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    result = []
    # Min heap: (sum, index_in_nums1, index_in_nums2)
    heap = [(nums1[0] + nums2[0], 0, 0)]
    visited = {(0, 0)}

    while heap and len(result) < k:
        total, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])

        # Explore next pair in nums2 (move right)
        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            visited.add((i, j + 1))

        # Explore next pair in nums1 (move down)
        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            visited.add((i + 1, j))

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3`

1. Heap: `[(3, 0, 0)]`
2. Pop `(3, 0, 0)` → result: `[[1,2]]` → push `(5, 0, 1)` and `(9, 1, 0)`
3. Heap: `[(5, 0, 1), (9, 1, 0)]`
4. Pop `(5, 0, 1)` → result: `[[1,2],[1,4]]` → push `(7, 0, 2)` and `(11, 1, 1)`
5. Heap: `[(7, 0, 2), (9, 1, 0), (11, 1, 1)]`
6. Pop `(7, 0, 2)` → result: `[[1,2],[1,4],[1,6]]` ✓

### Edge Case Testing

- **Empty input:** Guarded by the early return check.
- **Single element:** `nums1 = [1], nums2 = [1], k = 1` → return `[[1, 1]]`.
- **Typical case:** Covered in dry run.
- **Extreme values:** Large k close to m * n — explores most of the grid, still correct.

### Complexity

- **Time:** O(k log k) — at most k pops and 2k pushes, each O(log k) since heap size is bounded by ~2k.
- **Space:** O(k) — heap and visited set each hold at most O(k) entries.

### Optimization Discussion

- **Alternative without visited set:** Seed the heap with `(nums1[i] + nums2[0], i, 0)` for all i. Then only push `(i, j+1)`. This avoids the visited set but starts with min(m, k) entries.
- The visited-set approach is more general and works for any grid exploration.

### Follow-up Variations

- **Kth Smallest Sum** — instead of all k pairs, return only the kth pair's sum.
- **K pairs with largest sums** — start from `(m-1, n-1)` and explore in reverse.
- **More than 2 arrays** — generalize with a heap merging approach (like k-way merge).

### ⚠️ Common Traps

- **Duplicate pairs in the heap.** Without a visited set or careful expansion strategy, `(i, j)` can be pushed multiple times.
- **Generating all m * n pairs.** The whole point is to avoid this — only explore O(k) candidates.
- **Assuming the arrays contain unique elements.** Duplicate values are fine; we track by index, not value.
