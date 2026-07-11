# Solution — Count Distinct Substrings

## Brute Force

Insert every substring into a hash set and return its size. There are
`O(n^2)` substrings and each has length up to `n`, so hashing them all costs
**O(n^3)** time (or `O(n^2)` with rolling hashes, but with collision risk) and
**O(n^2)** space for storing them. Infeasible for `n = 10^5`.

## Optimal Approach (Suffix Array + LCP / Kasai)

**Key bijection:** every non-empty substring of `s` is a **prefix of exactly one
suffix** — specifically, of the *lexicographically smallest* suffix that starts
with it. If we list suffixes in sorted order (the suffix array), then when we
move from sorted suffix `i-1` to sorted suffix `i`, the prefixes of suffix `i`
that are **also prefixes of suffix `i-1`** are precisely its first `LCP[i]`
prefixes — those substrings were already counted. Every longer prefix of suffix
`i` is brand new.

So sorted suffix `i` (which has length `n - SA[i]`) contributes

```
new(i) = (n - SA[i]) - LCP[i]
```

distinct substrings, and the total is

```
answer = sum_i (n - SA[i]) - sum_i LCP[i]
       = n(n+1)/2 - sum(LCP)
```

because `sum_i (n - SA[i])` is just the sum of all suffix lengths
`n + (n-1) + ... + 1 = n(n+1)/2`.

### Steps

1. Build suffix array `SA` (`O(n log n)`).
2. Build `LCP` via Kasai (`O(n)`).
3. Return `n*(n+1)//2 - sum(LCP)`.

```python
def count_distinct_substrings(s):
    n = len(s)
    if n == 0:
        return 0
    sa = build_suffix_array(s)
    lcp = build_lcp_kasai(s, sa)
    return n * (n + 1) // 2 - sum(lcp)
```

### Worked check on "banana"

`SA = [5, 3, 1, 0, 4, 2]` (suffixes `a, ana, anana, banana, na, nana`),
`LCP = [0, 1, 3, 0, 0, 2]`, so `sum(LCP) = 6`.
`n(n+1)/2 = 6*7/2 = 21`, and `21 - 6 = 15`. Matches.

### Complexity

- Suffix array: **O(n log n)** time, **O(n)** space.
- Kasai LCP + final sum: **O(n)** time, **O(n)** space.
- Overall: **O(n log n)** time, **O(n)** space.

## Key Insights & Edge Cases

- **The formula `n(n+1)/2 - sum(LCP)`** is the whole trick: total substrings
  minus the ones that duplicate a prefix already seen from the previous sorted
  suffix.
- **Why adjacency suffices:** duplicated prefixes only need to be discounted
  against the immediately preceding sorted suffix, because any repeat of a
  prefix appears among a contiguous block of sorted suffixes, and the LCP with
  the direct predecessor captures exactly the overlap with everything before it.
- **64-bit overflow:** in languages with fixed-width integers, the answer can
  reach ~`5 * 10^9`; use `long`/`int64`. Python integers are unbounded.
- **Empty string:** return 0. Single character: returns 1.
- An alternative accepted answer is a **suffix automaton**, which counts
  distinct substrings in `O(n)` overall; the suffix-array + LCP approach is the
  standard array-based method.
