# Maximum Gap — Solution

## Brute Force

Sort the array and scan adjacent pairs for the largest difference.

```python
def maximumGap(nums):
    if len(nums) < 2:
        return 0
    nums.sort()
    return max(b - a for a, b in zip(nums, nums[1:]))
```

- **Time:** `O(n log n)` for the comparison sort.
- **Space:** `O(1)` extra (or `O(n)` depending on the sort).

Correct, but it violates the required **linear-time, linear-space** bound. We
need a distribution approach.

## Optimal Approach (Bucket Sort / Pigeonhole)

**The insight:** with `n` numbers spanning `[lo, hi]`, the values that would be
adjacent in the sorted order differ by *at least* the average gap
`ceil((hi - lo) / (n - 1))`. If we make each bucket **narrower than** this
minimum possible maximum gap, then the maximum gap can never lie *inside* a
single bucket — it must straddle the empty space *between* one bucket's max and
the next non-empty bucket's min. That means we never have to sort within a
bucket at all; we only track each bucket's min and max.

### Steps

1. If `len(nums) < 2`, return `0`.
2. Let `lo = min(nums)`, `hi = max(nums)`. If `lo == hi`, all values are equal,
   so the answer is `0`.
3. Choose a bucket width `w = max(1, (hi - lo) // (n - 1))` and the number of
   buckets `count = (hi - lo) // w + 1`.
4. For each value `x`, its bucket index is `(x - lo) // w`. Store only the
   running `min` and `max` for each bucket (skip empty buckets).
5. Walk the buckets left to right. The answer is the largest difference between
   the current non-empty bucket's `min` and the previous non-empty bucket's
   `max`.

```python
from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        lo, hi = min(nums), max(nums)
        if lo == hi:
            return 0

        # Bucket width and count. Width >= 1, and small enough that the max gap
        # cannot fit inside one bucket.
        w = max(1, (hi - lo) // (n - 1))
        count = (hi - lo) // w + 1

        bucket_min = [float("inf")] * count
        bucket_max = [float("-inf")] * count
        for x in nums:
            idx = (x - lo) // w
            bucket_min[idx] = min(bucket_min[idx], x)
            bucket_max[idx] = max(bucket_max[idx], x)

        best = 0
        prev_max = lo  # max of the last non-empty bucket seen
        for i in range(count):
            if bucket_min[i] == float("inf"):
                continue  # empty bucket
            best = max(best, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
        return best
```

### Why It Is Correct

There are `n` numbers, and `lo` and `hi` are two of them, so at most `n - 1`
gaps separate the sorted values. By pigeonhole, the maximum gap is at least
`ceil((hi - lo) / (n - 1)) >= w + `(a fraction)`, which is strictly greater than
the bucket width `w`. Therefore two values sitting in the *same* bucket differ
by less than `w`, which is less than the true maximum gap — so the maximum gap
must occur between the maximum of one bucket and the minimum of the next
non-empty bucket. Scanning left to right and comparing `bucket_min[i]` against
the previous non-empty `bucket_max` examines exactly these cross-bucket gaps, so
the largest one found is the answer.

### Complexity

- **Time:** `O(n + count) = O(n)`. One pass to fill buckets, one pass over the
  `~n` buckets.
- **Space:** `O(n)` for the two bucket arrays.

## Key Insights & Edge Cases

- **Fewer than two elements** returns `0` immediately.
- **All equal values** (`lo == hi`): every gap is `0`; handle before computing
  `w` to avoid division issues.
- **`w = max(1, ...)`** guards against a width of `0` when `hi - lo < n - 1`
  (many close values), which would otherwise cause a divide-by-zero or a huge
  bucket count.
- **You never sort inside a bucket** — storing only min/max is what keeps this
  linear. This is the defining trick versus a naive bucket sort that sorts each
  bucket.
- **`prev_max` starts at `lo`** so the first non-empty bucket compares against
  the global minimum without a special case.
- Large values up to `10^9` are fine in Python (arbitrary precision ints); in
  fixed-width languages, use 64-bit arithmetic for `x - lo`.
