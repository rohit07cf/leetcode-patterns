# Shortest Word Distance

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Merge Style
**Link:** https://leetcode.com/problems/shortest-word-distance/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of strings `wordsDict` and two different strings `word1` and `word2`, return the **shortest distance** between any occurrence of `word1` and any occurrence of `word2` in the array. Distance is measured by index difference.

### 2. Clarification Questions
- Input constraints? `2 <= wordsDict.length <= 3 * 10^4`, `word1 != word2`, both words guaranteed to exist
- Edge cases? Words adjacent; words at opposite ends; multiple occurrences of each
- Expected output? Minimum absolute index difference
- Can input be modified? Not necessary

### 3. Brute Force Approach
- **Idea:** Collect all indices of `word1` and `word2`. Check every pair of indices for the minimum difference.
- **Time:** O(n * m) where n, m are occurrence counts (worst case O(n^2))
- **Space:** O(n) for index lists

### 4. Optimized Approach
- **Core Insight:** Track the **most recent index** of `word1` and `word2` as you scan. Whenever you see either word, compute the distance to the most recent occurrence of the other. This is a **merge-style interleave** — two streams of positions naturally walked in order.
- **Time:** O(n) — single pass
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| All pairs | O(n^2) worst | O(n) | Collect indices, compare all pairs |
| Sorted indices + merge | O(n) | O(n) | Merge two sorted index lists |
| Single pass | O(n) | O(1) | Track last seen index of each |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Scan left to right, keeping `idx1` and `idx2` as the last-seen positions of each word.
- Whenever either is updated, compute the distance if both have been seen.
- Track the global minimum.

```python
def shortestDistance(wordsDict: list[str], word1: str, word2: str) -> int:
    idx1 = -1  # last seen index of word1
    idx2 = -1  # last seen index of word2
    min_dist = len(wordsDict)  # upper bound

    for i, word in enumerate(wordsDict):
        if word == word1:
            idx1 = i
        elif word == word2:
            idx2 = i

        # Update min distance if both words have been seen
        if idx1 != -1 and idx2 != -1:
            min_dist = min(min_dist, abs(idx1 - idx2))

    return min_dist
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`wordsDict = ["practice", "makes", "perfect", "coding", "makes"]`
`word1 = "coding"`, `word2 = "practice"`

| i | word | idx1 (coding) | idx2 (practice) | distance |
|---|------|---------------|-----------------|----------|
| 0 | practice | -1 | 0 | — |
| 1 | makes | -1 | 0 | — |
| 2 | perfect | -1 | 0 | — |
| 3 | coding | 3 | 0 | 3 |
| 4 | makes | 3 | 0 | 3 |

Result: `3`

### Edge Case Testing
- **Empty input:** Not possible per constraints
- **Single element:** Not possible (both words must exist, and they're different)
- **Typical case:** As shown above
- **Extreme values:** Words are adjacent → distance 1; words at indices 0 and n-1 → distance n-1

### Complexity
- **Time:** O(n) — single linear scan
- **Space:** O(1) — just two index variables and a minimum tracker

### Optimization Discussion

The **merge-style** perspective: if you extract the sorted indices of `word1` and `word2`, the minimum distance is found by merging these two sorted lists and comparing consecutive elements from different lists. The single-pass approach implicitly does this merge in-place.

### Follow-up Variations
- Shortest Word Distance II (LeetCode 244) — called many times, precompute index lists and merge
- Shortest Word Distance III (LeetCode 245) — `word1` and `word2` can be the same
- Minimum Distance Between BST Nodes (LeetCode 783)

### Common Traps
- Checking distance before both words have been seen (idx1 or idx2 is still -1)
- Using `elif` incorrectly — `word == word2` must be in the `elif` branch so a word doesn't match both
- For follow-up II, not using the sorted merge technique for efficient repeated queries
