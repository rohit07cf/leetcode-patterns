# 1D Dynamic Programming Basics

## Baby Explanation (ELI10)

- 1D DP means your answer depends on ONE thing that changes (like a position in a list).
- You build a single row of answers: dp[0], dp[1], dp[2], ... dp[n].
- Each box in the row is filled using boxes you already filled. Like dominoes!
- Think of it as walking along a straight road. At each step you decide
  the best thing to do based on what happened at previous steps.

## Pattern Recognition

Use this when you see:
- A list/array and you need to find min/max/count from start to end
- "How many ways to reach step N?"
- "Maximum sum/profit with some constraint along a sequence"
- The answer at position i depends only on previous positions

Avoid when:
- The problem involves a 2D grid (use 2D DP)
- You need to track two changing things like (index, capacity)
- The problem asks you to print ALL solutions (use backtracking)

## The 1D DP Template

```python
def solve(nums):
    n = len(nums)
    dp = [0] * n              # Step 1: Create the table

    dp[0] = base_value        # Step 2: Base case(s)

    for i in range(1, n):     # Step 3: Fill left to right
        dp[i] = transition    # Step 4: Use previous dp values

    return dp[n - 1]          # (or max(dp), or dp[target])
```

---

## Problem 1: Climbing Stairs (LeetCode 70)

**The question:** You are climbing a staircase with n steps.
Each time you can climb 1 or 2 steps. How many distinct ways to reach the top?

### Baby Explanation

Imagine a toddler going up stairs. At each step, they can take
a baby step (1) or a big step (2). How many different ways can they walk up?

### State, Transition, Base Case

```
  State:      dp[i] = number of ways to reach step i
  Transition: dp[i] = dp[i-1] + dp[i-2]
              (come from one step below OR two steps below)
  Base case:  dp[0] = 1 (one way to stand at ground)
              dp[1] = 1 (one way to reach step 1)
```

### Step-by-Step Example

- Input: n = 5

```
  Step:    0    1    2    3    4    5
  dp:     [1]  [1]  [ ]  [ ]  [ ]  [ ]

  i=2: dp[2] = dp[1] + dp[0] = 1 + 1 = 2
  dp:     [1]  [1]  [2]  [ ]  [ ]  [ ]

  i=3: dp[3] = dp[2] + dp[1] = 2 + 1 = 3
  dp:     [1]  [1]  [2]  [3]  [ ]  [ ]

  i=4: dp[4] = dp[3] + dp[2] = 3 + 2 = 5
  dp:     [1]  [1]  [2]  [3]  [5]  [ ]

  i=5: dp[5] = dp[4] + dp[3] = 5 + 3 = 8
  dp:     [1]  [1]  [2]  [3]  [5]  [8]
```

- Output: 8

### Code

```python
def climbStairs(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

**Time:** O(n) | **Space:** O(n), or O(1) with two variables.

---

## Problem 2: House Robber (LeetCode 198)

**The question:** You are a robber. Houses are in a row. Each has some money.
You CANNOT rob two houses next to each other (alarm goes off!).
What is the maximum money you can rob?

### Baby Explanation

Imagine picking candies from a line, but you can never pick two candies
sitting right next to each other. How do you pick the most candy?

### State, Transition, Base Case

```
  State:      dp[i] = max money you can rob from houses 0..i
  Transition: dp[i] = max(
                  dp[i-1],          # skip house i
                  dp[i-2] + nums[i] # rob house i (add to best without neighbor)
              )
  Base case:  dp[0] = nums[0]
              dp[1] = max(nums[0], nums[1])
```

### Step-by-Step Example

- Input: nums = [2, 7, 9, 3, 1]

```
  House:     0    1    2    3    4
  Money:    [2]  [7]  [9]  [3]  [1]
  dp:       [2]  [7]  [ ]  [ ]  [ ]

  i=2: dp[2] = max(dp[1], dp[0] + 9) = max(7, 2+9) = max(7, 11) = 11
  dp:       [2]  [7]  [11] [ ]  [ ]

  i=3: dp[3] = max(dp[2], dp[1] + 3) = max(11, 7+3) = max(11, 10) = 11
  dp:       [2]  [7]  [11] [11] [ ]

  i=4: dp[4] = max(dp[3], dp[2] + 1) = max(11, 11+1) = max(11, 12) = 12
  dp:       [2]  [7]  [11] [11] [12]
```

- Output: 12 (rob houses 0, 2, 4 -> 2 + 9 + 1 = 12)

### Code

```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]
```

**Time:** O(n) | **Space:** O(n), or O(1) with two variables.

---

## Problem 3: Maximum Subarray / Kadane's Algorithm (LeetCode 53)

**The question:** Given an array of integers, find the contiguous subarray
with the largest sum.

### Baby Explanation

Imagine walking along a number line collecting coins (positive) and paying
tolls (negative). At each step you decide: keep going with what you have,
or start fresh from here?

### State, Transition, Base Case

```
  State:      dp[i] = maximum subarray sum ENDING at index i
  Transition: dp[i] = max(nums[i], dp[i-1] + nums[i])
              (start fresh at i  OR  extend the previous subarray)
  Base case:  dp[0] = nums[0]
  Answer:     max(dp)  (the best ending point among all)
```

### Step-by-Step Example

- Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

```
  Index:  0    1    2    3    4    5    6    7    8
  nums:  [-2] [ 1] [-3] [ 4] [-1] [ 2] [ 1] [-5] [ 4]
  dp:    [-2] [ ] [  ] [  ] [  ] [  ] [  ] [  ] [  ]

  i=1: dp[1] = max(1, -2+1) = max(1, -1) = 1
  i=2: dp[2] = max(-3, 1+(-3)) = max(-3, -2) = -2
  i=3: dp[3] = max(4, -2+4) = max(4, 2) = 4       <-- start fresh!
  i=4: dp[4] = max(-1, 4+(-1)) = max(-1, 3) = 3
  i=5: dp[5] = max(2, 3+2) = max(2, 5) = 5
  i=6: dp[6] = max(1, 5+1) = max(1, 6) = 6        <-- current best!
  i=7: dp[7] = max(-5, 6+(-5)) = max(-5, 1) = 1
  i=8: dp[8] = max(4, 1+4) = max(4, 5) = 5

  dp:  [-2, 1, -2, 4, 3, 5, 6, 1, 5]
```

- Output: max(dp) = 6 (subarray [4, -1, 2, 1])

### Code

```python
def maxSubArray(nums):
    dp = nums[0]
    best = nums[0]

    for i in range(1, len(nums)):
        dp = max(nums[i], dp + nums[i])
        best = max(best, dp)

    return best
```

**Time:** O(n) | **Space:** O(1) -- Kadane's only needs one variable!

---

## Common Variations

| Problem                | State dp[i] means...              | Transition                              |
|------------------------|-----------------------------------|-----------------------------------------|
| Climbing Stairs        | ways to reach step i              | dp[i-1] + dp[i-2]                      |
| House Robber           | max money from first i houses     | max(dp[i-1], dp[i-2] + nums[i])        |
| Maximum Subarray       | max subarray sum ending at i      | max(nums[i], dp[i-1] + nums[i])        |
| Min Cost Climbing      | min cost to reach step i          | min(dp[i-1], dp[i-2]) + cost[i]        |
| Decode Ways            | ways to decode first i chars      | dp[i-1] (if valid 1-digit) + dp[i-2]   |

## Top 5 Mistakes Beginners Make

1. **Off-by-one errors.** Is your dp array length n or n+1? Be consistent.
2. **Forgetting dp[1] base case.** Many 1D problems need BOTH dp[0] and dp[1].
3. **Returning dp[-1] when the answer is max(dp).** (Kadane's!)
4. **Not handling edge cases.** What if the array has only 1 element?
5. **Using 2D DP when 1D is enough.** Keep it simple -- start with 1D.

## Complexity (Time + Space)

- All three problems above: O(n) time
- Space: O(n) with array, O(1) if you only track previous 1-2 values

## What To Say In Interview (Talk Track)

> "I notice this is a 1D DP problem because the answer at each position
> depends only on previous positions in the array.
> My state dp[i] represents [what it means].
> The transition is dp[i] = [formula].
> Base case: dp[0] = [value].
> Let me trace through a small example to verify."
