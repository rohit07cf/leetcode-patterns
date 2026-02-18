# DP Interview Recipes: Quick Reference

## The 4-Step DP Recipe (Use This EVERY Time)

```
  STEP 1: DEFINE THE STATE
     "dp[i] represents ____."
     What info do I need to describe where I am?
          |
          v
  STEP 2: WRITE THE RECURRENCE (TRANSITION)
     "dp[i] = formula using dp[smaller]"
     How does dp[i] relate to smaller states?
          |
          v
  STEP 3: SET BASE CASES
     "dp[0] = ____, dp[1] = ____"
     Smallest version where I already know the answer?
          |
          v
  STEP 4: DETERMINE FILL ORDER + ANSWER LOCATION
     Left to right? Bottom to top?
     Is the answer dp[n], max(dp), or dp[m][n]?
```

---

## The Master "If You See X, Try Y" Table

```
 -----------------------------------------------------------------
 | IF YOU SEE THIS...           | TRY THIS PATTERN               |
 |------------------------------|---------------------------------|
 | "How many ways to reach..."  | 1D DP (Climbing Stairs style)   |
 | "Min/max along a sequence"   | 1D DP (House Robber / Kadane)   |
 | "Grid, top-left to bottom-right" | 2D Grid DP                 |
 | "Two strings, transform one" | 2D String DP (Edit Distance)    |
 | "Pick items under capacity"  | 0/1 Knapsack                   |
 | "Unlimited items, make target"| Unbounded Knapsack             |
 | "Can you partition into..."  | Subset Sum (0/1 Knapsack)       |
 | "Longest increasing..."      | LIS (O(n^2) or O(n log n))     |
 | "Common subsequence of two"  | LCS (2D DP)                     |
 | "Max/min on a tree"          | Tree DP (DFS returns values)    |
 | "Palindrome substring/subseq"| 2D DP or expand from center     |
 | "Break into words"           | 1D DP (Word Break)              |
 | "Decode/decode ways"         | 1D DP                           |
 | "Buy and sell stock"         | State machine DP                |
 -----------------------------------------------------------------
```

---

## Pattern to Template Mapping

### 1D DP Template

```python
def solve_1d(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = base
    for i in range(1, n):
        dp[i] = f(dp[i-1], dp[i-2], nums[i])   # transition
    return dp[n-1]   # or max(dp)
```

### 2D Grid Template

```python
def solve_grid(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for j in range(1, n): dp[0][j] = dp[0][j-1] + grid[0][j]  # first row
    for i in range(1, m): dp[i][0] = dp[i-1][0] + grid[i][0]  # first col
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = combine(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[m-1][n-1]
```

### 0/1 Knapsack Template

```python
def knapsack_01(weights, values, cap):
    dp = [0] * (cap + 1)
    for i in range(len(weights)):
        for w in range(cap, weights[i]-1, -1):     # BACKWARD
            dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
    return dp[cap]
```

### Unbounded Knapsack Template

```python
def knapsack_unbounded(weights, values, cap):
    dp = [0] * (cap + 1)
    for i in range(len(weights)):
        for w in range(weights[i], cap+1):          # FORWARD
            dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
    return dp[cap]
```

### LIS Template (O(n^2))

```python
def lis(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

### LIS Template (O(n log n))

```python
import bisect
def lis_fast(nums):
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails): tails.append(num)
        else: tails[pos] = num
    return len(tails)
```

### LCS Template

```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

### Tree DP Template

```python
def tree_dp(root):
    best = 0
    def dfs(node):
        nonlocal best
        if not node: return 0
        left = dfs(node.left)
        right = dfs(node.right)
        best = max(best, combine(left, right, node.val))
        return value_for_parent(left, right, node.val)
    dfs(root)
    return best
```

---

## State Definition Checklist

When defining your state, ask:

```
  [ ] What variable(s) change as I move through the problem?
  [ ] Is one variable enough (1D) or do I need two (2D)?
  [ ] Does dp[i] represent: a count? a max? a min? True/False?
  [ ] Can I clearly say "dp[i] represents ____" in one sentence?
  [ ] Does my state capture enough info to make the next decision?
```

## Transition Writing Tips

```
  1. Start with the CHOICE at each step.
     "At step i, I can either _____ or _____."

  2. Write the recurrence for each choice.
     "If I choose A: dp[i] = dp[i-1] + something"
     "If I choose B: dp[i] = dp[i-2] + something else"

  3. Combine with min/max/sum depending on what the problem asks.
     "Find maximum" --> dp[i] = max(choice_A, choice_B)
     "Count ways"   --> dp[i] = choice_A + choice_B
     "Is possible"  --> dp[i] = choice_A or choice_B
```

---

## Space Optimization Techniques

```
  TECHNIQUE 1: Two Variables (for 1D DP)
  When dp[i] only depends on dp[i-1] and dp[i-2]:
    prev2, prev1 = base0, base1
    for i in range(2, n+1):
        curr = f(prev1, prev2)
        prev2, prev1 = prev1, curr
    O(n) space --> O(1) space

  TECHNIQUE 2: Rolling Array (for 2D DP)
  When dp[i][j] only depends on dp[i-1][...]:
    Keep only prev_row and curr_row.
    O(m*n) space --> O(n) space

  TECHNIQUE 3: In-Place (for grid DP)
  If you are allowed to modify the input grid:
    Use the grid itself as the dp table.
    O(m*n) space --> O(1) extra space
```

---

## How to Present DP in an Interview

```
  1. IDENTIFY (30s):  "This has overlapping subproblems, so I will use DP."
  2. STATE (30s):     "dp[i] represents [meaning]."
  3. TRANSITION (1m): "dp[i] = [formula] because at step i I can [A] or [B]."
  4. BASE CASE (20s): "dp[0] = [value] because [reason]."
  5. TRACE (2m):      Walk through a small example, fill the table on the board.
  6. CODE (5m):       Write clean code. Mention space optimization at the end.
  7. COMPLEXITY (20s):"Time O(...), space O(...), optimizable to O(...)."
```

---

## Top 10 DP Problems for FAANG Interviews

Sorted by frequency and pattern:

```
  MUST KNOW (appear constantly):
  1.  Climbing Stairs          (1D DP, warm-up)
  2.  House Robber             (1D DP, skip constraint)
  3.  Coin Change              (Unbounded Knapsack)
  4.  Longest Increasing Subseq (LIS)
  5.  Unique Paths             (2D Grid DP)

  HIGH FREQUENCY:
  6.  Word Break               (1D DP + hash set)
  7.  Longest Common Subseq    (2D String DP)
  8.  Edit Distance            (2D String DP)
  9.  Maximum Subarray         (Kadane's / 1D DP)
  10. Partition Equal Subset Sum (0/1 Knapsack)
```

## Common DP Problems Grouped by Pattern

```
  1D DP:        Climbing Stairs, House Robber, Decode Ways, Word Break
  2D Grid:      Unique Paths, Min Path Sum, Dungeon Game, Maximal Square
  2D String:    Edit Distance, LCS, Longest Palindromic Subsequence
  0/1 Knapsack: Partition Equal Subset, Target Sum, Last Stone Weight II
  Unbounded:    Coin Change, Coin Change II, Perfect Squares
  LIS/Sequence: LIS, Russian Doll Envelopes, Longest String Chain
  Tree DP:      Diameter, House Robber III, Max Path Sum, Binary Tree Cameras
  Interval:     Burst Balloons, Matrix Chain, Palindrome Partitioning II
  State Machine: Best Time to Buy/Sell Stock (all variations)
```

---

## Quick Debugging Checklist

When your DP solution gives wrong answers:

```
  [ ] Is dp array the right size? (n vs n+1?)
  [ ] Are base cases correct? (trace by hand)
  [ ] Is the fill order correct? (do dependencies exist when you need them?)
  [ ] Is the answer in the right cell? (dp[n]? dp[m][n]? max(dp)?)
  [ ] Off-by-one? (is i starting at 0 or 1?)
  [ ] For knapsack: backward for 0/1, forward for unbounded?
  [ ] Edge cases: empty input? single element? all same values?
```

## Final Words

DP feels hard at first. That is normal. The secret:

```
  1. Learn the patterns (this chapter).
  2. Practice 2-3 problems per pattern.
  3. Always start with the 4-step recipe.
  4. Trace small examples on paper BEFORE coding.
  5. After 30-40 problems, DP will click. Trust the process.
```

You are not memorizing solutions. You are learning to RECOGNIZE patterns
and apply recipes. That skill transfers to any new DP problem you see.
