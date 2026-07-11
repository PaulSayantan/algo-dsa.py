# Solution — K Closest Points to Origin

## Brute Force

Compute each point's distance to the origin, sort all points by that distance, and return
the first `k`. Compare **squared** distances (`x*x + y*y`) to avoid the `sqrt` — it does not
change the ordering and keeps arithmetic exact on integers.

```python
def kClosest(points, k):
    points.sort(key=lambda p: p[0] * p[0] + p[1] * p[1])
    return points[:k]
```

- **Time:** `O(n log n)` for the sort.
- **Space:** `O(1)` extra (in-place) or `O(n)` for a copy.

Fine, but it orders all `n` points when only the closest `k` are needed.

## Optimal Approach (Top-K via Heap)

We want the `k` **smallest** distances. Maintain a **max-heap capped at size `k`** so the
*farthest* of the current best `k` sits at the root and is evicted first when a closer point
appears.

Python's `heapq` is a min-heap, so store the **negated** squared distance to simulate a
max-heap:

```python
import heapq

def kClosest(points, k):
    heap = []  # entries: (-squared_distance, x, y)  -> largest distance at root
    for x, y in points:
        d = x * x + y * y
        heapq.heappush(heap, (-d, x, y))
        if len(heap) > k:
            heapq.heappop(heap)      # discard the farthest survivor
    return [[x, y] for _, x, y in heap]
```

**Why it is correct:** the heap holds the invariant "the `k` closest points seen so far,"
with the farthest at the root (because distances are negated). When a new point is closer
than that root, pushing it and popping the root replaces the weakest member; when it is
farther, it is pushed then immediately evicted and cannot displace a rightful member. The
uniqueness guarantee means no tie can ambiguously split the boundary.

- **Time:** `O(n log k)` — `n` pushes, each `O(log k)`.
- **Space:** `O(k)` for the heap.

Best when `k << n` (few closest points among many) and for streaming coordinates where the
full list is never held at once.

### Alternative: Quickselect — `O(n)` average

Partition the array around a pivot distance until the boundary lands at index `k`; the first
`k` slots are then the closest `k` points (unordered). Average `O(n)`, worst `O(n^2)`,
`O(1)` extra space — but it mutates the input and does not keep them sorted.

## Key Insights & Edge Cases

- **Squared distance, no sqrt.** `sqrt` is monotonic, so ordering by `x^2 + y^2` gives the
  same ranking while staying in exact integer arithmetic and avoiding floating-point error.
- **Max-heap for k smallest.** To keep the `k` *smallest*, cap a *max*-heap and evict the
  current largest — the mirror image of the "min-heap for k largest" pattern. In Python,
  negate the key to turn the built-in min-heap into a max-heap.
- **Tuple ordering / tie handling.** Storing `(-d, x, y)` means Python never has to compare
  bare coordinate lists; the numeric distance dominates and the extra fields only break ties
  deterministically.
- **k = n.** All points are returned (the heap never trims) — no special case.
- **Origin duplicates / repeated points** are handled naturally; equal distances simply
  compete on the tie-break fields.
