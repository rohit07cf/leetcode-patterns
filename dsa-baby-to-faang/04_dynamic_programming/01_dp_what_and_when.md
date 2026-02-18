# Dynamic Programming: What It Is and When to Use It

## Baby Explanation (ELI10)

- Imagine you are adding 1+1+1+1+1. You get 5. Now I ask: add one more +1.
  You don't recount from scratch -- you remember 5 and just say 6. That is DP.
- DP = "remembering answers you already figured out so you never redo the work."
- Think of it like writing notes on a test. You solve a small problem, write the
  answer in the margin, and look it up later instead of re-solving it.
- Every DP problem is just a recursion problem where the same sub-question
  keeps popping up over and over again.

## The Two Magic Ingredients

A problem is a DP problem when it has BOTH of these:

```
  1) OVERLAPPING SUBPROBLEMS
     The same smaller question gets asked many times.

  2) OPTIMAL SUBSTRUCTURE
     The best answer to the big problem is built from
     the best answers to smaller problems.
```

If a problem has both -- congratulations, DP will work!

## The Classic First Example: Fibonacci

Fibonacci: F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2)

### The recursion tree for F(5):

```
                        F(5)
                       /    \
                    F(4)     F(3)       <-- F(3) appears TWICE!
                   /    \    /   \
                F(3)  F(2) F(2) F(1)    <-- F(2) appears THREE times!
               /   \  / \   / \
            F(2) F(1) F(1) F(0) F(1) F(0)
            / \
         F(1) F(0)
```

See how F(3), F(2), F(1) get called again and again?
That is "overlapping subproblems." We are doing wasted work!

### Approach 1: Plain Recursion (SLOW -- DO NOT USE)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Time: O(2^n)  <-- TERRIBLE
# Space: O(n) call stack
```

### Approach 2: Memoization / Top-Down (ADD A NOTEBOOK)

```python
def fib(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]            # already solved? just look it up!
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

# Time: O(n)   <-- each subproblem solved ONCE
# Space: O(n)
```

### Approach 3: Tabulation / Bottom-Up (FILL A TABLE)

```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0                    # base case
    dp[1] = 1                    # base case
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]   # transition
    return dp[n]

# Time: O(n)
# Space: O(n)  (can optimize to O(1) with two variables)
```

## Three Core Concepts

### What is a STATE?

The state is "what information do I need to describe where I am in the problem?"

```
  Fibonacci:  state = n  (which Fibonacci number am I computing?)
  Grid path:  state = (row, col)  (where am I on the grid?)
  Knapsack:   state = (item_index, remaining_capacity)
```

Think of it like your GPS coordinates. The state tells you exactly
where you are so you can figure out where to go next.

### What is a TRANSITION?

The transition is the formula that connects one state to other states.
It answers: "How do I compute dp[current] from dp[smaller]?"

```
  Fibonacci:  dp[n] = dp[n-1] + dp[n-2]
  Climbing:   dp[i] = dp[i-1] + dp[i-2]
  Grid:       dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

### What is a BASE CASE?

The base case is the tiniest version of the problem where you
already KNOW the answer without computing anything.

```
  Fibonacci:  dp[0] = 0, dp[1] = 1
  Grid:       dp[0][0] = grid[0][0]  (starting cell)
  Knapsack:   dp[0][w] = 0  (no items = no value)
```

## Memoization vs Tabulation

```
 ---------------------------------------------------------------
 |              | MEMOIZATION (Top-Down) | TABULATION (Bottom-Up)|
 |--------------|------------------------|------------------------|
 | Direction    | Start big, go small    | Start small, go big    |
 | Technique    | Recursion + cache      | For-loops + table      |
 | Solves all?  | Only needed states     | ALL states             |
 | Stack risk   | Yes (deep recursion)   | No                     |
 | Easier to    | Write (natural)        | Optimize space         |
 | Interview?   | Great for explaining   | Great for performance  |
 ---------------------------------------------------------------
```

**Rule of thumb:** Start with memoization (easier to think about),
then convert to tabulation if the interviewer asks for optimization.

## Pattern Recognition

How to RECOGNIZE a DP problem in an interview:

```
 The problem asks for:              --> Likely DP?
 -----------------------------------------------
 "Find the MINIMUM cost..."         --> YES
 "Find the MAXIMUM profit..."       --> YES
 "Count the NUMBER OF WAYS..."      --> YES
 "Is it POSSIBLE to..."             --> YES
 "Find the LONGEST..."              --> YES
 "Find the SHORTEST..."             --> MAYBE (could be BFS)
 "Print ALL solutions..."           --> NO (use backtracking)
 "Find a specific element..."       --> NO (use binary search)
```

## The 4-Step DP Recipe (Use This EVERY Time)

```
  +------------------------------------------+
  |  STEP 1: Define the STATE               |
  |    What does dp[i] (or dp[i][j]) mean?  |
  +------------------------------------------+
               |
               v
  +------------------------------------------+
  |  STEP 2: Write the TRANSITION            |
  |    dp[i] = some formula using dp[<i]     |
  +------------------------------------------+
               |
               v
  +------------------------------------------+
  |  STEP 3: Set BASE CASES                  |
  |    Fill in the answers you already know   |
  +------------------------------------------+
               |
               v
  +------------------------------------------+
  |  STEP 4: Determine FILL ORDER            |
  |    Which direction do you fill the table? |
  |    (left to right? bottom to top?)        |
  +------------------------------------------+
```

## How to Convert Recursion to DP

```
  1. Write the brute-force recursive solution.
  2. Identify the parameters that change -- those are your STATE.
  3. Add a memo dictionary. Before computing, check memo.
     After computing, store in memo. --> Done! (Top-Down DP)
  4. (Optional) Convert to a for-loop table. --> (Bottom-Up DP)
```

### Example: Converting Fibonacci

```
  Recursion:      fib(n) = fib(n-1) + fib(n-2)
                  State = n
                  Add memo --> top-down DP
                  Replace recursion with loop --> bottom-up DP
```

## Step-by-Step Example: Fibonacci Tabulation

- Input: n = 6
- Walkthrough:

```
  dp = [0, 1, _, _, _, _, _]

  i=2: dp[2] = dp[1] + dp[0] = 1 + 0 = 1   -->  [0, 1, 1, _, _, _, _]
  i=3: dp[3] = dp[2] + dp[1] = 1 + 1 = 2   -->  [0, 1, 1, 2, _, _, _]
  i=4: dp[4] = dp[3] + dp[2] = 2 + 1 = 3   -->  [0, 1, 1, 2, 3, _, _]
  i=5: dp[5] = dp[4] + dp[3] = 3 + 2 = 5   -->  [0, 1, 1, 2, 3, 5, _]
  i=6: dp[6] = dp[5] + dp[4] = 5 + 3 = 8   -->  [0, 1, 1, 2, 3, 5, 8]
```

- Output: dp[6] = 8

## Top 5 Mistakes Beginners Make

1. **Forgetting the base case.** Without it your recursion never stops.
2. **Wrong state definition.** If dp[i] is not clearly defined, everything breaks.
3. **Filling the table in the wrong order.** You must fill smaller states first.
4. **Not recognizing DP.** If the brute force has repeated sub-calls, try DP.
5. **Jumping to DP too fast.** Always start with recursion, THEN add memoization.

## Complexity

- Brute recursion (Fibonacci): O(2^n) time, O(n) space
- With memoization: O(n) time, O(n) space
- With tabulation: O(n) time, O(n) space (or O(1) with space trick)

## What To Say In Interview (Talk Track)

> "This problem has overlapping subproblems because the same recursive
> calls appear multiple times. It also has optimal substructure because
> the optimal solution builds on optimal sub-solutions.
> Let me define my state: dp[i] represents...
> The transition is dp[i] = ...
> Base cases are dp[0] = ..., dp[1] = ...
> I will fill from left to right. Let me trace through a small example."

This shows the interviewer you have a SYSTEM, not just guessing.
