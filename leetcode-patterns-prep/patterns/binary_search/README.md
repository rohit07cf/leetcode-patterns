# Binary Search

> **Binary search = "the answer is monotonic" detector.** If you can split the search space into "yes" and "no" with a clear boundary, binary search finds that boundary in O(log N).

---

## When to Use

- The input is **sorted** (or has a monotonic property)
- You need to **find a target** in O(log N) time
- You need to find the **first/last** element satisfying a condition
- The problem has a **rotated sorted array**
- You're searching for the **answer itself** (not an element) and can write a `check(mid)` function that's monotonic
- The brute force would be linear scan but the search space is huge (10^9)

---

## How to Spot It Fast

- "Search in a **sorted** array" → classic binary search
- "Find **first/last** occurrence" → boundary binary search
- "Search in **rotated** sorted array" → modified binary search
- "**Minimum/maximum** value that satisfies a condition" → binary search on answer
- "**Koko eating bananas**" / "ship packages within D days" → binary search on answer
- The constraint is N ≤ 10^5 but the answer space is up to 10^9 → binary search on answer
- "The answer is between **lo and hi**, and if X works, then X+1 also works" → monotonic → binary search

---

## Core Idea

- Divide the search space in half at each step
- Compare `mid` with your target/condition
- Eliminate the half that can't contain the answer
- Repeat until the search space has one element

```
Array: [1, 3, 5, 7, 9, 11, 13]    target = 7

Step 1: mid = 7, found!

But the real power is:
Answer space: [1, 2, 3, ..., 1000000000]
              can you do it with speed 500000000? yes → try smaller
              can you do it with speed 250000000? yes → try smaller
              ...
              can you do it with speed 4? no → try bigger
              can you do it with speed 5? yes → answer is 5!

  Only ~30 steps to search 10^9 values!
```

---

## Template (Python)

```python
def binary_search(arr, target):
    """Classic: find target in sorted array."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # avoid overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found


def binary_search_on_answer(lo, hi, check):
    """
    Find minimum value where check(mid) is True.
    Assumes: if check(x) is True, then check(x+1) is also True (monotonic).
    """
    while lo < hi:
        mid = lo + (hi - lo) // 2

        if check(mid):
            hi = mid        # mid might be the answer, search left
        else:
            lo = mid + 1    # mid too small, search right

    return lo  # lo == hi == answer
```

---

## Common Pitfalls

1. **Off-by-one errors.** The #1 bug. Use `left <= right` for classic search, `left < right` for boundary/answer search.
2. **Integer overflow with `(left + right) / 2`.** Use `left + (right - left) // 2` instead (Python handles big ints, but it's a good habit for interviews in other languages).
3. **Wrong `lo`/`hi` bounds in answer-space search.** Make sure the answer is within `[lo, hi]`. Too narrow → miss the answer. Too wide → still works, just slightly slower.
4. **Forgetting that rotated arrays have TWO sorted halves.** Identify which half is sorted, then check if target is in that half.
5. **Boundary search: updating `right = mid` vs `right = mid - 1`.** When searching for "first true", use `right = mid` (mid could be the answer). When searching for exact match, use `right = mid - 1`.
6. **Infinite loop when `lo == hi - 1`.** If `mid = lo`, and you set `lo = mid`, you're stuck. Make sure `lo` always increases: `lo = mid + 1`.
7. **Not defining the `check()` function clearly** for answer-space problems. Write it on paper first.
8. **Applying binary search when the property isn't monotonic.** Binary search on answer REQUIRES: if check(x) is True, check(x+1) is True (or the reverse).
9. **Confusing "find minimum that works" vs "find maximum that works."** Minimum → search left when check passes. Maximum → search right when check passes.
10. **Returning the wrong value.** After the loop, `lo == hi` — that's your answer (not `mid`).

---

## Curated Problem Sets (10 per subpattern)

### Classic Binary Search
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Binary Search (704) | Easy | `classic_binary_search/problem_01_binary_search.md` |
| 2 | Search Insert Position (35) | Easy | `classic_binary_search/problem_02_search_insert_position.md` |
| 3 | Guess Number (374) | Easy | `classic_binary_search/problem_03_guess_number.md` |
| 4 | First Bad Version (278) | Easy | `classic_binary_search/problem_04_first_bad_version.md` |
| 5 | Search a 2D Matrix (74) | Medium | `classic_binary_search/problem_05_search_2d_matrix.md` |
| 6 | Sqrt(x) (69) | Easy | `classic_binary_search/problem_06_sqrt_x.md` |
| 7 | Valid Perfect Square (367) | Easy | `classic_binary_search/problem_07_valid_perfect_square.md` |
| 8 | Find Peak Element (162) | Medium | `classic_binary_search/problem_08_find_peak_element.md` |
| 9 | Peak Index in Mountain (852) | Medium | `classic_binary_search/problem_09_peak_index_mountain.md` |
| 10 | Count Negative Numbers (1351) | Easy | `classic_binary_search/problem_10_count_negative_numbers.md` |

### Boundary Binary Search
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | First and Last Position (34) | Medium | `boundary_binary_search/problem_01_first_and_last_position.md` |
| 2 | Smallest Letter Greater (744) | Easy | `boundary_binary_search/problem_02_smallest_letter_greater.md` |
| 3 | H-Index II (275) | Medium | `boundary_binary_search/problem_03_h_index_ii.md` |
| 4 | Single Element in Sorted (540) | Medium | `boundary_binary_search/problem_04_single_element_sorted.md` |
| 5 | Arranging Coins (441) | Easy | `boundary_binary_search/problem_05_arranging_coins.md` |
| 6 | Kth Missing Positive (1539) | Easy | `boundary_binary_search/problem_06_kth_missing_positive.md` |
| 7 | Special Array (1608) | Easy | `boundary_binary_search/problem_07_special_array.md` |
| 8 | Count Negative Numbers (1351) | Easy | `boundary_binary_search/problem_08_count_negative_numbers.md` |
| 9 | Plates Between Candles (2055) | Medium | `boundary_binary_search/problem_09_plates_between_candles.md` |
| 10 | Find Target Indices (2089) | Easy | `boundary_binary_search/problem_10_find_target_indices.md` |

### Binary Search on Answer
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Koko Eating Bananas (875) | Medium | `binary_search_on_answer/problem_01_koko_eating_bananas.md` |
| 2 | Capacity To Ship (1011) | Medium | `binary_search_on_answer/problem_02_capacity_to_ship.md` |
| 3 | Split Array Largest Sum (410) | Hard | `binary_search_on_answer/problem_03_split_array_largest_sum.md` |
| 4 | Minimum Days Bouquets (1482) | Medium | `binary_search_on_answer/problem_04_minimum_days_bouquets.md` |
| 5 | Magnetic Force (1552) | Medium | `binary_search_on_answer/problem_05_magnetic_force.md` |
| 6 | Smallest Divisor (1283) | Medium | `binary_search_on_answer/problem_06_smallest_divisor.md` |
| 7 | Max Candies Allocated (2226) | Medium | `binary_search_on_answer/problem_07_max_candies_allocated.md` |
| 8 | Minimum Time Trips (2187) | Medium | `binary_search_on_answer/problem_08_minimum_time_trips.md` |
| 9 | Minimize Max Distance (774) | Hard | `binary_search_on_answer/problem_09_minimize_max_distance.md` |
| 10 | Cutting Ribbons (1891) | Medium | `binary_search_on_answer/problem_10_cutting_ribbons.md` |

### Modified Binary Search — Rotated Arrays
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Search in Rotated Sorted (33) | Medium | `modified_binary_search_rotated/problem_01_search_rotated_sorted.md` |
| 2 | Search in Rotated II (81) | Medium | `modified_binary_search_rotated/problem_02_search_rotated_sorted_ii.md` |
| 3 | Find Min Rotated (153) | Medium | `modified_binary_search_rotated/problem_03_find_min_rotated.md` |
| 4 | Find Min Rotated II (154) | Hard | `modified_binary_search_rotated/problem_04_find_min_rotated_ii.md` |
| 5 | Find Peak Element (162) | Medium | `modified_binary_search_rotated/problem_05_find_peak_element.md` |
| 6 | Search Unknown Size (702) | Medium | `modified_binary_search_rotated/problem_06_search_unknown_size.md` |
| 7 | Median of Two Sorted (4) | Hard | `modified_binary_search_rotated/problem_07_median_two_sorted.md` |
| 8 | Find K Closest (658) | Medium | `modified_binary_search_rotated/problem_08_find_k_closest.md` |
| 9 | Find Rotation Count | Medium | `modified_binary_search_rotated/problem_09_find_rotation_count.md` |
| 10 | Search Nearly Sorted | Medium | `modified_binary_search_rotated/problem_10_search_nearly_sorted.md` |

---

## TL;DR

- Classic binary search: `while left <= right`, return when found
- Boundary search: `while left < right`, narrow to first/last occurrence
- Binary search on answer: define `check(mid)`, search the answer space
- The #1 skill: recognizing that a problem has a monotonic `check()` function
- Off-by-one is your enemy — practice the template until it's muscle memory
