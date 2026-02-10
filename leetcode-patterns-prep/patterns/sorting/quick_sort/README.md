# Quick Sort

## Pattern in 1 Sentence

Pick a pivot, partition the array so everything smaller is left and everything bigger is right, then recursively sort both halves.

---

## When to Use

- You need to **sort in-place** with O(log N) extra space
- You need the **partition** step for quickselect (find Kth element in O(N) average)
- The problem involves **Dutch National Flag** style partitioning
- You're implementing sort from scratch in an interview

---

## How to Spot It Fast

- "Sort an array" (one of two standard answers)
- "Find Kth largest/smallest without full sort" → quickselect uses partition
- "Partition array into groups" → uses the same partition logic

---

## Core Idea

```
Array: [3, 6, 8, 10, 1, 2, 1]

1. Pick pivot (say 3)
2. Partition: [1, 2, 1, | 3 | 6, 8, 10]
                        ↑ pivot in correct position!
3. Recursively sort left [1, 2, 1] and right [6, 8, 10]
```

The partition step is the heart of quicksort. After partition, the pivot is in its FINAL sorted position.

---

## Template (Python)

```python
import random

def quicksort(arr, lo, hi):
    if lo < hi:
        pivot_idx = partition(arr, lo, hi)
        quicksort(arr, lo, pivot_idx - 1)
        quicksort(arr, pivot_idx + 1, hi)

def partition(arr, lo, hi):
    # Random pivot to avoid O(N^2) worst case
    rand_idx = random.randint(lo, hi)
    arr[rand_idx], arr[hi] = arr[hi], arr[rand_idx]

    pivot = arr[hi]
    i = lo  # boundary of "smaller than pivot" region

    for j in range(lo, hi):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[hi] = arr[hi], arr[i]  # place pivot
    return i  # pivot's final index
```

---

## Common Pitfalls

1. **Not using random pivot.** Sorted/reverse-sorted input → O(N^2) without randomization.
2. **Off-by-one in partition boundary.** `i` is the boundary between "smaller" and "unknown." After the loop, swap pivot to position `i`.
3. **Forgetting base case `if lo < hi`.** Without it, recursion doesn't terminate.
4. **Quicksort is NOT stable.** Equal elements can change relative order.
5. **Stack overflow on large inputs.** Worst case recursion depth = O(N). Random pivot makes this extremely unlikely.

---

## TL;DR

- Pick pivot → partition → recurse on both halves
- ALWAYS use random pivot
- Partition is the key skill — practice it separately
- O(N log N) average, O(N^2) worst (rare with random pivot)
- O(log N) space (recursion stack)
