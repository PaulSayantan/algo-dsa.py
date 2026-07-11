# Solution — Edit Distance

## Brute Force

Recurse on the two strings. Compare the last characters of `word1[:i]` and `word2[:j]`:

- If they match, recurse on `(i-1, j-1)` with no added cost.
- Otherwise take `1 + min` over the three operations: delete → `(i-1, j)`,
  insert → `(i, j-1)`, replace → `(i-1, j-1)`.

Without memoization each call branches three ways, so the recursion tree has size roughly
`O(3^(n+m))`.

- **Time:** `O(3^(n+m))`
- **Space:** `O(n + m)` recursion depth

Correct, but exponential — every subproblem `(i, j)` is recomputed many times.

## Optimal Approach (Wagner–Fischer)

There are only `(n+1)(m+1)` distinct subproblems `(i, j)`, so memoize them into a table.
This is exactly Wagner–Fischer. Let

```
dp[i][j] = minimum edits to convert word1[:i] into word2[:j]
```

**Recurrence**

```
dp[0][j] = j          # insert j characters to build word2[:j] from ""
dp[i][0] = i          # delete i characters to reduce word1[:i] to ""

if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]                 # characters already match, no cost
else:
    dp[i][j] = 1 + min(
        dp[i-1][j],     # delete word1[i-1]
        dp[i][j-1],     # insert word2[j-1]
        dp[i-1][j-1],   # replace word1[i-1] with word2[j-1]
    )
```

The answer is `dp[n][m]`.

```python
def minDistance(self, word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[n][m]
```

### Worked table — `word1 = "horse"`, `word2 = "ros"`

Rows are prefixes of `"horse"`, columns are prefixes of `"ros"`:

```
        ""  r   o   s
    ""   0  1   2   3
    h    1  1   2   3
    o    2  2   1   2
    r    3  2   2   2
    s    4  3   3   2
    e    5  4   4   3
```

`dp[5][3] = 3`, matching the expected output. Reading a min-cost path backward from the
bottom-right gives one optimal edit script (replace `h→r`, delete `r`, delete `e`).

- **Time:** `O(n · m)` — one constant-time transition per cell.
- **Space:** `O(n · m)` for the full table, or `O(min(n, m))` with two rolling rows if you
  do not need to reconstruct the operations.

**Why it is correct.** Any optimal alignment ends in exactly one of four ways for the last
pair of prefix characters: they are aligned as a match (free), aligned as a substitution
(cost 1), `word1[i-1]` is deleted (cost 1), or `word2[j-1]` is inserted (cost 1). Each case
reduces to a strictly smaller subproblem whose optimum is already stored, so taking the
minimum yields the optimum for `(i, j)`. The base row/column encode transforming to/from the
empty string. Optimal substructure plus these non-overlapping cases make the recurrence exact.

## Key Insights & Edge Cases

- **All three neighbours matter on a mismatch.** Delete uses the cell above, insert the cell
  to the left, replace the diagonal. Forgetting the diagonal turns this into the delete-only
  variant and overcounts substitutions.
- **A match copies the diagonal directly** — do *not* also `min` in the neighbours + 1 on a
  match; that would ignore the free alignment and can inflate the answer.
- **Symmetry.** `editDistance(a, b) == editDistance(b, a)`; a deletion on one side is an
  insertion on the other.
- **Empty strings.** `("", s)` and `(s, "")` both return `len(s)` straight from the base
  row/column.
- **Bounds.** The distance is always between `|n - m|` and `max(n, m)`.
- **Rolling-array pitfall.** When compressing to one row, save the pre-overwrite diagonal
  value (`dp[i-1][j-1]`) in a temporary before you overwrite `dp[j]`, or you will read the
  already-updated value.
