# K Closest Points to Origin — Solution

## Brute Force

**Sort by distance and slice.** Compute each point's squared distance, sort all points
by it, and take the first `k`.

```python
points.sort(key=lambda p: p[0] * p[0] + p[1] * p[1])
return points[:k]
```

- **Time:** O(n log n).
- **Space:** O(n) (or O(log n)) for the sort.

A max-heap of size `k` gives O(n log k). Both are fine, but Quickselect is O(n) on
average and is the intended "partition" answer.

## Optimal Approach (Quickselect on squared distance)

We only need the `k` closest points occupying the first `k` positions — their internal
order does not matter. That is precisely what Quickselect delivers when the target
index is `k`:

1. Define the key `dist(p) = p[0]^2 + p[1]^2`. Comparing squared distances avoids the
   square root and stays in integer arithmetic.
2. Partition `points[lo..hi]` around a random pivot by this key so smaller-distance
   points move left. The pivot lands at final index `p`.
3. If `p == k` (using `k` as the boundary, i.e. we want indices `0..k-1`), the first
   `k` slots hold the `k` closest points — stop.
4. If `p < k`, recurse right (`lo = p + 1`); if `p > k`, recurse left (`hi = p - 1`).
5. Return `points[:k]`.

Note the target is index `k` (a *boundary*), so stopping when the partition index
reaches `k` guarantees `points[0..k-1]` are all `<=` everything in `points[k..]`.

### Why it is correct

Partitioning by distance places the pivot in its final rank-by-distance position and
puts all closer points before it. Once a partition boundary lands exactly at index `k`,
the left block `points[0..k-1]` consists of the `k` smallest-distance points (each is
`<=` the pivot which is `<=` the right block). Their order among themselves is
irrelevant because the problem accepts any order.

### Reference implementation

```python
import random
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(i: int) -> int:
            return points[i][0] ** 2 + points[i][1] ** 2

        def partition(lo: int, hi: int) -> int:
            r = random.randint(lo, hi)
            points[r], points[hi] = points[hi], points[r]
            pivot = dist(hi)
            i = lo
            for j in range(lo, hi):
                if dist(j) < pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[hi] = points[hi], points[i]
            return i

        lo, hi = 0, len(points) - 1
        while lo < hi:
            p = partition(lo, hi)
            if p == k:
                break
            elif p < k:
                lo = p + 1
            else:
                hi = p - 1
        return points[:k]
```

### Complexity

- **Time:** O(n) expected, O(n^2) worst case (random pivot makes this rare).
- **Space:** O(1) extra beyond the output slice; the partition is in place.

## Key Insights & Edge Cases

- **Use squared distance.** The square root is monotonic, so it never changes the
  ordering — dropping it avoids floating point and is faster.
- **Target is a boundary index `k`, not `k-1`.** Stopping when the pivot index equals
  `k` cleanly separates the first `k` elements from the rest.
- **`k == len(points)`** returns all points (the loop exits with `lo >= hi`); returning
  `points[:k]` still works.
- **Ties in distance** are acceptable in any order — Quickselect does not need to break
  them consistently (Example 3 has two equal-distance points).
- Because output order is unconstrained, this is a textbook fit for Quickselect over a
  heap.
