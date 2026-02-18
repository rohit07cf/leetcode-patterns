# Two Pointers

## Baby Explanation (ELI10)

- Imagine you have a ruler with numbers written on it. You put one finger on the left end and one finger on the right end. Now you slowly walk your fingers toward each other.
- That's **Two Pointers!** You use two positions (pointers) to scan through data smartly instead of checking every possible pair.
- Without two pointers, finding a pair takes O(n^2) -- like comparing every kid in class with every other kid. With two pointers on a sorted array, it's O(n) -- one sweep and done.
- Think of it like squeezing a sponge from both sides. You narrow in on the answer from both ends.
- The BIG requirement: the array usually needs to be **sorted** for the opposite-direction version to work.
- There's also a same-direction version, like two people walking the same way at different speeds.

## Pattern Recognition

Use this when you see:
- "Sorted array" + "find a pair"
- "Two numbers that sum to..."
- "Remove duplicates in-place"
- "Container with most water" or "trapping rain water"
- "Is this string a palindrome?"
- Any problem where brute force would check all pairs

Avoid when:
- The array is NOT sorted and sorting would lose important info (like original indices)
- You need to find more than 2 elements (consider sorting + two pointers inside a loop)
- The problem is about subarrays/substrings (think Sliding Window instead)

## ASCII Diagram: Opposite Direction Pointers

```
  Problem: Find two numbers in sorted array that sum to 10
  Array: [1, 3, 5, 6, 8, 11]

  Step 1:  L                    R
           [1,  3,  5,  6,  8,  11]
           sum = 1 + 11 = 12 > 10  --> move R left

  Step 2:  L                R
           [1,  3,  5,  6,  8,  11]
           sum = 1 + 8 = 9 < 10    --> move L right

  Step 3:      L            R
           [1,  3,  5,  6,  8,  11]
           sum = 3 + 8 = 11 > 10   --> move R left

  Step 4:      L        R
           [1,  3,  5,  6,  8,  11]
           sum = 3 + 6 = 9 < 10    --> move L right

  Step 5:          L    R
           [1,  3,  5,  6,  8,  11]
           sum = 5 + 6 = 11 > 10   --> move R left

  Hmm, that gives sum=5+6=11. Move R left:

  Step 5b:         LR
           [1,  3,  5,  6,  8,  11]
           Pointers crossed --> no pair found!

  (If target were 11: step 3 would have returned [3, 8])
```

## Minimal Python Template

### Pattern 1: Opposite Direction (Sorted Array Pair)

```python
def two_pointer_pair(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1        # need bigger sum, move left forward
        else:
            right -= 1       # need smaller sum, move right back

    return []  # no pair found
```

### Pattern 2: Same Direction (Remove Duplicates)

```python
def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0  # slow pointer marks the "write" position

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1  # length of unique portion
```

### Pattern 3: Container With Most Water

```python
def max_area(height):
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        best = max(best, width * h)

        if height[left] < height[right]:
            left += 1       # move the shorter side inward
        else:
            right -= 1

    return best
```

## Step-by-Step Example (Tiny Input)

### Remove Duplicates: nums = [1, 1, 2, 3, 3]

```
  slow
   v
  [1, 1, 2, 3, 3]
      ^
     fast

  fast=1: nums[1]=1 == nums[0]=1  --> skip (duplicate)

  fast=2: nums[2]=2 != nums[0]=1  --> slow=1, nums[1]=2
     slow
      v
  [1, 2, 2, 3, 3]
         ^
        fast

  fast=3: nums[3]=3 != nums[1]=2  --> slow=2, nums[2]=3
        slow
         v
  [1, 2, 3, 3, 3]
            ^
           fast

  fast=4: nums[4]=3 == nums[2]=3  --> skip (duplicate)

  Result: first 3 elements = [1, 2, 3], return slow+1 = 3
```

- **Input:** [1, 1, 2, 3, 3]
- **Walkthrough:** Slow pointer only moves when we find a new unique value. Fast pointer scans every element.
- **Output:** 3 (the array is modified in-place to [1, 2, 3, ...])

## Common Variations

1. **Opposite Direction** -- Two pointers start at ends, move inward. Used for: pair sum in sorted array, palindrome check, container with most water.

2. **Same Direction (Fast/Slow)** -- Both start at the beginning. Fast scans ahead, slow writes or marks position. Used for: remove duplicates, remove element, move zeroes.

3. **Three Sum** -- Sort the array, fix one number with a loop, then use two pointers for the remaining pair. Combines iteration + two pointers.

4. **Palindrome Check** -- Left pointer at start, right pointer at end. Compare characters moving inward. If all match, it's a palindrome.

5. **Trapping Rain Water** -- Two pointers from both ends, tracking max heights. Water at each position = min(left_max, right_max) - height.

## Top 5 Mistakes Beginners Make

1. **Forgetting to sort first.** Opposite-direction two pointers only works on sorted arrays. If the problem gives unsorted input, sort it first (but watch out -- sorting loses original indices).

2. **Using `left <= right` instead of `left < right`.** If both pointers can be at the same index, you might double-count an element. Use strict `<` for pairs.

3. **Not handling duplicates in Three Sum.** After finding a valid triplet, skip over duplicate values to avoid duplicate answers: `while left < right and nums[left] == nums[left+1]: left += 1`.

4. **Moving the wrong pointer.** If the sum is too small, move the LEFT pointer right (to get a bigger number). If the sum is too big, move the RIGHT pointer left. Mixing these up is an easy bug.

5. **Forgetting edge cases.** What if the array has 0 or 1 element? Always handle empty/tiny inputs at the top of your function.

## Complexity

- **Time:** O(n) for most two-pointer problems (single pass). O(n log n) if you need to sort first. O(n^2) for Three Sum (loop + two pointers).
- **Space:** O(1) extra space -- that's the beauty of two pointers! (Unless sorting counts, which is O(log n) for most sort implementations.)

## What To Say In Interview (Talk Track)

- "Since the array is sorted, I can use two pointers starting from opposite ends to find the pair in O(n) time."
- "If the current sum is too small, I move the left pointer right to increase it. If too large, I move the right pointer left."
- "This avoids the O(n^2) brute force of checking every pair."
- "For the in-place variant, I'll use a slow/fast pointer approach where the slow pointer tracks where to write the next valid element."
- "The space complexity is O(1) since I only need two pointer variables."
