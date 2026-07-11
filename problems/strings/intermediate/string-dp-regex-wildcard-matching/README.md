# String DP (Regex / Wildcard Matching)

## What it is

**String DP** is a family of dynamic-programming techniques that operate on
**two sequences** (usually two strings, or a string and a pattern). The core
idea is a 2D table

```
dp[i][j] = the answer for the first i characters of A and the first j characters of B
```

Every cell is filled from a small number of neighbors — typically
`dp[i-1][j-1]`, `dp[i-1][j]`, and `dp[i][j-1]` — which correspond to the
decisions "match/replace a character", "delete from A", or "delete from B".

The **regex / wildcard matching** variant is the most intricate member of this
family. Here `B` is not plain text but a *pattern* containing special operators:

| Operator | Meaning | Appears in |
|----------|---------|------------|
| `?` | matches exactly **one** arbitrary character | Wildcard Matching |
| `*` (wildcard) | matches **any sequence** (including empty) | Wildcard Matching |
| `.` | matches exactly **one** arbitrary character | Regex Matching |
| `x*` (regex) | matches **zero or more** of the *preceding* element | Regex Matching |

The `*` operator is what makes these problems hard: a single cell must consider
both "use the star to match nothing" and "use the star to consume one more
character", which is exactly the branching a 2D DP table captures cleanly.

## When to reach for it

Reach for String DP whenever a problem asks you to **compare, transform, or
match two sequences** and the answer for a prefix pair can be built from the
answers for slightly shorter prefixes. Tell-tale signs:

- "minimum operations to turn A into B" (edit distance),
- "longest / how-many common ..." between two strings,
- "does this string match this pattern with `*` / `?` / `.`",
- "count the number of ways ..." to embed one string in another.

Greedy usually fails on the `*` operator because a local choice ("let `*`
match as much as possible") can be wrong; DP explores both branches for free.

## Typical complexity

For strings of length `m` and `n`:

- **Time:** `O(m * n)` — one constant-time transition per table cell.
- **Space:** `O(m * n)`, reducible to `O(min(m, n))` with a rolling 1D array
  because each row depends only on the current and previous rows.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Longest Common Subsequence](problem-01-longest-common-subsequence/PROBLEM.md) | Foundational 2D string DP (match / skip) | Medium |
| 2 | [Edit Distance](problem-02-edit-distance/PROBLEM.md) | Insert / delete / replace transitions | Medium |
| 3 | [Wildcard Matching](problem-03-wildcard-matching/PROBLEM.md) | Pattern DP with `?` and `*` (any sequence) | Hard |
| 4 | [Distinct Subsequences](problem-04-distinct-subsequences/PROBLEM.md) | Counting-variant 2D string DP | Hard |
| 5 | [Regular Expression Matching](problem-05-regular-expression-matching/PROBLEM.md) | Pattern DP with `.` and `x*` (zero-or-more) | Hard |
