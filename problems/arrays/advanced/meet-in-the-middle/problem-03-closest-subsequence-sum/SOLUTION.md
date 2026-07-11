# Solution — Closest Subsequence Sum (LeetCode 1755)

## Brute Force

Enumerate all `2^n` subsequences, compute each sum, and track the minimum
`abs(sum - goal)`.

- **Time:** `O(2^n)` — with `n = 40` that is ~`10^12` subsequences, TLE.
- **Space:** `O(1)`.

A sum-indexed DP fails here because values (and hence achievable sums) range over roughly
`±4 · 10^8`, and negatives make the reachable-sum axis a large signed interval — far too
big to tabulate.

## Optimal Approach — Meet in the Middle + binary search

Split `nums` into halves `L` and `R` (each ≤ 20 elements). We want to pick a subset sum
`a` from `L` and `b` from `R` minimizing `abs(a + b - goal)`. Rewrite: for a fixed `b`,
the ideal `a` is the one closest to `goal - b`. If we keep `L`'s subset sums **sorted**,
we can binary-search for the value nearest `goal - b` in `O(log)` per `b`.

1. Compute `left = sorted(all subset sums of L)` and `right = all subset sums of R`.
2. For each `b` in `right`, let `want = goal - b`. Binary-search `want` in `left`; the
   closest candidate is at the insertion point or the element just before it. Update the
   global minimum with `abs(a + b - goal)` for those one or two candidates.

```python
from bisect import bisect_left

def all_subset_sums(arr):
    sums = [0]
    for x in arr:
        sums += [s + x for s in sums]
    return sums

class Solution:
    def minAbsDifference(self, nums, goal):
        mid = len(nums) // 2
        left = sorted(all_subset_sums(nums[:mid]))
        best = abs(goal)                      # empty subsequence, sum 0
        for b in all_subset_sums(nums[mid:]):
            want = goal - b
            i = bisect_left(left, want)
            if i < len(left):
                best = min(best, abs(left[i] + b - goal))
            if i > 0:
                best = min(best, abs(left[i - 1] + b - goal))
            if best == 0:
                return 0
        return best
```

### Why it is correct

Any subsequence's sum decomposes uniquely as `a + b` with `a` a subset sum of `L` and `b`
a subset sum of `R`. For a fixed `b`, `abs(a + b - goal)` is minimized by the `a` closest
to `goal - b`. In a sorted array the closest value to a query is always either the first
element `>= query` (insertion point `i`) or the element immediately before it (`i - 1`);
checking both is sufficient. Ranging over every `b` therefore examines the best `a` for
each half-pairing, and the minimum over all pairings is the global optimum. Seeding `best`
with `abs(goal)` covers the empty subsequence (`a = b = 0`).

### Complexity

- **Time:** `O(2^(n/2) · (n/2))` — building/sorting each half is `O(2^(n/2) · (n/2))`, and
  the combine loop does `2^(n/2)` binary searches at `O(n/2)` each. ~`10^6 · 20` ops.
- **Space:** `O(2^(n/2))` for the stored half sums.

## Key Insights & Edge Cases

- **Check both neighbors** returned by `bisect_left` (`i` and `i - 1`). Checking only one
  side misses the closest value when the query lands between two stored sums.
- **Early exit at 0.** Once `best == 0` you cannot do better; returning immediately can
  prune a lot of work.
- **Empty subsequence.** Its sum is `0`; initialise `best = abs(goal)` (or include `0` in
  both halves, which the `[0]` seed does) so the all-empty choice is always considered.
- **Sort the smaller work correctly.** Sorting one half costs `O(2^(n/2) log 2^(n/2)) =
  O(2^(n/2) · n/2)`, which dominates but stays within budget.
- Negatives are fully supported; the algorithm never assumes monotonic or non-negative
  sums.
