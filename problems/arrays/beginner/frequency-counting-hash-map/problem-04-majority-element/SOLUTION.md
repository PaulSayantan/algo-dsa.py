# Solution: Majority Element

## Brute Force

For each candidate value, count how many times it occurs by scanning the whole
array, and return the first one whose count exceeds `n / 2`.

```python
def majorityElement(nums):
    n = len(nums)
    for candidate in nums:
        count = sum(1 for v in nums if v == candidate)
        if count > n // 2:
            return candidate
```

- **Time:** `O(n^2)` — an inner scan per candidate.
- **Space:** `O(1)` — no extra structure.

Correct but quadratic.

## Optimal Approach (Frequency Counting)

Count every value's occurrences in one pass with a hash map, then return the
value whose count exceeds `n / 2`.

**Why it is correct:** By definition the majority element appears more than
`⌊n / 2⌋` times, and no other value can (two values each exceeding half the
length would together exceed the array size). So the value with a count greater
than `n / 2` is unique and is exactly the answer. You can even return the moment
a count crosses the threshold.

**Step by step:**
1. Create an empty map `counts`.
2. For each value `v`, increment `counts[v]`. If `counts[v] > n // 2`, return `v`.
3. (If the guarantee holds, the loop always returns before finishing.)

```python
from collections import Counter

def majorityElement(nums):
    counts = Counter()
    threshold = len(nums) // 2
    for v in nums:
        counts[v] += 1
        if counts[v] > threshold:
            return v
    # Guaranteed unreachable given the problem's promise.
    return counts.most_common(1)[0][0]
```

- **Time:** `O(n)` — a single pass.
- **Space:** `O(k)` where `k` is the number of distinct values (up to `O(n)`).

### Bonus: Boyer-Moore Voting (O(1) space)

The classic follow-up achieves constant space. Maintain a `candidate` and a
`count`. Walk the array: when `count` is 0, adopt the current value as the
candidate; then add 1 if the value matches the candidate, otherwise subtract 1.
The surviving candidate is the majority element.

```python
def majorityElement(nums):
    candidate, count = None, 0
    for v in nums:
        if count == 0:
            candidate = v
        count += 1 if v == candidate else -1
    return candidate
```

- **Time:** `O(n)`; **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Strictly greater than half:** The threshold is `> ⌊n / 2⌋`, not `>=`. For
  `n = 4`, a majority element must appear at least 3 times.
- **Guarantee simplifies logic:** Because the majority element is promised to
  exist, no "not found" handling is required.
- **Single element:** `[x]` returns `x` (`x` appears once, more than `0`).
- **Hash map vs. voting:** The hash map is the intuitive frequency-counting
  answer and generalizes to "count all values"; Boyer-Moore trades that
  generality for `O(1)` space specific to the majority guarantee.
