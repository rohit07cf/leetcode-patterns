# Dynamic Programming (DP) Cheat Sheet

> DP is just recursion + remembering answers you already computed. That is it.

---

## The 4-Step DP Recipe (Follow This Every Time)

```
Step 1: Define the STATE
   - What changes? What parameters describe a subproblem?
   - "dp[i] = the answer for the first i elements"

Step 2: Define the RECURRENCE (transition)
   - How does dp[i] relate to smaller subproblems?
   - "dp[i] = max(dp[i-1], dp[i-2] + nums[i])"

Step 3: Define the BASE CASE
   - What is the smallest subproblem you can solve directly?
   - "dp[0] = 0" or "dp[0] = nums[0]"

Step 4: Define the ANSWER
   - Where in the dp table is your final answer?
   - "return dp[n]" or "return max(dp)"
```

---

## State Definition Checklist

| # | Ask Yourself | Example |
|---|-------------|---------|
| 1 | What parameters change between subproblems? | Index i, remaining capacity, etc. |
| 2 | What does dp[i] represent? | "Max profit using first i items" |
| 3 | What is the base case? | dp[0] = 0 (no items = no profit) |
| 4 | What is the recurrence? | dp[i] = max(take, skip) |
| 5 | What is the fill order? | Left to right? Bottom-up? |
| 6 | Where is the final answer? | dp[n], dp[n][W], max(dp), etc. |

---

## Memoization vs Tabulation

| | Memoization (Top-Down) | Tabulation (Bottom-Up) |
|---|---|---|
| Approach | Recursion + cache | Iterative + table |
| Start from | Big problem -> small | Small problem -> big |
| Easier to write? | Yes (just add cache) | Sometimes trickier |
| Speed | Slight overhead (recursion) | Usually faster |
| Space optimize? | Harder | Easier |
| Stack overflow? | Possible for deep recursion | No |

**Tip:** Start with memoization (easier to think about), convert to tabulation if needed.

---

## 1D DP Template

```python
# Use when: answer depends on previous 1 or 2 states
# Examples: climbing stairs, house robber, fibonacci

def solve(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]                        # base case
    for i in range(1, n):
        dp[i] = max(dp[i-1], ...)          # recurrence
    return dp[n-1]
```

### Space-Optimized 1D DP (When You Only Need Last 1-2 Values)

```python
def solve(nums):
    prev2, prev1 = 0, nums[0]
    for i in range(1, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, curr
    return prev1
```

---

## 2D DP Template

```python
# Use when: two changing parameters (two strings, grid, etc.)
# Examples: LCS, edit distance, grid paths

def solve(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # base cases
    for i in range(m + 1):
        dp[i][0] = ...
    for j in range(n + 1):
        dp[0][j] = ...

    # fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = ...                  # recurrence

    return dp[m][n]
```

---

## 0/1 Knapsack Template

```
Problem: n items, each with weight and value. Max capacity W.
Each item: take it once or skip it.
State: dp[i][w] = max value using first i items with capacity w
```

```python
def knapsack_01(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i-1][w]                          # skip item
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w],
                    dp[i-1][w - weights[i-1]] + values[i-1]) # take item
    return dp[n][W]
```

### Space-Optimized 0/1 Knapsack (1D array, iterate w backwards!)

```python
def knapsack_01_optimized(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):    # BACKWARDS!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]
```

---

## Unbounded Knapsack Template

```
Same as 0/1, but you can take each item UNLIMITED times.
Only difference: iterate w FORWARDS (not backwards).
```

```python
def knapsack_unbounded(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for w in range(weights[i], W + 1):          # FORWARDS!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]
```

| Knapsack Type | Inner Loop Direction | Why |
|---------------|---------------------|-----|
| 0/1 (pick once) | **Backwards** | Prevents using same item twice |
| Unbounded (pick many) | **Forwards** | Allows reusing items |

---

## Longest Increasing Subsequence (LIS)

### O(n^2) Solution

```python
def lis(nums):
    n = len(nums)
    dp = [1] * n                            # every element is a subsequence of length 1
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

### O(n log n) Solution (Binary Search)

```python
import bisect

def lis_fast(nums):
    tails = []                              # smallest tail for each length
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)               # extend longest subsequence
        else:
            tails[pos] = num                # replace with smaller value
    return len(tails)
```

---

## Longest Common Subsequence (LCS)

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1       # match: extend
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # skip one
    return dp[m][n]
```

---

## Tree DP Template

```python
# Use when: optimal value for tree, max path, house robber on tree
def tree_dp(root):
    def dfs(node):
        if not node:
            return (0, 0)                   # (take_this_node, skip_this_node)
        left = dfs(node.left)
        right = dfs(node.right)
        take = node.val + left[1] + right[1]   # take node, must skip children
        skip = max(left) + max(right)           # skip node, free to take/skip children
        return (take, skip)
    return max(dfs(root))
```

---

## Quick Reference: Pattern -> State -> Transition

| Pattern | State dp[i] means... | Recurrence |
|---------|---------------------|------------|
| Fibonacci / Stairs | Ways to reach step i | dp[i] = dp[i-1] + dp[i-2] |
| House Robber | Max money from first i houses | dp[i] = max(dp[i-1], dp[i-2]+nums[i]) |
| Coin Change | Min coins for amount i | dp[i] = min(dp[i-c]+1) for each coin c |
| 0/1 Knapsack | Max value with capacity w | dp[w] = max(skip, take) |
| LCS | LCS length of s1[:i], s2[:j] | Match: +1, else max(skip one) |
| LIS | Length of LIS ending at i | dp[i] = max(dp[j]+1) for j < i |
| Edit Distance | Min ops for s1[:i] -> s2[:j] | Match: dp[i-1][j-1], else 1+min(...) |
| Grid Paths | Ways to reach cell (i,j) | dp[i][j] = dp[i-1][j] + dp[i][j-1] |
| Partition Equal Subset | Can we make sum s with first i nums? | dp[s] = dp[s] or dp[s-nums[i]] |
| Word Break | Can we segment s[:i]? | dp[i] = any(dp[j] and s[j:i] in dict) |
| Palindrome Partition | Min cuts for s[:i] | dp[i] = min(dp[j]+1) if s[j:i] is palindrome |
| Stock Buy/Sell | Max profit at day i with state | Depends on variant (k transactions, cooldown, etc.) |

---

## Space Optimization Tricks

| Original | Optimized | When |
|----------|-----------|------|
| dp[n] array | Two variables prev1, prev2 | Only need last 1-2 rows |
| dp[m][n] grid | dp[n] single row | Only need previous row |
| dp[n][W] knapsack | dp[W] single row | 0/1: backward, unbounded: forward |

**The trick:** Ask "which previous cells do I actually read?" If only the last row, keep one row.

---

## Common Mistakes to Avoid

1. Forgetting base cases (dp[0] = ?)
2. Off-by-one errors on table size (usually need n+1)
3. Wrong loop direction in knapsack (backwards vs forwards)
4. Not considering "skip this item" option
5. Returning dp[n] vs dp[n-1] vs max(dp) -- know where your answer is
6. Memoization: forgetting to actually return the cached value

---

## The "Is This DP?" Checklist

- Can I break it into overlapping subproblems? -> DP
- Does it ask for min/max/count of ways? -> Probably DP
- Does it say "how many ways"? -> DP (count)
- Does it say "minimum cost / maximum profit"? -> DP (optimization)
- Does it involve making choices at each step? -> DP
- Is there a greedy approach that works? -> Maybe NOT DP (try greedy first)

**DP is not magic. It is just smart recursion. Define your state, write your recurrence, and fill the table. You can do this.**
