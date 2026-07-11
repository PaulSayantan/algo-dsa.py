# Solution: Top K Frequent Elements

## Brute Force

Count each value, then fully sort the distinct values by their count in
descending order and take the first `k`.

```python
from collections import Counter

def topKFrequent(nums, k):
    counts = Counter(nums)
    ordered = sorted(counts.keys(), key=lambda v: counts[v], reverse=True)
    return ordered[:k]
```

- **Time:** `O(n + u log u)` where `u` is the number of distinct values (up to
  `O(n log n)`) — dominated by sorting all distinct values.
- **Space:** `O(u)` for the count map.

Correct, but it does more work than needed: we sort *everything* to keep only
the top `k`.

## Optimal Approach (Frequency Counting + Selection)

Count frequencies with a hash map, then select the top `k` without a full sort.
Two standard techniques:

### Option A: Heap of size k

Keep a min-heap of `(count, value)` limited to `k` entries. This yields the top
`k` in `O(u log k)`.

```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    counts = Counter(nums)
    # nlargest picks the k highest-count items using a size-k heap internally.
    return [v for v, _ in Counter(counts).most_common(k)]
    # Or explicitly:
    # return heapq.nlargest(k, counts.keys(), key=counts.get)
```

- **Time:** `O(n + u log k)`.
- **Space:** `O(u)`.

### Option B: Bucket sort by frequency (linear time)

A value's count is between `1` and `n`, so index buckets by count. Bucket `f`
holds every value that appears exactly `f` times. Walk buckets from highest
frequency down, collecting values until you have `k`.

```python
from collections import Counter

def topKFrequent(nums, k):
    counts = Counter(nums)
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]   # index = frequency
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

**Why it is correct:** The most frequent elements are, by definition, those with
the largest counts. Bucketing by exact frequency groups values by count; scanning
buckets from `n` down to `1` visits values in non-increasing frequency order, so
the first `k` collected are precisely the `k` most frequent. The unique-answer
guarantee means there is no ambiguity at the cutoff.

**Step by step (bucket sort):**
1. Build `counts` with a hash map.
2. Create `n + 1` empty buckets; place each value into the bucket equal to its
   frequency.
3. Iterate frequencies from high to low, appending values until `k` are
   collected.

- **Time:** `O(n)` — counting and bucket construction are linear, and the bucket
  scan touches each distinct value once.
- **Space:** `O(n)` — buckets plus the count map.

## Key Insights & Edge Cases

- **Counting is step one:** Every approach starts from the same hash-map
  frequency table; the difference is only in how the top `k` are selected.
- **Avoid the full sort:** A size-`k` heap (`O(u log k)`) or bucket sort
  (`O(n)`) beats sorting all distinct values (`O(u log u)`).
- **Frequencies are bounded by n:** This bound is what makes bucket sort
  applicable and linear.
- **`k` equals number of distinct values:** The answer is simply all distinct
  values.
- **Single element / k = 1:** `[x]` with `k = 1` returns `[x]`.
- **Order not required:** Any ordering of the correct `k` values is accepted.
