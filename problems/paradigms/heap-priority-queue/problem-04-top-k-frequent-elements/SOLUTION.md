# Top K Frequent Elements — Solution

## Brute Force

Count frequencies with a hash map, then sort the `(value, count)` pairs by count in
descending order and take the first `k` values.

- **Time:** `O(n + m log m)` where `n = len(nums)` and `m` = number of distinct values
  (`m <= n`). The sort of all `m` distinct pairs dominates.
- **Space:** `O(m)` for the frequency map and the sorted list.

Correct and simple. But sorting *all* distinct values is more than we need when `k` is
small — we only want the top `k`.

## Optimal Approach (Heap / Priority Queue)

**Idea:** Count first, then heap-select the top `k`. Build a frequency map in `O(n)`, then
push each `(count, value)` into a **min-heap capped at size `k`** (keyed on count). The
root is the *least frequent of the current top `k`*, so any value with a higher count
evicts it. After all distinct values are processed, the heap holds the `k` most frequent.

```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)                      # O(n)
    heap = []                                 # min-heap of (count, value), size <= k
    for value, count in freq.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, value))
        elif count > heap[0][0]:
            heapq.heapreplace(heap, (count, value))
    return [value for _, value in heap]
```

**Why it is correct:** The heap always contains the `k` highest-frequency values seen so
far; its root is the smallest count among them. A new value belongs in the top `k` iff its
count exceeds that minimum — exactly the `count > heap[0][0]` test. Uniqueness of the
answer (guaranteed) means there is no ambiguous tie at the `k`th boundary.

- **Time:** `O(n + m log k)` — `O(n)` to count, then `O(log k)` per distinct value.
  Strictly better than sorting when `k < m`.
- **Space:** `O(m)` for the counts plus `O(k)` for the heap.

### Bucket-sort alternative — `O(n)`

Frequencies are bounded by `n`, so you can bucket values by count into an array of size
`n + 1` and read buckets from high to low until you collect `k`:

```python
def topKFrequent(nums, k):
    freq = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]   # buckets[c] = values with count c
    for value, count in freq.items():
        buckets[count].append(value)
    result = []
    for count in range(len(buckets) - 1, 0, -1):
        for value in buckets[count]:
            result.append(value)
            if len(result) == k:
                return result
    return result
```

This is `O(n)` time and space — optimal — but the heap solution is the canonical answer
the problem is designed to teach and generalizes to streaming/unbounded-count settings.

## Key Insights & Edge Cases

- **Count then select:** the heap operates on distinct values (`m` of them), not the raw
  array — do the `O(n)` counting pass first.
- **Min-heap for "top" k:** keeping the *least* frequent of the chosen `k` at the root is
  what makes eviction and the size cap work — the mirror image of a max-heap of all `m`.
- **`k` equals the number of distinct values:** every distinct value is returned.
- **All elements identical** (`[7,7,7], k=1`): one bucket / one heap entry → `[7]`.
- **Order is irrelevant:** don't waste effort sorting the final `k`.
