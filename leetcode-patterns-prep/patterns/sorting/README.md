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

## Curated Problem Sets (10 per subpattern)

### Merge Sort
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Sort an Array (912) | Medium | `merge_sort/problem_01_sort_an_array.md` |
| 2 | Merge Sorted Array (88) | Easy | `merge_sort/problem_02_merge_sorted_array.md` |
| 3 | Sort List (148) | Medium | `merge_sort/problem_03_sort_list.md` |
| 4 | Count Smaller After Self (315) | Hard | `merge_sort/problem_04_count_smaller_after_self.md` |
| 5 | Reverse Pairs (493) | Hard | `merge_sort/problem_05_reverse_pairs.md` |
| 6 | Count of Range Sum (327) | Hard | `merge_sort/problem_06_count_of_range_sum.md` |
| 7 | Merge k Sorted Lists (23) | Hard | `merge_sort/problem_07_merge_k_sorted_lists.md` |
| 8 | Merge Two Sorted Lists (21) | Easy | `merge_sort/problem_08_merge_two_sorted_lists.md` |
| 9 | Squares of Sorted Array (977) | Easy | `merge_sort/problem_09_squares_of_sorted_array.md` |
| 10 | Sort Colors (75) | Medium | `merge_sort/problem_10_sort_colors.md` |

### Quick Sort / Partition
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Sort an Array (912) | Medium | `quick_sort/problem_01_sort_an_array.md` |
| 2 | Sort Colors (75) | Medium | `quick_sort/problem_02_sort_colors.md` |
| 3 | Kth Largest Element (215) | Medium | `quick_sort/problem_03_kth_largest_element.md` |
| 4 | Top K Frequent (347) | Medium | `quick_sort/problem_04_top_k_frequent.md` |
| 5 | Wiggle Sort II (324) | Medium | `quick_sort/problem_05_wiggle_sort_ii.md` |
| 6 | K Closest Points (973) | Medium | `quick_sort/problem_06_k_closest_points.md` |
| 7 | Sort Array By Parity (905) | Easy | `quick_sort/problem_07_sort_array_by_parity.md` |
| 8 | Move Zeroes (283) | Easy | `quick_sort/problem_08_move_zeroes.md` |
| 9 | Partition Labels (763) | Medium | `quick_sort/problem_09_partition_labels.md` |
| 10 | Largest Number (179) | Medium | `quick_sort/problem_10_largest_number.md` |

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
