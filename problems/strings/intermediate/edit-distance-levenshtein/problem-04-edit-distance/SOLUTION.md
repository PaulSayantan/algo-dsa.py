# Edit Distance — Solution

## Brute Force

Recurse on the two strings. Compare the last characters:

- If they match, recurse on both prefixes with no cost.
- Otherwise take `1 + min(insert, delete, replace)` where each option recurses
  on a slightly shorter pair of strings.

```
def rec(i, j):
    if i == 0: return j          # insert remaining j chars
    if j == 0: return i          # delete remaining i chars
    if word1[i-1] == word2[j-1]:
        return rec(i-1, j-1)
    return 1 + min(rec(i-1, j),      # delete
                   rec(i, j-1),      # insert
                   rec(i-1, j-1))    # replace
```

- **Time:** `O(3^(m+n))` — each call branches three ways, recomputing the same
  subproblems repeatedly.
- **Space:** `O(m + n)` recursion depth.

The subproblems overlap heavily, which is the signal to memoize / tabulate.

## Optimal Approach (Edit Distance (Levenshtein) DP)

Define a table where

```
dp[i][j] = edit distance between word1[:i] and word2[:j]
```

**Base cases** (turning a prefix into the empty string, or vice versa):

```
dp[0][j] = j     # insert j characters to build word2[:j] from ""
dp[i][0] = i     # delete all i characters of word1[:i]
```

**Transition** for `i, j >= 1`:

```
if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]                 # last chars agree, no new op
else:
    dp[i][j] = 1 + min(
        dp[i-1][j],      # delete word1[i-1]
        dp[i][j-1],      # insert word2[j-1]
        dp[i-1][j-1],    # replace word1[i-1] with word2[j-1]
    )
```

The answer is `dp[m][n]`.

### Interpreting the three neighbors

- `dp[i-1][j]` (cell above): we deleted `word1[i-1]`, so we still must convert
  `word1[:i-1]` into `word2[:j]`.
- `dp[i][j-1]` (cell to the left): we inserted `word2[j-1]` at the end, so
  `word1[:i]` must still become `word2[:j-1]`.
- `dp[i-1][j-1]` (diagonal): we aligned the last characters, either free (match)
  or via one replace (mismatch).

### Why it is correct

The problem has **optimal substructure**: an optimal edit script for the full
strings, restricted to its last operation, leaves an optimal script for a
strictly smaller prefix pair. The three transitions enumerate every possible
last operation affecting the final characters, and the match case handles the
"do nothing" alignment. Because we take the minimum over all cases and fill the
table in increasing `i, j` order, every cell holds the true optimum by
induction. Overlapping subproblems are each computed once.

### Reference implementation (with `O(n)` space)

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))          # dp[0][j] = j
        for i in range(1, m + 1):
            curr = [i] + [0] * n           # dp[i][0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(prev[j],        # delete
                                      curr[j - 1],    # insert
                                      prev[j - 1])    # replace
            prev = curr
        return prev[n]
```

- **Time:** `O(m * n)`.
- **Space:** `O(n)` with the rolling-row optimization (`O(m * n)` for the full
  table if you need to reconstruct the actual edit operations by backtracking).

## Key Insights & Edge Cases

- **Insert vs. delete are symmetric.** "Insert into `word1`" and "delete from
  `word2`" describe the same table move; pick one consistent interpretation.
- **The diagonal is free only on a match**; on a mismatch it represents a
  replace and costs 1.
- **Empty-string edges:** distance from `""` to a length-`k` string is `k`
  (Example 3). Both empty -> 0.
- **Bounds:** the answer is always between `|m - n|` and `max(m, n)`.
- If you also need the sequence of edits (not just the count), keep the full
  table and backtrack from `dp[m][n]`, choosing which neighbor produced the
  value at each step.
- The rolling-row version must set `curr[0] = i` at the start of each row;
  forgetting this base value is a frequent mistake.
