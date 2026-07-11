# Wildcard Matching — Solution

## Brute Force

Recurse over both indices. When you hit a `'*'`, try **every** possible split:
let it match 0 characters, 1 character, 2 characters, and so on, recursing on
each.

```
match(i, j):
    if j == len(p): return i == len(s)
    if p[j] == '*':
        # match empty, or consume one char of s and stay on '*'
        return match(i, j+1) or (i < len(s) and match(i+1, j))
    if i < len(s) and (p[j] == '?' or p[j] == s[i]):
        return match(i+1, j+1)
    return False
```

Without memoization the branching on `'*'` makes this exponential.

- **Time:** `O(2^(m+n))` in the worst case (e.g. many stars against many chars).
- **Space:** `O(m + n)` recursion depth.

## Optimal Approach (String DP)

Let `dp[i][j]` = `True` if `s[:i]` matches `p[:j]`.

**Base cases**

- `dp[0][0] = True` — empty string matches empty pattern.
- `dp[0][j] = True` only while every pattern character so far is `'*'`
  (a leading run of stars can match the empty string). Concretely,
  `dp[0][j] = dp[0][j-1] and p[j-1] == '*'`.
- `dp[i][0] = False` for `i > 0` — a non-empty string cannot match an empty
  pattern.

**Transitions**

- If `p[j-1] == '*'`:
  `dp[i][j] = dp[i][j-1]     # '*' matches the empty sequence`
  `           or dp[i-1][j]  # '*' absorbs s[i-1] and stays available`
- If `p[j-1] == '?'` or `p[j-1] == s[i-1]`:
  `dp[i][j] = dp[i-1][j-1]`  (consume one matching character).
- Otherwise `dp[i][j] = False`.

**Why the `'*'` rule is correct.** A star can match a variable-length chunk.
Either that chunk is empty — meaning the star contributes nothing and we defer
to `dp[i][j-1]` — or the chunk is non-empty, in which case its last character is
`s[i-1]`; we "use up" that character (`dp[i-1][j]`) while keeping the same star
available for earlier characters. Every matching is captured by exactly one of
these two branches, so their OR is exact.

**Step by step** for `s = "adceb"`, `p = "*a*b"` (rows = `s`, cols = `p`):

```
         ""   *   a   *   b
    ""    T   T   F   F   F
     a    F   T   T   T   F
     d    F   T   F   T   F
     c    F   T   F   T   F
     e    F   T   F   T   F
     b    F   T   F   T   T   <- dp[5][4] = True
```

**Reference implementation**

```python
def isMatch(self, s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]
```

- **Time:** `O(m * n)`.
- **Space:** `O(m * n)`, reducible to `O(n)` with a rolling row. A greedy
  two-pointer solution also achieves `O(1)` extra space, but the DP is the
  clearest correct baseline.

## Key Insights & Edge Cases

- **`'*'` is standalone here** (contrast with regex `x*`). It is *not* tied to a
  preceding character, so the transition looks only at the star cell's left and
  up neighbors.
- **Leading-star initialization is essential:** without setting `dp[0][j]` for a
  run of stars, patterns like `"*a*b"` against a string whose first star must
  match empty would wrongly fail.
- **Consecutive stars** (`"**"`) behave like a single star; the recurrence
  handles them for free because each just propagates `dp[i][j-1]`.
- **Empty pattern** matches only the empty string; **empty string** matches a
  pattern only if it is all stars.
- **Whole-string match:** the answer is `dp[m][n]`; partial matches are never
  accepted because the base column forces non-empty `s` to consume pattern.
