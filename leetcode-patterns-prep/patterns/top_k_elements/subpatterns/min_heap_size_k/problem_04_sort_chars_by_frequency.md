# Sort Characters By Frequency

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Min Heap of Size K
**Link:** https://leetcode.com/problems/sort-characters-by-frequency/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a string `s`, sort it in **decreasing order** based on the frequency of its characters. If multiple characters have the same frequency, their relative order doesn't matter. Return the sorted string.

### 2. Clarification Questions

- **Input constraints?** `1 <= s.length <= 5 * 10^5`, upper/lowercase letters and digits.
- **Edge cases?** All characters identical; all characters unique (each appears once); ties in frequency.
- **Expected output?** A string with characters grouped and ordered by frequency.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Count character frequencies, sort all characters by frequency descending, rebuild the string.
- **Time:** O(n + u log u) where u = unique characters
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Use a **max heap** (all unique characters pushed with frequency). Since we need **all** characters sorted by frequency (not just top k), we extract them one by one. This is a heap-sort on frequencies. The "size k" insight applies when the alphabet is bounded — at most 62 unique characters (a-z, A-Z, 0-9), so the heap is tiny.
- **Time:** O(n + u log u) — but u ≤ 62, so effectively O(n)
- **Space:** O(n) for the output string

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort all chars | O(n log n) | O(n) | Sorts every character position |
| Heap on frequencies | O(n + u log u) | O(n) | **u ≤ 62, so heap ops are constant** |
| Bucket sort | O(n) | O(n) | Optimal, buckets indexed by frequency |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Count frequencies with a hash map.
- Push all `(-count, char)` pairs into a max heap (negate for max behavior).
- Pop from heap, append `char * count` to result.

```python
import heapq
from collections import Counter

def frequencySort(s):
    freq = Counter(s)

    # Max heap by frequency (negate count for max-heap behavior)
    heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(heap)

    result = []
    while heap:
        neg_count, char = heapq.heappop(heap)
        # Append character repeated by its frequency
        result.append(char * (-neg_count))

    return ''.join(result)
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`s = "tree"`

Frequencies: `{'t': 1, 'r': 1, 'e': 2}`

1. Heap after heapify: `[(-2, 'e'), (-1, 'r'), (-1, 't')]`
2. Pop `(-2, 'e')` → append `"ee"`
3. Pop `(-1, 'r')` → append `"r"`
4. Pop `(-1, 't')` → append `"t"`
5. Result: `"eert"` ✓

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `s = "a"` → freq `{'a': 1}` → return `"a"`.
- **Typical case:** Covered in dry run.
- **Extreme values:** All same character → one heap entry, return string as-is.

### Complexity

- **Time:** O(n + u log u) — counting is O(n), heap operations on u unique chars is O(u log u). Since u ≤ 62, this simplifies to **O(n)**.
- **Space:** O(n) — output string has length n.

### Optimization Discussion

- **Bucket sort:** Create frequency buckets (index 1 to n). Walk from highest bucket down, collecting characters. Avoids the heap entirely.
- **Sorted with key:** `sorted(freq, key=freq.get, reverse=True)` then build string — simple and fast given small u.
- The heap approach generalizes better if the alphabet is unbounded (e.g., Unicode).

### Follow-up Variations

- **Top K frequent characters** — stop after extracting k characters from the heap.
- **Sort by frequency ascending** — flip the heap sign (use positive counts).
- **Maintain original order for ties** — requires a stable sort or secondary key.

### ⚠️ Common Traps

- **Returning unique characters instead of repeating them.** Each character must appear `count` times in the output.
- **Case sensitivity.** `'a'` and `'A'` are different characters — don't lowercase.
- **Using `sorted()` on the entire string.** This is O(n log n). Sorting just the unique characters by frequency is O(u log u), which is better since u ≤ 62.
