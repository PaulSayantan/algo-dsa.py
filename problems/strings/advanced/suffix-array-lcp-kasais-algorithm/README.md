# Suffix Array + LCP (Kasai's Algorithm)

## What it is

A **suffix array** of a string `s` of length `n` is a sorted array `SA[0..n-1]`
containing the starting indices of all `n` suffixes of `s`, ordered
lexicographically. It is a compact, cache-friendly alternative to a suffix tree.

The **LCP array** stores, for each adjacent pair of suffixes *in sorted order*,
the length of their Longest Common Prefix:

```
LCP[i] = lcp( s[SA[i-1]:] , s[SA[i]:] )   for i = 1..n-1 ,   LCP[0] = 0
```

**Kasai's algorithm** computes the entire LCP array in **O(n)** time once the
suffix array is known. The key insight is that if suffix starting at `i` has
LCP value `h` with its predecessor in sorted order, then the suffix starting at
`i+1` has an LCP of at least `h-1` with *its* predecessor. So we walk the
suffixes in *original string order* (not sorted order) and only ever decrease
the running match length `h` by one between steps, giving an amortized linear
scan.

## When to reach for it

Reach for Suffix Array + LCP whenever a problem is about **substrings** of a
single string (or a small set of strings glued together) and you need
lexicographic order or shared-prefix information:

- Longest repeated / longest common substring
- Counting **distinct** substrings
- k-th lexicographically smallest substring
- Substrings that repeat at least `k` times
- Pattern matching / substring search via binary search on `SA`

The LCP array turns "compare two substrings" (naively O(n)) into an O(1) table
lookup after preprocessing, which is what makes these problems tractable.

## Typical complexity

| Step | Time | Space |
|------|------|-------|
| Build suffix array (prefix-doubling) | O(n log n) | O(n) |
| Build suffix array (SA-IS / DC3) | O(n) | O(n) |
| Build LCP array (Kasai) | **O(n)** | O(n) |

Most interview / contest solutions pair an **O(n log n)** doubling suffix array
with the **O(n)** Kasai LCP pass. The total is dominated by the suffix-array
build. Answering each of the problems below is then a single linear scan over
`SA` and `LCP`.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Longest Repeated Substring](problem-01-longest-repeated-substring/PROBLEM.md) | Length of the longest substring that occurs at least twice — the max LCP value | Medium |
| 2 | [Count Distinct Substrings](problem-02-count-distinct-substrings/PROBLEM.md) | Count all distinct non-empty substrings via `n(n+1)/2 - sum(LCP)` | Medium |
| 3 | [Longest Common Substring of Two Strings](problem-03-longest-common-substring-two-strings/PROBLEM.md) | Longest substring shared by two strings using a glued suffix array | Hard |
| 4 | [K-th Smallest Distinct Substring](problem-04-kth-smallest-distinct-substring/PROBLEM.md) | Find the k-th lexicographically smallest distinct substring | Hard |
| 5 | [Longest Substring With At Least K Occurrences](problem-05-longest-substring-at-least-k-occurrences/PROBLEM.md) | Longest substring that appears at least `k` times (overlaps allowed) via sliding-window minimum over LCP | Hard |
