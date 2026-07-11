# Solution — K Closest Points to Origin

## Brute Force

Compute every point's distance, sort all points by distance, and take the first
`k`.

```python
points.sort(key=lambda p: p[0] * p[0] + p[1] * p[1])
return points[:k]
```

- **Time:** `O(n log n)` — sorts all `n` points even though only `k` are needed.
- **Space:** `O(n)` (or `O(log n)` in place).

Fine, but it ranks every point when we only care about the closest `k`.

## Optimal Approach (Max-heap of size `k`)

Rank points by **squared** distance `d = x*x + y*y`. Squaring is monotonic for
non-negative distances, so it preserves ordering, keeps arithmetic integral, and
avoids `sqrt` entirely.

Maintain a **max-heap of size `k`** holding the `k` closest points seen so far.
Its root is the *farthest* of those `k`, which is exactly the candidate to evict
when a nearer point arrives. Python's `heapq` is a min-heap, so store `(-d, ...)`
to simulate a max-heap.

```python
import heapq

def kClosest(self, points, k):
    heap = []                                    # max-heap via negated distance
    for x, y in points:
        d = x * x + y * y
        heapq.heappush(heap, (-d, x, y))
        if len(heap) > k:
            heapq.heappop(heap)                  # drop the current farthest
    return [[x, y] for _, x, y in heap]
```

- **Time:** `O(n log k)` — one `O(log k)` push (and possible pop) per point.
- **Space:** `O(k)` for the heap.

**Why it is correct.** The heap invariant is that after processing any prefix of
the points it contains the `k` closest of them. When a new point arrives with
squared distance `d`: if the heap is not yet full it joins; otherwise if `d` is
smaller than the current maximum (the root, stored negated) the new point belongs
in the top `k` and displaces the farthest, and if `d` is not smaller it can never
be among the `k` closest. Using squared distance never changes the ordering
because `sqrt` is monotonic on `[0, inf)`.

### Worked trace on `points = [[3,3],[5,-1],[-2,4]], k = 2`

```
[3,3]  -> d=18  push (-18,3,3)          heap=[(-18,3,3)]
[5,-1] -> d=26  push (-26,5,-1)         heap=[(-26,5,-1),(-18,3,3)]   size 2 == k
[-2,4] -> d=20  push (-20,-2,4)         size 3 > k
                pop root (-26,5,-1)     (farthest, d=26)
                heap=[(-20,-2,4),(-18,3,3)]
answer -> [[-2,4],[3,3]]                (any order)
```

## Key Insights & Edge Cases

- **Skip the `sqrt`.** Comparing `x*x + y*y` gives the same order as the true
  Euclidean distance, stays in integer arithmetic, and avoids floating-point
  error. This is the single most important trick here.
- **Max-heap of size `k` for "k closest".** As with top-k-frequent, keeping the
  *worst* survivor at the root makes eviction `O(log k)`.
- **`heapq` is a min-heap** — negate the distance (or wrap in a comparison key)
  to get max-heap behavior.
- **`O(n log k)` vs `O(n log n)`.** Bounding the heap at `k` beats the full sort
  when `k << n`.
- **Alternatives:** a full-array max-heap popped down to `k` also works
  (`O(n + (n-k) log n)`), and Quickselect on squared distance gives `O(n)`
  average time. The size-`k` heap is the cleanest streaming-friendly choice.
- **Edge cases:** `k == len(points)` returns every point; a single point with
  `k = 1` returns it directly. Ties in distance do not matter because the answer
  is guaranteed unique up to ordering.
