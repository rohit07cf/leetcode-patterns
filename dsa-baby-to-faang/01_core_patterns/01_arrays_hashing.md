# Arrays & Hashing

## Baby Explanation (ELI10)

- An **array** is like a row of numbered boxes. Box 0, Box 1, Box 2... You can jump to any box instantly if you know its number.
- A **hash map** (dictionary) is like a magic label maker. You stick a label on a box, and later you can say "give me the box labeled 'apple'" and it appears instantly.
- When a problem says "find something fast," your brain should scream **hash map!** because looking things up in a hash map takes O(1) -- basically instant.
- Arrays are great for ordered stuff. Hash maps are great for "have I seen this before?" stuff.
- Together, they solve a HUGE chunk of interview problems. Learn these first.

## Pattern Recognition

Use this when you see:
- "Find two numbers that add up to..."
- "Count how many times each thing appears"
- "Group things that are similar"
- "Check for duplicates"
- "Find the first non-repeating..."
- The word "frequency" or "count" anywhere in the problem

Avoid when:
- The array is already sorted (think Two Pointers instead)
- You need elements in a specific order and can't afford extra space
- The problem says "in-place" (hash maps use extra space)

## How a Hash Map Works (ASCII Diagram)

```
  key -> hash function -> index -> value

  Example: storing {"apple": 3, "banana": 7}

  Keys         Hash Map (under the hood)
  ------       --------------------------
  "apple"  --> | bucket 0 |              |
               | bucket 1 | "apple" : 3  |  <-- "apple" hashed to bucket 1
               | bucket 2 |              |
               | bucket 3 | "banana": 7  |  <-- "banana" hashed to bucket 3
               | bucket 4 |              |
               --------------------------

  lookup("apple") --> bucket 1 --> returns 3    O(1) instant!
```

## Minimal Python Template

### Pattern 1: Hash Map Lookup (Two Sum Style)

```python
def two_sum(nums, target):
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []
```

### Pattern 2: Frequency Counting

```python
def frequency_count(nums):
    count = {}  # value -> how many times it appears

    for num in nums:
        count[num] = count.get(num, 0) + 1

    return count
```

### Pattern 3: Grouping by Key

```python
def group_by_key(items):
    from collections import defaultdict
    groups = defaultdict(list)

    for item in items:
        key = make_key(item)  # define what makes items "similar"
        groups[key].append(item)

    return list(groups.values())
```

## Step-by-Step Example (Tiny Input)

### Two Sum: nums = [2, 7, 11, 15], target = 9

```
Step 1: i=0, num=2
        complement = 9 - 2 = 7
        seen = {}          --> 7 not in seen
        seen = {2: 0}      --> store 2 at index 0

Step 2: i=1, num=7
        complement = 9 - 7 = 2
        seen = {2: 0}      --> 2 IS in seen! Found it!
        return [0, 1]
```

- **Input:** [2, 7, 11, 15], target = 9
- **Walkthrough:** We needed 7's partner (2). We had already stored 2 in our hash map. Match found!
- **Output:** [0, 1]

### Frequency Count: nums = [1, 2, 2, 3, 3, 3]

```
Step 1: num=1 --> count = {1: 1}
Step 2: num=2 --> count = {1: 1, 2: 1}
Step 3: num=2 --> count = {1: 1, 2: 2}
Step 4: num=3 --> count = {1: 1, 2: 2, 3: 1}
Step 5: num=3 --> count = {1: 1, 2: 2, 3: 2}
Step 6: num=3 --> count = {1: 1, 2: 2, 3: 3}
```

- **Output:** {1: 1, 2: 2, 3: 3}

## Common Variations

1. **Two Sum** (LC #1) -- Find two numbers that add to target. Use hash map to store what you've seen.

2. **Contains Duplicate** (LC #217) -- Are there any repeats? Use a set. If you try to add something already in the set, return True.

3. **Group Anagrams** (LC #49) -- Group words that use the same letters. Sort each word to make a key, group by that key.

4. **Top K Frequent Elements** (LC #347) -- Count frequencies, then find the top K. Use a hash map + bucket sort.

5. **Valid Anagram** (LC #242) -- Do two words have the same letter counts? Compare two frequency maps.

## Top 5 Mistakes Beginners Make

1. **Forgetting to check BEFORE storing.** In Two Sum, you must check if the complement exists BEFORE you add the current number. Otherwise you might match a number with itself.

2. **Using a list when you need a set or dict.** Checking "is X in my_list" is O(n). Checking "is X in my_set" is O(1). This matters!

3. **Not handling the "not found" case.** Always think: what if there is no answer? Return -1, empty list, or whatever the problem asks.

4. **Confusing index vs. value.** In Two Sum, the hash map stores {value: index}, not {index: value}. Read carefully.

5. **Overcomplicating the key for grouping.** For Group Anagrams, just sort the word to make the key: `tuple(sorted(word))`. Keep it simple.

## Complexity

- **Time:** O(n) for most hash map patterns (one pass through the array)
- **Space:** O(n) for the hash map (worst case, you store every element)

Note: Sorting-based approaches (like Group Anagrams key) add O(k log k) per item where k is item length.

## What To Say In Interview (Talk Track)

- "I notice we need to find a matching pair / count frequencies, so I'll use a hash map for O(1) lookups."
- "I'll make one pass through the array, storing each element as I go, and checking if its complement already exists."
- "This gives us O(n) time and O(n) space, which is optimal for this problem since we need to see every element at least once."
- "The key insight is that instead of checking every pair (O(n^2)), we trade space for time with a hash map."
