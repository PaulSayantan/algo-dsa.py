# Russian Doll Envelopes — Solution

## Brute Force

Treat nesting as a directed acyclic graph: draw an edge from envelope `a` to envelope `b`
whenever `a` strictly fits inside `b`, then find the longest path.

- A common quadratic version sorts (or not) and runs a 2D longest-chain DP: for each `i`,
  `dp[i] = 1 + max(dp[j])` over all `j` that fit strictly inside `i`.
- **Time:** `O(n^2)` for the pairwise DP. **Space:** `O(n)`.

At `n = 10^5`, `n^2 = 10^10` is too slow, so we need to reduce a dimension.

## Optimal Approach (Sorting as Preprocessing)

**Idea:** Sort to collapse the 2D nesting into a 1D **Longest Increasing Subsequence
(LIS)** on heights, then solve LIS in `O(n log n)` with binary search (patience sorting).

Sort by **width ascending**; for equal widths, sort by **height descending**. After this,
scan the heights and compute the LIS with **strict** increase.

**Why the tie-break matters:** Once sorted by increasing width, if we simply took the LIS
of heights we might chain two envelopes of the *same width* (illegal, since width must be
*strictly* greater). By ordering equal-width envelopes with **height descending**, their
heights form a non-increasing run, so an increasing subsequence can pick **at most one**
of them — automatically forbidding same-width nesting. With that guarantee, any strictly
increasing subsequence of heights corresponds to a valid chain (widths strictly increase
across the chosen elements because equal-width duplicates can't both be picked).

**Why LIS with binary search is `O(n log n)`:** Maintain an array `tails`, where
`tails[k]` is the smallest possible tail height of any increasing subsequence of length
`k+1` seen so far. `tails` stays sorted, so for each new height `h` we binary-search for
the leftmost tail `>= h` (strict LIS) and overwrite it, or append `h` if it exceeds all
tails. The length of `tails` at the end is the LIS length.

**Step by step:**

1. Sort `envelopes` by `(width asc, height desc)`.
2. Extract the sequence of heights `H`.
3. Compute the strictly-increasing LIS of `H`:
   - For each `h` in `H`, binary-search the leftmost index `i` in `tails` with
     `tails[i] >= h`.
   - If `i == len(tails)`, append `h`; else set `tails[i] = h`.
4. Return `len(tails)`.

```python
import bisect

def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    envelopes.sort(key=lambda e: (e[0], -e[1]))   # width asc, height desc on ties
    tails = []                                    # tails[k] = min tail of an LIS of length k+1
    for _, h in envelopes:
        i = bisect.bisect_left(tails, h)          # strict increase -> bisect_left
        if i == len(tails):
            tails.append(h)
        else:
            tails[i] = h
    return len(tails)
```

- **Time:** `O(n log n)` for the sort plus `O(n log n)` for the LIS sweep.
- **Space:** `O(n)` for the `tails`/height arrays.

## Key Insights & Edge Cases

- **Sorting turns 2D into 1D.** Fixing the width order lets you ignore width entirely and
  optimize only over heights — the paradigm's payoff.
- **Height-descending tie-break is essential.** Using height *ascending* on ties would
  wrongly allow two equal-width envelopes to both appear in the increasing height
  subsequence, over-counting nestable envelopes.
- **Strict vs. non-strict LIS:** because nesting is strict, use `bisect_left` (leftmost
  `>= h`). For a non-strict "increasing" variant you would use `bisect_right`.
- **All identical envelopes** (`[[1,1],[1,1],[1,1]]`): after `(w asc, h desc)` sorting the
  heights are `[1,1,1]`; `bisect_left` keeps overwriting index 0, so `tails` stays length
  1 — correct, since duplicates can't nest.
- **Single envelope:** returns 1.
- **`tails` is not the actual subsequence** — it only tracks minimal tails, so its length
  is the LIS length even though its contents may not be a real chain. That's fine here
  because only the length is asked for.
