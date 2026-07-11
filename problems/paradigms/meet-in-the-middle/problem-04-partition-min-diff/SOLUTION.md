# Partition Array Into Two Halves — Solution

## Reframing the objective

Let `S = sum(nums)`. If the first array has sum `s1`, the second has
`S - s1`, and the difference is

```
abs(s1 - (S - s1)) = abs(2 * s1 - S).
```

So we only need to choose `n` of the `2n` elements whose sum `s1` is as close
as possible to `S / 2`. That is a *balanced* subset-sum problem: exactly `n`
elements must be chosen.

## Brute Force

Try every way to choose `n` elements for the first array.

```python
from itertools import combinations

def minimumDifference(nums):
    S = sum(nums)
    n = len(nums) // 2
    best = float("inf")
    for combo in combinations(range(2 * n), n):
        s1 = sum(nums[i] for i in combo)
        best = min(best, abs(2 * s1 - S))
    return best
```

- **Time:** `O(C(2n, n) * n)`. For `n = 15`, `C(30, 15) ≈ 1.55 * 10^8`
  combinations times `n` — too slow.
- **Space:** `O(n)`.

## Optimal Approach (Meet in the Middle, grouped by count)

Split `nums` into a left half `L` and right half `R`, each of size `n`.

The first array takes some `k` elements from `L` and the remaining `n - k`
elements from `R` (for some `0 <= k <= n`). Its sum is

```
s1 = (sum of a k-subset of L) + (sum of an (n - k)-subset of R).
```

So we must combine a `k`-element choice on the left with an `(n - k)`-element
choice on the right — the counts are *constrained* to add up to `n`. This is
why plain subset-sum MITM is not enough: we bucket sums by cardinality.

**Step by step**

1. Enumerate all subsets of `L`. Bucket their sums by popcount:
   `left[k]` = sorted list of sums of all `k`-element subsets of `L`.
   Do the same for `R` to get `right[k]`.
2. For each `k` from `0` to `n`:
   - The left contributes a `k`-subset (`a` in `left[k]`), the right an
     `(n - k)`-subset (`b` in `right[n - k]`).
   - We want `2 * (a + b) - S` closest to 0, i.e. `b` closest to the real
     target `t = S / 2 - a`. Binary search `t` in the sorted `right[n - k]`
     and test the neighbor on each side.

```python
from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums):
        S = sum(nums)
        n = len(nums) // 2
        L, R = nums[:n], nums[n:]

        def sums_by_count(arr):
            buckets = [[] for _ in range(len(arr) + 1)]
            for mask in range(1 << len(arr)):
                k = bin(mask).count("1")
                s = sum(arr[i] for i in range(len(arr)) if mask & (1 << i))
                buckets[k].append(s)
            return buckets

        left = sums_by_count(L)
        right = sums_by_count(R)
        for b in right:
            b.sort()

        best = float("inf")
        for k in range(n + 1):
            others = right[n - k]
            for a in left[k]:
                # want b so that 2*(a+b) is closest to S  ->  b near (S/2 - a)
                # search the value (S - 2a) against 2*b to avoid floats:
                lo, hi = 0, len(others)
                target2 = S - 2 * a          # want 2*b closest to this
                # binary search over sorted `others` by 2*b
                idx = bisect_left(others, target2 / 2)
                for j in (idx - 1, idx):
                    if 0 <= j < len(others):
                        s1 = a + others[j]
                        best = min(best, abs(2 * s1 - S))
        return best
```

Why it is correct: any balanced partition assigns `k` of the first array's
elements to positions in `L` and `n - k` to positions in `R`, for some `k`.
By iterating `k` and, for every `k`-subset sum `a` of `L`, finding the
`(n - k)`-subset sum `b` of `R` that pushes `a + b` closest to `S / 2`, we
examine an optimum for every possible split shape. The two neighbors around the
binary-search insertion point bracket the closest achievable `b`.

- **Time:** enumerating each half is `O(2^n * n)`; sorting the buckets is
  `O(2^n * n)`; the combine loop does one binary search per left sum, `O(2^n *
  log 2^n) = O(n * 2^n)`. Overall `O(n * 2^n)`. For `n = 15`, `2^15 = 32768`,
  so about `10^6`–`10^7` ops — fast.
- **Space:** `O(2^n)` for the bucketed sums.

## Key Insights & Edge Cases

- **The cardinality constraint is the twist.** Unlike Problems 1–3, halves
  cannot be combined freely; a left choice of `k` elements must meet a right
  choice of exactly `n - k`. Bucketing subset sums by popcount encodes this.
- **Transform the objective** to `abs(2 * s1 - S)` so there is a single scalar
  to minimize; then it is "closest subset sum to `S/2` with exactly `n` picks."
- **Avoid float target if you like:** searching for `2*b` closest to `S - 2a`
  keeps everything integer; the version above uses `target2 / 2` purely for the
  `bisect` key and still checks both neighbors, so rounding cannot lose the
  optimum.
- **Check both neighbors** of the insertion index — the nearest value can lie
  just below or just above the target.
- **Edge counts `k = 0` and `k = n`** (all first-array elements come from one
  half) are included by the loop, so no special casing is needed.
- **Negative numbers** are handled naturally; nothing assumes positivity.
