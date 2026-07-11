# Solution — Edit Distance

## Brute Force

Recurse on the two prefix lengths. If the current last characters match, move both
pointers back with no cost; otherwise try all three edits and take the cheapest:

```python
def dist(i, j):
    if i == 0:
        return j            # insert all remaining chars of word2
    if j == 0:
        return i            # delete all remaining chars of word1
    if word1[i - 1] == word2[j - 1]:
        return dist(i - 1, j - 1)
    return 1 + min(dist(i - 1, j),      # delete from word1
                   dist(i, j - 1),      # insert into word1
                   dist(i - 1, j - 1))  # replace
```

Up to three branches per call gives exponential time.

- **Time:** `O(3^(m+n))`.
- **Space:** `O(m + n)` recursion depth.

`(i, j)` repeats across many branches — overlapping subproblems.

## Optimal Approach (Dynamic Programming)

**State:** `dp[i][j]` = minimum edits to turn the first `i` chars of `word1` into the
first `j` chars of `word2`.

**Recurrence:**

```
if word1[i - 1] == word2[j - 1]:
    dp[i][j] = dp[i - 1][j - 1]                       # no operation needed
else:
    dp[i][j] = 1 + min(dp[i - 1][j],      # delete word1[i-1]
                       dp[i][j - 1],      # insert word2[j-1]
                       dp[i - 1][j - 1])  # replace word1[i-1] with word2[j-1]
```

**Base cases:** `dp[i][0] = i` (delete all `i` chars), `dp[0][j] = j` (insert all `j`
chars).

### Bottom-up (tabulation)

```python
class Solution:
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
                    dp[i][j] = 1 + min(dp[i - 1][j],
                                       dp[i][j - 1],
                                       dp[i - 1][j - 1])
        return dp[m][n]
```

**Why it is correct:** Look at the last characters of the two prefixes. If they are
equal, an optimal alignment pairs them at no cost, reducing to `dp[i-1][j-1]`. If not,
the final edit in an optimal script must be a delete, an insert, or a replace — those
three sub-results are optimal for their smaller prefixes (optimal substructure), so
adding 1 to the cheapest is optimal. The cases are exhaustive.

### Trace on `word1 = "horse", word2 = "ros"`

```
        ""  r  o  s
    ""   0  1  2  3
    h    1  1  2  3
    o    2  2  1  2
    r    3  2  2  2
    s    4  3  3  2
    e    5  4  4  3
```

Bottom-right cell `dp[5][3] = 3`. ✔

### Space optimization

Each cell depends only on the current row and the previous row, so two rows reduce space
to `O(n)`.

- **Time:** `O(m * n)`.
- **Space:** `O(m * n)` for the full table, or `O(min(m, n))` with rolling rows.

## Key Insights & Edge Cases

- The three transitions map exactly onto the three allowed operations, plus a free
  diagonal move when characters match — memorizing this quartet unlocks the whole family
  of alignment DPs.
- **Base row/column are not zero here** (unlike LCS): turning a string into the empty
  string costs its length. Seeding `dp[i][0] = i` and `dp[0][j] = j` is essential.
- **Empty inputs:** if either word is empty the answer is the other's length, handled by
  the base cases (`""` → `"abc"` costs 3).
- **Relationship to LCS:** when only insert and delete are allowed (no replace), the
  minimum edit distance is `m + n - 2 * LCS(word1, word2)`. Allowing replace can only
  lower or equal the cost.
- Diagonal dependency (`dp[i-1][j-1]`) means a one-row rolling optimization must stash the
  old diagonal value in a temp before overwriting it.
