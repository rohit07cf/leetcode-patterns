# Common Mistakes and How to Fix Them

## Baby Explanation (ELI10)

- Everyone makes mistakes when learning DSA — it's part of the process
- The best engineers aren't the ones who never make mistakes
- They're the ones who learned WHICH mistakes to avoid
- This file lists the 15 biggest beginner traps
- Read this BEFORE you start grinding problems
- Come back and re-read it every week

---

## Pattern Recognition

✅ Use this when you see:
- Yourself making the same mistake twice
- Feeling stuck on every problem
- Getting frustrated during practice

❌ Avoid:
- Beating yourself up — mistakes = learning

---

## Thinking Mistakes

### Mistake 1: Jumping to Code Immediately

**What happens:** You read the problem and start typing code in 30 seconds.

**Why it's bad:** You end up writing the wrong solution, then wasting 20 minutes debugging.

**The fix:** Always spend 3-5 minutes PLANNING first.

```
BAD:  Read problem → Start coding → Get confused → Start over
GOOD: Read problem → Restate it → Pick a pattern → Plan → THEN code
```

---

### Mistake 2: Trying to Memorize Solutions

**What happens:** You look at the answer, memorize it, move to the next problem.

**Why it's bad:** In an interview, the problem will be slightly different, and you'll freeze.

**The fix:** Learn the PATTERN, not the specific solution.

```
BAD:  "Two Sum uses a hash map to store complements" (memorized)
GOOD: "When I need O(1) lookup, I think hash map" (pattern)
```

---

### Mistake 3: Not Understanding the Problem

**What happens:** You assume you understand and start solving the wrong problem.

**Why it's bad:** Perfect solution to the wrong problem = zero points.

**The fix:** Always restate the problem in your own words. Ask:
- What's the input?
- What's the output?
- What are the constraints?
- What are the edge cases?

---

### Mistake 4: Ignoring Constraints

**What happens:** You write an O(n^2) solution when n = 1,000,000.

**Why it's bad:** It will time out. The interviewer expected O(n) or O(n log n).

**The fix:** Always check constraints FIRST.

| n size | Max Big O |
|--------|-----------|
| n <= 1,000 | O(n^2) is OK |
| n <= 100,000 | O(n log n) is needed |
| n <= 1,000,000 | O(n) is needed |

---

### Mistake 5: Overthinking Simple Problems

**What happens:** You try to use fancy algorithms on a problem that just needs a hash map.

**Why it's bad:** You waste time and write overly complex code.

**The fix:** Start with the simplest approach. Only optimize if needed.

```
Ask yourself: "Can I solve this with just a loop and a hash map?"
If yes → do that. Don't overcomplicate it.
```

---

## Coding Mistakes

### Mistake 6: Off-by-One Errors

**What happens:** Your loop goes one step too far or one step too short.

**Why it's bad:** Wrong answers on edge cases.

**The fix:** Always test with the smallest possible input.

```python
# BAD: Does this include the last element?
for i in range(len(arr)):    # 0 to len-1 ✓
for i in range(1, len(arr)): # 1 to len-1 (skips first!)

# GOOD: Be explicit
for i in range(len(arr)):       # every element
for i in range(len(arr) - 1):   # every element except last
```

---

### Mistake 7: Not Handling Edge Cases

**What happens:** Your code works for normal input but crashes on empty arrays, single elements, etc.

**Why it's bad:** Interviewers ALWAYS test edge cases.

**The fix:** Before coding, list your edge cases:

```
Always check:
- Empty input: []
- Single element: [1]
- Two elements: [1, 2]
- All same: [3, 3, 3]
- Negative numbers: [-1, -2]
- Already sorted / reverse sorted
```

---

### Mistake 8: Modifying a Collection While Iterating

**What happens:** You add/remove items from a list while looping through it.

**Why it's bad:** Causes bugs, skipped elements, or infinite loops.

**The fix:** Create a new collection or iterate over a copy.

```python
# BAD
for item in my_list:
    if item == target:
        my_list.remove(item)  # DON'T DO THIS

# GOOD
my_list = [item for item in my_list if item != target]
```

---

### Mistake 9: Using Wrong Data Structure

**What happens:** Using a list when you need a set, or an array when you need a hash map.

**Why it's bad:** Makes your solution slow or overly complicated.

**The fix:** Ask yourself what operations you need:

| Need | Use |
|------|-----|
| Fast lookup (is X in here?) | Set or Hash Map |
| Ordered data | Array or List |
| LIFO (last in first out) | Stack |
| FIFO (first in first out) | Queue (deque) |
| Fast min/max | Heap |

---

### Mistake 10: Forgetting to Return

**What happens:** Your function does the work but doesn't return the answer.

**Why it's bad:** Returns None instead of the answer.

**The fix:** Always check: does my function have a return statement on every path?

```python
# BAD
def find_max(arr):
    best = arr[0]
    for x in arr:
        best = max(best, x)
    # forgot to return!

# GOOD
def find_max(arr):
    best = arr[0]
    for x in arr:
        best = max(best, x)
    return best  # don't forget this!
```

---

## Interview Mistakes

### Mistake 11: Staying Silent

**What happens:** You think quietly for 5 minutes while the interviewer stares.

**Why it's bad:** The interviewer can't help you if they don't know what you're thinking.

**The fix:** ALWAYS think out loud.

```
"I'm thinking about whether a hash map or sorting would work better here..."
"Let me consider the edge cases..."
"I think this is similar to a sliding window pattern because..."
```

---

### Mistake 12: Not Asking Clarifying Questions

**What happens:** You assume things about the problem that aren't true.

**Why it's bad:** You solve the wrong problem.

**The fix:** Always ask at least 3 questions:

1. "Can the input be empty?"
2. "Are there duplicates?"
3. "Are there negative numbers?"
4. "Is the input sorted?"
5. "What should I return if there's no valid answer?"

---

### Mistake 13: Giving Up Too Quickly

**What happens:** You can't solve it in 2 minutes and say "I don't know."

**Why it's bad:** Interviewers want to see how you THINK, not just correct answers.

**The fix:** Talk through your thought process:

```
"I don't see the optimal solution yet, but let me start with brute force..."
"Let me think about what data structure could help here..."
"Could I sort the input first to make this easier?"
```

---

### Mistake 14: Not Testing Your Code

**What happens:** You write the code and say "done" without tracing through it.

**Why it's bad:** You miss bugs that a 1-minute walkthrough would catch.

**The fix:** Always trace through your code with a small example:

```
"Let me walk through this with arr = [2, 7, 11] and target = 9..."
"At i=0, we check if 9-2=7 is in our map... no, add 2..."
"At i=1, we check if 9-7=2 is in our map... yes! Return [0, 1]."
```

---

### Mistake 15: Skipping Complexity Analysis

**What happens:** You finish coding but don't mention Big O.

**Why it's bad:** Interviewers ALWAYS want to hear time and space complexity.

**The fix:** End every solution with:

```
"The time complexity is O(n) because we iterate through the array once."
"The space complexity is O(n) because our hash map can store up to n elements."
```

---

## Step-by-Step Example: Fixing a Common Mistake

**Problem:** Two Sum — find two numbers that add to target.

**The mistake (jumping to brute force without thinking):**

```python
# O(n^2) — beginner mistake
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

**The fix (think first: "I need fast lookup → hash map"):**

```python
# O(n) — after learning the pattern
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

---

## What To Say In Interview (Talk Track)

> "Before I start coding, let me make sure I understand the problem correctly..."
> "Let me think about edge cases — what if the input is empty?"
> "I notice this looks like a [pattern] problem because of [reason]."
> "Let me start with brute force and then see if I can optimize."
> "Let me trace through my code with this small example to verify."

---

## What's Next?

Go to: [04_interview_workflow_template.md](04_interview_workflow_template.md)
