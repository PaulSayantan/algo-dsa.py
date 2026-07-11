# Edit Distance — Solution

## Brute Force

Recursively compare the tails of the two words. At position `(i, j)`:

- if the last characters match, recurse on `(i-1, j-1)` with no cost;
- otherwise try all three operations and add 1:
  - **replace:** `(i-1, j-1)`,
  - **delete** from `word1`: `(i-1, j)`,
  - **insert** into `word1`: `(i, j-1)`.

```
edit(i, j):
    if i == 0: return j          # insert the remaining j chars
    if j == 0: return i          # delete the remaining i chars
    if word1[i-1] == word2[j-1]: return edit(i-1, j-1)
    return 1 + min(edit(i-1, j-1), edit(i-1, j), edit(i, j-1))
```

- **Time:** `O(3^(m+n))` without memoization — every state branches three ways.
- **Space:** `O(m + n)` recursion depth.

## Optimal Approach (String DP)

Let `dp[i][j]` be the edit distance between `word1[:i]` and `word2[:j]`.

**Base cases** (turning a prefix into/from the empty string):

- `dp[0][j] = j` — insert `j` characters.
- `dp[i][0] = i` — delete `i` characters.

**Transitions**

- If `word1[i-1] == word2[j-1]`: `dp[i][j] = dp[i-1][j-1]` (no operation).
- Otherwise:
  `dp[i][j] = 1 + min(dp[i-1][j-1],  # replace`
  `                    dp[i-1][j],    # delete from word1`
  `                    dp[i][j-1])    # insert into word1`

**Why it is correct:** any optimal edit script must, at its last step, either
match/replace the final characters, delete `word1`'s last character, or insert
`word2`'s last character. These map exactly to the diagonal, up, and left
neighbors. Taking the minimum over the three (plus the diagonal free case)
guarantees the global optimum by optimal substructure.

**Step by step** for `word1 = "horse"`, `word2 = "ros"`:

```
        ""  r  o  s
    ""   0  1  2  3
     h   1  1  2  3
     o   2  2  1  2
     r   3  2  2  2
     s   4  3  3  2
     e   5  4  4  3   <- answer dp[5][3] = 3
```

**Reference implementation**

```python
def minDistance(self, word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1],
                                   dp[i - 1][j],
                                   dp[i][j - 1])
    return dp[m][n]
```

- **Time:** `O(m * n)`.
- **Space:** `O(m * n)`, reducible to `O(n)` with a rolling row (remember to
  cache the diagonal value before overwriting it).

## Key Insights & Edge Cases

- **The three neighbors are the whole game.** Diagonal = replace/match,
  up = delete, left = insert. Every richer string DP (wildcard `*`, regex `x*`)
  is this template with extra branches added for the operators.
- **Non-square base cases matter:** the first row/column must be `0..n` and
  `0..m`, not zeros — an empty source still costs insertions.
- **Empty inputs** (Example 3) fall straight out of the base row: distance
  equals the other string's length.
- **Symmetry:** `minDistance(a, b) == minDistance(b, a)`, because insert and
  delete are mirror operations.
- **Rolling-array pitfall:** when compressing to 1D you overwrite `dp[j-1]`
  before using it as the "diagonal", so stash the previous diagonal in a
  temporary variable first.
