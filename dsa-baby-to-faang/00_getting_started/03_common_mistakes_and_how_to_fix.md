# Common Mistakes and How to Fix Them

> Every mistake you make is a lesson your brain is learning. The goal isn't to never make mistakes -- it's to recognize them quickly and know exactly how to fix them.

---

## Baby Explanation (ELI10)

Imagine you're learning to ride a bike. You're going to fall a few times. That's completely okay! But what if someone told you the 15 most common ways people fall off bikes *before* you started? You'd fall a lot less, right?

That's what this page is. Here are the most common "falls" that beginners take when learning to solve coding problems, and exactly how to get back up.

- **Everyone makes these mistakes.** You are not alone. Even experienced engineers made every single one of these when they started.
- **Mistakes are how your brain learns.** Your brain literally needs to make mistakes to build new pathways. That's just science.
- **Knowing the mistake is half the fix.** Once you can spot it happening, fixing it becomes almost automatic.
- **Speed comes later.** Right now, focus on getting it right. Getting it fast comes naturally with practice.
- **You will re-make some of these mistakes.** That's fine. Each time, you'll catch it a little faster.
- **Be patient with yourself.** You're learning one of the hardest skills in software engineering. Give yourself credit just for showing up.

---

## Pattern Recognition

### When You're Probably Making a Mistake

Look for these warning signs:

- You've been staring at the problem for 20+ minutes with no plan
- You started coding before you fully understood the problem
- Your code keeps getting longer and messier with every line
- You keep adding `if` statements to handle special cases you didn't think of
- You're not sure what your own variables represent anymore
- You can't explain your approach in one or two plain English sentences

### When You're On the Right Track

Look for these good signs:

- You can explain your approach in one or two sentences before coding
- You worked through an example by hand first
- Your code is short and clean
- You know what every single variable represents
- You can predict what your code will output before you run it
- You thought about edge cases before the interviewer had to ask about them

---

## The Top 15 Beginner Mistakes

We've organized these into three categories: **Thinking Mistakes** (before you code), **Coding Mistakes** (while you code), and **Interview Mistakes** (how you communicate). Five in each category.

&nbsp;

---

### Thinking Mistakes

These happen before you write a single line of code. They're about **how you approach** the problem.

&nbsp;

#### Mistake 1: Jumping Straight Into Code

**The mistake:** You read the problem and immediately start typing code without any plan.

**Why it's bad:** This is like driving to a new city without a map. You'll write 30 lines of code, realize your approach doesn't work, delete everything, and start over. You've wasted 15 precious minutes and your confidence is shattered.

**The fix:** Always follow the 7-step workflow (see `04_interview_workflow_template.md`). Before writing any code:

1. Restate the problem in your own words
2. Walk through an example by hand
3. Identify which pattern fits
4. Describe your approach out loud (or write pseudocode)

**Example:**

Problem: "Given an array of integers, return the two numbers that add up to a target."

```
BAD APPROACH:
   Read problem --> Immediately start writing nested for loops --> Get confused
   --> Realize it's wrong --> Start over --> Panic

GOOD APPROACH:
   Read problem --> Restate: "I need to find two numbers that sum to target"
   --> Example: [2, 7, 11, 15], target 9... so 2 + 7 = 9, return [0, 1]
   --> Pattern: "I need fast lookup... hash map!"
   --> Plan: "For each number, check if target - number is in my map"
   --> NOW code
```

The good approach takes 3 extra minutes of planning but saves 15 minutes of confused debugging.

&nbsp;

#### Mistake 2: Not Understanding the Problem Before Solving It

**The mistake:** You think you understand the problem, but you actually misread it or missed a key detail.

**Why it's bad:** You solve the wrong problem perfectly. In an interview, you've used 20 minutes building a beautiful solution to something nobody asked for. Zero points.

**The fix:** Before doing anything else, ask yourself (or the interviewer) these questions:

- What exactly is the input? (What type? How big? Can it be empty? Can values be negative?)
- What exactly is the output? (Return a value? Modify the input in place? Return indices or the actual values?)
- Are there duplicates in the input?
- Is the input sorted?
- What should I return if there's no valid answer?

**Example:**

Problem: "Two Sum" -- Return indices of two numbers that add up to target.

Common misread: Returning the *values* instead of the *indices*. You write a perfect solution that returns `[2, 7]` instead of `[0, 1]`. Wrong answer, even though your logic was correct.

The one-second fix: Re-read the problem statement carefully. Say out loud: "I need to return the *indices*, not the values themselves."

&nbsp;

#### Mistake 3: Trying to Find the Perfect Solution Immediately

**The mistake:** You refuse to even consider a brute force solution because you know it's "not good enough" or "not impressive."

**Why it's bad:** In an interview, a working brute force solution is worth infinitely more than an incomplete optimal solution. You get zero points for a half-finished "optimal" answer. Also, the brute force approach often naturally reveals the path to the optimal solution.

**The fix:** Always start with brute force. Say this out loud:

> "Let me start with the simplest approach first. The brute force would be to check every pair -- that's O(n squared). It works, but let me see if I can do better."

Interviewers love hearing this. It shows you can think systematically and improve step by step.

**Example:**

Problem: "Find if any two numbers in an array sum to target."

```
Step 1 (brute force): "I can check every pair with two loops. O(n^2) time, O(1) space."
Step 2 (think):       "The bottleneck is searching for the complement of each number."
Step 3 (optimize):    "If I store seen numbers in a hash set, I can search in O(1)."
Step 4 (result):      "That brings it down to O(n) time, O(n) space."
```

See how the brute force naturally led to the optimization? That's the magic of starting simple.

&nbsp;

#### Mistake 4: Ignoring Edge Cases

**The mistake:** Your solution works beautifully for the example input but crashes or gives wrong answers on edge cases like empty arrays, single elements, negative numbers, or very large inputs.

**Why it's bad:** Interviewers specifically test edge cases. If your code crashes on an empty input, it signals that you don't think defensively -- and defensive thinking is critical for production code.

**The fix:** Before coding, write down (or mentally note) these edge cases:

| Edge Case | Example | Why It Matters |
|-----------|---------|----------------|
| Empty input | `[]`, `""`, `None` | Crashes if you access index 0 without checking |
| Single element | `[5]`, `"a"` | Loops expecting pairs will fail |
| All same values | `[3, 3, 3, 3]` | Duplicate handling logic gets tested |
| Already sorted | `[1, 2, 3, 4, 5]` | May expose assumptions about order |
| Reverse sorted | `[5, 4, 3, 2, 1]` | Same as above |
| Negative numbers | `[-5, -2, 0, 3]` | Many beginners forget these exist |
| Very large values | `n = 1,000,000` | O(n^2) will time out |

**Example:**

Problem: "Find the maximum element in an array."

Your solution: `return max(nums)`

But what if `nums` is empty? `max([])` throws a `ValueError`. The fix: check first.

```python
if not nums:
    return None  # Or ask the interviewer what to return
return max(nums)
```

&nbsp;

#### Mistake 5: Not Recognizing the Pattern

**The mistake:** You see each problem as completely unique and try to invent a brand-new approach from scratch every single time.

**Why it's bad:** There are only about 10-15 core patterns in coding interviews. If you don't recognize them, every problem feels impossible. If you do recognize them, most problems feel like variations of something you've already seen.

**The fix:** After reading a problem, run through these quick questions:

| If the problem involves... | Try this pattern |
|---------------------------|-----------------|
| Finding something in a sorted array | Binary Search |
| Subarrays or substrings (contiguous) | Sliding Window or Two Pointers |
| A tree or graph structure | DFS or BFS |
| Optimization with overlapping subproblems | Dynamic Programming |
| Matching, counting, or checking existence | Hash Map or Hash Set |
| Ordering or nesting (like parentheses) | Stack |
| Dependencies or ordering of tasks | Topological Sort |

See the Pattern Recognition Map in the main README for the full decision tree.

**Example:**

Problem: "Find the longest substring with at most K distinct characters."

Without pattern knowledge: "I have no idea where to start."

With pattern knowledge: "Substring... variable length... a constraint on distinct characters... this is a sliding window problem! I'll expand the right side and shrink the left side when I exceed K distinct characters."

&nbsp;

---

### Coding Mistakes

These happen while you're writing code. They're about **how you translate your idea into working code**.

&nbsp;

#### Mistake 6: Off-by-One Errors

**The mistake:** Your loop goes one step too far or one step too short. You access `array[n]` when the last valid index is `array[n-1]`, or your loop skips the first or last element.

**Why it's bad:** Off-by-one errors are the #1 source of bugs in coding interviews. They cause index-out-of-bounds crashes, infinite loops, or subtly wrong answers that are really hard to debug under pressure.

**The fix:** Be extremely deliberate about your loop boundaries. For every loop, ask:

- Does my loop start at `0` or `1`?
- Does my loop end at `n`, `n-1`, or `n+1`?
- Am I using `<` or `<=`?
- After the loop ends, what is the value of my index variable?

**Example:**

```python
# BAD: crashes when i is the last element
for i in range(len(nums)):
    if nums[i] == nums[i + 1]:  # IndexError when i = len(nums) - 1
        print("found duplicate")

# GOOD: stop one element early so i+1 is always valid
for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        print("found duplicate")
```

**Pro tip:** When in doubt, trace through your loop with a tiny example (an array of just 2 or 3 elements) and carefully check what happens at the boundaries.

&nbsp;

#### Mistake 7: Modifying a Collection While Iterating Over It

**The mistake:** You add or remove elements from a list, set, or dictionary while you're looping through it.

**Why it's bad:** This causes unpredictable behavior. In Python, you might silently skip elements or get a `RuntimeError`. In other languages, it can cause crashes or infinite loops. The worst part is these bugs are really hard to spot.

**The fix:** If you need to modify a collection while iterating:

- Build a new collection instead of modifying the original
- Or make a copy first and iterate over the copy
- Or iterate by index in reverse (if removing elements from a list)

**Example:**

```python
# BAD: removing items while iterating -- will skip elements!
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num % 2 == 0:
        nums.remove(num)  # Dangerous! The loop skips elements after removal.

# GOOD: build a new list with only the items you want
nums = [1, 2, 3, 4, 5]
nums = [num for num in nums if num % 2 != 0]
# Result: [1, 3, 5]
```

&nbsp;

#### Mistake 8: Using the Wrong Data Structure

**The mistake:** You use a list when you should use a set, or a plain array when a hash map would be much better. Your code ends up slow, long, or both.

**Why it's bad:** Choosing the wrong data structure can turn an O(n) solution into O(n^2), or make your code three times longer than it needs to be. It also makes your solution harder to read and debug.

**The fix:** Know these rules of thumb:

| If you need to... | Use this | Why |
|-------------------|----------|-----|
| Check if something exists quickly | `set` (Hash Set) | O(1) lookup vs O(n) for a list |
| Map keys to values | `dict` (Hash Map) | O(1) lookup by key |
| Keep things in insertion order | `list` (Array) | Maintains order, fast index access |
| Process things first-in-first-out | `collections.deque` (Queue) | O(1) append and popleft |
| Process things last-in-first-out | `list` used as Stack | O(1) append and pop |
| Get the smallest/largest quickly | `heapq` (Heap) | O(log n) push/pop, O(1) peek |

**Example:**

```python
# BAD: checking membership in a list is O(n) each time
seen = []
for num in nums:
    if num in seen:      # O(n) search every time! Total: O(n^2)
        return True
    seen.append(num)

# GOOD: checking membership in a set is O(1) each time
seen = set()
for num in nums:
    if num in seen:      # O(1) search every time! Total: O(n)
        return True
    seen.add(num)
```

This one change turns an O(n^2) solution into O(n). That's the difference between passing and failing on large inputs.

&nbsp;

#### Mistake 9: Writing Messy, Unreadable Code

**The mistake:** You use single-letter variable names everywhere, write very long lines, skip whitespace between sections, and have no logical structure to your code.

**Why it's bad:** In an interview, the interviewer is reading your code *live*. If they can't follow it, they'll assume you can't either. Messy code also makes it much harder for *you* to find your own bugs. When you're under pressure, you need your code to be as readable as possible.

**The fix:** Follow these simple rules:

- Use descriptive variable names: `left`, `right`, `count`, `result` -- not `a`, `b`, `c`, `x`
- Add a blank line between logical sections of your code
- Keep each line under about 80 characters
- Add a brief comment for anything non-obvious

**Example:**

```python
# BAD: even the person who wrote this will be confused in 2 minutes
def f(a, t):
    d = {}
    for i, v in enumerate(a):
        x = t - v
        if x in d:
            return [d[x], i]
        d[v] = i

# GOOD: anyone can read this, including future-you under pressure
def two_sum(nums, target):
    seen = {}  # Maps each number to its index

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index
```

Same logic. Same performance. But the second version is something you can debug at a glance when you're nervous and the clock is ticking.

&nbsp;

#### Mistake 10: Not Testing Your Code After Writing It

**The mistake:** You finish writing code and say "I think that's right" without actually tracing through it with an example.

**Why it's bad:** Interviewers expect you to verify your solution. Skipping this step signals overconfidence or carelessness. Plus, you miss bugs that a simple 30-second trace-through would have caught immediately.

**The fix:** After coding, pick a simple example and walk through your code line by line. Track the value of every variable at each step. Say it out loud:

> "Let me trace through with `nums = [2, 7, 11, 15]` and `target = 9`. Starting with an empty `seen` dictionary."
>
> "First loop: `index = 0`, `num = 2`, `complement = 9 - 2 = 7`. Is `7` in `seen`? No. Add `{2: 0}` to `seen`."
>
> "Second loop: `index = 1`, `num = 7`, `complement = 9 - 7 = 2`. Is `2` in `seen`? Yes, at index `0`. Return `[0, 1]`."
>
> "That matches the expected output. Let me also quickly check the edge case of `nums = [3, 3]`, `target = 6`..."

This takes 30-60 seconds and catches the vast majority of bugs.

&nbsp;

---

### Interview Mistakes

These happen during the interview itself. They're about **how you communicate** and **how you handle pressure**.

&nbsp;

#### Mistake 11: Being Silent

**The mistake:** You read the problem and go completely quiet for 5 minutes while you think. The interviewer sits there with no idea what's happening in your head.

**Why it's bad:** The interviewer can't give you helpful hints if they don't know what you're thinking. They also can't give you credit for your thought process if you don't share it. Five minutes of silence feels like five hours to everyone in the room.

**The fix:** Think out loud. Always. Even if your thoughts are messy and half-formed, say them:

> "Hmm, my first instinct is to use two nested loops, but that's O(n squared). Let me think if there's a way to avoid that..."
>
> "What if I used a hash map? For each number, I could check if its complement is already stored..."
>
> "Actually wait, I need to be careful about the order I add things to the map, so I don't accidentally use the same element twice..."

**The golden rule:** If you're thinking it, say it.

&nbsp;

#### Mistake 12: Not Asking Clarifying Questions

**The mistake:** The interviewer gives you a problem and you immediately start solving it without asking a single question.

**Why it's bad:** You might solve the wrong problem entirely. You also miss a golden opportunity to show the interviewer that you think carefully and communicate well before diving in. Not asking clarifying questions is actually a red flag for interviewers -- it suggests you make assumptions in real work too.

**The fix:** Always ask at least 2-3 clarifying questions. Here are reliable ones that work for almost any problem:

- "Can the input be empty or null?"
- "Are there duplicate values in the input?"
- "Can values be negative or zero?"
- "Is the input sorted?"
- "Should I return the values or their indices?"
- "What should I return if there's no valid answer?"
- "Can I assume the input always has a valid solution?"

Even if the answers seem obvious, asking shows professionalism and thoroughness.

&nbsp;

#### Mistake 13: Panicking When You Get Stuck

**The mistake:** You hit a wall, your mind goes blank, and you either freeze up completely or start rambling without direction.

**Why it's bad:** Everyone gets stuck sometimes. The interviewer knows this and expects it. What they're really evaluating is **how you handle it**. Freezing tells them you can't deal with ambiguity. Rambling tells them you can't organize your thoughts under pressure.

**The fix:** Have a script ready in your back pocket for when you're stuck:

> "I'm a bit stuck on the optimization here. Let me take a step back. What I know so far is that I need to find pairs that sum to the target. The bottleneck in my brute force is the inner search. Let me think about what data structure could speed that up..."

Other good moves when you're stuck:

- Go back to your example and trace through it again slowly
- Ask yourself: "What's the bottleneck? What operation is slow?"
- Think about which data structure could eliminate that bottleneck
- Ask yourself: "Have I seen a similar problem before? What pattern did it use?"
- It's perfectly okay to say: "I'm considering a few approaches. Could I get a small nudge on the direction?"

Asking for a hint is not a failure. Interviewers *want* to help you succeed.

&nbsp;

#### Mistake 14: Dismissing Your Brute Force Solution

**The mistake:** You can think of a brute force solution, but you don't mention it because you think it's "too simple" or "not impressive enough" for a FAANG interview.

**Why it's bad:** A working brute force solution is worth WAY more than no solution at all. Many candidates have received offers after implementing only the brute force but explaining clearly how they'd optimize it. Also, interviewers often specifically want to see you start with brute force and then improve -- that's the process they're evaluating.

**The fix:** Always state the brute force first:

> "The brute force approach would be to check every pair using two nested loops. That's O(n squared) time and O(1) space. Let me code this up first, and then we can discuss how to optimize."

Or, if time is short:

> "I can see a brute force O(n squared) solution using nested loops. I think we can optimize to O(n) using a hash map. Should I go straight to the optimized version, or would you like to see the brute force first?"

Either way, you've shown the interviewer you can think about the problem at multiple levels.

&nbsp;

#### Mistake 15: Not Analyzing Time and Space Complexity

**The mistake:** You finish your solution and just... stop. The interviewer asks "What's the time complexity?" and you freeze or guess.

**Why it's bad:** Complexity analysis is expected in every FAANG interview without exception. If you can't analyze your own code, it raises doubts about whether you truly understand what you wrote.

**The fix:** Practice saying complexity out loud after every single problem you solve during preparation. Use this simple framework:

1. **Time:** Count your loops. One loop over n elements = O(n). Two nested loops = O(n^2). A loop with binary search inside = O(n log n). For recursion, think about how many total calls are made.
2. **Space:** Count your data structures. A hash map storing up to n elements = O(n). Only using a few variables = O(1). A recursion stack going n levels deep = O(n).

**Example script (say this every time):**

> "The time complexity is O(n) because I iterate through the array exactly once, and each hash map lookup is O(1) on average."
>
> "The space complexity is O(n) because in the worst case, I store all n elements in the hash map before finding a valid pair."

If you say this after every practice problem, it'll be automatic by interview day.

&nbsp;

---

## Step-by-Step Example: Spotting and Fixing a Mistake

Let's walk through a real scenario where a beginner makes a common mistake and then fixes it step by step.

&nbsp;

### The Problem

**Two Sum (LeetCode #1):** Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

Example: `nums = [2, 7, 11, 15]`, `target = 9` --> return `[0, 1]`

&nbsp;

### The Beginner's First Attempt (Contains Mistakes #6 and #8)

```python
def twoSum(nums, target):
    # Check every pair (brute force)
    for i in range(len(nums)):
        for j in range(len(nums)):  # BUG #1: j starts at 0!
            if nums[i] + nums[j] == target:
                return [i, j]
```

**What goes wrong:**

- **Bug #1 (Off-by-one, Mistake #6):** When `i = 0` and `j = 0`, we check `nums[0] + nums[0] = 2 + 2 = 4`. We're adding a number to *itself*. If the target happened to be `4`, we'd return `[0, 0]` -- using the same element twice, which isn't allowed.
- **Bug #2 (Wrong data structure, Mistake #8):** Even after fixing the loop, this is O(n^2). A hash map would make it O(n).

&nbsp;

### The Fix (Step by Step)

**Step 1:** Fix the off-by-one error. Make `j` start at `i + 1` so we never compare an element with itself, and never check the same pair twice:

```python
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # Fixed: j always comes after i
            if nums[i] + nums[j] == target:
                return [i, j]
```

This works correctly now, but it's O(n^2). Let's optimize.

**Step 2:** Use the right data structure. A hash map lets us search for the complement in O(1) instead of O(n):

```python
def twoSum(nums, target):
    seen = {}  # Maps each number to its index

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index
```

**Step 3:** Verify with the example.

```
nums = [2, 7, 11, 15], target = 9

index=0: num=2, complement=7, seen={} --> 7 not found, add {2: 0}
index=1: num=7, complement=2, seen={2: 0} --> 2 found at index 0! Return [0, 1]

Output: [0, 1] -- Correct!
```

**Step 4:** Check an edge case.

```
nums = [3, 3], target = 6

index=0: num=3, complement=3, seen={} --> 3 not found, add {3: 0}
index=1: num=3, complement=3, seen={3: 0} --> 3 found at index 0! Return [0, 1]

Output: [0, 1] -- Correct! (Uses two different elements.)
```

---

## Interview Talk Track

Here's what it sounds like when you handle mistakes well in an interview:

> **When you catch your own mistake:**
> "Actually, wait -- I just realized my inner loop starts at 0, which means I might compare an element with itself. Let me fix that by starting `j` at `i + 1`. Good catch by me."

> **When the interviewer points out a mistake:**
> "Oh, you're right -- I missed that edge case. Thank you. Let me add a check for that at the top of the function... there. Now it handles empty input correctly."

> **When discussing your growth:**
> "The biggest mistakes I've learned to avoid are: jumping into code without a plan, ignoring edge cases, and staying silent when I'm thinking. I now always start by clarifying the problem, planning my approach, and thinking out loud throughout."

Owning your mistakes calmly and fixing them quickly is actually *more* impressive to interviewers than never making mistakes at all.

---

## Complexity: How Complexity Mistakes Happen

This file isn't about a specific algorithm, so there's no single complexity to analyze. But since "forgetting to analyze complexity" and "getting complexity wrong" are both in our top 15 mistakes, let's cover the most common ways people mess up complexity analysis.

&nbsp;

### The Most Common Complexity Mistakes

| What You Think | What's Actually Happening | The Reality |
|----------------|--------------------------|-------------|
| "My solution is O(n)" | You have a loop inside a loop | It's actually O(n^2) |
| "Hash map lookup is O(1)" | You're using a list, not a set or dict | Lookup in a list is O(n) |
| "Sorting is O(n)" | No, sorting is O(n log n) | Almost always O(n log n) |
| "Recursion is O(n)" | Each call branches into 2 calls | It's O(2^n) without memoization |
| "My space is O(1)" | You're building a string in a loop | Strings are immutable; O(n) per concatenation |

&nbsp;

### Quick Complexity Reference

| Operation | Time Complexity |
|-----------|----------------|
| Accessing an array element by index | O(1) |
| Searching in an unsorted array | O(n) |
| Searching in a sorted array (binary search) | O(log n) |
| Inserting / searching in a hash map or set | O(1) average |
| Sorting an array | O(n log n) |
| Checking all pairs in an array | O(n^2) |
| All subsets of a set with n elements | O(2^n) |
| All permutations of n elements | O(n!) |

&nbsp;

### How to Avoid Complexity Mistakes

1. **Count your loops.** One loop = O(n). Two nested loops = O(n^2). A loop with binary search inside = O(n log n). It's usually that simple.

2. **Check your data structures.** `if x in my_list` is O(n). `if x in my_set` is O(1). This one difference can change your entire solution's performance.

3. **Watch for hidden loops.** These Python operations have hidden O(n) costs:
   - String concatenation in a loop (`result += char` creates a new string each time)
   - `list.remove(value)` searches the list first -- O(n)
   - `list.insert(0, value)` shifts all elements -- O(n)
   - Slicing: `nums[1:]` creates a copy -- O(n)

4. **For recursion, draw the call tree.** How many total nodes does the tree have? That's your time complexity. If each call makes 2 sub-calls and the depth is n, that's 2^n nodes -- which is very slow.

---

## Quick Reference: All 15 Mistakes at a Glance

| # | Category | Mistake | One-Line Fix |
|---|----------|---------|-------------|
| 1 | Thinking | Jumping straight into code | Always plan for 3-5 min before coding |
| 2 | Thinking | Not understanding the problem | Ask clarifying questions first |
| 3 | Thinking | Skipping brute force | Start simple, then optimize |
| 4 | Thinking | Ignoring edge cases | List edge cases before writing code |
| 5 | Thinking | Not recognizing the pattern | Use the Pattern Recognition Map |
| 6 | Coding | Off-by-one errors | Trace loop boundaries with a 2-3 element example |
| 7 | Coding | Modifying while iterating | Build a new collection instead |
| 8 | Coding | Wrong data structure | Use set for lookup, dict for mapping, list for order |
| 9 | Coding | Messy, unreadable code | Descriptive names + whitespace + short lines |
| 10 | Coding | Not testing after coding | Trace through with a small example out loud |
| 11 | Interview | Being silent | If you're thinking it, say it |
| 12 | Interview | Not asking clarifying questions | Ask at least 2-3 before solving |
| 13 | Interview | Panicking when stuck | Use the "I'm stuck" script (see above) |
| 14 | Interview | Dismissing brute force | A working solution always beats no solution |
| 15 | Interview | Skipping complexity analysis | State time and space after every solution |

---

## What's Next?

Now that you know the mistakes to avoid, learn the process that keeps you on track.

Go to: [04_interview_workflow_template.md](04_interview_workflow_template.md)

---

*You're going to make some of these mistakes. That's okay. The fact that you read this page means you'll catch them faster than most people ever do. Keep going -- you're doing great.*
