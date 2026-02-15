# Partition Labels

**Difficulty:** Medium
**Pattern:** Sorting
**Subpattern:** Quick Sort / Partition
**Link:** https://leetcode.com/problems/partition-labels/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a string `s`, partition it into as many parts as possible so that each letter appears in **at most one part**. Return a list of the sizes of these parts.

### 2. Clarification Questions

- **Input constraints?** `1 <= s.length <= 500`, lowercase English letters only
- **Edge cases?** Single character string, all same characters, all unique characters
- **Expected output?** List of integers representing partition sizes
- **Can input be modified?** N/A (string is immutable in Python)

### 3. Brute Force Approach

- **Idea:** For each possible partition, check if any character appears in multiple partitions. Try all valid splits.
- **Time:** O(2^n) — exponential number of partition possibilities
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Track the **last occurrence** of each character. A partition ends when we reach a position where all characters seen so far have their last occurrence at or before this position. This is like a **greedy partition** — extend the boundary until all characters are contained.
- **Time:** O(n)
- **Space:** O(1) — at most 26 letters

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(2^n) | O(n) | Try all partitions |
| Optimized | O(n) | O(1) | Greedy with last-occurrence map |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Build a map of last occurrence index for each character
- Use a greedy scan: track the farthest `end` we must reach
- When current index equals `end`, we've found a partition boundary

```python
def partitionLabels(s: str) -> list[int]:
    # Precompute last occurrence of each character
    last = {ch: i for i, ch in enumerate(s)}

    result = []
    start = 0
    end = 0

    for i, ch in enumerate(s):
        # Extend partition to include all of current char's occurrences
        end = max(end, last[ch])

        if i == end:
            # All chars in [start..end] are fully contained
            result.append(end - start + 1)
            start = i + 1

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `"ababcbacadefegdehijhklij"`

- last: `{a:8, b:5, c:7, d:14, e:15, f:11, g:13, h:19, i:22, j:23, k:20, l:21}`
- i=0 'a': end=8 → keep going
- i=8 'a': end=8, i==end → partition size = 9
- i=9 'd': end=14
- i=15 'e': end=15, i==end → partition size = 7
- i=16 'h': end=19
- i=23 'j': end=23, i==end → partition size = 8
- Result: `[9, 7, 8]`

### Edge Case Testing

- **Empty input:** Not possible per constraints
- **Single element:** `"a"` → `[1]`
- **Typical case:** `"ababcbacadefegdehijhklij"` → `[9, 7, 8]`
- **All same:** `"aaaa"` → `[4]`

### Complexity

- **Time:** O(n) — two passes: one to build last map, one to scan
- **Space:** O(1) — at most 26 entries in the map

### Optimization Discussion

Already optimal at O(n). Could combine into a single pass but readability is more important in interviews.

### Follow-up Variations

- **Merge Intervals version:** Convert each char's range to an interval `[first, last]`, then merge overlapping intervals
- **Return the partition strings** instead of sizes
- **Minimize number of partitions** instead of maximizing (trivially 1 partition)

### ⚠️ Common Traps

- Forgetting to **extend** `end` with `max()` — each new character may push the boundary further
- Off-by-one: partition size is `end - start + 1`, not `end - start`
- Not recognizing this as a **greedy** problem — tempting to use backtracking
