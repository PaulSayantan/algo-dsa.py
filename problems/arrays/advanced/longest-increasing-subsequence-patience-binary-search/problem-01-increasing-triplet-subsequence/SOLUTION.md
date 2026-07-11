# Solution — Increasing Triplet Subsequence

## Brute Force

Try every triple of indices `i < j < k` and check the strict-increase
condition. Or, a smarter quadratic-ish variant: for each `j`, scan left for a
smaller element and right for a larger element.

- The full triple scan is `O(n^3)` time, `O(1)` space.
- The "smaller-on-left, larger-on-right" precomputation (prefix min and suffix
  max arrays) gives `O(n)` time and `O(n)` space, but it is really just a
  special case of the LIS idea below.

Both are correct but the triple scan blows up at `n = 5 * 10^5`.

## Optimal Approach (Longest Increasing Subsequence via patience)

This problem is exactly "does the LIS length reach 3?" The `O(n log n)`
patience-sorting LIS keeps a `tails` array where `tails[i]` is the smallest
possible tail value of any increasing subsequence of length `i + 1`. As soon
as `tails` would grow to length 3, the answer is `true`.

Because we only care about length 3, `tails` never needs more than two slots,
so the binary search collapses into two scalar variables:

- `first`  = smallest value seen so far  (best tail of a length-1 subsequence)
- `second` = smallest tail of a length-2 increasing subsequence seen so far

Walk left to right. For each `x`:

1. If `x <= first`, we found an even smaller starting value: set `first = x`.
   (This is patience "place on pile 1".)
2. Else if `x <= second`, `x` can extend some length-1 run into a length-2
   run with a smaller tail: set `second = x`. (Place on pile 2.)
3. Else `x > second`, so there is a value `< second` that appeared before the
   value that set `second`, which in turn appeared before `x`. That is a
   length-3 increasing subsequence → return `true`.

### Why it is correct

The subtle point: when we assign `second = x`, there was some earlier element
strictly less than `x` (the value that owned `first` at that moment). Even if
`first` is later overwritten by a still-smaller value that sits to the *right*
of `second`, the historical fact "a value < second occurred before second"
remains true. So reaching step 3 always corresponds to a genuine ordered
triple. This mirrors the patience-sorting invariant: opening pile 3 means
some card went onto pile 2 (needing a smaller card before it) and pile 1
(needing a smaller card before that), all in index order.

Use `<=` (not `<`) in steps 1 and 2 so that equal values do not falsely count
as increases — we need **strict** `<`.

### Reference implementation

```python
def increasingTriplet(self, nums: List[int]) -> bool:
    first = second = float("inf")
    for x in nums:
        if x <= first:
            first = x
        elif x <= second:
            second = x
        else:
            return True
    return False
```

- **Time:** `O(n)` — a single pass (the LIS binary search degenerates to
  constant work because `tails` has at most 2 entries).
- **Space:** `O(1)` — two scalars.

## Key Insights & Edge Cases

- This is the base case of the whole LIS/patience family: cap the `tails`
  array at length `k` and you get "is there an increasing subsequence of
  length `k`?" For general `k`, keep the real `tails` array and binary search.
- **Strictness matters:** `[1, 1, 1, 1]` must return `false`. Using `<=` in
  the comparisons handles duplicates correctly.
- **Negatives / INT_MIN / INT_MAX:** initializing `first` and `second` to
  `+inf` (Python) avoids any overflow concerns; the logic is value-agnostic.
- Arrays shorter than 3 always return `false` and the loop handles that
  naturally without a special case.
- `second` being finite does **not** by itself mean an increasing pair still
  "exists to the left of the current index" in the naive sense — but the
  correctness argument above shows the returned `true` is always valid.
