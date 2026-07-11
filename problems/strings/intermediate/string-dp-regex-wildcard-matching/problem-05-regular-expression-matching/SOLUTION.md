# Regular Expression Matching — Solution

## Brute Force

Recurse over both indices. The interesting case is a `'*'` that follows the
current pattern character `p[j]` (so we look at `p[j+1] == '*'`):

```
match(i, j):
    if j == len(p): return i == len(s)
    first = i < len(s) and (p[j] == s[i] or p[j] == '.')
    if j+1 < len(p) and p[j+1] == '*':
        # '*' matches zero of p[j], OR one more p[j] then stay
        return match(i, j+2) or (first and match(i+1, j))
    return first and match(i+1, j+1)
```

Without memoization the `'*'` branch makes this exponential.

- **Time:** `O(2^(m+n))` worst case.
- **Space:** `O(m + n)` recursion depth.

## Optimal Approach (String DP)

Let `dp[i][j]` = `True` if `s[:i]` matches `p[:j]`.

**Base cases**

- `dp[0][0] = True`.
- `dp[0][j]`: an empty string can match a non-empty pattern only through
  `x*` groups that each contribute zero characters. So for `j >= 2`,
  `dp[0][j] = (p[j-1] == '*') and dp[0][j-2]`.
- `dp[i][0] = False` for `i > 0`.

**Transitions**

- If `p[j-1] == '*'` (a quantifier on `p[j-2]`):
  - **Zero occurrences** of `p[j-2]`: `dp[i][j-2]`.
  - **One or more:** allowed only if `p[j-2]` matches `s[i-1]`
    (`p[j-2] == s[i-1]` or `p[j-2] == '.'`), giving `dp[i-1][j]`.
  - Combine: `dp[i][j] = dp[i][j-2] or (matches_prev and dp[i-1][j])`.
- Else if `p[j-1] == '.'` or `p[j-1] == s[i-1]`:
  `dp[i][j] = dp[i-1][j-1]`.
- Otherwise `dp[i][j] = False`.

**Why the `'*'` rule is correct.** The group `p[j-2]p[j-1]` (`x*`) can expand to
zero or more copies of `x`. If it expands to zero, the group is invisible and we
skip both pattern cells (`dp[i][j-2]`). If it expands to one or more, its last
copy must match the last string character `s[i-1]` (requiring `p[j-2]` to match
`s[i-1]`), and after consuming that character the **same** `x*` group is still
available for earlier characters, which is `dp[i-1][j]`. These two cases are
exhaustive, so the OR is exact.

**Step by step** for `s = "aa"`, `p = "a*"` (rows = `s`, cols = `p`):

```
          ""   a   *
    ""     T   F   T
     a     F   T   T
     a     F   F   T   <- dp[2][2] = True
```

- `dp[0][2] = True`: `a*` matches empty (zero `a`s).
- `dp[2][2] = True`: `'*'` at `j=2`, `p[0]='a'` matches `s[1]='a'`, so it reads
  `dp[1][2] = True`.

**Reference implementation**

```python
def isMatch(self, s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # zero occurrences of the preceding element
                dp[i][j] = dp[i][j - 2]
                # one-or-more, if the preceding element matches s[i-1]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]
```

- **Time:** `O(m * n)`.
- **Space:** `O(m * n)`, reducible to `O(n)` with two rolling rows.

## Key Insights & Edge Cases

- **`'*'` looks two cells back.** Unlike wildcard `'*'` (Problem 3), regex `'*'`
  is a quantifier on `p[j-2]`. The "zero occurrences" branch therefore jumps to
  `dp[i][j-2]`, skipping the whole `x*` group — this is the single most common
  bug source.
- **`.*` matches everything**, including the empty string, because `'.'` matches
  any character and the star lets it repeat any number of times (Example 3).
- **Empty-string base column** must pre-fill `dp[0][j]` for star groups, or
  patterns like `"a*b*c*"` against `""` wrongly report no match.
- **A `'*'` is never evaluated alone:** the constraints guarantee it always has a
  valid preceding character, so `p[j-2]` is always safe to read when
  `p[j-1] == '*'`.
- **Greedy fails:** letting `.*` grab as much as possible can overshoot
  (Example 4, `"mis*is*p*."`), which is exactly why the DP explores both the
  "consume" and "stop" branches.
