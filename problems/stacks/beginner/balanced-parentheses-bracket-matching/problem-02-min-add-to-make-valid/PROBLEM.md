# Minimum Add to Make Parentheses Valid

**Difficulty:** Medium

**Source:** LeetCode 921 — Minimum Add to Make Parentheses Valid

## Description

A parentheses string is valid iff every `(` has a matching `)` and vice versa. Given `s` of `(` and `)`, return the minimum number of single-character insertions (of `(` or `)`) needed to make it valid.

## Examples

### Example 1

```
Input:  s = "())"
Output: 1
```

### Example 2

```
Input:  s = "((("
Output: 3
```

## Hint

Track open count; an unmatched ')' needs an insertion. Leftover '(' also each need one.
