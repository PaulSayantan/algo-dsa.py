# Minimum ASCII Delete Sum for Two Strings — Solution

## Brute Force

Try every subset of characters to delete from each string that makes the two
equal, and keep the subset with the smallest total ASCII cost. Equivalently,
enumerate all common subsequences and, for each, sum the ASCII values of the
non-kept characters.

- **Time:** exponential — `O(2^m * 2^n)` in the worst case.
- **Space:** `O(m + n)` recursion depth.

Infeasible for strings up to length 1000.

## Optimal Approach (Weighted delete-only Edit Distance (Levenshtein))

This is the delete-only edit distance from Problem 2, but every deletion costs
`ord(c)` instead of a flat `1`. Define:

```
dp[i][j] = minimum ASCII delete sum to make s1[:i] equal to s2[:j]
```

**Base cases** (one prefix is empty, so every character of the other must be
deleted):

```
dp[0][0] = 0
dp[i][0] = dp[i-1][0] + ord(s1[i-1])     # delete all of s1's prefix
dp[0][j] = dp[0][j-1] + ord(s2[j-1])     # delete all of s2's prefix
```

**Transition:**

```
if s1[i-1] == s2[j-1]:
    dp[i][j] = dp[i-1][j-1]                       # keep the matching char, free
else:
    dp[i][j] = min(
        dp[i-1][j] + ord(s1[i-1]),   # delete s1[i-1]
        dp[i][j-1] + ord(s2[j-1]),   # delete s2[j-1]
    )
```

The answer is `dp[m][n]`.

Note there is **no replace transition** — replacing is not an allowed
operation, so a mismatch can only be resolved by deleting one side.

### Why it is correct

When the current characters match, keeping both is always optimal: a matched
pair adds nothing to the cost and can never hurt (deleting them instead would
only add cost and still require making the rest equal). When they differ, one of
the two current characters cannot survive, so we pay to delete the cheaper-total
option, recursing on the smaller subproblem. The DP evaluates every prefix pair
exactly once with optimal substructure, guaranteeing the global minimum.

An equivalent view: with total ASCII `T = sum(ord(c) for all chars in both)`,
minimizing deleted ASCII equals maximizing `2 * (ASCII of kept common
subsequence)`. The kept characters form a common subsequence, so this is a
*maximum-ASCII-weight* LCS. Both formulations produce the same number; the
direct-cost DP above is usually cleaner to code.

### Reference implementation

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),
                        dp[i][j - 1] + ord(s2[j - 1]),
                    )
        return dp[m][n]
```

- **Time:** `O(m * n)`.
- **Space:** `O(m * n)`, reducible to `O(n)` with a rolling row.

## Key Insights & Edge Cases

- **Cost is ASCII, not count.** The minimum-count solution and the
  minimum-ASCII-sum solution can differ, so you cannot reuse Problem 2's answer.
  Example: it may be cheaper to make one extra deletion of a low-code character
  than to keep it and delete a high-code one.
- **Base rows/columns are cumulative sums**, not `i` or `j` as in the unweighted
  version — forgetting this is the most common bug.
- **Verification:** `"sea"`/`"eat"` deletes `'s'`(115) and `'t'`(116) = 231.
  `"delete"`/`"leet"` keeps `"let"` and deletes `d,e,e`(302) plus `e`(101) = 403.
- **Equal strings** cost 0; disjoint strings cost the full ASCII sum of both.
- Watch for integer sums getting large-ish but well within native ints in
  Python; no overflow concerns.
