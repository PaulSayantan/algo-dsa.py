# Solution — Online Majority Element in Subarray

## Brute Force

For each query, scan `arr[left..right]`, tally counts in a hash map, and check
whether any count reaches `threshold`. `O(m)` per query where `m = right-left+1`;
with `q` queries and ranges up to `n`, worst case `O(nq)` ≈ `2 * 10^8`. Borderline
and clunky, and it wastes the fact that the array is fixed.

The accepted LeetCode approaches include: (a) per-value sorted index lists +
binary search on a **random-sampling** candidate, or (b) a **segment tree of
Boyer–Moore votes**. Both are `O(log n)` per query after preprocessing. The
Wavelet Tree gives a clean, deterministic `O(log sigma)` per query without
randomization.

## Optimal Approach (Wavelet Tree)

### Key observation: the answer must be the median

If a value `v` occurs more than half the times in `arr[left..right]` (which the
guarantee `2 * threshold > len` forces for any qualifying element), then `v`
occupies more than half of the sorted order of that range. Therefore `v` **must**
sit at the middle position of the sorted range — it is the **median**. So there
is exactly one candidate to test, and we can find it with a single k-th-smallest
descent.

### Algorithm

Let `len = right - left + 1` and use half-open window `[left, right + 1)`.

1. **Build** a Wavelet Tree over `arr` supporting `kthSmallest` (Problem 3) and
   value frequency in a range (`rank`/`rangeCountLeq`, Problems 1–2):
   `O(n log sigma)`.
2. **Candidate** = `kthSmallest(left, right + 1, len // 2 + 1)` — the (lower)
   median. `O(log sigma)`.
3. **Verify**: `cnt = occurrences of candidate in [left, right + 1)`. Using
   range-count identities this is
   `rangeCountLeq(left, right+1, c) - rangeCountLeq(left, right+1, c - 1)`, or
   equivalently `rank(c, right+1) - rank(c, left)`. `O(log sigma)`.
4. Return `candidate` if `cnt >= threshold`, else `-1`.

```python
class MajorityChecker:
    def __init__(self, arr):
        self.wt = WaveletTree(arr)   # supports kth_smallest and rank/range_count

    def query(self, left, right, threshold):
        n = right - left + 1
        cand = self.wt.kth_smallest(left, right + 1, n // 2 + 1)
        cnt = self.wt.count_equal(left, right + 1, cand)   # frequency in range
        return cand if cnt >= threshold else -1
```

### Why it is correct

If an element `e` satisfies `count(e) >= threshold` and `2 * threshold > len`,
then `count(e) > len / 2`. In the sorted order of the range, the block of `e`'s
spans strictly more than half the positions, so position `len // 2` (0-based),
i.e. the `(len // 2 + 1)`-th smallest, falls inside that block — hence the median
equals `e`. Conversely, if no element exceeds half, the median might be anything,
but its verified count will be `< threshold`, so we correctly return `-1`. Either
way, testing only the median candidate is sufficient and necessary.

**Complexity:** build `O(n log sigma)` time and space; each `query`
`O(log sigma)` (one k-th-smallest descent + one/two range-count queries). With
`sigma <= 2 * 10^4`, `log sigma <= 15`.

## Key Insights & Edge Cases

- **Inclusive bounds**: the problem uses `[left, right]` inclusive; convert to
  the half-open `[left, right + 1)` the Wavelet Tree routines expect.
- **Median index**: with 0-based ranks, the guaranteed majority sits at the
  `(len // 2 + 1)`-th smallest (1-based `k`). This holds for both even and odd
  `len` given the `2 * threshold > len` guarantee.
- **Always verify**: the median is only a *candidate*. You must count its true
  frequency and compare to `threshold`; skipping this returns wrong answers when
  no majority exists (Example 2 returns `-1`).
- **Frequency query**: `count_equal(l, r, c)` can be `rangeCountLeq(l, r, c) -
  rangeCountLeq(l, r, c - 1)`, or a two-`rank` subtraction — both `O(log sigma)`.
- **Single-element range** (`left == right`): median is that element, count `1`;
  returns it iff `threshold <= 1`.
- No randomization needed — unlike the sampling solution, this is deterministic
  and never has a "bad luck" failure mode.
