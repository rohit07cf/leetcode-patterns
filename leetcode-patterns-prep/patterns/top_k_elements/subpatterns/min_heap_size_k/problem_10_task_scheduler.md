# Task Scheduler

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Min Heap of Size K
**Link:** https://leetcode.com/problems/task-scheduler/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of CPU tasks (uppercase letters) and a cooldown integer `n`, find the **minimum number of intervals** the CPU needs to complete all tasks. The same task must be separated by at least `n` intervals. The CPU can idle during intervals.

### 2. Clarification Questions

- **Input constraints?** `1 <= tasks.length <= 10^4`, tasks are uppercase letters (A-Z), `0 <= n <= 100`.
- **Edge cases?** `n = 0` (no cooldown, answer = len(tasks)); all tasks identical; all tasks distinct.
- **Expected output?** A single integer — minimum total intervals.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Simulate the schedule: each interval, pick the most frequent available task (greedy), track cooldowns.
- **Time:** O(total_intervals * 26)
- **Space:** O(26)

### 4. Optimized Approach

- 💡 **Core Insight:** Use a **max heap** to always pick the most frequent available task (greedy minimizes idle time). Use a **cooldown queue** to hold tasks that are on cooldown. Each cycle of `n + 1` slots, pop from the heap, execute tasks, and track when they become available again.
- **Time:** O(total_intervals)
- **Space:** O(26) = O(1)

**Mathematical shortcut:**

- 💡 Let `f_max` = highest frequency, `count_max` = number of tasks with that frequency.
- Formula: `max(len(tasks), (f_max - 1) * (n + 1) + count_max)`

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Simulation (heap) | O(total_intervals) | O(26) | Clear, models the actual schedule |
| Math formula | O(n) | O(26) | **Fastest, one pass for counting** |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

**Approach 1: Heap Simulation (demonstrates the pattern)**

- Use a max heap of task counts and a cooldown queue.
- Each time unit: pop from heap, decrement count, put on cooldown with a ready-time.
- When a task's ready-time arrives, push it back onto the heap.

```python
import heapq
from collections import Counter, deque

def leastInterval(tasks, n):
    freq = Counter(tasks)

    # Max heap of remaining counts (negated)
    heap = [-count for count in freq.values()]
    heapq.heapify(heap)

    # Cooldown queue: (ready_time, neg_remaining_count)
    cooldown = deque()
    time = 0

    while heap or cooldown:
        time += 1

        if heap:
            neg_count = heapq.heappop(heap)
            remaining = neg_count + 1  # Decrement (add 1 since negated)
            if remaining < 0:
                # Task still has executions left — put on cooldown
                cooldown.append((time + n, remaining))

        # Check if front of cooldown queue is ready
        if cooldown and cooldown[0][0] == time:
            _, neg_count = cooldown.popleft()
            heapq.heappush(heap, neg_count)

    return time
```

**Approach 2: Math Formula (optimal)**

```python
from collections import Counter

def leastInterval_math(tasks, n):
    freq = Counter(tasks)
    f_max = max(freq.values())
    # Count how many tasks share the max frequency
    count_max = sum(1 for f in freq.values() if f == f_max)

    # (f_max - 1) full blocks of (n + 1) + count_max for the last partial block
    # But never less than len(tasks) (when no idle time needed)
    return max(len(tasks), (f_max - 1) * (n + 1) + count_max)
```

---

## PHASE 3 — AFTER CODING

### Dry Run (Math approach)

`tasks = ["A","A","A","B","B","B"], n = 2`

- Frequencies: `{'A': 3, 'B': 3}`
- `f_max = 3`, `count_max = 2`
- Formula: `max(6, (3 - 1) * (2 + 1) + 2) = max(6, 8) = 8`
- Schedule: `A B _ A B _ A B` → 8 intervals ✓

### Dry Run (Heap approach)

1. Heap: `[-3, -3]`, time=0
2. time=1: pop -3 → remaining -2, cooldown: `[(3, -2)]`. Heap: `[-3]`
3. time=2: pop -3 → remaining -2, cooldown: `[(3,-2),(4,-2)]`. Heap: `[]`
4. time=3: heap empty → idle. Cooldown front ready (time=3) → push -2. Heap: `[-2]`
5. time=4: pop -2 → remaining -1, cooldown: `[(4,-2),(6,-1)]`. Front ready → push -2. Heap: `[-2]`
6. time=5: pop -2 → remaining -1, cooldown: `[(6,-1),(7,-1)]`. Heap: `[]`
7. time=6: idle. Front ready → push -1. Heap: `[-1]`
8. time=7: pop -1 → remaining 0 (done). Front ready → push -1. Heap: `[-1]`
9. time=8: pop -1 → remaining 0. Done. Return `8` ✓

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `tasks = ["A"], n = 5` → `max(1, 0 * 6 + 1) = 1`.
- **Typical case:** Covered in dry run.
- **Extreme values:** `n = 0` → no cooldown → answer is simply `len(tasks)`.

### Complexity

**Heap approach:**
- **Time:** O(total_intervals) — each interval is one loop iteration with O(log 26) = O(1) heap ops.
- **Space:** O(26) = O(1) — heap and cooldown queue hold at most 26 task types.

**Math approach:**
- **Time:** O(n) — single pass to count frequencies.
- **Space:** O(26) = O(1).

### Optimization Discussion

- The **math formula** is the ideal interview answer for its simplicity and O(n) time.
- The **heap simulation** is valuable because it generalizes — if you need to output the actual schedule (not just the count), the simulation approach gives you the ordering.
- Interviewers often ask for both: formula first, then "what if you need the actual schedule?"

### Follow-up Variations

- **Output the actual schedule** — use the heap simulation and record which task runs each interval.
- **Rearrange String K Distance Apart** (LeetCode 358) — same cooldown idea applied to characters.
- **Different cooldown per task type** — requires a more complex simulation with per-task timers.

### ⚠️ Common Traps

- **Forgetting `max(len(tasks), ...)` in the formula.** When there are many distinct tasks and small n, no idle time is needed, so the answer is just `len(tasks)`.
- **Off-by-one in the cooldown.** Cooldown of `n` means `n` intervals **between** same tasks, so the cycle length is `n + 1`.
- **Using the heap approach without the cooldown queue.** You need to track when each task becomes available again. Without the queue, you'd re-scan all tasks each interval.
