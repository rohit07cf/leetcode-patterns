# Partition Labels

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Partition Style
**Link:** https://leetcode.com/problems/partition-labels/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a string, partition it into as many parts as possible so that **each letter appears in at most one part**. Return the sizes of these parts.

### 2. Clarification Questions

- **Input constraints?** String length 1–500, lowercase English letters only.
- **Edge cases?** Single character; all same characters; all unique characters.
- **Expected output?** List of integers representing partition sizes.
- **Can input be modified?** Not needed; we just read the string.

### 3. Brute Force Approach

- **Idea:** For each starting position, try all possible end positions. Check if the partition is valid (no character appears outside it). Greedily pick the smallest valid partition.
- **Time:** O(n²) or worse with validation.
- **Space:** O(1) extra (beyond output).

### 4. Optimized Approach

- 💡 **Core Insight:** Precompute the **last occurrence** of each character. Then scan left to right, maintaining the **farthest reach** of the current partition. When the scan index equals the farthest reach, we've found a partition boundary — every character inside has its last occurrence within this segment.
- **Time:** O(n)
- **Space:** O(1) — fixed 26-char map.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force validation | O(n²) | O(1) | Repeated scanning |
| Last-occurrence greedy | O(n) | O(1) | Two passes, optimal |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Pass 1:** Build a map of each character's last index.
- **Pass 2:** Track `partition_end` (farthest last-occurrence seen so far) and `partition_start`. When `i == partition_end`, a complete partition is found.

```python
def partitionLabels(s: str) -> list[int]:
    # Last occurrence of each character
    last = {ch: i for i, ch in enumerate(s)}

    result = []
    partition_start = 0
    partition_end = 0

    for i, ch in enumerate(s):
        # Extend partition to include all occurrences of current char
        partition_end = max(partition_end, last[ch])

        if i == partition_end:
            # All chars in [partition_start..i] have their last occurrence here
            result.append(i - partition_start + 1)
            partition_start = i + 1

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `"ababcbacadefegdehijhklij"`

**Last occurrences:** a→8, b→5, c→7, d→14, e→15, f→11, g→13, h→19, i→22, j→23, k→20, l→21

| i | ch | partition_end | Action |
|---|----|---------------|--------|
| 0 | a | 8 | extend |
| 1 | b | 8 | no change |
| ... | | | |
| 8 | a | 8 | i == end → partition size = 9 |
| 9 | d | 14 | new partition starts |
| ... | | | |
| 15 | e | 15 | i == end → partition size = 7 |
| 16 | h | 19 | new partition starts |
| ... | | | |
| 23 | j | 23 | i == end → partition size = 8 |

Result: `[9, 7, 8]`

### Edge Case Testing

- **Empty input:** Not possible per constraints (length ≥ 1).
- **Single element:** `"a"` → `[1]`.
- **Typical case:** `"ababcbacadefegdehijhklij"` → `[9, 7, 8]`.
- **Extreme values:** All unique `"abcd"` → `[1, 1, 1, 1]`; all same `"aaaa"` → `[4]`.

### Complexity

- **Time:** O(n) — two linear passes.
- **Space:** O(1) — the `last` dictionary has at most 26 entries.

### Optimization Discussion

This is already optimal. The problem is a greedy interval-merging problem in disguise. Each character defines an interval `[first, last]` and we merge overlapping intervals.

### Follow-up Variations

- **Merge Intervals (LC 56)** — same underlying concept with explicit intervals.
- **Partition to minimize max partition size** — different objective, same precomputation.
- **Return the actual partitioned substrings** instead of sizes.

### ⚠️ Common Traps

- **Using first occurrence instead of last:** The partition boundary depends on the **last** occurrence of every character seen so far.
- **Off-by-one on partition size:** Size is `i - partition_start + 1`, not `i - partition_start`.
