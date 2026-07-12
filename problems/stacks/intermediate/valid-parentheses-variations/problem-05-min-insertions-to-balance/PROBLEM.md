# Minimum Insertions to Balance a Parentheses String

**Difficulty:** Medium

**Source:** LeetCode 1541 — Minimum Insertions to Balance a Parentheses String

## Description

Given a string `s` of `(` and `)`, a balanced string is one where every `(` is matched by **two** consecutive `)`, i.e. `()) `-style pairing. Formally:

- Any `(` must be closed by exactly two `)` immediately following its match.
- `()` alone is **not** balanced; `())` is balanced.

Return the minimum number of insertions (of either `(` or `)`, at any position) needed to make `s` balanced.

## Examples

### Example 1

```
Input:  s = "(()))"
Output: 1
```

**Explanation:** The first `(` needs `))` and gets them; the second `(` is closed by only one `)`, so one more `)` must be inserted, giving `(())) )` -> `(())))` which is balanced.

### Example 2

```
Input:  s = "())"
Output: 0
```

**Explanation:** `())` is already balanced: one `(` closed by two `)`.

### Example 3

```
Input:  s = "))())("
Output: 3
```

**Explanation:** The two leading `)` need a `(` inserted before them and one more `)`; the trailing `(` needs `))`. Three insertions in total balance the string.

## Hint

Scan left to right tracking how many `)` are still owed by open `(`. Because each `(` demands two `)`, an unmatched `(` bumps the owed count by 2; a lone `)` that leaves the owed count odd forces an inserted `)`. Count forced insertions as you go, then add whatever is still owed at the end.
