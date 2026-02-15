# Largest Number

**Difficulty:** Medium
**Pattern:** Sorting
**Subpattern:** Quick Sort / Partition
**Link:** https://leetcode.com/problems/largest-number/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a list of non-negative integers `nums`, arrange them such that they form the **largest number** and return it as a string.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 100`, `0 <= nums[i] <= 10^9`
- **Edge cases?** All zeroes → "0", single element, numbers with same prefix (e.g., 3 vs 30)
- **Expected output?** String representation of the largest number
- **Can input be modified?** Yes

### 3. Brute Force Approach

- **Idea:** Try all permutations and pick the one that forms the largest number.
- **Time:** O(n! × n) — factorial permutations
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Define a **custom comparator**: for two numbers `a` and `b`, compare `str(a) + str(b)` vs `str(b) + str(a)`. If `"ab" > "ba"`, then `a` should come before `b`. This creates a **total ordering** that gives the largest number.
- **Time:** O(n log n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n! × n) | O(n) | Try all permutations |
| Optimized | O(n log n) | O(n) | Custom comparator sort |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Convert numbers to strings for concatenation comparison
- Use `functools.cmp_to_key` for custom comparator in Python
- Handle edge case: all zeroes should return "0", not "000..."

```python
from functools import cmp_to_key

def largestNumber(nums: list[int]) -> str:
    # Convert to strings for comparison
    strs = [str(n) for n in nums]

    # Custom comparator: which concatenation is larger?
    def compare(a, b):
        if a + b > b + a:
            return -1  # a should come first
        elif a + b < b + a:
            return 1   # b should come first
        return 0

    strs.sort(key=cmp_to_key(compare))

    # Edge case: all zeroes
    if strs[0] == "0":
        return "0"

    return "".join(strs)
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[3, 30, 34, 5, 9]`

- Strings: `["3", "30", "34", "5", "9"]`
- Compare "3" vs "30": "330" > "303" → "3" before "30"
- Compare "3" vs "34": "334" < "343" → "34" before "3"
- After sort: `["9", "5", "34", "3", "30"]`
- Result: `"9534330"`

### Edge Case Testing

- **Empty input:** Not possible per constraints
- **Single element:** `[5]` → `"5"`
- **All zeroes:** `[0, 0, 0]` → `"0"` (not `"000"`)
- **Typical case:** `[10, 2]` → `"210"`
- **Same prefix:** `[3, 30, 34]` → `"34330"`

### Complexity

- **Time:** O(n log n) — sorting with O(k) string comparison where k is digit count
- **Space:** O(n) — storing string representations

### Optimization Discussion

The O(n log n) sort is optimal for comparison-based sorting. The comparator proof: this defines a valid total order (transitivity can be proven mathematically).

### Follow-up Variations

- **Smallest number** instead of largest — reverse the comparator
- **Largest number with at most k digits** — variation with constraints
- **Prove the comparator is transitive** — common math follow-up in interviews

### ⚠️ Common Traps

- ⚠️ **Not handling all-zeroes case** — joining `["0","0","0"]` gives `"000"` instead of `"0"`
- Comparing numbers directly instead of string concatenations — `9 > 30` but we need `"930"` not `"309"`
- Using Python 3 without `cmp_to_key` — Python 3 sort doesn't accept `cmp` directly
- Forgetting that comparator must return `-1, 0, 1` (not boolean)
