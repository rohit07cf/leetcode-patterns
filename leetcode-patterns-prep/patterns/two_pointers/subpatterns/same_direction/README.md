# Same Direction Two Pointers (In-Place Modify)

## What This Subpattern Means

- Two pointers move in the **same direction**: a **read** pointer that scans every element, and a **write** pointer that only advances when we keep an element.
- Think of it as: "one person reads the mail, another person only files the important ones."

---

## The Trigger (How You Recognize It)

- "Remove element **in-place**"
- "Remove **duplicates** from sorted array"
- "Move all **zeroes** to the end"
- The constraint says **O(1) extra space** and you need to modify the array
- The relative order of kept elements must be preserved

---

## Template

```python
def same_direction(arr, val_to_remove):
    write = 0

    for read in range(len(arr)):
        if arr[read] != val_to_remove:   # ← your keep condition
            arr[write] = arr[read]
            write += 1

    return write  # new length
```

```
Before:  [3, 2, 2, 3]  remove 3
          r
          w

Step by step:
  read=0: arr[0]=3, skip
  read=1: arr[1]=2, keep → arr[0]=2, w=1
  read=2: arr[2]=2, keep → arr[1]=2, w=2
  read=3: arr[3]=3, skip

After:   [2, 2, _, _]  return 2
```

---

## Mistakes

- **Returning the array instead of the length.** These problems ask for the new length; the array is modified in-place.
- **Using extra space.** The whole point is O(1) space — don't create a new array.
- **Wrong keep condition for "remove duplicates."** For sorted arrays: `if arr[read] != arr[write - 1]` (compare with last written, not last read).
- **Off-by-one with write pointer.** `write` always points to the NEXT position to write, so the valid portion is `arr[0..write-1]`.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Remove Element | Same Direction | DONE | |
| Remove Duplicates from Sorted Array | Same Direction | DONE | |
| Move Zeroes | Same Direction | DONE | |

---

## TL;DR

- Read pointer scans everything; write pointer stores only keepers
- `write` = next empty slot; valid result is `arr[0..write-1]`
- O(N) time, O(1) space — no extra array needed
- Check your keep condition carefully (it changes per problem)
