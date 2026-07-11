# Solution — Subset Sum Exists

## Brute Force

Enumerate every one of the `2^n` subsets and check whether any sums to `target`.

- **Time:** `O(2^n)` — for `n = 40` that is ~`10^12` subsets, far too slow.
- **Space:** `O(1)` (or `O(n)` for a recursion stack).

The classic pseudo-polynomial DP (`dp[sum] = reachable?`) is also out: `target` can be
as large as `10^14`, so a table indexed by sum needs `10^14` cells — infeasible in both
time and space. And with negative numbers the reachable sums span a huge signed range.

## Optimal Approach — Meet in the Middle

Split `nums` into two halves `L` (first `⌈n/2⌉` elements) and `R` (the rest). Each half
has at most 20 elements, so each has at most `2^20 ≈ 10^6` subsets.

1. Enumerate **all** subset sums of `L` into a set `left_sums`.
2. Enumerate **all** subset sums of `R`.
3. A full subset sum equals `l + r` where `l` comes from `L` and `r` from `R`. We need
   `l + r == target`, i.e. `l == target - r`. So for each `r` in `R`'s subset sums,
   check whether `target - r` is present in `left_sums`.

Because `left_sums` is a hash set, each membership test is `O(1)`.

```python
from itertools import combinations

def all_subset_sums(arr):
    sums = [0]
    for x in arr:
        sums += [s + x for s in sums]   # doubles the list each step
    return sums

def subset_sum_exists(nums, target):
    mid = len(nums) // 2
    left = set(all_subset_sums(nums[:mid]))
    for r in all_subset_sums(nums[mid:]):
        if target - r in left:
            return True
    return False
```

### Why it is correct

Every subset of `nums` chooses some elements from `L` and some from `R` independently, so
its sum is exactly (a subset sum of `L`) + (a subset sum of `R`). Enumerating all subset
sums of each half therefore covers every possible full-subset sum. Checking
`target - r ∈ left_sums` finds a matching pair iff some full subset totals `target`. The
empty subset is included automatically because `all_subset_sums` starts from `[0]`.

### Complexity

- **Time:** `O(2^(n/2))` to build each half plus `O(2^(n/2))` hash lookups →
  `O(2^(n/2))` overall ≈ `2 · 10^6` operations for `n = 40`.
- **Space:** `O(2^(n/2))` to store `left_sums`.

## Key Insights & Edge Cases

- **Negatives and zero are fine.** The method only relies on additivity, so signed
  values and zeros need no special handling.
- **Empty subset counts as 0.** If `target == 0`, the empty-empty pairing (`l = 0`,
  `r = 0`) returns `True`. If the problem wanted a *non-empty* subset, you would exclude
  the `(0, 0)` pairing.
- **Only one half needs to be stored.** You can keep the larger half in a set and stream
  the other half, halving peak memory.
- **Duplicates in `nums`** are handled naturally — subsets are chosen by index, and equal
  sums simply collide in the set (fine for a decision problem).
- Balance the split (`⌈n/2⌉` vs `⌊n/2⌋`) so neither half exceeds `2^20`.
