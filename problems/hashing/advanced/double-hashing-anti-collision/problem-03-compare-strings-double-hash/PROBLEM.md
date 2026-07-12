# Compare Two Strings via Double Hash

**Difficulty:** Easy

**Source:** Classic — robust hash equality

## Description

Given two strings `a` and `b`, decide whether they are equal using their double-hash keys (two independent polynomial hashes). Return a boolean. Strings of differing length are trivially unequal, and two empty strings are equal.

## Examples

### Example 1

```
Input:  a = "abcdef", b = "abcdef"
Output: True
```

## Hint

Different lengths -> False; otherwise compare the (h1, h2) key of each whole string.
