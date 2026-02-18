# Knapsack Patterns

## Baby Explanation (ELI10)

- You are packing a suitcase for vacation. Each item has a weight and a value.
  Your suitcase can only hold so much weight. What is the most valuable
  collection of items you can bring?
- **0/1 Knapsack:** Each item is unique -- you either take it or leave it.
  Like packing shirts: you have one of each, take it or skip it.
- **Unbounded Knapsack:** You can take as many copies as you want.
  Like buying from a store shelf: unlimited stock of each item.
- The trick is: for every item, you have a choice. DP remembers the best
  choice at every step so you don't re-decide.

## Pattern Recognition

Use this when you see:
- "Given items with weight/cost and a capacity/target"
- "Can you make exactly this sum from these numbers?"
- "What is the maximum value within a budget?"
- "How many ways to reach a target using these choices?"
- Partition problems: "Can you split into two equal halves?"

Avoid when:
- Items have dependencies (item A requires item B) -- use graph DP
- The problem says "find ALL combinations" -- use backtracking
- There is no capacity/limit constraint

---

## 0/1 Knapsack Template

Each item used AT MOST once. Iterate items forward, capacity BACKWARD.

```python
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):                          # for each item
        for w in range(capacity, weights[i] - 1, -1):  # BACKWARD!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]
```

Why backward? So each item is only used once. If we go forward,
we might accidentally use the same item again.

## Unbounded Knapsack Template

Each item can be used UNLIMITED times. Iterate capacity FORWARD.

```python
def knapsack_unbounded(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):               # for each item
        for w in range(weights[i], capacity + 1):       # FORWARD!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]
```

Forward means: when computing dp[w], you might use dp[w - weight[i]]
which already includes item i. That is fine -- unlimited copies allowed!

---

## Problem 1: Classic 0/1 Knapsack

- Input: weights = [1, 3, 4, 5], values = [1, 4, 5, 7], capacity = 7

### State, Transition, Base Case

```
  State:      dp[w] = maximum value achievable with capacity w
  Transition: dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
  Base case:  dp[0] = 0  (zero capacity = zero value)
```

### Step-by-Step (2D view for clarity)

```
  Items: (w=1,v=1), (w=3,v=4), (w=4,v=5), (w=5,v=7)
  Capacity: 0  1  2  3  4  5  6  7

  No items:  0  0  0  0  0  0  0  0

  Item 0 (w=1, v=1):
             0  1  1  1  1  1  1  1

  Item 1 (w=3, v=4):
             0  1  1  4  5  5  5  5

  Item 2 (w=4, v=5):
             0  1  1  4  5  6  6  9

  Item 3 (w=5, v=7):
             0  1  1  4  5  7  8  9
```

- Output: 9 (take items 1 and 2: weight 3+4=7, value 4+5=9)

---

## Problem 2: Subset Sum (Can you pick numbers that add to target?)

**The question:** Given numbers [2, 3, 7, 8, 10] and target = 11,
can you pick a subset that sums to exactly 11?

This is 0/1 Knapsack where "value" does not exist -- just "can I reach this sum?"

### State, Transition, Base Case

```
  State:      dp[s] = True/False, can we make sum s?
  Transition: dp[s] = dp[s] or dp[s - nums[i]]
  Base case:  dp[0] = True  (empty subset sums to 0)
```

### Step-by-Step

- Input: nums = [2, 3, 7, 8, 10], target = 11

```
  dp (True/False for sums 0..11):

  Start:     T F F F F F F F F F F F   (only sum 0 is reachable)

  Add 2:     T F T F F F F F F F F F   (can make 0, 2)
  Add 3:     T F T T F T F F F F F F   (can make 0, 2, 3, 5)
  Add 7:     T F T T F T F T F T T F   (can make 0,2,3,5,7,9,10)
                                         ^--- not 11 yet
  Add 8:     T F T T F T F T T T T T   (can make 11! = 3+8)
                                                        ^ YES!
```

- Output: True (subset {3, 8} sums to 11)

### Code

```python
def canPartition(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for s in range(target, num - 1, -1):   # backward for 0/1
            dp[s] = dp[s] or dp[s - num]

    return dp[target]
```

---

## Problem 3: Partition Equal Subset Sum (LeetCode 416)

**The question:** Can you split the array into two subsets with equal sum?

This is just Subset Sum where target = total_sum / 2.

```python
def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:         # odd total? impossible to split evenly
        return False
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    return dp[target]
```

---

## Problem 4: Coin Change (LeetCode 322) -- Unbounded Knapsack

**The question:** Given coin denominations and a target amount,
find the fewest coins to make that amount. (Unlimited coins of each type.)

### State, Transition, Base Case

```
  State:      dp[a] = minimum coins to make amount a
  Transition: dp[a] = min(dp[a], dp[a - coin] + 1)  for each coin
  Base case:  dp[0] = 0  (zero coins for amount zero)
              dp[1..amount] = infinity  (haven't figured these out yet)
```

### Step-by-Step

- Input: coins = [1, 3, 4], amount = 6

```
  amount:  0   1   2   3   4   5   6
  dp:     [0] [inf][inf][inf][inf][inf][inf]

  Coin 1:  0   1   2   3   4   5   6   (use all 1s)
  Coin 3:  0   1   2   1   4   5   2   (3 alone, or 3+3)
                        ^           ^
                     just 1 coin  2 coins (3+3)
  Coin 4:  0   1   2   1   1   2   2
                            ^
                         just 1 coin (the 4)

  Wait, let me redo coin 3 and 4 more carefully:

  After coin 1:  [0, 1, 2, 3, 4, 5, 6]

  Process coin 3 (forward):
    a=3: dp[3] = min(3, dp[0]+1) = min(3, 1) = 1
    a=4: dp[4] = min(4, dp[1]+1) = min(4, 2) = 2
    a=5: dp[5] = min(5, dp[2]+1) = min(5, 3) = 3
    a=6: dp[6] = min(6, dp[3]+1) = min(6, 2) = 2
  After coin 3:  [0, 1, 2, 1, 2, 3, 2]

  Process coin 4 (forward):
    a=4: dp[4] = min(2, dp[0]+1) = min(2, 1) = 1
    a=5: dp[5] = min(3, dp[1]+1) = min(3, 2) = 2
    a=6: dp[6] = min(2, dp[2]+1) = min(2, 3) = 2
  After coin 4:  [0, 1, 2, 1, 1, 2, 2]
```

- Output: 2 (coins: 3 + 3, or could be seen from the dp table)

### Code

```python
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for a in range(coin, amount + 1):       # FORWARD (unbounded)
            dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

---

## 0/1 vs Unbounded: The Key Difference

```
  -------------------------------------------------------
  |                | 0/1 Knapsack     | Unbounded         |
  |----------------|------------------|-------------------|
  | Each item      | used at most once | used any # times  |
  | Inner loop     | BACKWARD         | FORWARD           |
  | Example        | Subset Sum       | Coin Change       |
  | Analogy        | Packing suitcase | Shopping at store  |
  -------------------------------------------------------
```

The ONLY code difference is the direction of the inner loop!

## Common Variations

| Problem                     | Type       | Target         |
|-----------------------------|------------|----------------|
| 0/1 Knapsack                | 0/1        | max value      |
| Subset Sum                  | 0/1        | True/False     |
| Partition Equal Subset Sum  | 0/1        | can split?     |
| Coin Change (min coins)     | Unbounded  | min count      |
| Coin Change II (# ways)     | Unbounded  | count ways     |
| Target Sum (+/- signs)      | 0/1        | count ways     |

## Top 5 Mistakes Beginners Make

1. **Wrong loop direction.** Backward for 0/1, forward for unbounded. Memorize this!
2. **Forgetting dp[0] base case.** dp[0] = 0 for value, dp[0] = True for boolean.
3. **Off-by-one on capacity.** dp array needs size (capacity + 1).
4. **Using infinity wrong.** Initialize to float('inf') for min, 0 for max.
5. **Not recognizing it as knapsack.** Any "select items under a budget" is knapsack.

## Complexity (Time + Space)

- Time: O(n * capacity) for both types
- Space: O(capacity) with 1D optimization

## What To Say In Interview (Talk Track)

> "This is a [0/1 / unbounded] knapsack problem. Each item can be
> used [once / unlimited times], so I iterate capacity [backward / forward].
> My state dp[w] represents [max value / min count / reachability] at capacity w.
> The transition is dp[w] = [formula].
> Base case: dp[0] = [value].
> Time is O(n * capacity), space is O(capacity)."
