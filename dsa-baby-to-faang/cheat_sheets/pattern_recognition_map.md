# Pattern Recognition Map

> The hardest part of coding interviews is knowing WHICH pattern to use. This file fixes that.

---

## The Master Decision Flowchart

```
START: What is the input?
|
|---> ARRAY / STRING
|     |
|     |---> Is it sorted (or can you sort it)?
|     |     |---> YES: Binary Search or Two Pointers
|     |     |---> NO: continue below
|     |
|     |---> Looking for a subarray / substring?
|     |     |---> Fixed size window? --> Sliding Window (Fixed)
|     |     |---> Variable size, find longest/shortest? --> Sliding Window (Variable)
|     |     |---> Sum of subarray? --> Prefix Sum or Sliding Window
|     |
|     |---> Looking for pairs / triplets?
|     |     |---> Sorted input? --> Two Pointers (Opposite)
|     |     |---> Need O(1) lookup? --> Hash Map
|     |
|     |---> Next greater / smaller element?
|     |     |---> Monotonic Stack
|     |
|     |---> All permutations / subsets / combinations?
|     |     |---> Backtracking
|     |
|     |---> Min/max/count with choices at each step?
|     |     |---> Dynamic Programming
|     |
|     |---> Merge overlapping intervals?
|           |---> Sort by start, then merge
|
|---> TREE
|     |
|     |---> Level-by-level processing?
|     |     |---> BFS (Level Order)
|     |
|     |---> Path from root to leaf?
|     |     |---> DFS (Preorder, pass info down)
|     |
|     |---> Gather info from subtrees?
|     |     |---> DFS (Postorder, gather info up)
|     |
|     |---> BST property (sorted)?
|     |     |---> Inorder traversal or Binary Search logic
|     |
|     |---> Lowest Common Ancestor?
|           |---> LCA Template (postorder DFS)
|
|---> GRAPH
|     |
|     |---> Shortest path?
|     |     |---> Unweighted? --> BFS
|     |     |---> Weighted (no negatives)? --> Dijkstra
|     |     |---> Weighted (negatives)? --> Bellman-Ford
|     |
|     |---> Connected components?
|     |     |---> BFS / DFS / Union Find
|     |
|     |---> Ordering with dependencies?
|     |     |---> Topological Sort
|     |
|     |---> Cycle detection?
|     |     |---> Undirected: DFS (parent tracking) or Union Find
|     |     |---> Directed: DFS (3-color)
|     |
|     |---> Grid problem (matrix)?
|           |---> Shortest path in grid? --> Grid BFS
|           |---> Count islands / regions? --> Grid DFS or BFS
|
|---> LINKED LIST
|     |
|     |---> Reverse? --> Iterative reversal (prev/curr/next)
|     |---> Cycle detection? --> Fast & Slow pointers
|     |---> Find middle? --> Fast & Slow pointers
|     |---> Merge two sorted? --> Two pointers with dummy head
|
|---> NUMBER / MATH
      |
      |---> Bit manipulation? --> AND, OR, XOR, shifts
      |---> Prime / divisor? --> Sieve or trial division
      |---> Power / modular? --> Fast exponentiation
```

---

## Trigger Phrase Lookup Table

| # | If you see this phrase... | Think this pattern... | Template File |
|---|--------------------------|----------------------|---------------|
| 1 | "sorted array" | Binary Search | faang_coding_templates.md #1-3 |
| 2 | "two sum" / "pair that sums to" | Hash Map or Two Pointers | faang_coding_templates.md #4 |
| 3 | "subarray of size k" | Sliding Window (Fixed) | faang_coding_templates.md #6 |
| 4 | "longest substring without repeating" | Sliding Window (Variable) | faang_coding_templates.md #7 |
| 5 | "minimum window substring" | Sliding Window (Variable) | faang_coding_templates.md #7 |
| 6 | "all permutations" / "all subsets" | Backtracking | -- |
| 7 | "maximum/minimum path" + choices | Dynamic Programming | dp_cheatsheet.md |
| 8 | "how many ways" | DP (counting) | dp_cheatsheet.md |
| 9 | "connected components" | Union Find or BFS/DFS | graphs_cheatsheet.md |
| 10 | "shortest path" (unweighted) | BFS | faang_coding_templates.md #8-9 |
| 11 | "shortest path" (weighted) | Dijkstra | faang_coding_templates.md #16 |
| 12 | "course schedule" / "prerequisites" | Topological Sort | faang_coding_templates.md #14 |
| 13 | "number of islands" | Grid DFS / BFS | graphs_cheatsheet.md |
| 14 | "next greater element" | Monotonic Stack | faang_coding_templates.md #17 |
| 15 | "merge intervals" / "overlapping" | Sort + Merge | -- |
| 16 | "lowest common ancestor" | LCA Template | trees_cheatsheet.md |
| 17 | "validate BST" | DFS with range | trees_cheatsheet.md |
| 18 | "level order" / "by level" | BFS (Tree) | faang_coding_templates.md #10 |
| 19 | "diameter" / "longest path in tree" | DFS Postorder + global var | trees_cheatsheet.md |
| 20 | "knapsack" / "subset sum" / "partition" | 0/1 Knapsack DP | dp_cheatsheet.md |
| 21 | "coin change" / "unlimited supply" | Unbounded Knapsack DP | dp_cheatsheet.md |
| 22 | "longest increasing subsequence" | LIS (DP or Binary Search) | dp_cheatsheet.md |
| 23 | "edit distance" / "transform string" | 2D DP | dp_cheatsheet.md |
| 24 | "palindrome substring/subsequence" | DP or Expand Around Center | dp_cheatsheet.md |
| 25 | "cycle in linked list" | Fast & Slow Pointers | faang_coding_templates.md #5 |
| 26 | "reverse linked list" | Iterative Reversal | faang_coding_templates.md #21 |
| 27 | "top k" / "k largest" / "k smallest" | Heap (heapq) | -- |
| 28 | "meeting rooms" / "min platforms" | Sort + Sweep or Heap | -- |
| 29 | "word search in grid" | Backtracking on Grid | -- |
| 30 | "decode ways" / "climb stairs" | 1D DP | dp_cheatsheet.md |

---

## Pattern-by-Input-Type Quick Reference

### Arrays

| Problem Type | Pattern | Key Data Structure |
|-------------|---------|-------------------|
| Find target in sorted array | Binary Search | -- |
| Two numbers that sum to target | Hash Map / Two Pointers | dict / sorted array |
| Three numbers that sum to target | Sort + Two Pointers | sorted array |
| Maximum subarray sum | Kadane's Algorithm | running sum |
| Subarray with given sum | Prefix Sum + Hash Map | dict |
| Max/min of all windows of size k | Sliding Window + Deque | collections.deque |
| Next greater element | Monotonic Stack | stack |
| Merge overlapping intervals | Sort by start + merge | list |
| Find duplicate in range [1,n] | Floyd's Cycle (or set) | fast/slow pointers |
| Rotate array by k | Reverse three times | -- |

### Strings

| Problem Type | Pattern | Key Data Structure |
|-------------|---------|-------------------|
| Anagram check / grouping | Sort or Counter | dict |
| Longest substring (condition) | Sliding Window (Variable) | dict for window |
| Palindrome check | Two Pointers (Opposite) | -- |
| All permutations | Backtracking | -- |
| String matching / search | KMP or Rolling Hash | -- |
| Decode/parse string | Stack | stack |
| Word break | DP | dp array + set |

### Trees

| Problem Type | Pattern | Reference |
|-------------|---------|-----------|
| Traversal | DFS (pre/in/post) or BFS | trees_cheatsheet.md |
| Height / depth | DFS Postorder | trees_cheatsheet.md |
| Path sum | DFS Preorder (pass sum down) | trees_cheatsheet.md |
| Validate BST | DFS with (lo, hi) range | trees_cheatsheet.md |
| LCA | Postorder DFS | trees_cheatsheet.md |
| Serialize / deserialize | BFS or Preorder DFS | trees_cheatsheet.md |

### Graphs

| Problem Type | Pattern | Reference |
|-------------|---------|-----------|
| Shortest path (unweighted) | BFS | graphs_cheatsheet.md |
| Shortest path (weighted) | Dijkstra | graphs_cheatsheet.md |
| Connected components | DFS / BFS / Union Find | graphs_cheatsheet.md |
| Cycle detection | DFS (colors) / Union Find | graphs_cheatsheet.md |
| Topological ordering | Kahn's BFS | graphs_cheatsheet.md |
| Island problems (grid) | Grid DFS / BFS | graphs_cheatsheet.md |

---

## "I Am Stuck" Fallback Strategies

If you have been staring at a problem for 3+ minutes and have no idea:

### Strategy 1: Try Brute Force First
- Write the naive O(n^2) or O(2^n) solution
- Then ask: "How can I avoid repeated work?" -> That often leads to DP, hash map, or two pointers

### Strategy 2: Work Through a Small Example
- Use the simplest non-trivial input (3-5 elements)
- Trace through by hand
- Patterns often become obvious with a concrete example

### Strategy 3: Match to a Known Problem
- "This feels like Two Sum" -> Hash Map
- "This feels like Number of Islands" -> Grid DFS
- "This feels like Climbing Stairs" -> 1D DP
- Use the trigger phrase table above

### Strategy 4: Ask These Questions
| Question | If YES, then... |
|----------|-----------------|
| Is the input sorted? | Binary Search or Two Pointers |
| Am I looking at subarrays/substrings? | Sliding Window |
| Do I need all possibilities? | Backtracking |
| Can I break this into subproblems? | DP |
| Is this about connections/reachability? | Graph BFS/DFS |
| Do I need fast insert + lookup? | Hash Map or Heap |

### Strategy 5: Communicate with Your Interviewer
- Say: "I am thinking this might be a [pattern] problem because [reason]"
- Ask: "Can I assume the input is sorted?" or "Are there constraints on the values?"
- Talking through your thought process scores points even if you are wrong

---

## Complexity Cheat Sheet (What to Tell Your Interviewer)

| Pattern | Time | Space |
|---------|------|-------|
| Binary Search | O(log n) | O(1) |
| Two Pointers | O(n) | O(1) |
| Sliding Window | O(n) | O(k) or O(1) |
| Hash Map lookup | O(n) | O(n) |
| BFS / DFS (graph) | O(V + E) | O(V) |
| BFS / DFS (grid) | O(m * n) | O(m * n) |
| Topological Sort | O(V + E) | O(V + E) |
| Dijkstra | O((V+E) log V) | O(V) |
| Union Find | O(alpha(n)) per op | O(n) |
| Sorting | O(n log n) | O(n) |
| 1D DP | O(n) | O(n) or O(1) |
| 2D DP | O(m * n) | O(m * n) or O(n) |
| Backtracking | O(2^n) or O(n!) | O(n) |
| Heap operations | O(n log k) | O(k) |
| Monotonic Stack | O(n) | O(n) |

---

## Final Pre-Interview Checklist

```
[ ] I know the 21 templates in faang_coding_templates.md
[ ] I can recognize patterns using the trigger phrase table
[ ] I know when to use BFS vs DFS vs Dijkstra
[ ] I know the 4-step DP recipe
[ ] I can explain my approach BEFORE coding
[ ] I remember to handle edge cases (empty input, single element, etc.)
[ ] I know the time/space complexity of every pattern I use
[ ] I will talk through my thinking out loud
[ ] I will ask clarifying questions first
[ ] I will test my solution with a small example
```

**You have the patterns. You have the templates. Now go show them what you can do.**
