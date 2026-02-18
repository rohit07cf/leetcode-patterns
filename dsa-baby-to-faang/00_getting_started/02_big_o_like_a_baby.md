# Big O Like a Baby

## Baby Explanation (ELI10)

- Big O tells you **how slow your code gets** when the input gets bigger
- Imagine counting 10 toys — easy! Now count 1,000,000 toys...
- Big O answers: "If I double the input, how much longer does it take?"
- It's NOT about exact time — it's about the **growth rate**
- We always care about the **worst case**
- Interviewers ALWAYS ask about Big O. Always.

---

## Pattern Recognition

✅ Use this when you see:
- "What is the time complexity?"
- "Can you do better?"
- "What's the space complexity?"
- Any FAANG interview question (they WILL ask)

❌ Avoid:
- Overthinking exact operations
- Counting every single line

---

## The Pizza Analogy

You're delivering pizzas to `n` houses.

| Big O | What You Do | How It Scales |
|-------|------------|---------------|
| O(1) | Call them all at once | Same time, no matter how many houses |
| O(log n) | Split the neighborhood in half each time | 1000 houses? Only ~10 steps |
| O(n) | Visit each house once | 1000 houses = 1000 visits |
| O(n log n) | Visit each house, but sort them first | A bit more than n |
| O(n^2) | Every house visits every other house | 1000 houses = 1,000,000 visits! |
| O(2^n) | Every possible combination of houses | Don't even try |

---

## How To Count Big O (Baby Method)

### Rule 1: Count the loops

```python
# ONE loop = O(n)
for i in range(n):
    print(i)

# TWO nested loops = O(n^2)
for i in range(n):
    for j in range(n):
        print(i, j)

# THREE nested loops = O(n^3)  — very bad
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
```

### Rule 2: Drop the constants

```
O(2n)  → just say O(n)
O(5n^2) → just say O(n^2)
O(n + 100) → just say O(n)
```

### Rule 3: Keep only the biggest term

```
O(n^2 + n) → just say O(n^2)
O(n + log n) → just say O(n)
```

### Rule 4: Halving = O(log n)

```python
# If you cut the problem in HALF each step → O(log n)
while n > 0:
    n = n // 2   # halving!
```

---

## Visual: How Big O Grows

```
Input size:  10    100    1,000    1,000,000

O(1)         1      1        1            1
O(log n)     3      7       10           20
O(n)        10    100    1,000    1,000,000
O(n log n)  30    700   10,000   20,000,000
O(n^2)     100  10000 1,000,000  too slow!!
O(2^n)    1024  impossible... don't even.
```

---

## Space Complexity (Baby Version)

- Time = how long it takes
- Space = how much memory it uses

```python
# O(1) space — no extra memory
total = 0
for x in arr:
    total += x

# O(n) space — storing a copy
new_arr = [x * 2 for x in arr]

# O(n) space — using a hash map
seen = set()
for x in arr:
    seen.add(x)
```

---

## FAANG Complexity Cheat Table

| n size | Max acceptable Big O |
|--------|---------------------|
| n <= 10 | O(n!) or O(2^n) is OK |
| n <= 100 | O(n^3) is OK |
| n <= 1,000 | O(n^2) is OK |
| n <= 100,000 | O(n log n) is needed |
| n <= 1,000,000 | O(n) is needed |
| n <= 10^9 | O(log n) or O(1) is needed |

> **Pro tip:** Look at the constraints in the problem.
> They TELL you what Big O you need!

---

## Minimal Python Template

```python
# Recognizing complexity by pattern

# O(1) - constant
def get_first(arr):
    return arr[0]

# O(n) - linear
def find_max(arr):
    best = arr[0]
    for x in arr:
        best = max(best, x)
    return best

# O(n^2) - quadratic (try to avoid!)
def all_pairs(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(arr[i], arr[j])

# O(log n) - logarithmic
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

---

## Interview Talk Track

> "This solution runs in O(n) time because we iterate through
> the array once. The space complexity is O(n) because we use
> a hash map that could store up to n elements."

> "The brute force would be O(n^2) with nested loops.
> We can optimize to O(n) using a hash map."

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Saying "O(2n)" | Drop constants → O(n) |
| Forgetting space complexity | Always mention both time AND space |
| Not checking constraints | Constraints tell you the required Big O |
| Saying "it's fast" without proof | Always give the Big O notation |

---

## What's Next?

Go to: [03_common_mistakes_and_how_to_fix.md](03_common_mistakes_and_how_to_fix.md)
