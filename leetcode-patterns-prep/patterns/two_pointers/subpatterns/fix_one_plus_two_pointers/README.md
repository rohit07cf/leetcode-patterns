# Fix One + Two Pointers (Multi-Pointer)

## What This Subpattern Means

- **Fix one element** with a loop, then use **two pointers** on the remaining portion.
- Reduces a 3-element problem to a 2-element problem you already know how to solve.
- Think of it as: "hold one card steady, use two-pointer to find the other two."

---

## The Trigger (How You Recognize It)

- "Find all **triplets** that sum to X" → 3Sum
- "Find the triplet **closest** to target" → 3Sum Closest
- "Find all **quadruplets** that sum to X" → 4Sum (fix two, two-pointer the rest)
- The brute force would be O(N^3) and you need O(N^2)

---

## Template

```python
def three_sum(arr, target=0):
    arr.sort()  # MUST sort first
    result = []

    for i in range(len(arr) - 2):
        # Skip duplicate fixed element
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left, right = i + 1, len(arr) - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == target:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                # Skip duplicates
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return result
```

---

## Mistakes

- **Not sorting first.** The two-pointer inner loop requires sorted order.
- **Not skipping duplicates for the fixed element AND the two pointers.** Both levels need dedup.
- **Off-by-one in the range:** `range(len(arr) - 2)` because you need at least 2 elements after `i`.
- **4Sum trap:** don't forget to skip duplicates at BOTH fixed positions.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| 3Sum | Fix One + Two Pointers | DONE | |
| 3Sum Closest | Fix One + Two Pointers | DONE | |
| 4Sum | Fix One + Two Pointers | | |

---

## TL;DR

- Fix one element with a for loop, two-pointer the rest
- SORT first, always
- Skip duplicates at every level (fixed element + both pointers)
- Reduces O(N^3) brute force to O(N^2)
