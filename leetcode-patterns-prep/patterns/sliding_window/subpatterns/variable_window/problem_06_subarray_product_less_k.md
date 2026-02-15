# Subarray Product Less Than K

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Variable Window
**Link:** https://leetcode.com/problems/subarray-product-less-than-k/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an array of **positive integers** `nums` and an integer `k`, return the **number of contiguous subarrays** where the product of all elements is **strictly less than** `k`.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 3 * 10^4`, `1 <= nums[i] <= 1000`, `0 <= k <= 10^6`.
- Edge cases? `k <= 1` — no subarray of positive integers has product < 1, return 0.
- Expected output? An integer — the count of valid subarrays.
- Can input be modified? Yes, but we don't need to.

### 3. Brute Force Approach
- **Idea:** For every pair `(i, j)`, compute the product of `nums[i..j]`. Count subarrays with product < k.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** Since all values are **positive**, the product is **monotonically increasing** as we expand right. Use a sliding window: expand right to include new elements, shrink left when the product >= k. For each `right`, the number of new valid subarrays **ending at right** is `right - left + 1`.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Check all subarrays |
| Sliding Window | O(n) | O(1) | Count subarrays ending at each right |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Maintain a running `product` for the window.
- Expand `right`, multiply into product.
- Shrink `left` while `product >= k`.
- **Counting trick:** Each position `right` contributes `right - left + 1` new subarrays (those ending at `right` and starting at any index from `left` to `right`).

```python
def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
    if k <= 1:
        return 0  # product of positive ints is always >= 1

    left = 0
    product = 1
    count = 0

    for right in range(len(nums)):
        product *= nums[right]

        # Shrink until product < k
        while product >= k:
            product //= nums[left]
            left += 1

        # All subarrays ending at right with start in [left, right] are valid
        count += right - left + 1

    return count
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `nums = [10, 5, 2, 6]`, `k = 100`

| right | nums[r] | product | left | valid subarrays ending at right | count |
|-------|---------|---------|------|---------------------------------|-------|
| 0 | 10 | 10 | 0 | [10] → 1 | 1 |
| 1 | 5 | 50 | 0 | [10,5], [5] → 2 | 3 |
| 2 | 2 | 100→50 | 1 | [5,2], [2] → 2 | 5 |
| 3 | 6 | 300→60 | 1 | [5,2,6], [2,6], [6] → 3 | 8 |

- right=2: product=100 >= 100, shrink: product=100/10=10... wait, let me recalculate.
  - product = 50 * 2 = 100, >= 100 → divide by nums[0]=10 → product=10, left=1. Subarrays: [5,2],[2] → 2.
- right=3: product=10*6=60 < 100. Subarrays: [5,2,6],[2,6],[6] → 3.

Output: **8**

### Edge Case Testing
- **Empty input:** Constraint says `len >= 1`, not applicable.
- **Single element:** `nums = [1], k = 2` — product=1 < 2, count=1.
- **Typical case:** `nums = [10,5,2,6], k = 100` — returns 8.
- **Extreme values:** `k = 0` or `k = 1` — early return 0 (no positive product is < 1).

### Complexity
- **Time:** O(n) — each element is added and removed from the window at most once.
- **Space:** O(1) — only running product, pointers, and counter.

### Optimization Discussion
The key insight is the **counting formula**: `right - left + 1` counts all subarrays ending at the current `right` pointer. This avoids double-counting and is the standard technique for "count subarrays" sliding window problems.

For very large products, consider using **log-sum** instead of direct multiplication to avoid overflow (not needed in Python, but relevant in C++/Java).

### Follow-up Variations
- **Minimum Size Subarray Sum** (LC 209) — find min window with sum >= target (opposite direction).
- **Maximum Product Subarray** (LC 152) — includes negatives, requires different approach (DP, not sliding window).
- **Count subarrays with sum less than K** — similar template but with addition.

### Common Traps
- Forgetting `k <= 1` edge case — dividing in the while loop when `left > right` causes issues.
- Using `//` (integer division) vs `/` — use `//` since all values are integers, but be careful: `product //= nums[left]` works cleanly because `nums[left]` always divides `product` evenly.
- **Counting logic:** The `right - left + 1` formula is the core — missing this leads to wrong answers or O(n^2) enumeration.
