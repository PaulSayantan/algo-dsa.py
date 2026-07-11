# Wagner–Fischer (Edit Distance DP)

**Wagner–Fischer** is the canonical dynamic-programming algorithm for computing the
**Levenshtein edit distance** between two strings — the minimum number of single-character
**insertions, deletions, and substitutions** needed to transform one string into the other.

## The core idea

Let `a` (length `n`) and `b` (length `m`) be the two strings. Define

```
dp[i][j] = edit distance between the prefix a[:i] and the prefix b[:j]
```

Fill an `(n+1) x (m+1)` table row by row. The recurrence is:

```
dp[0][j] = j                      # turn "" into b[:j] with j insertions
dp[i][0] = i                      # turn a[:i] into "" with i deletions

if a[i-1] == b[j-1]:
    dp[i][j] = dp[i-1][j-1]       # characters match, no new cost
else:
    dp[i][j] = 1 + min(
        dp[i-1][j],               # delete a[i-1]
        dp[i][j-1],               # insert b[j-1]
        dp[i-1][j-1],             # substitute a[i-1] -> b[j-1]
    )
```

The answer is `dp[n][m]`. Because each cell depends only on its top, left, and
top-left neighbours, the table can be filled in a single top-to-bottom,
left-to-right sweep.

## When to reach for it

Use Wagner–Fischer whenever a problem asks for the **minimum cost to transform one
sequence into another** using a fixed set of per-element operations (insert / delete /
substitute), or any close relative:

- Making two strings equal using only deletions.
- Weighting operations by character cost instead of a flat 1.
- Deciding whether two strings are within a bounded distance.
- Reconstructing an alignment / shortest common supersequence from the filled table.

It is the string-alignment cousin of Longest Common Subsequence — both are 2D DP over
the prefixes of two sequences.

## Complexity

| Resource | Cost |
|----------|------|
| Time | `O(n · m)` |
| Space | `O(n · m)` for the full table, or `O(min(n, m))` with a rolling one-row array |

Path reconstruction (recovering the actual edit script or alignment) requires the full
`O(n · m)` table so you can walk backwards from `dp[n][m]`.

## Problems

| # | Problem | Difficulty | Summary |
|---|---------|------------|---------|
| 1 | [One Edit Distance](problem-01-one-edit-distance/PROBLEM.md) | Medium | Decide whether two strings are *exactly* one edit apart (bounded edit distance). |
| 2 | [Delete Operation for Two Strings](problem-02-delete-operation-for-two-strings/PROBLEM.md) | Medium | Minimum single-character deletions to make two strings equal (delete-only edit distance). |
| 3 | [Minimum ASCII Delete Sum for Two Strings](problem-03-minimum-ascii-delete-sum/PROBLEM.md) | Medium | Minimum ASCII-weighted deletion cost to make two strings equal. |
| 4 | [Edit Distance](problem-04-edit-distance/PROBLEM.md) | Medium/Hard | The canonical Levenshtein distance with insert, delete, and replace. |
| 5 | [Shortest Common Supersequence](problem-05-shortest-common-supersequence/PROBLEM.md) | Hard | Build the shortest string containing both inputs as subsequences via table reconstruction. |

Work them top to bottom: each one adds a twist (bounding, restricted operations,
weighted costs, all three operations, then reconstruction) on top of the same table.
