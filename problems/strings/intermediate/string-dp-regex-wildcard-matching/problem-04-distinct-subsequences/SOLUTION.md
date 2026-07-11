# Distinct Subsequences — Solution

## Brute Force

Enumerate every subset of positions in `s` (there are `2^m`), form the
corresponding subsequence, and count how many equal `t`.

- **Time:** `O(2^m * n)` — exponential.
- **Space:** `O(m)` recursion depth.

A cleaner recursion walks both strings and, at each character of `s`, decides to
use it (only if it equals the current `t` character) or skip it:

```
count(i, j):
    if j == len(t): return 1          # fully matched t
    if i == len(s): return 0          # ran out of s
    total = count(i+1, j)             # skip s[i]
    if s[i] == t[j]:
        total += count(i+1, j+1)      # use s[i]
    return total
```

## Optimal Approach (String DP)

Let `dp[i][j]` be the number of distinct ways `t[:j]` occurs as a subsequence of
`s[:i]`.

**Base cases**

- `dp[i][0] = 1` for all `i` — the empty target is matched exactly one way (pick
  nothing).
- `dp[0][j] = 0` for `j > 0` — a non-empty target cannot come from an empty
  source.

**Transition**

- You can always **skip** `s[i-1]`: this contributes `dp[i-1][j]`.
- If `s[i-1] == t[j-1]`, you may **also use** `s[i-1]` to match `t[j-1]`, adding
  `dp[i-1][j-1]`.

So:

```
dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if s[i-1] == t[j-1] else 0)
```

**Why it is correct.** Partition all matchings of `t[:j]` in `s[:i]` by whether
they use the last source character `s[i-1]`. Matchings that ignore it are
exactly the matchings in `s[:i-1]` (`dp[i-1][j]`). Matchings that use it require
`s[i-1] == t[j-1]` and reduce to matching `t[:j-1]` in `s[:i-1]`
(`dp[i-1][j-1]`). The two sets are disjoint and exhaustive, so their sizes add.

**Step by step** for `s = "rabbbit"`, `t = "rabbit"` (rows = `s`, cols = `t`):

```
          ""  r  a  b  b  i  t
    ""     1  0  0  0  0  0  0
     r     1  1  0  0  0  0  0
     a     1  1  1  0  0  0  0
     b     1  1  1  1  0  0  0
     b     1  1  1  2  1  0  0
     b     1  1  1  3  3  0  0
     i     1  1  1  3  3  3  0
     t     1  1  1  3  3  3  3   <- dp[7][6] = 3
```

**Reference implementation**

```python
def numDistinct(self, s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    return dp[m][n]
```

- **Time:** `O(m * n)`.
- **Space:** `O(m * n)`, reducible to `O(n)` with a rolling row. When using 1D,
  iterate `j` from **high to low** so `dp[j-1]` still holds the previous row's
  value.

## Key Insights & Edge Cases

- **Counting, not deciding.** Because we sum instead of taking a max or an OR,
  the "skip vs. use" choice becomes an addition. This is the same branching used
  by the `'*'` operator in pattern matching, only aggregated differently.
- **The empty-target base row of 1s** is the crux; forgetting it makes every
  count collapse to 0.
- **`t` longer than `s`** (Example 3) yields 0 naturally — the DP never reaches a
  full match of `t`.
- **Duplicate characters in `s`** are exactly what create multiple counts; each
  extra matching source character adds another path (see the growing `b`
  column above).
- **Overflow:** the problem guarantees a 32-bit result, so Python's big ints are
  safe; in languages with fixed-width ints, use 64-bit accumulators.
