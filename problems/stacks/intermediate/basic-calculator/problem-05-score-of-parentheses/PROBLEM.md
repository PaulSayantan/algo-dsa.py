# Score of Parentheses

**Difficulty:** Medium

**Source:** LeetCode 856 — Score of Parentheses

## Description

Given a balanced parentheses string `s`, return its score computed by these rules:

- `()` has a score of `1`.
- `AB` has a score of `A + B`, where `A` and `B` are balanced parentheses strings.
- `(A)` has a score of `2 * A`, where `A` is a balanced parentheses string.

`s` consists only of `(` and `)` and is guaranteed to be balanced.

## Examples

### Example 1

```
Input:  s = "()"
Output: 1
```

**Explanation:** The single empty pair scores `1`.

### Example 2

```
Input:  s = "(()(()))"
Output: 6
```

**Explanation:** Inside the outer pair sit `()` (score 1) and `(())` (score 2), summing to 3; wrapping doubles it to `2 * 3 = 6`.

## Hint

Like the calculator's sign/context stack: push a running frame on `(`; on `)` pop it and merge `max(2 * inner, 1)` into the frame beneath.
