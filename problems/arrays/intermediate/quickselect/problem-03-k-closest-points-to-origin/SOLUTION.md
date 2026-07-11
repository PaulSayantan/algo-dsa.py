# Solution — K Closest Points to Origin

## Brute Force

Sort all points by squared distance and take the first `k`.

```python
def kClosest(self, points, k):
    points.sort(key=lambda p: p[0] * p[0] + p[1] * p[1])
    return points[:k]
```

- **Time:** `O(n log n)`.
- **Space:** `O(1)` to `O(n)` depending on the sort.

A **max-heap of size k** (push squared distance, pop when size exceeds k) gives
`O(n log k)` time and `O(k)` space — preferable when `k << n` or in a streaming setting.

## Optimal Approach (Quickselect)

We need the **set** of k nearest points, not a sorted list, so Quickselect is ideal.
Order points by their **squared** distance `d = x*x + y*y` (monotonic in true distance,
so `sqrt` is unnecessary and avoids floating point). We want the k smallest distances in
the first `k` positions.

### Why it is correct

Partition rearranges the array so that after placing a pivot at final index `p`, every
point at index `< p` has distance `<=` the pivot's and every point at index `> p` has
distance `>=` the pivot's. We target index `k - 1`:

- If `p == k - 1`, then indices `0 .. k-1` hold exactly the k smallest-distance points
  (each `<=` the pivot at `k-1`), so `points[:k]` is the answer.
- If `p < k - 1`, we still need more small elements to the right: search `[p + 1, hi]`.
- If `p > k - 1`, we overshot: search `[lo, p - 1]`.

The order **within** the first k slots does not matter, which is why we never sort them —
partitioning to the boundary is enough.

### Reference implementation

```python
import random
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(i: int) -> int:
            x, y = points[i]
            return x * x + y * y

        def partition(lo: int, hi: int) -> int:
            rand = random.randint(lo, hi)
            points[rand], points[hi] = points[hi], points[rand]
            pivot = dist(hi)
            i = lo
            for j in range(lo, hi):
                if dist(j) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[hi] = points[hi], points[i]
            return i

        lo, hi, target = 0, len(points) - 1, k - 1
        while lo <= hi:
            p = partition(lo, hi)
            if p == target:
                break
            elif p < target:
                lo = p + 1
            else:
                hi = p - 1
        return points[:k]
```

- **Time:** expected `O(n)`; worst case `O(n^2)` (random pivot makes it unlikely).
- **Space:** `O(1)` extra (partitions the `points` list in place).

## Key Insights & Edge Cases

- **Compare squared distance, not the real distance.** `x*x + y*y` preserves ordering,
  is exact integer arithmetic, and skips a costly `sqrt`.
- **Target index is `k - 1`**, not `k` — we want the first `k` slots `[0 .. k-1]` filled.
- **Return the prefix, not a sorted list.** The problem allows any order, so avoid an extra
  `O(k log k)` sort.
- **k == n:** the loop still works; the whole array is "closest," and `points[:k]` returns
  everything.
- **Ties in distance:** the problem guarantees a unique answer set, and `<=` in partition
  handles equal distances without infinite loops.
- **In-place mutation:** `points` is reordered. Copy it first if the caller needs the
  original ordering preserved.
