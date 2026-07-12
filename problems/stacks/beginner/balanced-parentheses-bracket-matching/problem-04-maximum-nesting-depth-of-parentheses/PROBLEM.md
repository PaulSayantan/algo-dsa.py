# Maximum Nesting Depth of the Parentheses

**Difficulty:** Easy

**Source:** LeetCode 1614 — Maximum Nesting Depth of the Parentheses

## Description

A valid parentheses string (VPS) is a string that consists of `(`, `)`, digits, and the operators `+`, `-`, `*`, `/`, in which the parentheses are balanced. The *nesting depth* of a VPS is the maximum number of parentheses that are open at the same point while scanning it. Given a VPS `s`, return its maximum nesting depth.

`s` is guaranteed to be a valid parentheses string.

## Examples

### Example 1

```
Input:  s = "(1+(2*3)+((8)/4))+1"
Output: 3
```

**Explanation:** The digit `8` sits inside three simultaneously open parentheses, the deepest point in the string.

### Example 2

```
Input:  s = "(1)+((2))+(((3)))"
Output: 3
```

**Explanation:** The innermost `3` is wrapped by three open parentheses.

## Hint

Keep a running open-bracket count (the current stack height): `+1` on `(`, `-1` on `)`, and track the maximum height reached.
