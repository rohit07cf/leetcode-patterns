# Sorting

> **Sorting is not a pattern itself — it's a fundamental skill** that shows up inside other patterns. Knowing quicksort's partition and merge sort's merge is essential because many interview problems use these as building blocks.

---

## When to Use

- The problem requires **custom ordering** or **rearranging** elements
- You need **quicksort's partition** logic (e.g., Kth element, Dutch National Flag)
- You need **merge sort's merge** logic (e.g., merge intervals, count inversions)
- The problem says "sort an array" (know both algorithms cold)
- Understanding sorting helps you recognize when two-pointer or binary search can replace a sort

---

## How to Spot It Fast

- "Sort an array" → know quicksort AND merge sort
- "Kth largest without full sort" → quickselect (partition logic)
- "Count inversions" → merge sort with counting
- "Sort linked list" → merge sort (no random access needed)
- Any problem where you need to sort before applying another pattern

---

## The Two Sorts You Must Know

| | Quicksort | Merge Sort |
|--|-----------|------------|
| **Best/Avg** | O(N log N) | O(N log N) |
| **Worst** | O(N^2) | O(N log N) |
| **Space** | O(log N) stack | O(N) extra array |
| **Stable** | No | Yes |
| **Key Idea** | Partition around pivot | Divide, sort halves, merge |
| **Interview Use** | Partition logic, quickselect | Merge logic, count inversions |

---

## Common Pitfalls

1. **Using quicksort when stability matters.** Quicksort is NOT stable. Use merge sort for stable sorting.
2. **Worst-case quicksort on already-sorted input.** Always use random pivot to avoid O(N^2).
3. **Forgetting merge sort uses O(N) extra space.** This matters for space-constrained problems.
4. **Not knowing the partition step cold.** Practice writing Lomuto or Hoare partition from memory.
5. **Confusing in-place with stable.** Quicksort is in-place but not stable. Merge sort is stable but not in-place.

---

## Subfolders

- [`quick_sort/`](quick_sort/) — Partition logic, quickselect
- [`merge_sort/`](merge_sort/) — Merge logic, divide & conquer

---

## TL;DR

- Know both quicksort and merge sort from memory
- Quicksort's superpower: the partition step (used in quickselect, Dutch National Flag)
- Merge sort's superpower: the merge step (used in merge intervals, count inversions)
- Random pivot for quicksort to avoid O(N^2) worst case
- Python's built-in `sorted()` is Timsort (hybrid) — use it freely in interviews unless they say "implement sort"
