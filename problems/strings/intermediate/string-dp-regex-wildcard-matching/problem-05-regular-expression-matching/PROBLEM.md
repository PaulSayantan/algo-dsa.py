# Regular Expression Matching

**Difficulty:** Hard

**Source:** LeetCode 10 — Regular Expression Matching

## Description

Given an input string `s` and a pattern `p`, implement regular-expression
matching with support for `'.'` and `'*'` where:

- `'.'` matches any **single** character.
- `'*'` matches **zero or more** of the **preceding element**.

The matching should cover the **entire** input string `s` (not a partial match).

The key difference from Wildcard Matching (Problem 3) is that `'*'` here is a
**quantifier** bound to the character immediately before it: `a*` means "zero or
more `a`", `.*` means "zero or more of anything". This coupling makes the DP
transition look at the pattern **two cells back**, and it is the reason regex
matching is the hardest member of this String-DP family.

## Constraints

- `1 <= s.length <= 20`
- `1 <= p.length <= 30`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'.'`, and `'*'`.
- It is guaranteed that for each appearance of the character `'*'`, there will be
  a previous valid character to match.

## Examples

### Example 1

```
Input:  s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

### Example 2

```
Input:  s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding 'a'. Here 'a' repeats once,
             so it matches "aa".
```

### Example 3

```
Input:  s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more of any character", which matches "ab".
```

### Example 4

```
Input:  s = "mississippi", p = "mis*is*p*."
Output: false
Explanation: The trailing "p*." cannot consume the "ippi" tail correctly, so
             the full string is not matched.
```

## Hint

Use **String DP (regex/wildcard matching)**: `dp[i][j]` = does `s[:i]` match
`p[:j]`. When `p[j-1] == '*'`, look at the pair `p[j-2] p[j-1]`: it can match
**zero** occurrences (`dp[i][j-2]`) or, if `p[j-2]` matches `s[i-1]`, **one
more** occurrence (`dp[i-1][j]`). A `'.'` or exact letter inherits `dp[i-1][j-1]`.
