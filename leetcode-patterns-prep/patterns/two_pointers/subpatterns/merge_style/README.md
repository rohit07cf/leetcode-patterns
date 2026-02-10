# Merge-Style Two Pointers

## What This Subpattern Means

- You have **two sorted sequences** and you merge them by comparing the current element of each.
- Think of it as: "two sorted stacks of papers — pick the smaller top card each time."

---

## The Trigger (How You Recognize It)

- "**Merge** two sorted arrays/lists"
- "**Squares** of a sorted array" (negative numbers squared create two sorted halves)
- Any problem combining two sorted inputs into one sorted output
- The phrase "sorted" appears twice in the problem

---

## Template

```python
def merge_sorted(arr1, arr2):
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # append remaining
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
```

---

## Mistakes

- **Forgetting to append the remaining elements** after the while loop — one array will run out first.
- **Off-by-one in Merge Sorted Array (LeetCode 88):** you merge backwards (from end) to avoid overwriting.
- **Not handling empty inputs.**

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Merge Sorted Array | Merge-Style | | |
| Merge Two Sorted Lists | Merge-Style | | |
| Squares of a Sorted Array | Merge-Style | | |

---

## TL;DR

- Two pointers, one per sorted input, compare and pick the smaller
- Don't forget the leftover tail
- For in-place merge (LeetCode 88): merge from the END to avoid overwriting
