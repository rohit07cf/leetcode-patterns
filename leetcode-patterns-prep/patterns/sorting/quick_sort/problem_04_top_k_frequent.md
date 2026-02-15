# Top K Frequent Elements

**Difficulty:** Medium
**Pattern:** Sorting
**Subpattern:** Quick Sort / Partition
**Link:** https://leetcode.com/problems/top-k-frequent-elements/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. The answer may be returned in **any order** and is guaranteed to be unique.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 10^5`, `1 <= k <= number of unique elements`
- **Edge cases?** k equals number of unique elements, all elements same, single element
- **Expected output?** List of k integers (any order)
- **Can input be modified?** Yes

### 3. Brute Force Approach

- **Idea:** Count frequencies with a hashmap, sort by frequency descending, take the first k.
- **Time:** O(n log n)
- **Space:** O(n)

### 4. Optimized Approach

- **💡 Core Insight:** Use **quickselect on frequencies**. After counting frequencies, apply quickselect to find the kth most frequent boundary — this partitions elements into "top k frequent" vs. the rest in **O(n) average** without fully sorting. Alternatively, **bucket sort** by frequency achieves O(n) guaranteed.

- **Time:** O(n) average (quickselect) or O(n) guaranteed (bucket sort)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort by frequency | O(n log n) | O(n) | Simple |
| Min-heap of size k | O(n log k) | O(n) | Good for streaming |
| **Quickselect** | **O(n) avg** | **O(n)** | Optimal average |
| Bucket sort | O(n) | O(n) | Optimal guaranteed |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Count frequencies using a hashmap
- Build a list of `(frequency, value)` pairs for unique elements
- Apply quickselect to partially sort so the top-k frequent are on one side
- Return those k elements

```python
import random
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        unique = list(freq.keys())

        # Quickselect: partition so top-k frequent are at indices [n-k:]
        n = len(unique)
        target = n - k  # We want elements at indices [target:] to be the top-k

        lo, hi = 0, n - 1
        while lo <= hi:
            pivot_idx = random.randint(lo, hi)
            pivot_freq = freq[unique[pivot_idx]]

            # 3-way partition by frequency
            lt, i, gt = lo, lo, hi
            while i <= gt:
                if freq[unique[i]] < pivot_freq:
                    unique[lt], unique[i] = unique[i], unique[lt]
                    lt += 1
                    i += 1
                elif freq[unique[i]] > pivot_freq:
                    unique[i], unique[gt] = unique[gt], unique[i]
                    gt -= 1
                else:
                    i += 1

            # Check if target falls in the "equal" zone
            if lt <= target <= gt:
                break  # Top-k are at unique[target:]
            elif target < lt:
                hi = lt - 1
            else:
                lo = gt + 1

        return unique[target:]
```

**Alternative: Bucket Sort (O(n) guaranteed)**

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)

        # Bucket index = frequency, max possible frequency = len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        # Collect from highest frequency bucket down
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `nums = [1,1,1,2,2,3]`, `k = 2`

**Quickselect approach:**
1. `freq = {1:3, 2:2, 3:1}`, `unique = [1, 2, 3]`, `target = 3 - 2 = 1`
2. Suppose pivot is `2` (freq=2). Partition by freq: `[3]` (freq 1) `[2]` (freq 2) `[1]` (freq 3)
3. lt=1, gt=1, target=1 -> target in [lt, gt] -> break
4. Return `unique[1:] = [2, 1]`

### Edge Case Testing

- **Empty input:** Constraint says `n >= 1`, not applicable
- **Single element:** `[5]`, k=1 -> `[5]`
- **Typical case:** `[1,1,1,2,2,3]`, k=2 -> `[1, 2]`
- **Extreme values:** All same `[7,7,7]`, k=1 -> `[7]`

### Complexity

- **Time:** O(n) average — O(n) for counting + O(m) quickselect where m = unique elements <= n
- **Space:** O(n) — hashmap storing frequencies

### Optimization Discussion

- **Bucket sort** is the cleanest O(n) guaranteed solution for this problem
- **Quickselect** is more general — works when you can't bucket by frequency
- **Heap** is preferred in streaming scenarios where you see elements one at a time

### Follow-up Variations

- Top K frequent words (same idea, but break ties alphabetically)
- Top K frequent elements in a data stream (min-heap of size k)
- Kth most frequent element (return just one element, not a list)

### Common Traps

- **Sorting unique values instead of frequencies** — you partition based on frequency, not value
- **Off-by-one on target index** — if you want top-k at the end of the array, target = `n - k`
- **Forgetting quickselect gives top-k in any order** — the problem allows any order, so this is fine
- **Bucket sort: using wrong bucket size** — max frequency is `len(nums)`, not `max(nums)`
