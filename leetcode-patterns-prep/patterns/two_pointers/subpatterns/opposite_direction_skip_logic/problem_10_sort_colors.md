# Sort Colors

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction — Skip Logic
**Link:** https://leetcode.com/problems/sort-colors/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array `nums` with `n` objects colored red (0), white (1), or blue (2), sort them **in-place** so that objects of the same color are adjacent, in the order red, white, blue. Do it in one pass without using a library sort.

### 2. Clarification Questions

- **Input constraints?** `1 <= n <= 300`, `nums[i]` is 0, 1, or 2
- **Edge cases?** All same color, only two colors present, single element, already sorted
- **Expected output?** Modify `nums` in-place — no return value
- **Can input be modified?** Yes — required

### 3. Brute Force Approach

- **Idea:** Count occurrences of 0, 1, 2, then overwrite the array. (Two-pass counting sort.)
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** **Dutch National Flag Algorithm** — three pointers. `lo` marks the boundary for 0s (left region), `hi` marks the boundary for 2s (right region), and `mid` scans through. The skip logic: when `nums[mid] == 1`, it's already in the right zone — **skip** (just advance `mid`). When it's 0, swap to the left region. When it's 2, swap to the right region (but don't advance `mid` since the swapped-in value hasn't been inspected yet).

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Counting Sort | O(n) | O(1) | Two passes — count then fill |
| Dutch Flag (3-pointer) | O(n) | O(1) | Single pass — one scan with swaps |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **`lo`** = next position to place a 0 (grows from left)
- **`hi`** = next position to place a 2 (shrinks from right)
- **`mid`** = current element being inspected
- If `nums[mid] == 0`: swap with `lo`, advance both `lo` and `mid` (swapped value from `lo` is always 0 or 1, already inspected).
- If `nums[mid] == 2`: swap with `hi`, decrement `hi`, do **NOT** advance `mid` (swapped value is unknown).
- If `nums[mid] == 1`: skip — just advance `mid`.

```python
def sortColors(nums: list[int]) -> None:
    lo, mid, hi = 0, 0, len(nums) - 1

    while mid <= hi:
        if nums[mid] == 0:
            # Swap 0 to the left region
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1  # Safe to advance — lo region only has 0s and 1s
        elif nums[mid] == 2:
            # Swap 2 to the right region
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1
            # Do NOT advance mid — swapped value needs inspection
        else:
            # nums[mid] == 1, skip — already in the correct zone
            mid += 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [2, 0, 2, 1, 1, 0]`

| Step | lo | mid | hi | nums | action |
|------|----|-----|----|------|--------|
| 1 | 0 | 0 | 5 | [2,0,2,1,1,0] | nums[0]=2 → swap with hi → [0,0,2,1,1,2] | hi=4 |
| 2 | 0 | 0 | 4 | [0,0,2,1,1,2] | nums[0]=0 → swap with lo → [0,0,2,1,1,2] | lo=1, mid=1 |
| 3 | 1 | 1 | 4 | [0,0,2,1,1,2] | nums[1]=0 → swap with lo → [0,0,2,1,1,2] | lo=2, mid=2 |
| 4 | 2 | 2 | 4 | [0,0,2,1,1,2] | nums[2]=2 → swap with hi → [0,0,1,1,2,2] | hi=3 |
| 5 | 2 | 2 | 3 | [0,0,1,1,2,2] | nums[2]=1 → skip | mid=3 |
| 6 | 2 | 3 | 3 | [0,0,1,1,2,2] | nums[3]=1 → skip | mid=4 |
| 7 | mid=4 > hi=3 → stop |

**Output:** `[0, 0, 1, 1, 2, 2]` ✓

### Edge Case Testing

- **Empty input:** Constraints guarantee `n >= 1`.
- **Single element:** `lo=0, mid=0, hi=0` → one iteration → unchanged. Correct.
- **Typical case:** Works as shown.
- **Extreme values:** All zeros → every step swaps with lo, both advance → stays `[0,0,...,0]`. All twos → every step swaps with hi, hi shrinks → stays `[2,2,...,2]`.

### Complexity

- **Time:** O(n) — each element processed at most twice (once by `mid`, possibly once more if swapped from `hi`)
- **Space:** O(1) — three pointer variables only

### Optimization Discussion

The counting sort (two-pass) approach is simpler to implement and debug. The Dutch Flag one-pass approach is the classic follow-up interviewers expect. Both are O(n) time, O(1) space — the difference is one pass vs. two.

### Follow-up Variations

- **Sort Colors with K colors:** Generalize to K distinct values — can use recursive partitioning O(n log K) or counting sort O(n + K).
- **Move Zeroes (LC 283):** Partition into zeros and non-zeros — simplified two-pointer version.
- **Wiggle Sort (LC 280):** Different ordering constraint after partitioning.
- **Partition Array (Quick Select):** The Dutch Flag algorithm is the partitioning step in 3-way quicksort.

### ⚠️ Common Traps

- **Advancing `mid` after swapping with `hi`** — the value swapped from `hi` is unexamined; you must inspect it before moving on. This is the #1 bug.
- **Using `mid < hi` instead of `mid <= hi`** — must use `<=` because the element at `hi` hasn't been classified yet.
- **Thinking `lo` swap also needs re-inspection** — it doesn't. The value swapped from `lo` is always 0 or 1 (already processed region), so advancing `mid` is safe.
- **Confusing this with a standard partition** — this is a 3-way partition, not 2-way. Three regions, not two.
