# Solution — Russian Doll Envelopes

## Brute Force

Sort envelopes and run the `O(n^2)` LIS dynamic program in 2D: `dp[i]` is the
longest chain ending at envelope `i`, and `dp[i] = 1 + max(dp[j])` over all
`j` whose width and height are both strictly smaller than envelope `i`'s.

- **Time:** `O(n^2)`. Too slow for `n = 10^5`.
- **Space:** `O(n)`.

## Optimal Approach (sort + patience LIS on height)

The two-dimensional nesting constraint collapses to a one-dimensional LIS once
the array is sorted the right way.

**Sort key:** ascending by width `w`; and for **equal widths**, descending by
height `h`.

```
sort envelopes by (w ascending, h descending)
```

After sorting, run the strictly-increasing LIS (patience + `bisect_left`) on
just the sequence of **heights**. The answer is that LIS length.

### Why the tricky sort works

We need both dimensions strictly increasing. Sorting by width ascending means
that as we scan left to right, widths never decrease — so any increasing
subsequence of heights we find comes from envelopes with non-decreasing
widths. The danger is two envelopes with the **same width**: they must never
both be in the chain (a tie in width breaks the strict-`<` requirement).

The descending-height tie-break neutralizes this: among envelopes of equal
width, their heights appear in *decreasing* order in the sorted array. A
strictly increasing LIS can therefore pick **at most one** of them (you can't
have a strict increase inside a decreasing block). This is exactly what we
want — one envelope per width bucket, at most.

Then, because widths are non-decreasing overall and equal-width groups can
contribute only a single element, a strictly increasing run of heights
guarantees strictly increasing widths as well. So the height-LIS length equals
the longest valid nesting chain.

Run the LIS on heights with `bisect_left` (strict increase) — heights within
the chain must also strictly increase.

### Reference implementation

```python
import bisect

def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    # width asc, height DESC on ties
    envelopes.sort(key=lambda e: (e[0], -e[1]))

    tails = []                       # LIS over heights
    for _, h in envelopes:
        pos = bisect.bisect_left(tails, h)   # strict increase
        if pos == len(tails):
            tails.append(h)
        else:
            tails[pos] = h
    return len(tails)
```

- **Time:** `O(n log n)` — the sort dominates, and the LIS pass is also
  `O(n log n)`.
- **Space:** `O(n)`.

## Key Insights & Edge Cases

- **The tie-break is the entire problem.** If you sort heights *ascending* on
  equal widths, two same-width envelopes could both be picked (their heights
  strictly increase), producing an invalid chain and an over-count. Descending
  heights on ties prevents that.
- **`bisect_left` for the height LIS** because heights must strictly increase.
  Pairing "width asc / height desc" sort with a `bisect_left` LIS is the exact
  combination that enforces strict inequality on both dimensions.
- **All-identical envelopes** → answer 1 (see example 2): the descending
  tie-break lines their heights up as a decreasing block, so LIS picks one.
- **Single envelope** → 1.
- This "sort one dimension, LIS the other" pattern generalizes to many 2D
  chaining / box-stacking problems.
