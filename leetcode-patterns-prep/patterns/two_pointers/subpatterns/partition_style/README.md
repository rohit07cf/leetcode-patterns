# Partition-Style Two Pointers

## What This Subpattern Means

- You're **rearranging** elements into groups (e.g., all 0s, then all 1s, then all 2s).
- Uses 2 or 3 pointers to partition the array in a single pass.
- Think of it as: "sorting cards into piles without a full sort."

---

## The Trigger (How You Recognize It)

- "Sort an array with only **2-3 distinct values**" → Dutch National Flag / Sort Colors
- "**Partition** array by some property" (even/odd, positive/negative)
- "**Sort Array By Parity**"
- The constraint says O(N) time and O(1) space, and there are few distinct categories

---

## Template

```python
def dutch_national_flag(arr):
    """Sort Colors: 0s, then 1s, then 2s. Single pass."""
    low, mid, high = 0, 0, len(arr) - 1

    # Invariant:
    #   arr[0..low-1]   = 0s
    #   arr[low..mid-1]  = 1s
    #   arr[mid..high]   = unknown
    #   arr[high+1..n-1] = 2s

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            # DON'T advance mid — the swapped element is unknown
```

---

## Mistakes

- **Advancing `mid` when swapping with `high`.** The element swapped from `high` hasn't been examined yet — don't skip it!
- **Only advancing `mid` when swapping with `low` is safe** because everything before `mid` has already been processed.
- **Confusing this with a simple two-partition.** Two-category partition (even/odd) only needs 2 pointers; three-category needs 3.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Sort Colors | Partition-Style | DONE | |
| Sort Array By Parity | Partition-Style | DONE | |
| Sort an Array (partition logic) | Partition-Style | | |

---

## TL;DR

- 3 pointers: `low`, `mid`, `high` for 3-way partition
- When swapping with `high`, DON'T advance `mid` (element is unexamined)
- When swapping with `low`, advance BOTH `low` and `mid`
- Single pass = O(N) time, O(1) space
