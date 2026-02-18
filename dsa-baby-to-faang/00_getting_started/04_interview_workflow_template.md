# Interview Workflow Template

## Baby Explanation (ELI10)

- A coding interview is like a cooking show — you need to explain while you cook
- The interviewer cares about HOW you think, not just the final answer
- Following a consistent workflow makes you look organized and confident
- This 7-step template works for ANY coding problem
- Practice this workflow with every single problem you solve
- By interview day, it should feel automatic

---

## Pattern Recognition

✅ Use this when you see:
- Any coding interview (phone screen, onsite, virtual)
- Any practice problem (build the habit early)
- Timed coding assessments

❌ Avoid:
- Skipping steps to "save time" — the steps ARE the solution

---

## The 7-Step Interview Workflow

### Step 1: Clarify (3-5 minutes)

**What to do:** Read the problem. Restate it in your own words. Ask questions.

**What to SAY:**

```
"Let me make sure I understand this correctly.
I'm given [input], and I need to return [output].
A few questions:
- Can the input be empty?
- Are there duplicates?
- Is the input sorted?
- What should I return if there's no valid answer?"
```

**Why:** Shows you're thorough. Prevents solving the wrong problem.

---

### Step 2: Work Through Examples (2-3 minutes)

**What to do:** Walk through 1-2 examples by hand. Draw them out.

**What to SAY:**

```
"Let me trace through this example to make sure I understand.
Input: [2, 7, 11, 15], target = 9
- I need two numbers that add to 9
- 2 + 7 = 9 ✓
- So the answer is indices [0, 1]"
```

**Why:** Confirms your understanding. Often reveals the pattern.

---

### Step 3: Identify the Pattern (2-3 minutes)

**What to do:** Think about which DSA pattern fits this problem.

**What to SAY:**

```
"This reminds me of a hash map problem because I need
fast lookup to check if a complement exists.
I can store numbers I've seen and check for each new number."
```

**Decision helpers:**

| Clue | Pattern |
|------|---------|
| "sorted array" + pairs | Two Pointers |
| "subarray" + contiguous | Sliding Window |
| "shortest path" | BFS or Dijkstra |
| "min/max" + choices | DP |
| "tree" + recursion | DFS |
| "levels" | BFS |

---

### Step 4: Plan Your Approach (3-5 minutes)

**What to do:** Describe your algorithm step-by-step BEFORE coding.

**What to SAY:**

```
"Here's my plan:
1. Create a hash map to store {number: index}
2. Loop through the array
3. For each number, calculate complement = target - number
4. If complement is in the hash map, return both indices
5. Otherwise, add current number to the hash map

This should be O(n) time and O(n) space."
```

**Why:** This is the MOST important step. If the interviewer spots a flaw, they'll tell you now (saving you 15 minutes of coding).

---

### Step 5: Code It Clean (15-20 minutes)

**What to do:** Write clean code while narrating.

**What to SAY while coding:**

```
"I'm creating a hash map called 'seen' to store numbers and their indices..."
"Now I'm looping through the array with enumerate to get both index and value..."
"Here I check if the complement exists in our map..."
```

**Code tips:**
- Use descriptive variable names (not `i`, `j`, `x`)
- Add a brief comment for tricky lines
- Write helper functions if the code gets long
- Don't worry about perfection — clean is better than clever

```python
def two_sum(nums, target):
    seen = {}  # num -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []  # no solution found
```

---

### Step 6: Test With Examples (3-5 minutes)

**What to do:** Trace through your code line by line with a small example.

**What to SAY:**

```
"Let me walk through with nums = [2, 7, 11], target = 9.

  i=0, num=2, complement=7, seen={}
    7 not in seen → add {2: 0}

  i=1, num=7, complement=2, seen={2: 0}
    2 IS in seen → return [0, 1] ✓

Let me also check an edge case: nums = [3, 3], target = 6
  i=0, num=3, complement=3, seen={}
    3 not in seen → add {3: 0}
  i=1, num=3, complement=3, seen={3: 0}
    3 IS in seen → return [0, 1] ✓"
```

**Why:** Catches bugs. Shows you're careful.

---

### Step 7: Analyze Complexity (1-2 minutes)

**What to SAY:**

```
"Time complexity: O(n) — we iterate through the array once.
Each hash map operation is O(1).

Space complexity: O(n) — in the worst case, we store all n
elements in the hash map before finding a pair."
```

**Why:** Interviewers ALWAYS ask this. Having it ready shows confidence.

---

## Full Walkthrough: Two Sum End-to-End

Here's what the ENTIRE interview looks like with all 7 steps:

```
INTERVIEWER: "Given an array of integers and a target, return
the indices of two numbers that add up to the target."

YOU: "Let me make sure I understand. I have an array of numbers
and a target value. I need to find two numbers in the array
that add up to the target and return their indices.

A few questions:
- Can I assume exactly one solution exists? [Yes]
- Can I use the same element twice? [No]
- Can the array be empty? [No, at least 2 elements]

Let me trace through an example.
nums = [2, 7, 11, 15], target = 9
2 + 7 = 9, so return [0, 1].

I think this is a hash map problem. For each number, I need to
quickly check if its complement (target - number) exists.
A hash map gives me O(1) lookup.

Here's my plan:
1. Create a hash map {number: index}
2. For each number, check if (target - number) is in the map
3. If yes, return both indices
4. If no, add current number to the map

Let me code this up.
[writes code while narrating]

Let me test with nums = [2, 7, 11], target = 9.
[traces through line by line]

Time: O(n), Space: O(n).

Is there anything you'd like me to optimize or handle differently?"
```

---

## Time Budget (45-minute interview)

```
+-------------------+----------+
| Step              | Time     |
+-------------------+----------+
| 1. Clarify        | 3-5 min  |
| 2. Examples       | 2-3 min  |
| 3. Pattern        | 2-3 min  |
| 4. Plan           | 3-5 min  |
| 5. Code           | 15-20 min|
| 6. Test           | 3-5 min  |
| 7. Complexity     | 1-2 min  |
| Buffer / Follow-up| 5 min    |
+-------------------+----------+
| TOTAL             | ~45 min  |
+-------------------+----------+
```

---

## Common Variations

### What If You're Stuck?

```
"I'm not immediately seeing the optimal approach.
Let me start with the brute force solution and see
if I can identify where to optimize."
```

Then code the brute force, identify the slow part, and improve it.

### What If the Interviewer Gives a Hint?

```
"That's a great hint, thank you. So you're suggesting I use a
[data structure/approach]. Let me think about how that applies..."
```

Don't be embarrassed. Hints are NORMAL and expected.

### What If Your Solution Is Brute Force?

```
"I have a working brute force solution at O(n^2).
I believe we can optimize this to O(n) using a hash map.
Would you like me to implement the optimized version?"
```

Always mention you KNOW it can be better.

---

## Top 5 Mistakes

1. **Coding before planning** — Spend 10 min planning, save 20 min debugging
2. **Staying silent** — Talk through EVERYTHING, even when thinking
3. **Skipping edge cases** — Always test with empty, single element, duplicates
4. **Not stating complexity** — Always end with time and space analysis
5. **Panicking when stuck** — Take a breath, talk it out, ask for a hint

---

## Complexity

- This isn't about Big O — it's about your interview PROCESS
- Time investment: Practice this workflow 20 times and it becomes natural
- Return on investment: This workflow alone can improve your interview performance dramatically

---

## What To Say In Interview (Talk Track)

> "Before I start coding, let me clarify a few things about the input..."
> "Let me trace through an example to build my intuition..."
> "I think this is a [pattern] problem. Here's my plan..."
> "Let me code this up while explaining my thinking..."
> "Let me verify by walking through a test case..."
> "The time complexity is O(...) because..."

---

## What's Next?

You're ready to learn patterns! Go to: [../01_core_patterns/01_arrays_hashing.md](../01_core_patterns/01_arrays_hashing.md)
