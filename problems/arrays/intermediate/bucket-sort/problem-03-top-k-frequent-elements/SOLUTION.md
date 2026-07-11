# Top K Frequent Elements — Solution

## Brute Force

Count frequencies with a hash map, then sort the `(value, count)` pairs by count
descending and take the first `k` values.

```python
from collections import Counter

def topKFrequent(nums, k):
    counts = Counter(nums)
    ordered = sorted(counts, key=counts.get, reverse=True)
    return ordered[:k]
```

- **Time:** `O(n + d log d)` where `d` is the number of distinct values. The
  sort dominates and is up to `O(n log n)`.
- **Space:** `O(n)` for the counter.

A heap-based variant (`heapq.nlargest(k, ...)`) improves this to
`O(n + d log k)`, but we can hit linear time by bucketing.

## Optimal Approach (Bucket Sort)

**Key observation:** a value's frequency is an integer in `[1, n]`. Use the
frequency itself as a bucket index. `buckets[f]` is the list of distinct values
that appear exactly `f` times. Reading buckets from the top gives values in
descending frequency order for free.

### Steps

1. Count frequencies with a hash map (`Counter`).
2. Allocate `n + 1` buckets. For each `(value, freq)`, append `value` to
   `buckets[freq]`.
3. Iterate `freq` from `n` down to `1`. Append every value in `buckets[freq]` to
   the result. Stop once the result holds `k` elements.

```python
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]  # buckets[f] -> values with freq f
        for value, freq in counts.items():
            buckets[freq].append(value)

        result = []
        for freq in range(n, 0, -1):
            for value in buckets[freq]:
                result.append(value)
                if len(result) == k:
                    return result
        return result
```

### Why It Is Correct

Each distinct value is placed in the single bucket whose index equals its exact
frequency. Scanning buckets from index `n` down to `1` yields values in
non-increasing frequency order, so the first `k` values collected are the `k`
most frequent. The problem guarantees the top-`k` set is unique, so ties never
force an ambiguous choice among elements that would change the answer set (and
any order within the result is accepted). We stop as soon as `k` values are
gathered.

### Complexity

- **Time:** `O(n)`. Counting is `O(n)`, filling buckets is `O(d) <= O(n)`, and
  the final scan touches at most `n` bucket slots plus `d` values.
- **Space:** `O(n)` for the counter and the `n + 1` buckets.

## Key Insights & Edge Cases

- **Frequency-as-index** is the same reusable idea as "Sort Characters By
  Frequency"; here we simply stop early after `k` elements.
- **`n + 1` buckets:** the max frequency is `n` (all elements identical), so
  index `n` must exist.
- **`k` equals the number of distinct values:** the loop naturally returns every
  value; the early-return simply fires on the last one.
- **Single element** (`[1], k=1`): lands in `buckets[1]`, returned immediately.
- **Negative values** are fine — they are dictionary keys, not indices. Only the
  *frequency* is used as an index.
- Compared to the heap solution, bucket sort trades `O(d log k)` for `O(n)` and
  is typically the intended "better than `O(n log n)`" answer.
