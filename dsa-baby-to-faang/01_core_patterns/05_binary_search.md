# Binary Search

## Baby Explanation (ELI10)

- Imagine I'm thinking of a number between 1 and 100. You guess 50. I say "too high." Now you KNOW the answer is between 1 and 49. You just eliminated HALF the possibilities with one guess!
- That's **Binary Search.** Every step, you cut the search space in half.
- 1000 items? Only 10 guesses needed. 1,000,000 items? Only 20 guesses. It's insanely fast.
- The catch: your data must be **sorted** (or have some monotonic property). You can't play the guessing game if the numbers are in random order.
- Think of it like opening a dictionary. You don't start at page 1. You open to the middle, see if your word comes before or after, and flip accordingly.
- The pattern is always: pick the **middle**, decide to go **left** or **right**, repeat.

## Pattern Recognition

Use this when you see:
- "Sorted array" + "find a target"
- "Find the first/last position of..."
- "Search insert position"
- "Minimum/maximum value that satisfies a condition" (binary search on answer)
- O(log n) time requirement
- "Rotated sorted array"

Avoid when:
- The data is unsorted and you can't sort it
- You need to find ALL occurrences (binary search finds one; you'd need extra steps)
- The search space isn't monotonic (no clear left/right decision)

## ASCII Diagram: Binary Search Halving

```
  Find target = 7 in sorted array:

  [1, 3, 5, 7, 9, 11, 13]
   L        M            R        mid=3, nums[3]=7. Found it!

  But let's say target = 9:

  Step 1: [1, 3, 5, 7, 9, 11, 13]
           L        M            R     nums[3]=7 < 9 --> go right
                                       (eliminate left half)

  Step 2: [1, 3, 5, 7, 9, 11, 13]
                       L   M      R    nums[5]=11 > 9 --> go left
                                       (eliminate right half)

  Step 3: [1, 3, 5, 7, 9, 11, 13]
                       LR              nums[4]=9 == 9 --> Found!
                       M

  3 steps to find it in a 7-element array. log2(7) ~ 3. Math checks out!
```

### Search Space Halving Visualization

```
  n = 16 elements

  Step 1:  [////////////////]     16 candidates
  Step 2:  [////////]              8 candidates
  Step 3:  [////]                  4 candidates
  Step 4:  [//]                    2 candidates
  Step 5:  [/]                     1 candidate --> answer!

  Only 4-5 steps for 16 elements. That's O(log n).
```

## Minimal Python Template

### Pattern 1: Exact Match

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2   # avoids integer overflow

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1  # not found
```

### Pattern 2: Lower Bound (First Position >= Target)

```python
def lower_bound(nums, target):
    lo, hi = 0, len(nums)  # note: hi = len, not len-1

    while lo < hi:          # note: strict <, not <=
        mid = lo + (hi - lo) // 2

        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid        # mid could be the answer, don't skip it

    return lo  # lo == hi == first position where nums[i] >= target
```

### Pattern 3: Binary Search on Answer

```python
def search_on_answer(lo, hi):
    """
    When the answer itself is what you're binary searching for.
    Example: "What's the minimum speed to finish in H hours?"
    """
    while lo < hi:
        mid = lo + (hi - lo) // 2

        if condition_is_satisfied(mid):
            hi = mid        # mid works, but maybe something smaller works too
        else:
            lo = mid + 1    # mid doesn't work, need bigger

    return lo  # smallest value that satisfies the condition
```

## Step-by-Step Example (Tiny Input)

### Search Insert Position: nums = [1, 3, 5, 6], target = 4

Where should 4 be inserted to keep the array sorted?

```
Step 1: lo=0, hi=4 (one past end)
        mid = 2
        nums[2] = 5 >= 4   --> hi = 2

Step 2: lo=0, hi=2
        mid = 1
        nums[1] = 3 < 4    --> lo = 2

Step 3: lo=2, hi=2
        lo == hi --> stop!

Return lo = 2

Verify: [1, 3, *4*, 5, 6]  --> index 2 is correct!
```

### First and Last Position: nums = [5, 7, 7, 8, 8, 10], target = 8

```
Find first 8 (lower bound):
  lo=0, hi=6 --> mid=3, nums[3]=8  >= 8 --> hi=3
  lo=0, hi=3 --> mid=1, nums[1]=7  <  8 --> lo=2
  lo=2, hi=3 --> mid=2, nums[2]=7  <  8 --> lo=3
  lo=3, hi=3 --> return 3  (first 8 is at index 3)

Find first 9 (to get one past last 8):
  lo=0, hi=6 --> mid=3, nums[3]=8  <  9 --> lo=4
  lo=4, hi=6 --> mid=5, nums[5]=10 >= 9 --> hi=5
  lo=4, hi=5 --> mid=4, nums[4]=8  <  9 --> lo=5
  lo=5, hi=5 --> return 5

Last 8 = 5 - 1 = 4

Answer: [3, 4]
```

- **Input:** [5, 7, 7, 8, 8, 10], target = 8
- **Output:** [3, 4]

## Common Variations

1. **Exact Match** -- Classic binary search. Return index if found, -1 if not. Use `lo <= hi` with `lo = mid+1` and `hi = mid-1`.

2. **Lower Bound** -- Find the first position >= target. Use `lo < hi` with `hi = mid` (not `mid-1`). This is the most versatile template.

3. **Upper Bound** -- Find the first position > target. Same as lower_bound(target + 1). Or: find last position <= target using lower_bound then subtract 1.

4. **Search on Answer** -- The answer is a number in a range. Binary search on that range, checking if each candidate answer is feasible. Examples: Koko eating bananas, split array largest sum.

5. **Rotated Sorted Array** -- Array was sorted then rotated. One half is always sorted. Check which half target falls in, search that half.

## Top 5 Mistakes Beginners Make

1. **`lo <= hi` vs `lo < hi`.** For exact match, use `<=`. For lower/upper bound, use `<`. Mixing these up causes infinite loops or missed elements.

2. **`hi = mid` vs `hi = mid - 1`.** With `lo < hi` template, use `hi = mid` (mid might be the answer). With `lo <= hi` template, use `hi = mid - 1` (mid was already checked).

3. **Integer overflow in mid calculation.** Use `mid = lo + (hi - lo) // 2` instead of `mid = (lo + hi) // 2`. The second form can overflow in some languages (not Python, but good habit).

4. **Forgetting edge cases.** Empty array? Target smaller than all elements? Target larger than all elements? Always think about boundaries.

5. **Not identifying the monotonic property.** Binary search needs a clear "left side = no, right side = yes" (or vice versa) boundary. If you can't define this, binary search won't work.

## Complexity

- **Time:** O(log n) -- you halve the search space each step.
- **Space:** O(1) -- just a few variables (lo, hi, mid). No extra data structures.

## What To Say In Interview (Talk Track)

- "The array is sorted, so I'll use binary search for O(log n) time."
- "I'll maintain lo and hi pointers. At each step, I compute mid and decide whether to search the left half or right half."
- "For finding the first/last occurrence, I'll use the lower bound template where I don't immediately return on a match -- I keep narrowing to find the boundary."
- "For 'search on answer' problems, I'll binary search on the answer space itself, using a helper function to check if a candidate answer is feasible."
- "This gives us O(log n) time and O(1) space."
