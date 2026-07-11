# Wildcard Matching

**Difficulty:** Hard

**Source:** LeetCode 44 — Wildcard Matching

## Description

Given an input string `s` and a pattern `p`, implement wildcard pattern matching
with support for `'?'` and `'*'` where:

- `'?'` matches any **single** character.
- `'*'` matches any **sequence** of characters, **including the empty sequence**.

The matching should cover the **entire** input string `s` (not a partial match).

Unlike regular-expression matching, here `'*'` is a standalone token — it does
**not** modify a preceding character. That makes it a clean introduction to
pattern-based String DP: the table cell `dp[i][j]` answers "does `s[:i]` match
`p[:j]`?" and the interesting work happens whenever `p[j-1]` is `'*'`.

## Constraints

- `0 <= s.length, p.length <= 2000`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'?'`, or `'*'`.

## Examples

### Example 1

```
Input:  s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

### Example 2

```
Input:  s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence, including "aa".
```

### Example 3

```
Input:  s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter 'a' does not match 'b'.
```

### Example 4

```
Input:  s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, the second '*' matches
             "dce", so the pattern matches the whole string.
```

## Hint

Use **String DP (regex/wildcard matching)**: `dp[i][j]` = does `s[:i]` match
`p[:j]`. When `p[j-1]` is `'*'`, it can match the empty sequence
(`dp[i][j-1]`) or absorb one more character of `s` (`dp[i-1][j]`). A `'?'` or an
exact letter match just inherits `dp[i-1][j-1]`.
