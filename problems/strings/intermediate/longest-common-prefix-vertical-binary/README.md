# Longest Common Prefix (Vertical / Binary)

The **Longest Common Prefix (LCP)** of a set of strings is the longest string that is
a prefix of *every* string in the set. Two complementary techniques compute it
efficiently:

- **Vertical scanning** — Walk the character *columns* left to right. At column `j`,
  compare `strs[0][j]` against `strs[i][j]` for every other string `i`. The moment a
  column has a mismatch (or some string ends), the answer is everything scanned so far.
  This inspects each character at most once, so it stops early on the first difference.

- **Binary search on the prefix length** — The predicate *"do all strings share a
  prefix of length `L`?"* is **monotonic**: if it holds for `L`, it holds for every
  `L' < L`. That lets you binary search for the largest feasible `L`, checking a
  candidate length by testing whether every string starts with `strs[0][:L]`.

## When to reach for it

- You need the common leading portion shared by *all* strings (autocomplete roots,
  common file-path ancestors, shared subnet prefixes, grouping by prefix).
- The strings are long and you want early termination (vertical) or you already have
  fast prefix-equality checks / hashing available (binary search).

## Complexity

Let `n` = number of strings and `m` = length of the shortest string (so `S = n*m` is the
work to touch every relevant character).

| Approach            | Time                  | Space  | Notes                                        |
|---------------------|-----------------------|--------|----------------------------------------------|
| Vertical scanning   | `O(S)` = `O(n*m)`     | `O(1)` | Stops at the first mismatched column.        |
| Binary search on L  | `O(n*m*log m)`        | `O(1)` | `log m` length guesses, each an `O(n*m)` check (cheaper with hashing). |
| Sorted first/last   | `O(n*L + sort)`       | `O(1)` | After sorting, LCP(all) = LCP(first, last).  |

Both run in linear time in the worst case; vertical scanning is usually the simplest and
fastest in practice, while binary search shines when prefix-equality checks are `O(1)`
(e.g. precomputed hashes) or when you must return only the *length*.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Longest Common Prefix of Two Strings](problem-01-longest-common-prefix-two-strings/PROBLEM.md) | LCP of a single pair — the primitive behind everything else. | Easy |
| 2 | [Longest Common Prefix](problem-02-longest-common-prefix-array/PROBLEM.md) | LeetCode 14: LCP across an array of strings. | Easy |
| 3 | [Longest Common Path](problem-03-longest-common-path/PROBLEM.md) | Longest common directory prefix of Unix paths (segment-wise LCP). | Medium |
| 4 | [Longest Common Binary Prefix](problem-04-longest-common-binary-prefix/PROBLEM.md) | Shared leading bits of fixed-width binary codes (common subnet prefix length). | Medium |
| 5 | [Find the Length of the Longest Common Prefix](problem-05-longest-common-prefix-of-pairs/PROBLEM.md) | LeetCode 3043: longest LCP length over all cross pairs of two integer arrays. | Medium |
