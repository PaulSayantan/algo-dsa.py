# Longest Common Subsequence (DP)

The **Longest Common Subsequence (LCS)** is the longest sequence of characters
that appears in two strings in the **same relative order** but not necessarily
contiguously. For example, the LCS of `"abcde"` and `"ace"` is `"ace"`.

## What it is

Given two strings `X` (length `n`) and `Y` (length `m`), define a 2D table where
`dp[i][j]` is the LCS length of the prefixes `X[:i]` and `Y[:j]`. Fill it with
the recurrence:

```
dp[i][j] = dp[i-1][j-1] + 1                 if X[i-1] == Y[j-1]
         = max(dp[i-1][j], dp[i][j-1])      otherwise
dp[0][*] = dp[*][0] = 0                      (empty prefix)
```

The answer is `dp[n][m]`. To recover the actual subsequence (needed by some
problems), walk backward from `dp[n][m]`: step diagonally on a match, otherwise
move toward the larger neighbor.

## When to reach for it

Reach for LCS-style 2D DP whenever a problem involves **two sequences** and asks
you to keep, align, or transform their **shared, order-preserving** content:

- "How many / which elements are common in order?" (LCS itself, uncrossed lines)
- "Minimum deletions / cost to make two strings equal?" (`n + m - 2*LCS`, or a
  weighted variant)
- "Shortest string containing both as subsequences?" (`n + m - LCS`, with
  reconstruction)
- "Longest palindromic subsequence?" (LCS of `s` with `reverse(s)`)

If the alignment must be **contiguous**, you want longest *common substring*
(a different, though related, DP), not LCS.

## Complexity

- **Time:** `O(n * m)` — one pass filling every table cell.
- **Space:** `O(n * m)` for the full table; reducible to `O(min(n, m))` with a
  rolling row **when you only need the length** (reconstruction requires the
  full table).

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Longest Common Subsequence](problem-01-longest-common-subsequence/PROBLEM.md) | The canonical LCS length of two strings | Medium |
| 2 | [Uncrossed Lines](problem-02-uncrossed-lines/PROBLEM.md) | LCS on two integer arrays disguised as non-crossing connections | Medium |
| 3 | [Delete Operation for Two Strings](problem-03-delete-operation-for-two-strings/PROBLEM.md) | Min deletions to equalize two strings via `n + m - 2*LCS` | Medium |
| 4 | [Minimum ASCII Delete Sum](problem-04-minimum-ascii-delete-sum/PROBLEM.md) | Weighted LCS minimizing ASCII cost of deletions | Medium |
| 5 | [Shortest Common Supersequence](problem-05-shortest-common-supersequence/PROBLEM.md) | Build the shortest superstring using LCS + path reconstruction | Hard |
| 6 | [Longest Palindromic Subsequence](problem-06-longest-palindromic-subsequence/PROBLEM.md) | LCS of a string with its reverse | Medium |

Work them top to bottom: problem 1 teaches the core table, 2-4 practice
recognizing LCS in disguise and the `n + m - 2*LCS` / weighted variants, 5 adds
backward reconstruction, and 6 shows the reverse-string reduction.
