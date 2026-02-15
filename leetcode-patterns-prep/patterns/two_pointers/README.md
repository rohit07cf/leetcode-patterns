# Two Pointers

> **Two pointers = two hands moving on an array.** You place two fingers on the data and move them according to a rule until they meet or cross.

---

## When to Use

- The input is a **sorted array** (or can be sorted)
- You need to find a **pair** that satisfies a condition (sum, difference, etc.)
- You need to **compare elements from both ends** (palindromes, container problems)
- You need to **remove/modify elements in-place** without extra space
- You need to **partition** an array into groups (e.g., Sort Colors)
- You need to **detect a cycle** or find the **middle** of a linked list

---

## How to Spot It Fast

- "Find two elements that..." → opposite direction pointers
- "Remove duplicates" or "remove element in-place" → same direction (read/write pointers)
- "Is it a palindrome?" → opposite direction, shrink inward
- "Container with most water" / "trapping rain water" → opposite direction
- "3Sum" or "4Sum" → fix one element, two-pointer the rest
- "Sort an array with only 2-3 distinct values" → partition-style (Dutch National Flag)
- "Detect cycle in linked list" → fast & slow pointers
- The constraint says **O(1) extra space** → strong two-pointer signal

---

## Core Idea

- Instead of checking every pair (O(N^2)), two pointers let you skip impossible pairs
- In a sorted array, if `arr[left] + arr[right] < target`, moving `left` right increases the sum
- If `arr[left] + arr[right] > target`, moving `right` left decreases the sum
- This "squeeze" eliminates an entire row/column of possibilities per step → O(N)

```
Sorted array: [1, 3, 5, 7, 9]
              L              R

  sum too small? → move L right
  sum too big?   → move R left
  sum just right? → found it!
```

---

## Template (Python)

```python
def two_pointer_opposite(arr, target):
    """Opposite direction: find pair with given sum in sorted array."""
    left, right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return [left, right]       # found
        elif current < target:
            left += 1                  # need bigger sum
        else:
            right -= 1                # need smaller sum

    return []  # no pair found


def two_pointer_same_direction(arr):
    """Same direction: remove duplicates / in-place modify."""
    write = 0  # slow pointer (where to write)

    for read in range(len(arr)):       # fast pointer (what to read)
        if should_keep(arr[read]):
            arr[write] = arr[read]
            write += 1

    return write  # new length
```

---

## Common Pitfalls

1. **Forgetting to sort first.** Two pointers on an unsorted array won't give correct results for sum-type problems.
2. **Using `<=` instead of `<` in `while left < right`.** If `left == right`, you're comparing an element with itself.
3. **Not handling duplicates.** In 3Sum, skip duplicate values: `while left < right and arr[left] == arr[left-1]: left += 1`
4. **Off-by-one in same-direction pointer.** The `write` pointer is the next position to write, not the last written position.
5. **Modifying the array when you shouldn't.** Some problems want a new result, not in-place modification. Read carefully.
6. **Forgetting the edge case: empty array or single element.** Always check `len(arr) < 2` for pair problems.
7. **Moving both pointers at once.** Only move ONE pointer per iteration (unless you found a match).
8. **Not returning to the right pointer position after skipping duplicates.** Keep track of where you are.
9. **Assuming sorted input.** If the problem doesn't say "sorted," you need to sort first (or use a hash map instead).
10. **Using two pointers when a hash map is simpler.** If the array isn't sorted and you can't sort it, a hash map might be O(N) vs O(N log N).

---

## Curated Problem Sets (10 per subpattern)

### Opposite Direction
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Two Sum II (167) | Medium | `opposite_direction/problem_01_two_sum_ii.md` |
| 2 | Valid Palindrome (125) | Easy | `opposite_direction/problem_02_valid_palindrome.md` |
| 3 | Container With Most Water (11) | Medium | `opposite_direction/problem_03_container_with_most_water.md` |
| 4 | Trapping Rain Water (42) | Hard | `opposite_direction/problem_04_trapping_rain_water.md` |
| 5 | Reverse String (344) | Easy | `opposite_direction/problem_05_reverse_string.md` |
| 6 | Two Sum Less Than K (1099) | Easy | `opposite_direction/problem_06_two_sum_less_than_k.md` |
| 7 | Boats to Save People (881) | Medium | `opposite_direction/problem_07_boats_to_save_people.md` |
| 8 | Valid Palindrome II (680) | Easy | `opposite_direction/problem_08_valid_palindrome_ii.md` |
| 9 | Squares of a Sorted Array (977) | Easy | `opposite_direction/problem_09_squares_of_sorted_array.md` |
| 10 | Sort Array By Parity (905) | Easy | `opposite_direction/problem_10_sort_array_by_parity.md` |

### Same Direction
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Move Zeroes (283) | Easy | `same_direction/problem_01_move_zeroes.md` |
| 2 | Remove Duplicates (26) | Easy | `same_direction/problem_02_remove_duplicates.md` |
| 3 | Remove Element (27) | Easy | `same_direction/problem_03_remove_element.md` |
| 4 | Remove Duplicates II (80) | Medium | `same_direction/problem_04_remove_duplicates_ii.md` |
| 5 | Merge Sorted Array (88) | Easy | `same_direction/problem_05_merge_sorted_array.md` |
| 6 | Backspace String Compare (844) | Easy | `same_direction/problem_06_backspace_string_compare.md` |
| 7 | String Compression (443) | Medium | `same_direction/problem_07_string_compression.md` |
| 8 | Find First Occurrence (28) | Easy | `same_direction/problem_08_implement_strstr.md` |
| 9 | Long Pressed Name (925) | Easy | `same_direction/problem_09_long_pressed_name.md` |
| 10 | Shortest Unsorted Subarray (581) | Medium | `same_direction/problem_10_shortest_unsorted_subarray.md` |

### Fast and Slow
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Linked List Cycle (141) | Easy | `fast_and_slow/problem_01_linked_list_cycle.md` |
| 2 | Linked List Cycle II (142) | Medium | `fast_and_slow/problem_02_linked_list_cycle_ii.md` |
| 3 | Happy Number (202) | Easy | `fast_and_slow/problem_03_happy_number.md` |
| 4 | Find the Duplicate Number (287) | Medium | `fast_and_slow/problem_04_find_duplicate_number.md` |
| 5 | Middle of Linked List (876) | Easy | `fast_and_slow/problem_05_middle_of_linked_list.md` |
| 6 | Palindrome Linked List (234) | Easy | `fast_and_slow/problem_06_palindrome_linked_list.md` |
| 7 | Reorder List (143) | Medium | `fast_and_slow/problem_07_reorder_list.md` |
| 8 | Remove Nth From End (19) | Medium | `fast_and_slow/problem_08_remove_nth_from_end.md` |
| 9 | Circular Array Loop (457) | Medium | `fast_and_slow/problem_09_circular_array_loop.md` |
| 10 | Intersection of Linked Lists (160) | Easy | `fast_and_slow/problem_10_intersection_of_linked_lists.md` |

### Fix One + Two Pointers
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | 3Sum (15) | Medium | `fix_one_plus_two_pointers/problem_01_three_sum.md` |
| 2 | 3Sum Closest (16) | Medium | `fix_one_plus_two_pointers/problem_02_three_sum_closest.md` |
| 3 | 3Sum Smaller (259) | Medium | `fix_one_plus_two_pointers/problem_03_three_sum_smaller.md` |
| 4 | 4Sum (18) | Medium | `fix_one_plus_two_pointers/problem_04_four_sum.md` |
| 5 | Valid Triangle Number (611) | Medium | `fix_one_plus_two_pointers/problem_05_valid_triangle_number.md` |
| 6 | 3Sum With Multiplicity (923) | Medium | `fix_one_plus_two_pointers/problem_06_three_sum_with_multiplicity.md` |
| 7 | Increasing Triplet (334) | Medium | `fix_one_plus_two_pointers/problem_07_increasing_triplet_subsequence.md` |
| 8 | Count Good Triplets (1534) | Easy | `fix_one_plus_two_pointers/problem_08_count_good_triplets.md` |
| 9 | Arithmetic Triplets (2367) | Easy | `fix_one_plus_two_pointers/problem_09_number_of_arithmetic_triplets.md` |
| 10 | Two Sum BSTs (1214) | Medium | `fix_one_plus_two_pointers/problem_10_two_sum_bst.md` |

### Merge Style
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Merge Sorted Array (88) | Easy | `merge_style/problem_01_merge_sorted_array.md` |
| 2 | Merge Two Sorted Lists (21) | Easy | `merge_style/problem_02_merge_two_sorted_lists.md` |
| 3 | Intersection of Two Arrays (349) | Easy | `merge_style/problem_03_intersection_of_two_arrays.md` |
| 4 | Intersection of Two Arrays II (350) | Easy | `merge_style/problem_04_intersection_of_two_arrays_ii.md` |
| 5 | Interval List Intersections (986) | Medium | `merge_style/problem_05_interval_list_intersections.md` |
| 6 | Merge k Sorted Lists (23) | Hard | `merge_style/problem_06_merge_k_sorted_lists.md` |
| 7 | Squares of a Sorted Array (977) | Easy | `merge_style/problem_07_squares_of_sorted_array.md` |
| 8 | Shortest Word Distance (243) | Easy | `merge_style/problem_08_shortest_word_distance.md` |
| 9 | Assign Cookies (455) | Easy | `merge_style/problem_09_assign_cookies.md` |
| 10 | Add Two Numbers II (445) | Medium | `merge_style/problem_10_add_two_numbers_ii.md` |

### Opposite Direction — Skip Logic
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | 3Sum (15) | Medium | `opposite_direction_skip_logic/problem_01_three_sum.md` |
| 2 | Container With Most Water (11) | Medium | `opposite_direction_skip_logic/problem_02_container_with_most_water.md` |
| 3 | Valid Palindrome II (680) | Easy | `opposite_direction_skip_logic/problem_03_valid_palindrome_ii.md` |
| 4 | Trapping Rain Water (42) | Hard | `opposite_direction_skip_logic/problem_04_trapping_rain_water.md` |
| 5 | Remove Duplicates II (80) | Medium | `opposite_direction_skip_logic/problem_05_remove_duplicates_ii.md` |
| 6 | 4Sum (18) | Medium | `opposite_direction_skip_logic/problem_06_four_sum.md` |
| 7 | Next Permutation (31) | Medium | `opposite_direction_skip_logic/problem_07_next_permutation.md` |
| 8 | Shortest Unsorted Subarray (581) | Medium | `opposite_direction_skip_logic/problem_08_shortest_unsorted_subarray.md` |
| 9 | Longest Mountain (845) | Medium | `opposite_direction_skip_logic/problem_09_longest_mountain.md` |
| 10 | Sort Colors (75) | Medium | `opposite_direction_skip_logic/problem_10_sort_colors.md` |

### Partition Style
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Sort Colors (75) | Medium | `partition_style/problem_01_sort_colors.md` |
| 2 | Move Zeroes (283) | Easy | `partition_style/problem_02_move_zeroes.md` |
| 3 | Sort Array By Parity (905) | Easy | `partition_style/problem_03_sort_array_by_parity.md` |
| 4 | Sort Array By Parity II (922) | Easy | `partition_style/problem_04_sort_array_by_parity_ii.md` |
| 5 | Partition Labels (763) | Medium | `partition_style/problem_05_partition_labels.md` |
| 6 | Rearrange Array by Sign (2149) | Medium | `partition_style/problem_06_rearrange_array_by_sign.md` |
| 7 | Wiggle Sort (280) | Medium | `partition_style/problem_07_wiggle_sort.md` |
| 8 | Remove Element (27) | Easy | `partition_style/problem_08_remove_element.md` |
| 9 | Kth Largest Element (215) | Medium | `partition_style/problem_09_kth_largest_element.md` |
| 10 | Segregate Even and Odd | Easy | `partition_style/problem_10_segregate_even_odd.md` |

---

## TL;DR

- Two pointers shrink the search space from O(N^2) to O(N) by exploiting sorted order
- **Opposite direction**: start at both ends, squeeze inward
- **Same direction**: read pointer scouts ahead, write pointer builds the result
- Always check: is the array sorted? Do I need to handle duplicates?
- When in doubt, draw the two pointers on paper and simulate 3 steps
