# Solution — Top K Frequent Elements

## Brute Force

Count frequencies, then sort the distinct values by count descending and take
the first `k`.

```python
from collections import Counter
counts = Counter(nums)
return [v for v, _ in counts.most_common(k)]   # sort-based
```

- **Time:** `O(m log m)` where `m` is the number of distinct values (the sort
  dominates). In the worst case `m = n`, giving `O(n log n)`.
- **Space:** `O(m)`.

This works but violates the "better than `O(n log n)`" requirement when all
elements are distinct, because it fully sorts.

## Optimal Approach (Heap keyed on frequency)

1. **Count** frequencies in `O(n)` with a hash map.
2. **Select the top `k`** with a **min-heap of size `k`** over `(count, value)`
   pairs. Iterate over the `m` distinct entries: push each pair, and whenever the
   heap grows to `k + 1`, pop the pair with the *smallest* count. The heap thus
   always retains the `k` highest-frequency pairs seen so far. Comparing on
   `count` first makes the heap order by frequency.

```python
import heapq
from collections import Counter

def topKFrequent(self, nums, k):
    counts = Counter(nums)                 # O(n)
    heap = []                              # min-heap of (count, value)
    for value, count in counts.items():    # m distinct values
        heapq.heappush(heap, (count, value))
        if len(heap) > k:
            heapq.heappop(heap)            # drop the least frequent so far
    return [value for count, value in heap]
```

- **Time:** `O(n)` to count + `O(m log k)` to select = `O(n + m log k)`. Since
  `m <= n` and `k <= m`, this is comfortably better than `O(n log n)`.
- **Space:** `O(m)` for the map + `O(k)` for the heap.

**Why it is correct.** The min-heap invariant is that after processing any prefix
of the distinct values it holds the `k` largest counts among them. When a new
pair arrives: if the heap has fewer than `k` items we simply keep it; otherwise
if its count exceeds the heap's minimum it belongs in the top `k` and displaces
that minimum, and if it does not exceed the minimum it can never be in the top
`k`. Because the problem guarantees the answer is unique there are no ties at the
`k`-th boundary to disambiguate.

### Worked trace on `nums = [1,1,1,2,2,3], k = 2`

```
counts = {1:3, 2:2, 3:1}
push (3,1) -> [(3,1)]
push (2,2) -> [(2,2),(3,1)]           size 2 == k
push (1,3) -> [(1,3),(3,1),(2,2)] pop (1,3) -> [(2,2),(3,1)]
heap values -> [2, 1]                 (order not required)
```

## Key Insights & Edge Cases

- **Heap keyed on frequency, not value.** The pair `(count, value)` puts `count`
  first so the heap orders by frequency; `value` is just carried along.
- **Min-heap of size `k` for "top k".** Counterintuitively you keep a *min*-heap
  when finding the *most* frequent, so the weakest survivor is cheap to evict.
- **`O(m log k)` vs `O(m log m)`.** Bounding the heap at `k` — rather than sorting
  all `m` distinct values — is what beats `O(n log n)`.
- **Alternative — bucket sort:** because counts lie in `[1, n]`, you can bucket
  values by count and scan buckets from high to low for a true `O(n)` solution.
  The heap version is the idiomatic "top-k with a heap" pattern and generalizes
  to streaming input.
- **Edge cases:** `k` equal to the number of distinct values returns all of them;
  a single-element array (Example 2) returns that element. The uniqueness
  guarantee means we never have to break count ties.
