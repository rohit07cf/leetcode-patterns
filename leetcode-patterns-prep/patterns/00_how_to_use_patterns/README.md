# How to Use Patterns

> Patterns are shortcuts. Instead of figuring out every problem from scratch, you recognize the *type* of problem and apply a known strategy.

---

## The Big Idea

Most LeetCode problems are variations of ~5-10 core patterns. Once you learn a pattern, you can solve dozens of problems that look completely different on the surface but share the same underlying structure.

```
Without patterns:  "I've never seen this problem before" → panic → brute force → TLE
With patterns:     "Oh, this is a sliding window" → template → adapt → accepted
```

---

## How to Learn a Pattern

### Step 1: Read the Pattern README
- Understand WHEN to use it (the triggers)
- Understand the CORE IDEA (what's actually happening)
- Read the TEMPLATE (this is your starting point for every problem)

### Step 2: Memorize the Template
- Write it from memory 3 times
- If you can't, read it again and try tomorrow
- The template should be muscle memory before you start solving problems

### Step 3: Solve 3 Easy Problems
- Use the template as your starting skeleton
- Don't look at solutions until you've spent at least 15 min stuck
- After solving, compare your code to the template — did you follow the pattern?

### Step 4: Review Your Mistakes
- Every mistake is a lesson. Write it down in `progress/tracker.md`
- Common mistakes are listed in each README — check if yours is there

### Step 5: Move to Medium Problems
- Same process, but expect to get stuck more
- Getting stuck is normal. Getting stuck on the same thing twice is the problem.

---

## How to Spot a Pattern in a New Problem

Ask yourself these questions (in order):

1. **Is it about a sorted array or searching?** → Binary Search
2. **Is it about a contiguous subarray/substring?** → Sliding Window
3. **Is it about pairs or comparing from both ends?** → Two Pointers
4. **Is it asking for "top K" or "Kth largest/smallest"?** → Heap / Top K
5. **Does it need custom ordering?** → Sorting

If none of these click, re-read the problem. The signal is usually in the constraints or the question phrasing.

---

## The Pattern Loop (Your Core Workflow)

```
    ┌──────────┐
    │  Learn   │ ← Read the README
    └────┬─────┘
         ▼
    ┌──────────┐
    │ Template │ ← Write from memory
    └────┬─────┘
         ▼
    ┌──────────┐
    │ Solve 3  │ ← Easy first, then medium
    └────┬─────┘
         ▼
    ┌──────────┐
    │ Review   │ ← Log mistakes, re-read pitfalls
    └────┬─────┘
         ▼
    ┌──────────┐
    │ Repeat   │ ← Next subpattern or harder problems
    └──────────┘
```

---

## Rules for Yourself

1. **Never solve a problem without identifying the pattern first.** Even if you're wrong, the act of guessing trains your pattern recognition.
2. **Template first, logic second.** Always start by writing the skeleton.
3. **Time yourself.** Easy = 15 min. Medium = 25 min. Hard = 40 min. If you exceed the limit, look at a hint (not the full solution).
4. **One pattern at a time.** Don't jump between patterns in the same session.
5. **Revision > new problems.** Re-solving a problem you struggled with last week is worth more than solving a new easy problem.
