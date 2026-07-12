# Remove Outermost Parentheses

**Difficulty:** Easy

**Source:** LeetCode 1021 — Remove Outermost Parentheses

## Description

A valid parentheses string `s` is *primitive* if it is non-empty and cannot be split into two non-empty valid parentheses strings. Every valid `s` decomposes uniquely into primitives `P_1 + P_2 + ... + P_k`. Return `s` with the outermost pair of parentheses of every primitive removed.

`s` is guaranteed to be a valid parentheses string containing only `(` and `)`.

## Examples

### Example 1

```
Input:  s = "(()())(())"
Output: "()()()"
```

**Explanation:** Primitives are `(()())` and `(())`; stripping each outer pair gives `()()` and `()`.

### Example 2

```
Input:  s = "(())"
Output: "()"
```

**Explanation:** Single primitive `(())`; removing the outer pair leaves `()`.

## Hint

Track nesting depth like a stack: a `(` at depth 0 (and its matching `)` returning to depth 0) is an outermost bracket — skip it, keep the rest.
