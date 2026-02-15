# Find Smallest Letter Greater Than Target

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Boundary Binary Search
**Link:** https://leetcode.com/problems/find-smallest-letter-greater-than-target/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted array of lowercase letters that wraps around, find the **smallest letter** in the array that is **strictly greater** than the given target. If no such letter exists (target >= last letter), wrap around and return the first letter.

### 2. Clarification Questions

- **Input constraints?** `2 <= letters.length <= 10^4`. Letters are sorted in non-decreasing order. At least two different characters.
- **Edge cases?** Target is larger than all letters (wrap around). Target is smaller than all letters. Duplicates in letters.
- **Expected output?** A single character — the smallest letter strictly greater than target.
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** Linear scan through the array and return the first letter greater than target. If none found, return `letters[0]`.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** This is a **lower bound search for the first element > target**. Binary search for the leftmost position where `letters[mid] > target`. The wrap-around is handled by returning `letters[0]` if the boundary is at the end.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Simple linear scan |
| Optimized | O(log n) | O(1) | Boundary binary search |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search for the **leftmost index** where `letters[mid] > target`.
- If no such index exists (all letters <= target), wrap around with modulo.

```python
def nextGreatestLetter(letters, target):
    lo, hi = 0, len(letters) - 1
    result = 0  # default wrap-around to first letter

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if letters[mid] > target:
            result = mid  # candidate found, keep searching left
            hi = mid - 1
        else:
            lo = mid + 1  # letters[mid] <= target, search right

    return letters[result]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `letters = ["c", "f", "j"]`, `target = "a"`

- `lo=0, hi=2` -> `mid=1`, `"f" > "a"` -> `result=1`, `hi=0`
- `lo=0, hi=0` -> `mid=0`, `"c" > "a"` -> `result=0`, `hi=-1`
- Exit. Return `letters[0]` = `"c"`

### Edge Case Testing

- **Empty input:** Not possible per constraints (length >= 2).
- **Single element:** Not possible per constraints.
- **Target > all letters:** `letters=["a","b"], target="z"` -> no `letters[mid] > target` found, `result` stays `0`. Returns `"a"` (wrap-around).
- **Target < all letters:** Returns `letters[0]`, the smallest letter.
- **Duplicates:** `letters=["a","a","b","b"], target="a"` -> finds first `"b"`.

### Complexity

- **Time:** O(log n) — standard binary search.
- **Space:** O(1) — constant extra space.

### Optimization Discussion

Already optimal. An alternative approach uses `bisect_right` from Python's `bisect` module with modulo for wrap-around: `letters[bisect_right(letters, target) % len(letters)]`.

### Follow-up Variations

- Find the **largest letter smaller than** target (reverse boundary).
- What if the array is **circularly sorted** (rotated)?
- Extend to Unicode characters or integers.

### Common Traps

- **Forgetting wrap-around** — when target >= all elements, you must return `letters[0]`, not go out of bounds.
- **Using `>=` instead of `>`** — the problem asks for **strictly greater**, so `letters[mid] == target` should move `lo = mid + 1`, not record as candidate.
- **Confusing with lower bound** — this is an **upper bound** search (first element strictly greater than target).
