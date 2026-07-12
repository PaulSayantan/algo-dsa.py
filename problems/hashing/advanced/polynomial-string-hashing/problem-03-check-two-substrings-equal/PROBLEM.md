# Check If Two Substrings Are Equal

**Difficulty:** Easy

**Source:** Classic — O(1) substring comparison

## Description

Given a string `s` and indices `a`, `b`, and a length `L`, determine whether the substrings `s[a : a+L]` and `s[b : b+L]` are equal, in O(1) after an O(n) prefix-hash build. Return a boolean.

## Examples

### Example 1

```
Input:  s = "abcabc", a=0, b=3, L=3
Output: True
```

## Hint

Compare hash(s[a:a+L]) and hash(s[b:b+L]) using the prefix-hash formula.
