# Sliding Window

> **Sliding window = a window on a train.** You're looking at the scenery through a fixed (or stretchy) window, and the train keeps moving forward. You never look backwards — you just slide the view.

---

## When to Use

- The problem asks about a **contiguous subarray** or **substring**
- You need to find the **max/min/count** of something within a window of elements
- The brute force would check every possible subarray — O(N^2) or worse
- The window has a **fixed size** (easy) or a **variable size** based on a condition (medium)
- Keywords: "subarray of size k", "longest substring", "minimum window"

---

## How to Spot It Fast

- "Maximum sum of subarray of size **k**" → fixed window
- "**Longest** substring without repeating characters" → variable window
- "**Minimum** window containing all characters of T" → minimum window pattern
- "Subarray with sum **at most/at least** K" → variable window
- "**Permutation** in string" → fixed window + HashMap
- "Count **distinct** elements in every window" → sliding window + HashMap
- The constraint mentions contiguous elements
- You can express the answer as: "find the best window [i..j] where..."

---

## Core Idea

- Maintain a "window" defined by two pointers: `left` and `right`
- **Expand** the window by moving `right` forward (add element to window)
- **Shrink** the window by moving `left` forward (remove element from window)
- At each step, update your answer based on the current window state
- Key: you never move backwards — each element enters and leaves the window at most once → O(N)

```
Array:  [2, 1, 5, 1, 3, 2]
Window:     [1, 5, 1]
            L        R

Slide right:
            [5, 1, 3]
               L        R
              ↑ removed   ↑ added
```

---

## Template (Python)

```python
def fixed_window(arr, k):
    """Fixed-size window of size k."""
    window_sum = sum(arr[:k])
    best = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]        # add new element
        window_sum -= arr[right - k]    # remove old element
        best = max(best, window_sum)

    return best


def variable_window(arr, condition):
    """Variable-size window: expand right, shrink left when invalid."""
    left = 0
    best = 0
    # window state variables here

    for right in range(len(arr)):
        # expand: add arr[right] to window state

        while not valid():  # ← your condition
            # shrink: remove arr[left] from window state
            left += 1

        best = max(best, right - left + 1)

    return best
```

---

## Common Pitfalls

1. **Off-by-one with window size.** Window `[left..right]` has size `right - left + 1`.
2. **Forgetting to update window state when shrinking.** When you move `left`, remove that element's contribution!
3. **Variable window: shrinking too much or too little.** The `while` condition must match exactly what makes the window invalid.
4. **Fixed window: starting the loop at the wrong index.** First window is `arr[0..k-1]`, loop starts at index `k`.
5. **Confusing "longest" vs "shortest" window.** For longest: update answer outside the shrink loop. For shortest: update answer inside the shrink loop.
6. **HashMap windows: not cleaning up entries with count 0.** A key with count 0 is NOT the same as a missing key in some problems.
7. **Sliding window on strings: forgetting that strings are immutable in Python.** Use a dict/Counter for character counts.
8. **Not handling edge case: window size > array length.**
9. **Thinking the window can shrink from the right.** It can't — `right` only moves forward.
10. **Applying sliding window to non-contiguous problems.** Sliding window ONLY works for contiguous subarrays/substrings.

---

## Curated Problem Sets (10 per subpattern)

### Fixed Window
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Max Sum Subarray of Size K | Easy | `fixed_window/problem_01_max_sum_subarray_k.md` |
| 2 | Maximum Average Subarray I (643) | Easy | `fixed_window/problem_02_max_average_subarray.md` |
| 3 | Find All Anagrams (438) | Medium | `fixed_window/problem_03_find_all_anagrams.md` |
| 4 | Permutation in String (567) | Medium | `fixed_window/problem_04_permutation_in_string.md` |
| 5 | Max Vowels in Substring (1456) | Medium | `fixed_window/problem_05_max_vowels_in_substring.md` |
| 6 | Repeated DNA Sequences (187) | Medium | `fixed_window/problem_06_repeated_dna_sequences.md` |
| 7 | Sliding Window Maximum (239) | Hard | `fixed_window/problem_07_sliding_window_maximum.md` |
| 8 | Grumpy Bookstore Owner (1052) | Medium | `fixed_window/problem_08_grumpy_bookstore_owner.md` |
| 9 | Diet Plan Performance (1176) | Easy | `fixed_window/problem_09_diet_plan_performance.md` |
| 10 | Min Difference K Scores (1984) | Easy | `fixed_window/problem_10_min_difference_k_scores.md` |

### Variable Window
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Longest Substring No Repeat (3) | Medium | `variable_window/problem_01_longest_substring_no_repeat.md` |
| 2 | Longest Repeating Replacement (424) | Medium | `variable_window/problem_02_longest_repeating_replacement.md` |
| 3 | Max Consecutive Ones III (1004) | Medium | `variable_window/problem_03_max_consecutive_ones_iii.md` |
| 4 | Min Size Subarray Sum (209) | Medium | `variable_window/problem_04_min_size_subarray_sum.md` |
| 5 | Fruit Into Baskets (904) | Medium | `variable_window/problem_05_fruit_into_baskets.md` |
| 6 | Subarray Product Less K (713) | Medium | `variable_window/problem_06_subarray_product_less_k.md` |
| 7 | Longest Substring Two Distinct (159) | Medium | `variable_window/problem_07_longest_substring_two_distinct.md` |
| 8 | Longest Turbulent Subarray (978) | Medium | `variable_window/problem_08_longest_turbulent_subarray.md` |
| 9 | Get Equal Substrings (1208) | Medium | `variable_window/problem_09_get_equal_substrings.md` |
| 10 | Max Consecutive Ones II (487) | Medium | `variable_window/problem_10_max_consecutive_ones_ii.md` |

### Minimum Window Pattern
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Minimum Window Substring (76) | Hard | `minimum_window_pattern/problem_01_minimum_window_substring.md` |
| 2 | Smallest Range Covering (632) | Hard | `minimum_window_pattern/problem_02_smallest_range_covering.md` |
| 3 | Minimum Window Subsequence (727) | Hard | `minimum_window_pattern/problem_03_minimum_window_subsequence.md` |
| 4 | Substring Concatenation (30) | Hard | `minimum_window_pattern/problem_04_substring_concatenation.md` |
| 5 | Subarrays K Different (992) | Hard | `minimum_window_pattern/problem_05_subarrays_k_different.md` |
| 6 | Shortest Subarray Sum K (862) | Hard | `minimum_window_pattern/problem_06_shortest_subarray_sum_k.md` |
| 7 | Count Nice Subarrays (1248) | Medium | `minimum_window_pattern/problem_07_count_nice_subarrays.md` |
| 8 | Min Operations Reduce X (1658) | Medium | `minimum_window_pattern/problem_08_min_operations_reduce_x.md` |
| 9 | Max Points From Cards (1423) | Medium | `minimum_window_pattern/problem_09_max_points_from_cards.md` |
| 10 | Min Consecutive Cards (2260) | Medium | `minimum_window_pattern/problem_10_min_consecutive_cards.md` |

### Sliding Window + Hashmap
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Longest Substring No Repeat (3) | Medium | `sliding_window_hashmap/problem_01_longest_substring_no_repeat.md` |
| 2 | Find All Anagrams (438) | Medium | `sliding_window_hashmap/problem_02_find_all_anagrams.md` |
| 3 | Permutation in String (567) | Medium | `sliding_window_hashmap/problem_03_permutation_in_string.md` |
| 4 | Fruit Into Baskets (904) | Medium | `sliding_window_hashmap/problem_04_fruit_into_baskets.md` |
| 5 | Longest K Distinct (340) | Medium | `sliding_window_hashmap/problem_05_longest_k_distinct.md` |
| 6 | Longest Repeating Replacement (424) | Medium | `sliding_window_hashmap/problem_06_longest_repeating_replacement.md` |
| 7 | Substrings Three Chars (1358) | Medium | `sliding_window_hashmap/problem_07_substrings_three_chars.md` |
| 8 | Max Consecutive Ones III (1004) | Medium | `sliding_window_hashmap/problem_08_max_consecutive_ones_iii.md` |
| 9 | Minimum Window Substring (76) | Hard | `sliding_window_hashmap/problem_09_minimum_window_substring.md` |
| 10 | Contains Duplicate II (219) | Easy | `sliding_window_hashmap/problem_10_contains_duplicate_ii.md` |

---

## TL;DR

- Fixed window: precompute first window, then slide by adding right and removing left
- Variable window: expand right always, shrink left when window becomes invalid
- Each element enters and leaves the window at most once → O(N) total
- "Longest" → update outside shrink loop. "Shortest" → update inside shrink loop.
- Always ask: what's in my window? What makes it valid/invalid?
