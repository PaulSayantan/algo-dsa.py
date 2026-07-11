# Solution — Top K Frequent Elements

## Brute Force

Count occurrences with a hash map, sort the `(element, count)` pairs by count descending,
and take the first `k` elements.

```python
from collections import Counter

def topKFrequent(nums, k):
    counts = Counter(nums)
    ordered = sorted(counts, key=counts.get, reverse=True)
    return ordered[:k]
```

- **Time:** `O(n + u log u)` where `u` is the number of unique elements (`u <= n`), so
  `O(n log n)` in the worst case.
- **Space:** `O(u)` for the counter.

It fully sorts every unique element even though only the top `k` matter.

## Optimal Approach (Top-K via Heap)

**Step 1 — count.** Build `counts = Counter(nums)` in `O(n)`.

**Step 2 — select the top k by count.** Push `(count, element)` pairs into a **min-heap
capped at size `k`**. When the heap exceeds `k`, pop the entry with the *smallest* count.
The survivors are the `k` most frequent elements.

```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    counts = Counter(nums)
    heap = []
    for element, count in counts.items():
        heapq.heappush(heap, (count, element))
        if len(heap) > k:
            heapq.heappop(heap)          # drop the least frequent survivor
    return [element for count, element in heap]
```

**Why it is correct:** the heap holds the invariant "the `k` highest-count entries seen so
far." Because the tuple's first field is the count, the root is always the current
lowest-frequency member — exactly the one to evict when a more frequent element arrives.
The problem guarantees a unique answer, so no ambiguous ties can split the top `k`.

- **Time:** `O(n + u log k)` — counting is `O(n)`, and each of `u` unique entries costs
  `O(log k)`. Since `k <= u <= n`, this is at most `O(n log k)`.
- **Space:** `O(u)` for the counter plus `O(k)` for the heap.

### Alternative: Bucket sort — `O(n)`

A count can be at most `n` (an element appears at most `n` times), so index elements into
buckets by frequency and scan from the highest bucket down:

```python
from collections import Counter

def topKFrequent(nums, k):
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]  # buckets[f] = elements with freq f
    for element, freq in counts.items():
        buckets[freq].append(element)
    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for element in buckets[freq]:
            result.append(element)
            if len(result) == k:
                return result
    return result
```

- **Time:** `O(n)` — counting, filling buckets, and one downward scan are all linear.
- **Space:** `O(n)` for the buckets.

Use bucket sort when the key is bounded by `n` and you want strictly linear time; use the
heap when `k << n` and you prefer `O(k)` working memory over `O(n)` buckets.

## Key Insights & Edge Cases

- **Heap on the count, not the value.** The comparison key is the frequency; wrapping it as
  the first tuple field `(count, element)` makes Python's min-heap order by count
  automatically.
- **Min-heap keeps the max-k.** Capping at `k` and popping the smallest count leaves the
  `k` largest counts — the same inversion as every Top-K problem.
- **k equals number of unique elements.** The heap simply never trims; every unique element
  is returned. Correct with no special case.
- **Order of the output is free.** LeetCode accepts any order, so you can return the heap
  contents directly without a final sort.
- **Negative and single-element inputs** need no special handling — counting works on any
  hashable value.
