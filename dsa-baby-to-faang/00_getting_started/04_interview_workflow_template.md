# Interview Workflow Template

> A coding interview is like a cooking show -- the audience (your interviewer) cares just as much about *how* you cook as the final dish. This template is your recipe for every single interview.

---

## Baby Explanation (ELI10)

Imagine you're showing someone how to build a LEGO set. You wouldn't just dump all the pieces on the floor and start jamming them together randomly, right? You'd:

1. Look at the picture on the box (understand what you're building)
2. Sort through the pieces (understand your inputs)
3. Follow the instructions step by step (have a plan)
4. Check your work as you go (test along the way)

A coding interview works exactly the same way. The interviewer doesn't just want to see the finished LEGO set -- they want to see that you can follow a clear, organized process to get there.

This 7-step template works for **any** coding problem. Practice it with every single problem you solve, and by interview day, it'll feel as natural as breathing.

- **Step 1-4** are about **thinking and planning** (before you write code)
- **Step 5** is about **coding** (the actual implementation)
- **Step 6-7** are about **verifying** (making sure it works)

Most beginners spend all their time on Step 5 and skip everything else. The best candidates spend almost *half* their time on Steps 1-4. That's the secret.

---

## The 7-Step Interview Workflow

&nbsp;

---

### Step 1: Clarify the Problem (3-5 minutes)

**What to do:**

Read the problem carefully. Then restate it in your own words to make sure you understand. Ask questions about anything that's unclear or ambiguous.

**Questions you should always ask:**

- "Can the input be empty or null?"
- "Are there duplicate values?"
- "Can values be negative or zero?"
- "Is the input sorted?"
- "Should I return indices or values?"
- "Is there always exactly one valid answer, or could there be multiple (or none)?"
- "What are the size constraints? How large can the input be?"

**What to say:**

> "Before I dive in, let me make sure I understand the problem correctly. I'm given [describe input], and I need to return [describe output]. Let me ask a few questions..."

**Time: 3-5 minutes**

**Why this matters:** Asking good questions shows the interviewer you're thoughtful and careful. It also prevents you from solving the wrong problem -- which wastes your entire interview.

**Example script for Two Sum:**

> "So I'm given an array of integers and a target number. I need to find two numbers in the array that add up to the target and return their indices. A few questions:
> - Can I assume there's always exactly one valid pair? [Interviewer: Yes]
> - Can I use the same element twice? [Interviewer: No]
> - Can the array be empty? [Interviewer: No, at least 2 elements]
> - Can there be negative numbers? [Interviewer: Yes]
> - Great, thank you. Let me work through an example."

&nbsp;

---

### Step 2: Work Through Examples (2-3 minutes)

**What to do:**

Take the given example (or create your own) and walk through it by hand. Don't write any code yet -- just trace through the logic with your brain.

If possible, try a second example that's slightly different from the first (a different size, or with an edge case).

**What to say:**

> "Let me trace through this example to build my intuition."

**Time: 2-3 minutes**

**Why this matters:** Working through examples by hand often reveals the pattern. It also catches misunderstandings early, before you've invested time in coding.

**Example script for Two Sum:**

> "Let me trace through the example. Input: `nums = [2, 7, 11, 15]`, `target = 9`.
>
> I need two numbers that add up to 9.
> - 2 + 7 = 9. That works!
> - So the answer is indices [0, 1].
>
> Let me try another example to make sure I get it. `nums = [3, 2, 4]`, `target = 6`.
> - 3 + 2 = 5, nope.
> - 3 + 4 = 7, nope.
> - 2 + 4 = 6. That works!
> - Answer: indices [1, 2].
>
> Okay, I understand the problem. Let me think about the approach."

&nbsp;

---

### Step 3: Identify the Pattern (2-3 minutes)

**What to do:**

Based on your understanding of the problem and the examples, figure out which algorithm pattern applies. Use the Pattern Recognition Map from the README if you need help.

**Key questions to ask yourself:**

- Is this about searching in sorted data? --> Binary Search
- Is this about subarrays or substrings? --> Sliding Window
- Is this about a tree or graph? --> DFS or BFS
- Is this about optimization with overlapping choices? --> DP
- Do I need fast lookup? --> Hash Map

**What to say:**

> "This reminds me of a [pattern] problem because [reason]. Let me think about how to apply that here."

**Time: 2-3 minutes**

**Why this matters:** Identifying the right pattern is what separates someone who "gets" algorithms from someone who's just memorized solutions. Once you name the pattern, the solution often writes itself.

**Example script for Two Sum:**

> "I need to find if a specific value exists in a collection quickly. For each number, I want to check if its complement -- that's `target minus the current number` -- has already appeared.
>
> Checking if something exists quickly... that sounds like a hash map problem. I can store each number as I see it, and for every new number, check if its complement is already in the map. That gives me O(1) lookup.
>
> This is a classic hash map lookup pattern."

&nbsp;

---

### Step 4: Plan the Approach (3-5 minutes)

**What to do:**

Describe your algorithm step by step in plain English (or pseudocode). Do NOT start coding yet. Explain the approach clearly enough that the interviewer can follow.

This is also a great time to state the expected time and space complexity of your approach.

**What to say:**

> "Here's my plan, step by step:
> 1. [First thing I'll do]
> 2. [Second thing I'll do]
> 3. [How I'll handle the core logic]
> 4. [What I'll return]
>
> This should be O([time]) time and O([space]) space."

**Time: 3-5 minutes**

**Why this matters:** This is the **most important step**. If there's a flaw in your approach, the interviewer will often point it out *now*, saving you 15 minutes of coding a wrong solution. Also, having a clear plan makes the actual coding much faster and cleaner.

**Example script for Two Sum:**

> "Here's my plan:
> 1. Create an empty hash map called `seen` that maps numbers to their indices.
> 2. Loop through the array. For each number, calculate `complement = target - number`.
> 3. Check if the complement is already in the hash map.
>    - If yes: we found our pair! Return the stored index and the current index.
>    - If no: add the current number and its index to the hash map, then continue.
> 4. This processes each element at most once, so it's O(n) time. The hash map can hold up to n elements, so it's O(n) space.
>
> Does that approach sound reasonable, or would you suggest a different direction?"

That last question is a power move. It invites the interviewer to course-correct before you invest time coding.

&nbsp;

---

### Step 5: Code It Clean (15-20 minutes)

**What to do:**

Now translate your plan into actual code. Write clean, readable code. Use descriptive variable names. Add a brief comment for anything non-obvious.

**Important:** Narrate as you code. Don't go silent.

**What to say while coding:**

> "I'm starting by initializing my hash map..."
> "Now I'm looping through the array with `enumerate` so I get both the index and value..."
> "Here I calculate the complement..."
> "This condition checks if we've already seen the complement..."

**Time: 15-20 minutes**

**Coding tips:**

- Use descriptive names: `seen`, `complement`, `result` -- not `d`, `x`, `r`
- Add whitespace between logical sections
- Write helper functions if any section gets too long
- If you're unsure about syntax, say so: "I believe the syntax is X, let me double-check..."

**Example code for Two Sum:**

```python
def twoSum(nums, target):
    seen = {}  # Maps each number to its index

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index

    return []  # No valid pair found (shouldn't happen per problem constraints)
```

**What to say after writing:**

> "Alright, I have my solution written out. Let me walk through it with an example to make sure it's correct."

&nbsp;

---

### Step 6: Test with Examples (3-5 minutes)

**What to do:**

Pick a small example and trace through your code line by line. Track the value of every variable at each step. Do this out loud.

Then check at least one edge case.

**What to say:**

> "Let me trace through my code with the example to verify it works."

**Time: 3-5 minutes**

**Why this matters:** This step catches bugs that a quick glance would miss. It also shows the interviewer you're thorough and don't just assume your code is correct.

**Example script for Two Sum:**

> "Let me walk through with `nums = [2, 7, 11, 15]`, `target = 9`.
>
> `seen` starts empty: `{}`
>
> **Iteration 1:** `index = 0`, `num = 2`, `complement = 9 - 2 = 7`
> Is `7` in `seen`? No. (`seen` is empty.)
> Add to `seen`: `{2: 0}`
>
> **Iteration 2:** `index = 1`, `num = 7`, `complement = 9 - 7 = 2`
> Is `2` in `seen`? Yes! It's at index `0`.
> Return `[0, 1]`.
>
> That's the expected answer. Let me check one more case.
>
> Edge case: `nums = [3, 3]`, `target = 6`
>
> **Iteration 1:** `index = 0`, `num = 3`, `complement = 3`
> Is `3` in `seen`? No.
> Add: `{3: 0}`
>
> **Iteration 2:** `index = 1`, `num = 3`, `complement = 3`
> Is `3` in `seen`? Yes, at index `0`.
> Return `[0, 1]`.
>
> Correct! It handles duplicates properly because we check *before* we add the current number."

&nbsp;

---

### Step 7: Analyze Complexity (1-2 minutes)

**What to do:**

State the time complexity and space complexity of your solution. Give a brief justification for each.

**What to say:**

> "Let me analyze the complexity of my solution."

**Time: 1-2 minutes**

**Template:**

> "The **time complexity** is O([X]) because [reason]."
>
> "The **space complexity** is O([X]) because [reason]."

**Example script for Two Sum:**

> "The time complexity is O(n), where n is the length of the input array. I iterate through the array exactly once, and each hash map lookup and insertion is O(1) on average.
>
> The space complexity is O(n) because in the worst case, I store almost all n elements in the hash map before finding the valid pair.
>
> Is there anything you'd like me to optimize further, or any edge cases you'd like me to handle?"

That closing question shows confidence and invites follow-up discussion.

&nbsp;

---

## Time Budget at a Glance (45-Minute Interview)

```
+------------------------+----------+-------------------------+
| Step                   | Time     | What You're Doing       |
+------------------------+----------+-------------------------+
| 1. Clarify             | 3-5 min  | Understanding + asking  |
| 2. Examples            | 2-3 min  | Tracing by hand         |
| 3. Identify Pattern    | 2-3 min  | Naming the approach     |
| 4. Plan                | 3-5 min  | Pseudocode / explain    |
| 5. Code                | 15-20 min| Writing clean code      |
| 6. Test                | 3-5 min  | Tracing through code    |
| 7. Complexity          | 1-2 min  | Time + space analysis   |
| Buffer / Follow-up     | 3-5 min  | Questions / optimization|
+------------------------+----------+-------------------------+
| TOTAL                  | ~40 min  | (5 min buffer)          |
+------------------------+----------+-------------------------+
```

Notice that Steps 1-4 take about **10-15 minutes** combined. That's a lot of time before you write any code! But this investment pays off enormously. A clear plan means faster coding and fewer bugs.

---

## Full Walkthrough: Two Sum from Start to Finish

Here's what the entire interview looks and sounds like when you follow all 7 steps. Read this several times until it feels natural.

&nbsp;

**Interviewer:** "Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`."

&nbsp;

**You (Step 1 -- Clarify):**

> "Thank you. Let me make sure I understand. I'm given an array of integers and a target number. I need to find exactly two numbers in the array that add up to the target, and I return their indices -- not the numbers themselves.
>
> A few questions:
> - Can I assume there's always exactly one valid pair? *(Interviewer: Yes)*
> - Can I use the same element twice? *(Interviewer: No, must be two different elements)*
> - Can the array be empty? *(Interviewer: No, at least 2 elements)*
> - Can numbers be negative? *(Interviewer: Yes)*
> - Great. Thank you."

&nbsp;

**You (Step 2 -- Examples):**

> "Let me trace through an example. With `nums = [2, 7, 11, 15]` and `target = 9`:
> - I need two numbers summing to 9.
> - 2 + 7 = 9. Found it.
> - Answer: indices `[0, 1]`.
>
> Let me also think of a trickier case: `nums = [3, 2, 4]`, `target = 6`.
> - 3 + 2 = 5, no.
> - 3 + 4 = 7, no.
> - 2 + 4 = 6, yes!
> - Answer: `[1, 2]`."

&nbsp;

**You (Step 3 -- Pattern):**

> "For each number, I need to check if its complement exists in the array. The key operation is 'fast lookup.' That points me to a hash map.
>
> This is a hash map lookup pattern."

&nbsp;

**You (Step 4 -- Plan):**

> "Here's my plan:
> 1. Create an empty hash map mapping values to indices.
> 2. Loop through the array.
> 3. For each number, compute `complement = target - number`.
> 4. If the complement is in the map, return both indices.
> 5. Otherwise, store the current number and index in the map.
>
> Time: O(n) -- single pass through the array.
> Space: O(n) -- for the hash map.
>
> Does this approach sound good?"

*(Interviewer nods or says "Go ahead.")*

&nbsp;

**You (Step 5 -- Code):**

> "Great, let me code this up."

```python
def twoSum(nums, target):
    seen = {}  # Maps value -> index

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index

    return []  # Fallback (problem guarantees a solution exists)
```

> "I'm using `enumerate` to get both the index and value. I calculate the complement, check if it's in my map, and either return the answer or add the current number to the map."

&nbsp;

**You (Step 6 -- Test):**

> "Let me trace through with `nums = [2, 7, 11, 15]`, `target = 9`.
>
> `seen = {}`
> - `i=0, num=2, complement=7` -- not in seen -- `seen = {2: 0}`
> - `i=1, num=7, complement=2` -- 2 IS in seen at index 0 -- return `[0, 1]`
>
> Correct!
>
> Quick edge case: `nums = [3, 3], target = 6`.
> - `i=0, num=3, complement=3` -- not in seen -- `seen = {3: 0}`
> - `i=1, num=3, complement=3` -- 3 IS in seen at index 0 -- return `[0, 1]`
>
> Correct! Handles duplicates because we check before adding."

&nbsp;

**You (Step 7 -- Complexity):**

> "Time complexity: O(n). We iterate through the array once, and each hash map operation is O(1) average.
>
> Space complexity: O(n). The hash map stores at most n elements.
>
> Is there anything you'd like me to adjust or any follow-up?"

&nbsp;

**That's it.** Clean, organized, confident. This is what a strong interview looks like.

---

## Common Variations

Real interviews don't always go perfectly. Here's how to handle the most common curveballs.

&nbsp;

### What If You're Stuck?

Don't panic. This happens to everyone. Use this script:

> "I don't see the optimal approach yet, so let me start with what I know. The brute force would be [describe it]. That's O([complexity]). Let me think about what the bottleneck is and whether a different data structure could help..."

Other strategies:
- Go back to your example and trace through it more carefully
- Think out loud about what's slow and what data structure could speed it up
- It's totally fine to say: "I have a few ideas but I'm not sure which is best. Could you point me in a direction?"

**Remember:** Getting a hint is not failure. Taking a hint gracefully and running with it is a strong signal.

&nbsp;

### What If the Interviewer Gives a Hint?

Accept it gratefully and build on it:

> "That's a great hint, thank you. So you're suggesting I think about using a [data structure/approach]. Let me see how that applies here..."

Then connect the hint to your solution. Don't just ignore hints or feel embarrassed. The interviewer is on your side.

&nbsp;

### What If Your Solution Is Brute Force?

That's okay! A working solution is always better than no solution. Frame it like this:

> "I have a working solution here at O(n squared). I believe we can optimize this to O(n) using a hash map to avoid the inner search. Would you like me to implement the optimized version, or should we discuss the approach first?"

This shows you understand the performance issue and know the path forward, even if you started simple.

&nbsp;

### What If You Make a Bug During Coding?

Stay calm. Bugs are normal.

> "Hmm, I see an issue here -- my loop boundary is off. Let me fix that... I should use `range(len(nums) - 1)` instead of `range(len(nums))` because I'm accessing `i + 1` inside the loop. There, fixed."

Catching and fixing your own bugs is actually *impressive*. It shows you can debug under pressure.

&nbsp;

### What If You Run Out of Time?

If you're running low on time:

> "I'm running a bit short on time, so let me quickly describe how I'd finish this. The remaining part would [describe]. The overall complexity would be O(n) time and O(n) space."

Showing that you know the complete solution, even if you can't fully code it, still earns significant credit.

---

## Top 5 Mistakes in the Interview Workflow

| # | Mistake | What to Do Instead |
|---|---------|-------------------|
| 1 | **Coding before planning** | Spend 10 minutes planning to save 20 minutes debugging. The plan is the most important step. |
| 2 | **Going silent** | Think out loud at all times. Even "Hmm, I'm considering whether to use a hash map or sorting..." is valuable. |
| 3 | **Skipping the test step** | Always trace through your code with at least one example. It takes 60 seconds and catches most bugs. |
| 4 | **Not stating complexity** | Always end with "Time is O(X) because... Space is O(X) because..." Make it automatic. |
| 5 | **Panicking when stuck** | Breathe. Go back to your example. Name the bottleneck. Ask for a nudge if needed. Calm problem-solving is more impressive than instant genius. |

---

## Complexity

This file is about your interview *process*, not a specific algorithm. So there's no single Big O to analyze here.

But here's the "complexity" of the workflow itself:

- **Time investment:** Practice this workflow with 15-20 problems and it becomes second nature. That's about 2-3 days of focused practice.
- **Return on investment:** Following a consistent workflow can dramatically improve your interview performance, even with the same level of algorithm knowledge. Structure and communication are half the battle.
- **What interviewers are really measuring:**
  - Can you break down a problem? (Steps 1-3)
  - Can you communicate a plan? (Step 4)
  - Can you write clean code? (Step 5)
  - Can you verify your work? (Step 6)
  - Do you understand performance? (Step 7)

The 7-step workflow hits every single one of these signals. That's why it works.

---

## Talk Track Quick Reference

Keep these phrases in your back pocket for interview day:

**Starting the problem:**
> "Let me make sure I understand the problem correctly..."

**After clarifying:**
> "Great. Let me trace through an example to build my intuition."

**Identifying the pattern:**
> "This feels like a [pattern] problem because [reason]."

**Before coding:**
> "Here's my plan: First I'll... then I'll... and finally I'll..."

**While coding:**
> "I'm initializing a hash map here to store... Now I'm looping through..."

**After coding:**
> "Let me verify by walking through a test case."

**Stating complexity:**
> "Time complexity is O(n) because... Space is O(n) because..."

**When stuck:**
> "I'm not seeing the optimal solution yet. Let me start with brute force and look for where to optimize."

**Closing:**
> "Is there anything you'd like me to optimize, or any edge cases you'd like to discuss?"

---

## What's Next?

You now have the process. Time to learn the patterns!

Go to: [../01_core_patterns/01_arrays_and_hashing.md](../01_core_patterns/01_arrays_and_hashing.md)

---

*Practice this workflow with every single problem you solve. By interview day, it will feel as natural as riding a bike -- and you won't even have to think about it. You'll just do it.*
