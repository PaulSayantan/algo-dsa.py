# Solution — Longest Common Substring of Two Strings

## Brute Force

Try every substring of `a` and test whether it occurs in `b`. There are
`O(n^2)` substrings of `a` and each search in `b` is `O(n)`, giving **O(n^3)**.

The classic dynamic-programming approach fills a table `dp[i][j]` = length of the
longest common suffix of `a[:i]` and `b[:j]`, taking the overall maximum. That is
**O(n * m)** time and **O(n * m)** space (reducible to `O(min(n, m))` space).
This is often good enough, but it is quadratic and cannot scale to two strings of
length `10^5` each.

## Optimal Approach (Suffix Array + LCP / Kasai)

**Idea:** glue the two strings into one with a separator that appears in neither:

```
s = a + '#' + b + '$'
```

The `'#'` prevents a suffix that begins in `a` from "leaking" a match across the
boundary into `b` (a common prefix can never span the separator because `'#'`
occurs only once). The trailing `'$'` guarantees every suffix is distinct.

Now build `SA` and `LCP` on `s`. A **common substring of `a` and `b`** is a
common prefix of some suffix starting in `a` and some suffix starting in `b`.
As with the single-string case, the best such match is achieved by an
**adjacent pair in the suffix array** — but only for pairs where the two
suffixes come from *different* source strings. So:

```
answer_len = max over adjacent i of  LCP[i]
             such that SA[i-1] and SA[i] lie in different original strings
```

Track which side each index belongs to: with `la = len(a)`, index `p` is in `a`
iff `p < la` (indices `> la` are in `b`; index `la` is the separator `'#'`).

### Steps

1. Form `s = a + '#' + b + '$'` (or use two distinct separators as shown).
2. Build `SA` (`O(N log N)`, `N = len(s)`).
3. Build `LCP` via Kasai (`O(N)`).
4. Scan adjacent pairs; whenever they straddle the boundary, update the best
   length and remember the start index to reconstruct the substring.

```python
def longest_common_substring(a, b):
    la = len(a)
    s = a + '#' + b + '$'
    n = len(s)
    sa = build_suffix_array(s)
    lcp = build_lcp_kasai(s, sa)

    def in_a(pos):
        return pos < la  # positions > la are in b; la itself is '#'

    best_len, best_start = 0, 0
    for i in range(1, n):
        p, q = sa[i - 1], sa[i]
        if in_a(p) != in_a(q):        # straddles the two source strings
            if lcp[i] > best_len:
                best_len, best_start = lcp[i], sa[i]
    return s[best_start:best_start + best_len]
```

### Why the separator matters

Without `'#'`, a suffix starting near the end of `a` would continue into the
characters of `b`, so a computed LCP could describe a string that is not a real
substring of `a` alone. Because `'#'` is unique and lexicographically distinct,
any common prefix stops at or before it, keeping matches confined to genuine
substrings of a single source string.

### Complexity

- Let `N = len(a) + len(b) + 2`.
- Suffix array: **O(N log N)** time, **O(N)** space.
- Kasai LCP + scan: **O(N)** time, **O(N)** space.
- Overall: **O(N log N)** time, **O(N)** space — far better than the `O(nm)` DP
  for large inputs.

## Key Insights & Edge Cases

- **Cross-string adjacency:** you must ignore adjacent pairs that are *both* from
  `a` or *both* from `b`; those describe repeats within one string, not a common
  substring.
- **Separator uniqueness:** the separators must not occur in `a` or `b`. If the
  alphabet could include them, remap to sentinel values smaller/larger than all
  real characters instead of literal `'#'`/`'$'`.
- **No common substring:** if no cross pair has `LCP > 0`, return `""`.
- **Generalization to k strings:** concatenate all with distinct separators and
  use a sliding window over the LCP array requiring the window to cover suffixes
  from all `k` strings (the "at least k colors" technique).
- Ties in length: any longest common substring is acceptable.
