# Longest Increasing Subsequence (LIS) and Sequence DP

## Baby Explanation (ELI10)

- Imagine you have a hand of cards with random numbers. You want to pick some
  cards (keeping their order) so the numbers go up: 2, 5, 8, 12...
  What is the LONGEST chain you can pick? That is LIS.
- A **subsequence** is NOT the same as a subarray. A subsequence can skip
  elements, but the order must stay the same.
- LCS (Longest Common Subsequence) is similar: given TWO sequences, find
  the longest subsequence that appears in BOTH.
- These are classic FAANG interview favorites. Learn them cold.

```
  Array: [10, 9, 2, 5, 3, 7, 101, 18]

  Subsequence [2, 5, 7, 101] -- valid (increasing, keeps order)
  Subsequence [2, 5, 7, 18]  -- also valid, same length = 4
  Length of LIS = 4
```

## Pattern Recognition

Use this when you see:
- "Longest increasing/decreasing subsequence"
- "Longest common subsequence of two strings/arrays"
- "Minimum deletions to make sorted"
- "Number of increasing subsequences"
- "Longest chain / Russian doll envelopes"

Avoid when:
- "Longest substring" (contiguous -- use sliding window or different DP)
- The problem is about contiguous subarrays (use Kadane's)

---

## Problem 1: Longest Increasing Subsequence (LeetCode 300)

### Approach A: O(n^2) DP (Easy to Understand)

#### State, Transition, Base Case

```
  State:      dp[i] = length of LIS ending at index i
  Transition: dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
              (look at all previous elements; if smaller, extend that chain)
  Base case:  dp[i] = 1 for all i (every element alone is a subsequence of length 1)
  Answer:     max(dp)
```

#### Step-by-Step Example

- Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]

```
  Index:    0    1    2    3    4    5    6     7
  nums:   [10] [ 9] [ 2] [ 5] [ 3] [ 7] [101] [18]
  dp:     [ 1] [ 1] [ 1] [ 1] [ 1] [ 1] [  1] [ 1]  (all start at 1)

  i=0: no j before it.                dp[0] = 1
  i=1: nums[0]=10 > 9? No.            dp[1] = 1
  i=2: nums[0]=10 > 2? No. nums[1]=9 > 2? No.   dp[2] = 1
  i=3: j=0: 10>5? No. j=1: 9>5? No. j=2: 2<5? YES -> dp[2]+1=2
       dp[3] = 2
  i=4: j=2: 2<3? YES -> dp[2]+1=2.   dp[4] = 2
  i=5: j=2: 2<7 -> 2. j=3: 5<7 -> 3. j=4: 3<7 -> 3.   dp[5] = 3
  i=6: j=0: 10<101 -> 2. j=3: 5<101 -> 3. j=5: 7<101 -> 4.
       dp[6] = 4
  i=7: j=2: 2<18 -> 2. j=3: 5<18 -> 3. j=5: 7<18 -> 4.
       dp[7] = 4

  dp:     [ 1] [ 1] [ 1] [ 2] [ 2] [ 3] [  4] [ 4]
```

- Output: max(dp) = 4

#### Code (O(n^2))

```python
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
```

**Time:** O(n^2) | **Space:** O(n)

---

### Approach B: O(n log n) with Binary Search (Patience Sorting)

This is faster and often expected at FAANG interviews.

**Idea:** Maintain an array `tails` where tails[k] = the smallest ending
element of any increasing subsequence of length k+1.

```
  For each number:
    - If it is bigger than all tails, append it (extends longest chain).
    - Otherwise, find the first tail >= num and replace it (keeps tails small).

  The length of tails at the end = length of LIS.
```

#### Walkthrough

- Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]

```
  Process 10:   tails = [10]          (start new chain)
  Process 9:    tails = [9]           (9 replaces 10 -- smaller is better)
  Process 2:    tails = [2]           (2 replaces 9)
  Process 5:    tails = [2, 5]        (5 > 2, extend!)
  Process 3:    tails = [2, 3]        (3 replaces 5)
  Process 7:    tails = [2, 3, 7]     (7 > 3, extend!)
  Process 101:  tails = [2, 3, 7, 101] (101 > 7, extend!)
  Process 18:   tails = [2, 3, 7, 18]  (18 replaces 101)
```

- LIS length = len(tails) = 4

**Note:** tails is NOT the actual LIS! It just tells you the length.

#### Code (O(n log n))

```python
import bisect

def lengthOfLIS(nums):
    tails = []

    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)       # extends the longest chain
        else:
            tails[pos] = num        # replace to keep tails small

    return len(tails)
```

**Time:** O(n log n) | **Space:** O(n)

---

## Problem 2: Longest Common Subsequence (LeetCode 1143)

**The question:** Given two strings, find the length of their longest
common subsequence.

### Baby Explanation

You and your friend each wrote a sentence. A common subsequence is a
sequence of letters that appears in BOTH sentences (in order, but not
necessarily next to each other). Find the longest one.

### State, Transition, Base Case

```
  State:      dp[i][j] = LCS of text1[0..i-1] and text2[0..j-1]
  Transition: if text1[i-1] == text2[j-1]:
                  dp[i][j] = dp[i-1][j-1] + 1     (match! extend it)
              else:
                  dp[i][j] = max(dp[i-1][j], dp[i][j-1])  (skip one char)
  Base case:  dp[0][j] = 0, dp[i][0] = 0  (empty string has LCS = 0)
```

### Step-by-Step Example

- Input: text1 = "abcde", text2 = "ace"

```
         ""   a    c    e
    ""  [ 0] [ 0] [ 0] [ 0]
    a   [ 0] [ 1] [ 1] [ 1]    a matches a -> 0+1=1
    b   [ 0] [ 1] [ 1] [ 1]    b matches nothing new
    c   [ 0] [ 1] [ 2] [ 2]    c matches c -> 1+1=2
    d   [ 0] [ 1] [ 2] [ 2]    d matches nothing new
    e   [ 0] [ 1] [ 2] [ 3]    e matches e -> 2+1=3
```

- Output: 3 (the LCS is "ace")

### Code

```python
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
```

**Time:** O(m * n) | **Space:** O(m * n), or O(n) with rolling array

---

## ASCII: How Subsequence Selection Works

```
  Array:  3   1   8   2   5

  Pick subsequence [1, 2, 5]:

  3   1   8   2   5
      ^       ^   ^       <-- picked these (in order, skip some)
      1       2   5       <-- increasing!

  This is a valid increasing subsequence of length 3.
```

## Common Variations

| Problem                        | Key Idea                              |
|--------------------------------|---------------------------------------|
| LIS (Longest Increasing Subseq)| dp[i] = best ending at i             |
| LCS (Longest Common Subseq)   | 2D DP on two strings                  |
| Longest Common Substring       | Like LCS but must be contiguous       |
| Min deletions to sort          | n - LIS length                        |
| Russian Doll Envelopes         | Sort + LIS                            |
| Number of LIS                  | Track count alongside length          |
| Longest Palindromic Subseq     | LCS of string and its reverse         |

## Top 5 Mistakes Beginners Make

1. **Confusing subsequence and substring.** Subsequence can skip, substring cannot.
2. **Forgetting the answer is max(dp), not dp[-1].** For LIS the best might not end last.
3. **Not sorting before LIS in envelope problems.** Sort by width, then LIS on height.
4. **Off-by-one with dp size in LCS.** dp is (m+1) x (n+1), not m x n.
5. **Using O(n^2) LIS when O(n log n) is expected.** Know both approaches.

## Complexity (Time + Space)

| Problem | Approach     | Time        | Space   |
|---------|-------------|-------------|---------|
| LIS     | DP          | O(n^2)     | O(n)    |
| LIS     | Binary Srch | O(n log n) | O(n)    |
| LCS     | 2D DP       | O(m * n)   | O(m*n)  |
| LCS     | Optimized   | O(m * n)   | O(n)    |

## What To Say In Interview (Talk Track)

> "For LIS, I will start with the O(n^2) DP where dp[i] is the length of
> the longest increasing subsequence ending at index i. The transition
> checks all j < i where nums[j] < nums[i]. I can optimize to O(n log n)
> using a tails array and binary search -- this is called patience sorting."
>
> "For LCS, my state dp[i][j] represents the LCS of the first i characters
> of text1 and first j characters of text2. If characters match, I extend
> from the diagonal. Otherwise, I take the max of skipping either character."
