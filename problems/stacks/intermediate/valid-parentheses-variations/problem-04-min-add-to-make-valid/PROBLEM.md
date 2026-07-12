# Minimum Add to Make Parentheses Valid

**Difficulty:** Medium

**Source:** LeetCode 921 — Minimum Add to Make Parentheses Valid

## Description

Given a string `s` of only `(` and `)`, return the minimum number of parentheses (of either kind, inserted at any positions) that must be **added** to make `s` valid. A string is valid when every `(` has a matching later `)` and every `)` has a matching earlier `(`.

## Examples

### Example 1

```
Input:  s = "())"
Output: 1
```

**Explanation:** One `(` added at the front (or a `)` removed conceptually) balances the extra `)`.

## Hint

Keep a running count of currently-unmatched `(`; every `)` that finds no open partner needs an inserted `(`. The answer is those forced insertions plus the `(` still open at the end.
