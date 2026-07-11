# K Closest Points to Origin — Solution

## Brute Force

Compute each point's distance to the origin, sort all points by that distance, and take
the first `k`.

- **Time:** `O(n log n)` — dominated by sorting all `n` points.
- **Space:** `O(n)` for the sorted copy (or `O(log n)` to `O(n)` depending on the sort).

Perfectly correct and often fast enough. But when `k << n` (e.g. the 10 closest of a
million points) we sort far more than we need — we only care about the `k` smallest.

## Optimal Approach (Heap / Priority Queue)

**Idea:** To keep the `k` *closest* points while streaming through the list, maintain a
**max-heap of size `k`** keyed on squared distance. The root is the *farthest* of the
current best `k`. When a new point is nearer than that root, it evicts the root; anything
farther is ignored. Use **squared** distance `x*x + y*y` — the ordering is identical to
Euclidean distance and avoids `sqrt` (faster and exact on integers).

Because `heapq` is a min-heap, negate the distance to simulate a max-heap:

```python
import heapq

def kClosest(points, k):
    heap = []                                  # max-heap via negated distance
    for x, y in points:
        d = x * x + y * y                      # squared distance
        if len(heap) < k:
            heapq.heappush(heap, (-d, x, y))
        elif -d > heap[0][0]:                  # closer than current farthest
            heapq.heapreplace(heap, (-d, x, y))
    return [[x, y] for _, x, y in heap]
```

**Why it is correct:** The heap always holds the `k` smallest-distance points seen so
far. Its root `heap[0]` is the largest distance among those `k`. A newcomer with distance
`d` belongs in the answer iff `d` is smaller than that maximum — exactly the eviction test
`-d > heap[0][0]`. After processing all points, the heap's `k` elements are the globally
`k` closest. Uniqueness of the answer set (guaranteed by the problem) means ties never
force an ambiguous choice.

- **Time:** `O(n log k)` — one heap push/replace (`O(log k)`) per point.
- **Space:** `O(k)` — the heap never exceeds `k` entries.

When `k` is close to `n`, `O(n log k) ≈ O(n log n)` and plain sorting is just as good;
the heap shines when `k` is much smaller than `n`.

> **Even faster (advanced):** Quickselect / `nth_element` partitions the array around the
> kth smallest distance in expected `O(n)` time and `O(1)` extra space, at the cost of a
> bad `O(n^2)` worst case and a more involved implementation. The heap is the clean,
> predictable choice for interviews.

## Key Insights & Edge Cases

- **Squared distance is enough:** never call `sqrt`. It is slower and can introduce
  floating-point error; integer squares preserve the exact ordering.
- **Max-heap of size `k`, not min-heap of size `n`:** we discard the far points as we go,
  bounding memory to `O(k)`.
- **`k == len(points)`:** every point qualifies; the heap ends up holding them all.
- **`k == 1`:** degenerates to a single-pass minimum search.
- **Store the tuple as `(-d, x, y)`** so Python compares by distance first; the raw
  coordinates only ever break ties and never cause an error since the answer is unique.
