# Valid Parenthesis String

**Difficulty:** Medium

**Source:** LeetCode 678 — Valid Parenthesis String

## Description

Given a string `s` containing only `(`, `)`, and `*`, return `True` if `s` is valid. The `*` wildcard may be treated as a single `(`, a single `)`, or the empty string `""`. A string is valid when every `(` has a matching later `)` and every `)` has a matching earlier `(`.

## Examples

### Example 1

```
Input:  s = "(*))"
Output: True
```

**Explanation:** Treat the `*` as `(`, giving `(())`, which is valid.

## Hint

Instead of a fixed open count, carry the range `[low, high]` of possible unmatched `(` counts; `*` widens it, `)` shrinks it, clamp `low` at 0 and fail if `high` goes negative.
