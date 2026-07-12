# Remove Duplicate Letters

**Difficulty:** Medium

**Source:** LeetCode 316 — Remove Duplicate Letters

## Description

Given a string `s`, remove duplicate letters so that every letter appears once and only once, and the result is the smallest in lexicographical order among all such strings.

## Examples

### Example 1

```
Input:  s = "cbacdcbc"
Output: "acdb"
```

## Hint

Monotonic stack; pop a larger top if it appears again later and isn't already in the stack.
