# Solution — Longest Common Substring of Two Strings

## Brute Force

Try every substring of `A` and test membership in `B`, or use dynamic programming
on `dp[i][j] = ` length of the longest common suffix of `A[:i]` and `B[:j]`.

- All-substrings-of-A search: O(|A|^2 * |B|).
- Classic DP: `dp[i][j] = dp[i-1][j-1] + 1` when `A[i-1] == B[j-1]`, else 0; answer
  is the maximum cell. **Time:** O(|A| * |B|), **Space:** O(|A| * |B|)
  (reducible to O(min) with rolling rows).
- The DP is great when both strings are a few thousand chars, but O(|A|*|B|) blows
  up at `10^5 x 10^5 = 10^10`.

## Optimal Approach — Suffix Array over the Concatenation + LCP

**Idea.** Put both strings into one string with a **separator** that occurs in
neither: `T = A + '#' + B`. Build the suffix array `SA` and LCP array of `T`. A
common substring of `A` and `B` is a shared prefix of some suffix starting in the
`A` region and some suffix starting in the `B` region. Because sorted suffixes that
share long prefixes are grouped together, the maximal such shared prefix is
realized by two **adjacent** entries of `SA` — one from `A`, one from `B`.

So: scan adjacent pairs `(SA[i-1], SA[i])`; whenever the two come from **different
source strings**, their `LCP[i]` is a candidate common-substring length. The
separator `#` (and end-of-string) prevents an LCP from spanning the boundary, so a
counted match never runs past the end of `A` into the separator.

**Why adjacency suffices.** For any two suffixes (one in `A`, one in `B`) sharing a
prefix of length `L`, all suffixes lying between them in sorted order also share
that prefix. The `LCP` of a range of sorted suffixes equals the **minimum** adjacent
LCP within it, so the pair achieving the overall best cross-source match can be
taken adjacent without loss.

**Steps.**
1. `T = A + '#' + B`; record `boundary = len(A)` (index of `#`).
2. `SA = build_suffix_array(T)`, `LCP = kasai(T, SA)`.
3. Define `source(idx)`: `A` if `idx < boundary`, `B` if `idx > boundary`, else the
   separator (skip it).
4. For `i` in `1..len(T)-1`: if `source(SA[i-1]) != source(SA[i])` and neither is the
   separator, update `(best_len, best_start)` with `LCP[i]` and `SA[i]`.
5. Return `T[best_start : best_start + best_len]`.

```python
def longest_common_substring(a, b):
    sep = "\x00"                     # a char guaranteed not in a or b
    t = a + sep + b
    n = len(t)
    boundary = len(a)
    sa = build_suffix_array(t)
    lcp = kasai(t, sa)

    def source(idx):
        if idx < boundary:
            return 0
        if idx > boundary:
            return 1
        return -1                    # the separator itself

    best_len, best_start = 0, 0
    for i in range(1, n):
        s1, s2 = source(sa[i - 1]), source(sa[i])
        if s1 != -1 and s2 != -1 and s1 != s2 and lcp[i] > best_len:
            best_len, best_start = lcp[i], sa[i]
    return t[best_start: best_start + best_len]
```

- Build SA over `|A|+|B|+1`: O((|A|+|B|) log(|A|+|B|)). Kasai + scan: O(|A|+|B|).
- **Time:** O((|A|+|B|) log(|A|+|B|)). **Space:** O(|A|+|B|).

## Key Insights & Edge Cases

- **Separator must be unique** and lexicographically fine — use a character (e.g.
  `'\x00'` or `'#'`) that appears in neither string; otherwise a false "common"
  match could straddle the boundary.
- **Cross-source constraint** is essential: comparing two suffixes both from `A`
  would find a repeat *within* `A`, not a common substring.
- **No common character** → no cross-source pair improves `best_len`, so it stays 0
  and we return `""`.
- **Generalizes to k strings** (generalized suffix array): concatenate with distinct
  separators and use a sliding window over sorted suffixes requiring all `k` sources
  present — that yields "longest substring common to all k" (or "to at least K of
  them").
- The plain O(|A|*|B|) DP is simpler and often preferable when both strings are
  small; reach for the suffix array when inputs are large or when you need multiple
  such queries / the generalized version.
