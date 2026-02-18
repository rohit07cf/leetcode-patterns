# Stack & Monotonic Stack

## Baby Explanation (ELI10)

- A **stack** is like a stack of plates in a cafeteria. You can only add a plate on top, and you can only take the top plate off. Last plate in, first plate out (LIFO).
- You can't pull a plate from the middle -- that would crash everything!
- A **monotonic stack** is like a line at a roller coaster where there's a height rule. Imagine everyone in line must be taller than the person in front of them. When a short person shows up, everyone shorter-or-equal in front of them has to leave. The line always stays in order.
- Stacks are perfect for "matching" problems -- like matching opening and closing parentheses.
- Monotonic stacks are perfect for "next greater/smaller element" problems -- finding who is the next taller person in line.
- When you hear "nested" or "matching" or "next bigger/smaller," think stack!

## Pattern Recognition

Use this when you see:
- "Valid parentheses" or "balanced brackets"
- "Next greater element" or "next smaller element"
- "Daily temperatures" (how many days until warmer?)
- "Largest rectangle in histogram"
- Any problem with nested structures (like HTML tags or math expressions)
- "Previous greater" or "previous smaller"

Avoid when:
- You need random access to elements (use array or hash map)
- The problem requires sorting (use sort + other patterns)
- You need to process things in FIFO order (use a queue instead)

## ASCII Diagram: Stack Operations

```
  Stack = pile of plates. Top is where the action happens.

  push(3)    push(7)    push(1)    pop()      peek()
  -------    -------    -------    -------    -------
                        | 1 | <-- top
             | 7 |     | 7 |     | 7 | <-- top  | 7 | <-- returns 7
  | 3 |     | 3 |     | 3 |     | 3 |          | 3 |     (doesn't remove)
  -----     -----     -----     -----          -----
```

### Monotonic Stack (Decreasing) -- Next Greater Element

```
  Array: [2, 1, 4, 3]
  Goal:  For each element, find the next element that is greater.

  Process right to left, maintain a decreasing stack:

  i=3: num=3   stack=[]       --> nothing greater, ans=-1    stack=[3]
  i=2: num=4   stack=[3]      --> pop 3 (4>3), stack empty   ans=-1    stack=[4]
  i=1: num=1   stack=[4]      --> 4>1, so ans=4              stack=[4,1]
  i=0: num=2   stack=[4,1]    --> pop 1 (2>1), peek 4>2     ans=4     stack=[4,2]

  Result: [4, 4, -1, -1]
          2's next greater = 4
          1's next greater = 4
          4 has no next greater = -1
          3 has no next greater = -1
```

## Minimal Python Template

### Pattern 1: Basic Stack (Valid Parentheses)

```python
def is_valid(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in matching:
            # Closing bracket: check if it matches the top
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
        else:
            # Opening bracket: push onto stack
            stack.append(char)

    return len(stack) == 0  # stack should be empty if all matched
```

### Pattern 2: Next Greater Element (Monotonic Stack)

```python
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(n):
        # Pop elements that are SMALLER than current
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]  # current element is the "next greater"

        stack.append(i)

    return result
```

### Pattern 3: Daily Temperatures

```python
def daily_temperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []  # stores indices of days we haven't resolved yet

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day  # days until warmer

        stack.append(i)

    return answer
```

## Step-by-Step Example (Tiny Input)

### Valid Parentheses: s = "({[]})"

```
Step 1: char='('  --> opening, push         stack = ['(']
Step 2: char='{'  --> opening, push         stack = ['(', '{']
Step 3: char='['  --> opening, push         stack = ['(', '{', '[']
Step 4: char=']'  --> closing, top='[' matches!  pop   stack = ['(', '{']
Step 5: char='}'  --> closing, top='{' matches!  pop   stack = ['(']
Step 6: char=')'  --> closing, top='(' matches!  pop   stack = []

Stack is empty --> return True (valid!)
```

### Daily Temperatures: temps = [73, 74, 75, 71, 69, 76]

```
i=0: temp=73  stack=[]        --> push 0          stack=[0]
i=1: temp=74  74>73(stack[0]) --> pop 0, ans[0]=1-0=1    stack=[1]
i=2: temp=75  75>74(stack[1]) --> pop 1, ans[1]=2-1=1    stack=[2]
i=3: temp=71  71<75           --> push 3          stack=[2,3]
i=4: temp=69  69<71           --> push 4          stack=[2,3,4]
i=5: temp=76  76>69 --> pop 4, ans[4]=5-4=1
              76>71 --> pop 3, ans[3]=5-3=2
              76>75 --> pop 2, ans[2]=5-2=3       stack=[5]
```

- **Input:** [73, 74, 75, 71, 69, 76]
- **Output:** [1, 1, 3, 2, 1, 0]
- Meaning: from day 0, wait 1 day. From day 2, wait 3 days. Day 5 never gets warmer (0).

## Common Variations

1. **Next Greater Element** -- For each element, find the first larger element to its right. Use a monotonic decreasing stack scanning left to right.

2. **Next Smaller Element** -- Same idea but find the first smaller element. Use a monotonic increasing stack.

3. **Previous Greater Element** -- Find the first larger element to the LEFT. Scan left to right, pop elements smaller than current. The top of stack (after popping) is the answer.

4. **Largest Rectangle in Histogram** -- For each bar, find how far it extends left and right. Uses both "previous smaller" and "next smaller" in one pass.

5. **Evaluate Reverse Polish Notation** -- Use a basic stack. Push numbers, when you see an operator, pop two numbers, compute, push result.

## Top 5 Mistakes Beginners Make

1. **Popping from an empty stack.** Always check `if stack` or `len(stack) > 0` before calling `stack.pop()` or accessing `stack[-1]`.

2. **Storing values when you should store indices.** For problems like Daily Temperatures, you need the INDEX to calculate distances. Store indices in the stack, not the values themselves.

3. **Getting the monotonic direction wrong.** "Next greater" needs a decreasing stack (pop smaller elements). "Next smaller" needs an increasing stack (pop larger elements). Draw it out if confused!

4. **Forgetting unresolved elements.** After processing all elements, anything left in the stack has no "next greater/smaller." Make sure your result array defaults to -1 or 0 for these.

5. **Confusing stack with queue.** Stack = LIFO (last in, first out). Queue = FIFO (first in, first out). If you need FIFO, use `collections.deque` and `popleft()`.

## Complexity

- **Time:** O(n) -- each element is pushed once and popped at most once.
- **Space:** O(n) -- worst case, every element sits in the stack (like a sorted array for monotonic stack).

## What To Say In Interview (Talk Track)

- "This problem has a matching/nesting structure, so I'll use a stack."
- "For the 'next greater element' pattern, I'll use a monotonic stack. I process elements and pop anything from the stack that the current element resolves."
- "Each element is pushed and popped at most once, so the total time is O(n) even though there's a while loop inside the for loop."
- "I'll store indices in the stack rather than values, so I can compute distances or reference the original array."
- "After the loop, anything remaining in the stack has no answer, which I handle by initializing the result to -1."
