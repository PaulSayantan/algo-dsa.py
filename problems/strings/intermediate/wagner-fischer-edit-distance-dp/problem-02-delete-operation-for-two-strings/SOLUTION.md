# Solution — Delete Operation for Two Strings

## Brute Force

Enumerate every subsequence of `word1` and every subsequence of `word2`, find the longest
string that appears in both (the longest common subsequence, LCS), and delete everything
else. With lengths up to 500 there are up to `2^500` subsequences per side, so explicit
enumeration is astronomically infeasible.

- **Time:** `O(2^n · 2^m)` — hopeless.
- **Space:** exponential.

## Optimal Approach (Wagner–Fischer with deletions only)

This is the Wagner–Fischer edit-distance table with the **substitution transition
removed**. The only moves are "delete from `word1`" (move up a row) and "delete from
`word2`" (move left a column). Let

```
dp[i][j] = minimum deletions to make word1[:i] equal to word2[:j]
```

**Recurrence**

```
dp[0][j] = j      # delete all j chars of word2's prefix
dp[i][0] = i      # delete all i chars of word1's prefix

if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]          # matched pair kept for free
else:
    dp[i][j] = 1 + min(dp[i-1][j],   # delete word1[i-1]
                       dp[i][j-1])   # delete word2[j-1]
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
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]
```

- **Time:** `O(n · m)`
- **Space:** `O(n · m)`, or `O(min(n, m))` with a rolling one-row array.

**Why it is correct.** Deleting characters until the two strings match keeps exactly the
characters common to both, in order — that is precisely a common subsequence. Minimizing
deletions means maximizing the kept subsequence, so the optimum keeps the *longest* common
subsequence and deletes the rest. The recurrence above is the standard DP for that: on a
matching pair we extend the alignment for free (`dp[i-1][j-1]`), and on a mismatch we must
pay one deletion on whichever side we advance.

**Equivalent LCS formulation.** If `L = LCS(word1, word2)`, the answer is
`(n - L) + (m - L) = n + m - 2L`. Compute `L` with the classic LCS DP and subtract. Both
formulations are the same `O(n · m)` table.

## Key Insights & Edge Cases

- **No substitution.** Turning one character into another would need one substitution; here
  it costs **two** deletions (remove the bad char from each side). That is why the mismatch
  branch omits the `dp[i-1][j-1]` diagonal option that ordinary edit distance uses.
- **Answer = `n + m - 2 · LCS`.** Handy sanity check: Example 2 has `n = 8`, `m = 4`,
  `LCS = 4`, giving `8 + 4 - 8 = 4`. ✔
- **Identical strings** → `0` deletions (`dp[i][i]` stays on the free diagonal the whole way).
- **Disjoint alphabets** (e.g. `"a"` vs `"b"`, LCS = 0) → delete everything: `n + m`.
- **Rolling array.** Only the previous row is needed; compress to `O(min(n, m))` space by
  iterating with the shorter string on the inner axis.
