# Decode String

**Difficulty:** Medium

**Source:** LeetCode 394 — Decode String

## Description

Given an encoded string `s` following the rule `k[encoded]` (the `encoded` substring repeats exactly `k` times), return its decoded form. `k` is a positive integer; brackets may be nested; the input is always valid and contains no stray digits outside `k`.

## Examples

### Example 1

```
Input:  s = "3[a2[c]]"
Output: "accaccacc"
```

## Hint

Stack of (prefix, count); on '[' push and reset, on ']' pop and append prefix + cur*count.
