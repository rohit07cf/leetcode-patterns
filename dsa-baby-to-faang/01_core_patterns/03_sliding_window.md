# Sliding Window

## Baby Explanation (ELI10)

- Imagine you have a magnifying glass and a long sentence on paper. You slide the magnifying glass across the sentence, looking at a few words at a time.
- That's a **Sliding Window!** Instead of recalculating everything from scratch each time, you slide a "window" across the data and just update what changed.
- **Fixed window:** Your magnifying glass is always the same size (like "look at exactly 3 letters at a time").
- **Variable window:** Your magnifying glass can grow and shrink (like "find the smallest group of letters that contains all vowels").
- The trick is: when the window slides right, you ADD the new element on the right and REMOVE the old element on the left. No need to re-examine the whole window!
- This turns O(n*k) brute force into O(n). Huge speedup.

## Pattern Recognition

Use this when you see:
- "Maximum/minimum sum of subarray of size k"
- "Longest/shortest substring with some condition"
- "Contiguous subarray" or "contiguous substring"
- "At most K distinct characters"
- The words "subarray" or "substring" (NOT subsequence!)

Avoid when:
- The problem says "subsequence" (elements don't need to be contiguous)
- You need to compare all pairs, not contiguous groups
- The data isn't in a sequence (like a tree or graph)

## ASCII Diagram: Sliding Window

### Fixed Window (size k=3)

```
  Array: [2, 1, 5, 1, 3, 2]

  Window 1:  [2, 1, 5] 1, 3, 2    sum = 8
              --------
  Window 2:   2 [1, 5, 1] 3, 2    sum = 8 - 2 + 1 = 7
                 --------
  Window 3:   2, 1 [5, 1, 3] 2    sum = 7 - 1 + 3 = 9  <-- max!
                    --------
  Window 4:   2, 1, 5 [1, 3, 2]   sum = 9 - 5 + 2 = 6
                       --------

  Instead of summing 3 numbers each time (O(k)),
  we just subtract the leaving element and add the entering one (O(1)).
```

### Variable Window (shrink when condition breaks)

```
  String: "abcabcbb"   Goal: longest substring without repeating chars

  Step 1:  [a] b c a b c b b         window="a"      len=1
  Step 2:  [a b] c a b c b b         window="ab"     len=2
  Step 3:  [a b c] a b c b b         window="abc"    len=3
  Step 4:   a [b c a] b c b b        window="bca"    len=3
            ^ shrink! 'a' repeated    (removed left 'a')
  Step 5:   a  b [c a b] c b b       window="cab"    len=3
  Step 6:   a  b  c [a b c] b b      window="abc"    len=3
  Step 7:   a  b  c  a [b c b] b     ... keep going
            shrink as needed...

  Answer: 3 ("abc")
```

## Minimal Python Template

### Pattern 1: Fixed-Size Window

```python
def max_sum_subarray(nums, k):
    # Build the first window
    window_sum = sum(nums[:k])
    best = window_sum

    # Slide the window: remove left, add right
    for i in range(k, len(nums)):
        window_sum += nums[i]       # add new element entering window
        window_sum -= nums[i - k]   # remove old element leaving window
        best = max(best, window_sum)

    return best
```

### Pattern 2: Variable-Size Window

```python
def longest_substring_no_repeat(s):
    seen = {}       # char -> most recent index
    left = 0
    best = 0

    for right in range(len(s)):
        char = s[right]

        # If char is a repeat inside our current window, shrink
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right
        best = max(best, right - left + 1)

    return best
```

### Pattern 3: Variable Window with Frequency Map

```python
def min_window_substring(s, t):
    from collections import Counter

    need = Counter(t)       # characters we need
    missing = len(t)        # how many chars still missing
    left = 0
    best_start, best_len = 0, float('inf')

    for right in range(len(s)):
        # Expand: add s[right] to window
        if need[s[right]] > 0:
            missing -= 1
        need[s[right]] -= 1

        # Shrink: try to make window smaller
        while missing == 0:
            # Update best
            if right - left + 1 < best_len:
                best_start = left
                best_len = right - left + 1

            # Remove s[left] from window
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    return "" if best_len == float('inf') else s[best_start:best_start + best_len]
```

## Step-by-Step Example (Tiny Input)

### Max Sum Subarray of Size k=3: nums = [2, 1, 5, 1, 3, 2]

```
Build first window:  sum(nums[0:3]) = 2+1+5 = 8
best = 8

i=3: window_sum = 8 + nums[3] - nums[0] = 8 + 1 - 2 = 7
     best = max(8, 7) = 8

i=4: window_sum = 7 + nums[4] - nums[1] = 7 + 3 - 1 = 9
     best = max(8, 9) = 9

i=5: window_sum = 9 + nums[5] - nums[2] = 9 + 2 - 5 = 6
     best = max(9, 6) = 9
```

- **Input:** [2, 1, 5, 1, 3, 2], k=3
- **Walkthrough:** Slide a window of size 3 across the array, keeping a running sum.
- **Output:** 9 (from subarray [5, 1, 3])

## Common Variations

1. **Fixed Window** -- Window size is given (k). Slide across, update by adding/removing one element. Examples: max sum subarray of size k, max average subarray.

2. **Variable Window (grow/shrink)** -- No fixed size. Expand the right side, shrink the left side when a condition breaks. Examples: longest substring without repeating characters, minimum size subarray sum.

3. **Variable Window with Hash Map** -- Track character frequencies inside the window with a hash map. Examples: minimum window substring, longest substring with at most K distinct characters, permutation in string.

4. **Sliding Window Maximum** -- Find the max in each window position. Uses a deque (monotonic queue) to track candidates. This is the hard variant.

5. **Count Subarrays** -- Count how many subarrays meet a condition. Often uses the trick: at_most(k) - at_most(k-1) = exactly(k).

## Top 5 Mistakes Beginners Make

1. **Re-computing the whole window every time.** The whole point of sliding window is incremental updates. If you're using a loop inside a loop to sum the window, you're doing it wrong.

2. **Off-by-one on window size.** The window from index `left` to `right` has size `right - left + 1`. Forgetting the `+1` is a classic bug.

3. **Forgetting to shrink the window.** In variable-size problems, you MUST shrink from the left when the window becomes invalid. If you only expand, you'll get wrong answers.

4. **Not initializing the first window correctly.** For fixed-size windows, build the first window of size k separately, then start sliding from index k.

5. **Confusing subarray vs. subsequence.** Sliding window works for **contiguous** subarrays/substrings only. If the problem asks for subsequences (non-contiguous), you need a different approach (like dynamic programming).

## Complexity

- **Time:** O(n) -- each element enters the window once and leaves once.
- **Space:** O(1) for fixed window with just a sum. O(k) or O(alphabet size) when using a hash map to track window contents.

## What To Say In Interview (Talk Track)

- "This is a subarray/substring problem, so I'll use a sliding window approach."
- "For the fixed-size version: I'll build the initial window, then slide it by adding the new right element and removing the old left element."
- "For the variable-size version: I'll expand the right pointer, and shrink from the left whenever the window condition is violated."
- "Each element enters and leaves the window at most once, giving us O(n) total time."
- "I'll use a hash map to track character frequencies inside the window."
