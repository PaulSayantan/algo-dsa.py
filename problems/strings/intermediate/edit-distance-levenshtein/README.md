# Edit Distance (Levenshtein)

**Edit distance** measures how different two strings are by counting the minimum
number of single-character edits needed to turn one string into the other. In
the classic **Levenshtein** variant, the allowed edits are:

- **Insert** a character
- **Delete** a character
- **Replace** (substitute) a character

The tool of choice is **dynamic programming**. We build a table `dp` where
`dp[i][j]` holds the edit distance between the first `i` characters of string
`A` and the first `j` characters of string `B`. Each cell is computed from three
neighbors:

```
if A[i-1] == B[j-1]:
    dp[i][j] = dp[i-1][j-1]                       # characters match, no cost
else:
    dp[i][j] = 1 + min(
        dp[i-1][j],      # delete A[i-1]
        dp[i][j-1],      # insert B[j-1]
        dp[i-1][j-1],    # replace A[i-1] with B[j-1]
    )
```

## When to reach for it

- You must transform, align, or compare two sequences and count/weigh the
  operations (spell-check, DNA alignment, diff tools, fuzzy matching).
- The problem restricts the allowed operations (only deletions, weighted
  deletions, at most one edit, or adds transposition) — these are all edit
  distance with a tweaked recurrence.
- You need the *minimum* number of steps, which screams optimal substructure +
  overlapping subproblems = DP.

## Typical complexity

For strings of lengths `m` and `n`:

- **Time:** `O(m * n)` — every cell of the table is filled once.
- **Space:** `O(m * n)` for the full table, reducible to `O(min(m, n))` when
  only the distance (not the actual edit sequence) is needed, since each row
  depends only on the previous row.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [One Edit Distance](problem-01-one-edit-distance/PROBLEM.md) | Check if strings are exactly one edit apart (linear scan of the recurrence) | Easy/Medium |
| 2 | [Delete Operation for Two Strings](problem-02-delete-operation-two-strings/PROBLEM.md) | Edit distance with only deletions (LCS-based) | Medium |
| 3 | [Minimum ASCII Delete Sum for Two Strings](problem-03-minimum-ascii-delete-sum/PROBLEM.md) | Weighted deletion edit distance | Medium |
| 4 | [Edit Distance](problem-04-edit-distance/PROBLEM.md) | Full Levenshtein (insert/delete/replace) | Medium |
| 5 | [Damerau-Levenshtein Distance](problem-05-damerau-levenshtein-distance/PROBLEM.md) | Levenshtein plus adjacent transposition | Hard |
