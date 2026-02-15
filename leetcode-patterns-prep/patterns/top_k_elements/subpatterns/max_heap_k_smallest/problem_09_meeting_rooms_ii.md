# Meeting Rooms II

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Max Heap for K Smallest
**Link:** https://leetcode.com/problems/meeting-rooms-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of meeting time intervals `[start, end]`, find the **minimum number of conference rooms** required so that no two overlapping meetings share a room.

### 2. Clarification Questions

- **Input constraints?** 1 <= intervals.length <= 10^4, 0 <= start < end <= 10^6.
- **Edge cases?** Single meeting (1 room), no overlaps (1 room), all meetings overlap (n rooms).
- **Expected output?** A single integer — the minimum number of rooms.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** For each meeting, check against all other meetings for overlap. Track maximum concurrent meetings.
- **Time:** O(n^2)
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Sort meetings by start time. Use a **min heap** to track end times of ongoing meetings. The heap size at any point equals the number of rooms in use. Before assigning a new meeting, check if the earliest-ending meeting (heap root) has finished — if so, reuse that room (pop it). Always push the new meeting's end time. The **max heap size** reached is the answer. This is a "k smallest end times" problem — the heap maintains the k rooms with the smallest (earliest) end times.
- **Time:** O(n log n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force overlap check | O(n^2) | O(n) | Slow |
| Min heap of end times | O(n log n) | O(n) | Clean, intuitive |
| Chronological ordering (events) | O(n log n) | O(n) | Also optimal, different style |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort by start time.
- Min heap stores end times of active meetings.
- For each meeting: if `start >= heap[0]`, the earliest room is free — pop it.
- Push the current meeting's end time.
- Answer = max heap size seen (or final heap size, since we never pop prematurely).

```python
import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        # Sort by start time
        intervals.sort(key=lambda x: x[0])

        # Min heap of end times — each entry = one room in use
        rooms = []

        for start, end in intervals:
            # If earliest ending room is free, reuse it
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            # Allocate room for current meeting
            heapq.heappush(rooms, end)

        # Heap size = number of rooms needed
        return len(rooms)
```

**Alternative — event-based sweep line:**

```python
class Solution:
    def minMeetingRooms(self, intervals):
        events = []
        for start, end in intervals:
            events.append((start, 1))   # meeting starts
            events.append((end, -1))    # meeting ends

        events.sort()

        max_rooms = 0
        current = 0
        for _, delta in events:
            current += delta
            max_rooms = max(max_rooms, current)

        return max_rooms
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`intervals = [[0,30],[5,10],[15,20]]`

Sorted: [[0,30],[5,10],[15,20]]

- [0,30]: rooms empty → push 30 → rooms=[30], size=1
- [5,10]: rooms[0]=30 > 5, can't reuse → push 10 → rooms=[10,30], size=2
- [15,20]: rooms[0]=10 <= 15, reuse → pop 10, push 20 → rooms=[20,30], size=2

Answer: **2** ✓

### Edge Case Testing

- **Empty input:** Return 0 (handled by guard clause).
- **Single element:** One meeting → one room.
- **Typical case:** Mixed overlaps — heap tracks active rooms correctly.
- **Extreme values:** All meetings overlap → heap grows to n, answer = n.

### Complexity

- **Time:** O(n log n) — sorting + n heap operations at O(log n) each.
- **Space:** O(n) — heap can hold up to n end times.

### Optimization Discussion

The **sweep line** approach is equally optimal and sometimes preferred because it avoids the heap entirely. Both are O(n log n) due to sorting. The heap approach is more intuitive for "resource allocation" framing.

### Follow-up Variations

- **Meeting Rooms I (LC 252)** — just check if any meetings overlap (sort + compare consecutive).
- **Minimum Platforms (train station)** — identical problem, different story.
- **Car Pooling (LC 1094)** — sweep line with capacity constraint.

### ⚠️ Common Traps

- **Comparing `<` vs `<=`** — a meeting ending at time 10 and one starting at time 10 do **not** overlap. Use `rooms[0] <= start` (not `<`).
- **Not sorting by start time** — the greedy room reuse only works when meetings arrive in order.
- **Thinking the answer is just the max overlap count** — that's correct, but the heap naturally computes it; the final heap size equals the peak concurrency.
