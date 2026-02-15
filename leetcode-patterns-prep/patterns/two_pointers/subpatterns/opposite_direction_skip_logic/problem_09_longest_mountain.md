# Longest Mountain in Array

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction — Skip Logic
**Link:** https://leetcode.com/problems/longest-mountain-in-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `arr`, return the length of the longest subarray that forms a **mountain**. A mountain has length >= 3, strictly increases to a peak, then strictly decreases. Return 0 if no mountain exists.

### 2. Clarification Questions

- **Input constraints?** `1 <= arr.length <= 10^4`, `0 <= arr[i] <= 10^4`
- **Edge cases?** All equal, strictly increasing only, strictly decreasing only, length < 3, plateau at the peak
- **Expected output?** Integer — length of the longest mountain, or 0 if none exists
- **Can input be modified?** Not necessary

### 3. Brute Force Approach

- **Idea:** For each possible peak (index with `arr[i-1] < arr[i] > arr[i+1]`), expand left and right to measure the mountain.
- **Time:** O(n^2) in the worst case (overlapping expansions)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** Scan left-to-right. At each position, try to build a mountain: first climb up (skip non-increasing), then descend (skip non-decreasing). The skip logic efficiently jumps over flat/wrong-direction elements. If both up and down phases have length > 0, it's a valid mountain. Start the next search from where the current mountain's descent ended — no need to re-scan.

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Expand from each peak |
| Optimized | O(n) | O(1) | Single pass — climb + descend + skip |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use a base pointer that walks through the array.
- From each base, try to ascend: move `end` forward while strictly increasing.
- If we climbed (ascent length > 0) and there's a descent available, continue moving `end` while strictly decreasing.
- If both phases happened, we have a valid mountain — update max length.
- **Key skip logic:** set `base = end` to skip the entire processed segment; if no mountain started, just advance `base` by 1 to skip the current flat/decreasing element.

```python
def longestMountain(arr: list[int]) -> int:
    n = len(arr)
    if n < 3:
        return 0

    longest = 0
    base = 0

    while base < n - 2:
        end = base

        # Phase 1: Ascend — skip while strictly increasing
        if arr[end] < arr[end + 1]:
            while end < n - 1 and arr[end] < arr[end + 1]:
                end += 1

            # Phase 2: Descend — skip while strictly decreasing
            if end < n - 1 and arr[end] > arr[end + 1]:
                while end < n - 1 and arr[end] > arr[end + 1]:
                    end += 1

                # Valid mountain found
                longest = max(longest, end - base + 1)

        # Skip to end of processed segment (or advance by 1 if no ascent)
        base = max(end, base + 1)

    return longest
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `arr = [2, 1, 4, 7, 3, 2, 5]`

| base | Phase | end progression | Mountain? | Length | longest |
|------|-------|-----------------|-----------|--------|---------|
| 0 | arr[0]=2 > arr[1]=1, no ascent | end=0 | no | — | 0 |
| 1 | ascend: 1→4→7 (end=3), descend: 7→3→2 (end=5) | 1→5 | **yes** | 5 | 5 |
| 5 | arr[5]=2 < arr[6]=5, ascend only (end=6), no descent | no | — | 5 |
| 6 | base >= n-2, stop | — | — | — | 5 |

**Output:** `5` (subarray `[1, 4, 7, 3, 2]`) ✓

### Edge Case Testing

- **Empty input:** Constraints guarantee `n >= 1`.
- **Single element:** `n < 3` → returns 0.
- **Typical case:** Works as shown.
- **Extreme values:** All equal `[3,3,3,3]` → no ascent ever → returns 0. Strictly increasing → no descent → returns 0. Strictly decreasing → no ascent → returns 0.

### Complexity

- **Time:** O(n) — each element is visited at most twice (once by `base`, once by `end`)
- **Space:** O(1) — only pointer and counter variables

### Optimization Discussion

An alternative approach uses two auxiliary arrays: `up[i]` = length of increasing run ending at `i`, `down[i]` = length of decreasing run starting at `i`. A mountain at peak `i` has length `up[i] + down[i] + 1`. This uses O(n) space but is easier to understand.

### Follow-up Variations

- **Valid Mountain Array (LC 941):** Check if the entire array is a mountain — simpler version.
- **Peak Index in a Mountain Array (LC 852):** Find the peak index — binary search.
- **Minimum Number of Removals to Make Mountain Array (LC 1671):** Hard — DP + LIS.

### ⚠️ Common Traps

- **Treating plateaus as mountains** — `[1, 2, 2, 1]` is NOT a mountain; the peak must be strict.
- **Counting ascent-only or descent-only as mountains** — a mountain requires BOTH an ascending and descending phase.
- **Not advancing `base` on failure** — if no ascent starts, you must advance `base` by at least 1 to avoid an infinite loop.
- **Double-counting elements** — setting `base = end` correctly starts the next search at the foot of the previous descent, which could be the start of a new ascent.
