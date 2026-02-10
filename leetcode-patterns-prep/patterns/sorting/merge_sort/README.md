# Merge Sort

## Pattern in 1 Sentence

Split the array in half, recursively sort both halves, then merge them back together in sorted order.

---

## When to Use

- You need a **stable sort** (equal elements keep their original order)
- You need **guaranteed O(N log N)** worst case (no O(N^2) risk like quicksort)
- You need to **count inversions** (how many swaps to sort)
- You need to **sort a linked list** (merge sort doesn't need random access)
- The problem uses **divide and conquer** with a merge step

---

## How to Spot It Fast

- "Sort a linked list" → merge sort (quicksort needs random access)
- "Count inversions / count smaller numbers after self" → merge sort + counting
- "Merge K sorted lists" → same merge logic, extended
- Any stable sort requirement

---

## Core Idea

```
Array: [38, 27, 43, 3, 9, 82, 10]

Split:  [38, 27, 43, 3]  |  [9, 82, 10]
Split:  [38, 27] | [43, 3] | [9, 82] | [10]
Split:  [38]|[27] | [43]|[3] | [9]|[82] | [10]

Merge:  [27, 38] | [3, 43] | [9, 82] | [10]
Merge:  [3, 27, 38, 43]  |  [9, 10, 82]
Merge:  [3, 9, 10, 27, 38, 43, 82]  ✓
```

---

## Template (Python)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= for stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

## Common Pitfalls

1. **Using `<` instead of `<=` in merge.** Use `<=` to maintain stability (equal elements keep original order).
2. **Forgetting to append remaining elements** after the while loop.
3. **Not recognizing O(N) extra space.** Merge sort creates new arrays at each level.
4. **For in-place merge sort:** it's possible but complex — in interviews, the extra-space version is fine.
5. **Count inversions:** increment the count when you pick from the RIGHT array (an element jumped over remaining left elements). The count is `len(left) - i`.

---

## TL;DR

- Split → sort halves → merge. Always O(N log N).
- Merge step: two pointers, pick smaller, append remainder
- `<=` in merge for stability
- O(N) extra space — that's the trade-off vs quicksort
- Key interview application: count inversions during merge
