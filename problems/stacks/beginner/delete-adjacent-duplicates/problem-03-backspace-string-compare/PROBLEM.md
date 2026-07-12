# Backspace String Compare

**Difficulty:** Easy

**Source:** LeetCode 844 — Backspace String Compare

## Description

Given two strings `s` and `t`, return `True` if they are equal when both are typed into empty text editors, where `'#'` means a backspace character (it deletes the character immediately before it, if any). A backspace on empty text does nothing. Both strings contain only lowercase letters and `'#'`.

## Examples

### Example 1

```
Input:  s = "ab#c", t = "ad#c"
Output: true
```

**Explanation:** Both become `"ac"` — the `#` deletes the `b` in `s` and the `d` in `t`.

## Hint

Build each result with a stack: push a letter, but pop the top on a `#` — the same "check the top and delete instead of keeping" collapse.
