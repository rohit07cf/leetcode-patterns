# Modified Binary Search (Rotated / Special Arrays)

## What This Subpattern Means

- The array was **sorted but then rotated** (e.g., `[4,5,6,7,0,1,2]`).
- Or the array has a special structure (peak element, mountain array).
- Standard binary search won't work directly — you need to figure out **which half is sorted** first.

---

## The Trigger (How You Recognize It)

- "Search in **rotated** sorted array"
- "Find **minimum** in rotated sorted array"
- "Find **peak element**" (element greater than its neighbors)
- The array was sorted once but shifted/rotated

---

## Template

```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        # Figure out which half is sorted
        if arr[left] <= arr[mid]:
            # LEFT half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1     # target is in sorted left half
            else:
                left = mid + 1      # target is in right half
        else:
            # RIGHT half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1      # target is in sorted right half
            else:
                right = mid - 1     # target is in left half

    return -1
```

```
Rotated: [4, 5, 6, 7, 0, 1, 2]
                   ↑ pivot

Left half sorted:  [4, 5, 6, 7]   arr[left] <= arr[mid]
Right half sorted: [0, 1, 2]      arr[mid] > arr[right]
```

---

## Mistakes

- **Not checking which half is sorted first.** You MUST determine if the left or right half is sorted before deciding where to search.
- **Using `<` instead of `<=` in `arr[left] <= arr[mid]`.** The `=` handles the case when `left == mid`.
- **Peak element: using `arr[mid] > arr[mid+1]`** — make sure `mid+1` is in bounds! Use `left < right` loop to guarantee safety.
- **Duplicates in rotated array** make it harder (worst case O(N)). The basic template assumes no duplicates.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Search in Rotated Sorted Array | Modified (Rotated) | | |
| Find Minimum in Rotated Sorted Array | Modified (Rotated) | | |
| Peak Element | Modified (Special) | | |

---

## TL;DR

- Rotated array = two sorted halves. Find which half is sorted first.
- Check if target is in the sorted half; if yes, search there; if no, search the other half.
- Peak element: go toward the "uphill" side (`arr[mid] < arr[mid+1]` → go right)
- Watch for duplicates — they can break the "which half is sorted" logic
