# Solution — Partition Array to Minimize Sum Difference (LeetCode 2035)

## Brute Force

Try every way to choose which `n` of the `2n` elements go into the first array
(`C(2n, n)` ways), and track the minimum `|sum(A) - sum(B)|`.

- **Time:** `O(C(2n, n) · n)`. For `n = 15`, `C(30, 15) ≈ 1.55 × 10^8`; times the work
  per combination this is too slow / borderline TLE.
- **Space:** `O(1)`.

A capacity-indexed knapsack DP is also awkward: sums span `±1.5 × 10^8` and we must also
track the count of chosen elements, blowing up the state.

## Optimal Approach — Meet in the Middle grouped by subset size

Let `total = sum(nums)`. If the first array has sum `s`, the difference is
`|s - (total - s)| = |total - 2s|`, so we want `s` (over subsets of size exactly `n`) as
close as possible to `total / 2`.

Split `nums` into a **left** half `L` and a **right** half `R`, each of size `n`. A valid
size-`n` selection takes `k` elements from `L` and `n - k` from `R`, for some
`0 <= k <= n`. Its sum is `ls + rs` where `ls` is a size-`k` subset sum of `L` and `rs` a
size-`(n-k)` subset sum of `R`.

1. **Enumerate by count.** Build `left[k]` = list of subset sums of `L` using exactly `k`
   elements, for all `k`; similarly `right[j]`.
2. **Sort** each `right[j]`.
3. **Combine.** For each `k`, and each `ls` in `left[k]`, we need `rs` from `right[n-k]`
   with `ls + rs` closest to `total / 2`, i.e. `rs` closest to `total/2 - ls`. Binary-search
   that value in the sorted `right[n-k]`, check the neighbor(s), and update the answer with
   `|total - 2 * (ls + rs)|`.

To avoid fractions, search for `target = total - 2*ls` inside `2 * right[n-k]` (or search
`rs` near `(total - 2*ls) / 2`, checking both floor and ceil neighbors).

```python
from bisect import bisect_left
from itertools import combinations

class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 2
        total = sum(nums)
        L, R = nums[:n], nums[n:]

        # right[j] = sorted subset sums of R using exactly j elements
        right = [[] for _ in range(n + 1)]
        for j in range(n + 1):
            for comb in combinations(R, j):
                right[j].append(sum(comb))
            right[j].sort()

        best = abs(total - 2 * sum(L))       # k = n baseline (all of L, none of R)
        for k in range(n + 1):
            arr = right[n - k]
            for comb in combinations(L, k):
                ls = sum(comb)
                # want rs closest to (total - 2*ls) / 2  ->  minimize |total - 2*(ls+rs)|
                want = (total - 2 * ls) / 2
                i = bisect_left(arr, want)
                for cand in (i, i - 1):
                    if 0 <= cand < len(arr):
                        s = ls + arr[cand]
                        best = min(best, abs(total - 2 * s))
        return best
```

### Why it is correct

Every size-`n` selection uses some `k` elements from the left half and the remaining
`n - k` from the right half, and these choices are independent. Enumerating `left[k]` and
`right[n-k]` for all `k` therefore reproduces every possible size-`n` sum `s = ls + rs`.
For fixed `ls`, `|total - 2(ls + rs)|` is minimized by the `rs` nearest `(total - 2ls)/2`,
which in a sorted array is one of the two neighbors of the query. Taking the best over all
`k` and all `ls` yields the global minimum difference.

### Complexity

- **Time:** `O(2^n · n)` — enumerating each half is `Σ_k C(n,k) = 2^n` sums, sorting adds
  a `log` factor, and the combine loop does `2^n` binary searches. For `n = 15` that is
  ~`3 × 10^4` subsets per half — trivial.
- **Space:** `O(2^n)` to store the right half's sums bucketed by size.

## Key Insights & Edge Cases

- **Group by count.** The size-`n` constraint is the crux; you must pair size-`k` left
  subsets only with size-`(n-k)` right subsets. Forgetting the size split reduces this to
  ordinary subset-sum and produces wrong answers.
- **Query both neighbors** from `bisect_left`, exactly as in the closest-sum problem.
- **Avoid float rounding.** Comparing via `|total - 2*s|` (all integers) sidesteps
  precision issues even though the search target `(total - 2ls)/2` may be a half-integer;
  checking both neighbors guarantees the true closest is found.
- **Baseline.** Seed `best` with a valid selection (e.g. `k = n`, the entire left half) so
  the answer is defined even before the loop refines it.
- **Negatives / zeros** are handled naturally; the method never assumes positivity.
- `n = 1` (Example 2) forces the two singletons apart, giving `|nums[0] - nums[1]|`.
