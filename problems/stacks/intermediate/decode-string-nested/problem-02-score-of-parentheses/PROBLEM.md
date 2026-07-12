# Score of Parentheses

**Difficulty:** Medium

**Source:** LeetCode 856 — Score of Parentheses

## Description

Given a balanced parentheses string `s`, return its score under these rules:

- `()` has score `1`.
- `AB` has score `A + B`, where `A` and `B` are balanced strings.
- `(A)` has score `2 * A`, where `A` is a balanced string.

`s` consists only of `(` and `)`, is balanced, and `1 <= len(s) <= 50`.

## Examples

### Example 1

```
Input:  s = "(()(()))"
Output: 6
```

**Explanation:** `(()(()))` = `2 * ( () + (()) )` = `2 * (1 + 2)` = `6`.

## Hint

Keep a stack whose top holds the score accumulated inside the current bracket frame; `(` pushes a fresh `0`, `)` pops that frame and folds `max(2*inner, 1)` into the parent.
