# Solution — Count Subsets With Given Sum

## Brute Force

Enumerate all `2^n` subsets, sum each, and increment a counter whenever the sum equals
`target`.

- **Time:** `O(2^n)` — ~`10^12` for `n = 40`, far too slow.
- **Space:** `O(1)`.

The pseudo-polynomial counting DP (`dp[s] += dp[s - x]`) needs a table indexed by sum,
which is impossible when `target` can be `10^14` and values can be negative.

## Optimal Approach — Meet in the Middle

The idea mirrors the decision problem, but instead of a *set* of reachable sums we keep a
*multiplicity map*: how many subsets of a half produce each sum.

1. Split `nums` into halves `L` and `R`.
2. Build `left_count`, a dictionary mapping each subset sum of `L` to the number of
   `L`-subsets achieving it.
3. Enumerate every subset sum `r` of `R`. Any full subset with total `target` pairs an
   `R`-subset summing to `r` with an `L`-subset summing to `target - r`. So add
   `left_count.get(target - r, 0)` to the answer for each `r`.

Because the two halves are chosen independently, multiplying/adding counts across the
split counts every full subset exactly once.

```python
from collections import Counter

def subset_sum_counts(arr):
    counts = Counter({0: 1})            # one way to make sum 0: the empty subset
    for x in arr:
        nxt = Counter(counts)
        for s, c in counts.items():
            nxt[s + x] += c
        counts = nxt
    return counts

def count_subsets_with_sum(nums, target):
    mid = len(nums) // 2
    left = subset_sum_counts(nums[:mid])
    total = 0
    for r, c in subset_sum_counts(nums[mid:]).items():
        total += c * left.get(target - r, 0)
    return total
```

### Why it is correct

Every full subset partitions uniquely into its `L`-part and `R`-part. If the `L`-part
sums to `a` and the `R`-part to `b`, the full subset is counted in the term
`left_count[a] * right_count[b]` exactly once, and it contributes to the answer iff
`a + b == target`. Iterating over all `r = b` and adding `right_count[b] * left_count[target - b]`
therefore sums the product over all valid `(a, b)` pairs — i.e. the total number of
qualifying full subsets. The empty subset is represented by the `{0: 1}` seed in each
half, so it is counted when `target == 0`.

### Complexity

- **Time:** `O(2^(n/2))` to build each half's counter and `O(2^(n/2))` to combine.
- **Space:** `O(2^(n/2))` for the left counter.

## Key Insights & Edge Cases

- **Count, don't dedupe by value.** Two subsets with the same value multiset but different
  index sets are distinct (see Example 2). Using a `Counter` of sums handles this since
  equal partial sums accumulate their counts rather than collapsing.
- **Multiply the two halves' counts.** The combine step is a product `c_R * c_L`, not just
  a `+= 1`; forgetting this undercounts whenever a half has multiple subsets at the same
  sum.
- **Empty subset.** Seeding each half with `{0: 1}` makes the empty subset fall out
  naturally; the global empty subset is the pairing (`a=0`, `b=0`).
- **Overflow.** In languages with fixed-width ints, the count of subsets can approach
  `2^40`, so use 64-bit. Python integers are unbounded, so no concern there.
- Negatives and zeros need no special treatment — additivity is all that matters.
