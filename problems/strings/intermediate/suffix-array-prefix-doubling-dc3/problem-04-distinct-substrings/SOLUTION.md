# Solution — Number of Distinct Substrings

## Brute Force

Insert every substring into a hash set and return its size, or build a trie of all
suffixes and count nodes.

- There are O(n^2) substrings, each of length up to O(n); hashing them all is
  O(n^3) time and O(n^2) storage for the distinct strings.
- A suffix trie counts nodes in O(n^2) time / O(n^2) space.
- **Time:** O(n^3) (set of strings) or O(n^2) (trie). **Space:** O(n^2).
- Infeasible for `n = 10^5`.

## Optimal Approach — Suffix Array + LCP

**Idea.** Every substring of `S` is a prefix of exactly one suffix. Suffix `S[i:]`
has `n - i` non-empty prefixes, so the number of substrings counted *with
multiplicity* is

```
sum over suffixes of (length) = n + (n-1) + ... + 1 = n(n+1)/2.
```

Now process suffixes in **sorted** order. When we move from suffix `SA[i-1]` to
`SA[i]`, they share a common prefix of length `LCP[i]`. Those `LCP[i]` prefixes of
`SA[i]` are **exactly** the prefixes we already counted for `SA[i-1]` (and earlier),
so they are duplicates. Every longer prefix of `SA[i]` (there are
`(n - SA[i]) - LCP[i]` of them) is brand new. Summing the *new* contributions:

```
distinct = sum_i [ (n - SA[i]) - LCP[i] ]
         = sum_i (n - SA[i])  -  sum_i LCP[i]
         = n(n+1)/2  -  sum(LCP).
```

**Why it is correct.** Sorting guarantees that all suffixes sharing a given prefix
are grouped, so a repeated prefix is always shared with the *immediately preceding*
sorted suffix — never missed and never double-subtracted. Thus subtracting `LCP[i]`
per step removes each duplicate substring exactly once.

**Steps.**
1. `SA = build_suffix_array(S)`  — O(n log n).
2. `LCP = kasai(S, SA)`          — O(n).
3. Return `n*(n+1)//2 - sum(LCP)`.

```python
def count_distinct_substrings(s):
    n = len(s)
    if n == 0:
        return 0
    sa = build_suffix_array(s)
    lcp = kasai(s, sa)            # lcp[0] = 0, lcp[i] = LCP(sa[i-1], sa[i])
    return n * (n + 1) // 2 - sum(lcp)
```

- **Time:** O(n log n) (dominated by the suffix-array build). **Space:** O(n).

## Key Insights & Edge Cases

- **Counting formula `n(n+1)/2 - sum(LCP)`** is the canonical distinct-substring
  identity — memorize it.
- **`LCP[0]` must be 0** (the first sorted suffix has no predecessor); using Kasai
  as written guarantees this.
- **All-equal string** (`"aaa"`): `sum(LCP) = 2+1 = 3`, distinct `= 6 - 3 = 3`.
- **All-distinct characters** (`"abc"`): `sum(LCP) = 0`, distinct `= n(n+1)/2`.
- **Big answer:** for `n = 10^5` the count approaches `5 * 10^9`, which exceeds
  32-bit range — use 64-bit integers (automatic in Python, but relevant in C++/Java).
- **Empty string** → 0 distinct substrings; guard the `n == 0` case.
- To count distinct substrings **of a fixed length `L`**, count sorted suffixes
  whose length `>= L` and whose `LCP` with the predecessor is `< L` — a small variant
  of the same LCP idea.
