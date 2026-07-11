# Count Subsets with a Given Sum — Solution

## Brute Force

Enumerate all `2^n` subsets and count those whose sum equals `target`.

```python
def count_subsets_with_sum(nums, target):
    n = len(nums)
    count = 0
    for mask in range(1 << n):
        s = sum(nums[i] for i in range(n) if mask & (1 << i))
        if s == target:
            count += 1
    return count
```

- **Time:** `O(2^n * n)` — for `n = 40` that is `~4 * 10^13`, hopeless.
- **Space:** `O(1)`.

A pseudo-polynomial DP (`dp[i][s]`) does not help here: `target` and the values
can be as large as `10^9`–`10^10`, so the sum dimension is astronomically wide.
What saves us is that `n` is small.

## Optimal Approach (Meet in the Middle)

Split `nums` into two halves `L` (first `n/2` elements) and `R` (the rest).
Each half has at most 20 elements, so each has at most `2^20 ≈ 10^6` subsets.

A subset of the whole array = (a subset of `L`) ∪ (a subset of `R`), and its
sum is `leftSum + rightSum`. We want `leftSum + rightSum == target`, i.e.

```
rightSum == target - leftSum
```

**Step by step**

1. Enumerate all `2^|L|` subset sums of `L`; store their frequencies in a hash
   map `left_counts` (a multiset — several subsets can share a sum).
2. Enumerate all `2^|R|` subset sums of `R`. For each `rightSum`, the number of
   left subsets that complete the target is `left_counts[target - rightSum]`.
   Accumulate that.

```python
from collections import Counter

def subset_sums(arr):
    sums = [0]
    for x in arr:
        sums += [s + x for s in sums]   # doubles the list each step
    return sums

def count_subsets_with_sum(nums, target):
    mid = len(nums) // 2
    left_counts = Counter(subset_sums(nums[:mid]))
    total = 0
    for right_sum in subset_sums(nums[mid:]):
        total += left_counts[target - right_sum]
    return total
```

Why it is correct: every subset of the whole array corresponds to exactly one
(left subset, right subset) pair, and vice versa, because the index sets of the
two halves are disjoint and cover everything. So summing
`left_counts[target - rightSum]` over all right subsets counts each qualifying
full subset once. The empty subset is naturally represented by `sum = 0` in both
halves (the seed `[0]`), so `target = 0` correctly includes the empty set.

- **Time:** `O(2^(n/2) * n)` to build both halves' sums plus `O(2^(n/2))` to
  combine. For `n = 40`: about `2 * 10^6` work — instant.
- **Space:** `O(2^(n/2))` for the two lists / the `Counter`.

## Key Insights & Edge Cases

- **Multiset, not set.** Distinct subsets may share the same sum, so counts
  must accumulate frequencies. Using a `set` would undercount.
- **Empty subset.** Seed each half's enumeration with `0` so the empty subset
  is included; for `target = 0` this contributes the empty-set solution.
- **Negative values / negative target** work without change — sums are just
  keys in the hash map; nothing assumes non-negativity (another reason DP over
  a `[0..target]` array fails but MITM does not).
- **Balance the halves** (`n/2` each). An unbalanced split like `5 + 35` gives
  `2^35` on the big side and destroys the speedup.
- **From counting to existence / enumeration:** the same split answers "does a
  subset with this sum exist?" (check membership) or "find one" (store one
  witness per sum). Sorting a half instead of hashing also lets you answer
  *closest sum* queries — see Problem 3.
