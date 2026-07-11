# Solution — LCS Length in Linear Space

## Brute Force

Enumerate every subsequence of `text1` (there are `2^n`) and check whether it is a
subsequence of `text2`, keeping the longest match.

- **Time:** `O(2^n · m)` — exponential.
- **Space:** `O(n)` for the recursion / current candidate.

Completely impractical beyond ~20 characters.

## Standard DP (for reference)

Define `dp[i][j]` = LCS length of `text1[:i]` and `text2[:j]`.

```
dp[i][j] = dp[i-1][j-1] + 1                 if text1[i-1] == text2[j-1]
         = max(dp[i-1][j], dp[i][j-1])       otherwise
```

- **Time:** `O(n·m)`
- **Space:** `O(n·m)` — the full table.

## Optimal Approach (Linear-Space Score Pass)

The recurrence for row `i` depends **only on row `i-1`** and the current row. So we never
need more than two rows in memory — and with a little care, a single rolling row plus one
scalar for the "diagonal" value.

To guarantee `O(min(n, m))` space, first make the string that indexes the row the shorter
one (swap the arguments if needed; LCS is symmetric).

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Ensure text2 (the one indexing the row) is the shorter string.
        if len(text2) > len(text1):
            text1, text2 = text2, text1
        n, m = len(text1), len(text2)

        prev = [0] * (m + 1)
        for i in range(1, n + 1):
            curr = [0] * (m + 1)
            ci = text1[i - 1]
            for j in range(1, m + 1):
                if ci == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = prev[j] if prev[j] >= curr[j - 1] else curr[j - 1]
            prev = curr
        return prev[m]
```

### Why it is correct

`curr[j]` is computed strictly from `prev[j-1]` (diagonal), `prev[j]` (up), and
`curr[j-1]` (left) — all available at the moment we need them. After finishing row `i`,
`prev` holds the exact values that `dp[i][*]` would hold in the full table, so the final
`prev[m]` equals `dp[n][m]`, the true LCS length.

### Complexity

- **Time:** `O(n·m)` — one constant-time update per cell.
- **Space:** `O(min(n, m))` — a single row whose width is the shorter length + 1.

### Connection to Hirschberg

This routine — often called the **NW-score** or **LCS-score** pass — is the building
block Hirschberg's algorithm invokes twice per recursion (once forward, once on the
reversed strings). Problem 2 uses it to reconstruct the actual subsequence, not just its
length, still in linear space.

## Key Insights & Edge Cases

- **Symmetry lets you minimise the row width:** swapping arguments so the shorter string
  drives the row is what turns `O(min(n, m))` from a claim into reality.
- **Empty input:** if either string is empty the answer is `0`; the loops simply don't
  run and `prev[m]` stays `0`.
- **No common characters** (Example 3): every cell inherits from a neighbour, never the
  `+1` branch, so the result is `0`.
- **Tie-breaking in the `max`** does not affect the *length* (either neighbour gives the
  same optimum); it only matters when you must reconstruct a specific subsequence.
