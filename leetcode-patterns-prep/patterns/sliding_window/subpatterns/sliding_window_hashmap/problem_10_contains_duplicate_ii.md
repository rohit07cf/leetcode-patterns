# Contains Duplicate II

**Difficulty:** Easy
**Pattern:** Sliding Window
**Subpattern:** Sliding Window + Hashmap
**Link:** https://leetcode.com/problems/contains-duplicate-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an integer array `nums` and an integer `k`, return `True` if there are **two distinct indices** `i` and `j` such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

### 2. Clarification Questions
- **Input constraints?** `1 <= nums.length <= 10^5`, `-10^9 <= nums[i] <= 10^9`, `0 <= k <= 10^5`.
- **Edge cases?** `k = 0` → only true if same index (impossible for distinct indices, so `False`). Array of all unique elements → `False`.
- **Expected output?** Boolean — `True` or `False`.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach
- **Idea:** For each pair `(i, j)` where `j > i` and `j - i <= k`, check if `nums[i] == nums[j]`.
- **Time:** O(n * k)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** Maintain a hashmap storing each value's **most recent index**. For each element, check if it was seen before and the distance is <= k. Alternatively, use a **sliding window set** of size k — if a duplicate enters the window, return `True`.
- **Time:** O(n)
- **Space:** O(min(n, k))

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n * k) | O(1) | Check all nearby pairs |
| Hashmap (last index) | O(n) | O(n) | Store all indices |
| Sliding Window Set | O(n) | O(k) | Bounded space |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

**Approach 1: Hashmap storing last seen index (simpler)**

```python
def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    last_seen = {}  # value -> most recent index

    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i  # update to most recent index

    return False
```

**Approach 2: Sliding window with set (bounded space)**

```python
def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    window = set()

    for i, num in enumerate(nums):
        # Remove element leaving the window
        if i > k:
            window.remove(nums[i - k - 1])

        # Check for duplicate in current window
        if num in window:
            return True

        window.add(num)

    return False
```

---

## PHASE 3 — AFTER CODING

### Dry Run (Hashmap approach)
**Input:** `nums = [1, 2, 3, 1]`, `k = 3`

| i | num | last_seen       | check               | result |
|---|-----|-----------------|----------------------|--------|
| 0 | 1   | {1:0}           | 1 not in map         |        |
| 1 | 2   | {1:0, 2:1}      | 2 not in map         |        |
| 2 | 3   | {1:0, 2:1, 3:2} | 3 not in map         |        |
| 3 | 1   | {1:0,...}        | 1 in map, 3-0=3 <= 3 | **True** |

**Output:** `True`

### Dry Run (Sliding window set approach)
**Input:** `nums = [1, 0, 1, 1]`, `k = 1`

| i | num | remove?      | window before check | dup? |
|---|-----|-------------|---------------------|------|
| 0 | 1   | No (i<=k)    | {}                  | No → {1} |
| 1 | 0   | No (i<=k)    | {1}                 | No → {1,0} |
| 2 | 1   | Yes: nums[0]=1 | {0}                | No → {0,1} |
| 3 | 1   | Yes: nums[1]=0 | {1}                | **Yes** → return True |

**Output:** `True`

### Edge Case Testing
- **Empty input:** Not possible per constraints.
- **Single element:** `[1]`, k=0 → `False` (no pair possible).
- **Typical case:** `[1,2,3,1]`, k=3 → `True`.
- **Extreme values:** `k = 0` → always `False` (distinct indices can't have distance 0). All unique → `False`. `[1,1]`, k=1 → `True`.

### Complexity
- **Time:** O(n) — single pass.
- **Space:** O(n) for hashmap approach; O(min(n, k)) for sliding window set.

### Optimization Discussion
- The hashmap approach is simpler and typically preferred in interviews.
- The sliding window set approach uses bounded O(k) space, which matters for very large arrays with small k.
- Both are O(n) time.

### Follow-up Variations
- **Contains Duplicate** (LeetCode 217) — simpler: just check if any duplicate exists.
- **Contains Duplicate III** (LeetCode 220) — harder: values within range `t` AND indices within range `k` (use bucket sort / sorted container).

### Common Traps
- Forgetting to check `k = 0` — with distinct indices, `abs(i - j) <= 0` means `i == j`, which contradicts "distinct indices." So `k = 0` should return `False`.
- In the set approach: removing `nums[i - k - 1]` not `nums[i - k]` — the window includes indices `[i-k, i]`, so the element leaving is at `i - k - 1`.
- Storing the first index instead of the **most recent** index in the hashmap — you want the closest prior occurrence.
