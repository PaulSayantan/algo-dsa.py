# Suffix Array (prefix-doubling / DC3)

A **suffix array** is the array of starting indices of *all* suffixes of a string
`S`, sorted in lexicographic order. It is a compact, cache-friendly alternative to
a suffix tree that solves an enormous range of string problems: substring search,
counting/locating pattern occurrences, longest repeated substring, number of
distinct substrings, longest common substring of several strings, and more —
especially when paired with the **LCP array** (longest-common-prefix between
adjacent sorted suffixes, built in O(n) by Kasai's algorithm).

## What it is

For `S = "banana"` the sorted suffixes are

```
index  suffix
  5    a
  3    ana
  1    anana
  0    banana
  4    na
  2    nana
```

so the suffix array is `SA = [5, 3, 1, 0, 4, 2]`.

## When to reach for it

- You need to answer **many** substring queries on a fixed text (search / count / locate).
- You need the **longest repeated substring**, **number of distinct substrings**,
  or the **longest common substring** of two or more strings.
- You want suffix-tree power with roughly 1/3 the memory and simpler code.
- The alphabet is large or arbitrary (comparison-based / radix-based builds handle it well).

If you only need a single pattern match once, plain KMP / Z-algorithm is simpler.
Reach for a suffix array when the *preprocessing cost is amortized* over many
queries or when you specifically need the sorted-suffix / LCP structure.

## Complexity

| Build method                     | Time            | Space | Notes |
|----------------------------------|-----------------|-------|-------|
| Naive sort of suffixes           | O(n^2 log n)    | O(n^2)| easy but slow; good as a reference/brute force |
| Prefix doubling (with `sort`)    | O(n log^2 n)    | O(n)  | short, practical, most-used in contests |
| Prefix doubling (radix sort)     | O(n log n)      | O(n)  | doubling + counting sort on rank pairs |
| DC3 / skew algorithm             | O(n)            | O(n)  | linear but larger constant & more code |
| LCP array (Kasai)                | O(n)            | O(n)  | needs `SA` and its inverse `rank` |

**Prefix doubling** sorts suffixes by their first `2^k` characters in round `k`,
reusing the previous round's ranks so each round is one sort of *pairs of ranks*.
After `ceil(log2 n)` rounds every suffix has a unique rank. **DC3 (skew)** recursively
sorts the suffixes at positions `i mod 3 != 0`, then merges in the rest, achieving
true linear time.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Build the Suffix Array](problem-01-build-suffix-array/PROBLEM.md) | Prefix doubling / DC3 core construction | Medium |
| 2 | [Count Pattern Occurrences](problem-02-count-pattern-occurrences/PROBLEM.md) | Binary search on the suffix array | Medium |
| 3 | [Longest Repeated Substring](problem-03-longest-repeated-substring/PROBLEM.md) | Suffix array + LCP (max LCP) | Medium-Hard |
| 4 | [Number of Distinct Substrings](problem-04-distinct-substrings/PROBLEM.md) | Suffix array + LCP counting | Hard |
| 5 | [Longest Common Substring of Two Strings](problem-05-longest-common-substring/PROBLEM.md) | Concatenation + LCP across sources | Hard |
| 6 | [Longest Duplicate Substring](problem-06-longest-duplicate-substring/PROBLEM.md) | Suffix array + LCP (LeetCode 1044) | Hard |
