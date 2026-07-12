# Group Shifted Strings

**Difficulty:** Medium

**Source:** LeetCode 249 — Group Shifted Strings

## Description

A string can be *shifted* by advancing every letter by the same amount (with wrap-around from `z` to `a`), e.g. `"abc" -> "bcd" -> ...`. Given an array `strings`, group all strings that belong to the same shifting sequence. Groups may be returned in any order; the reference sorts each group and the list of groups for a canonical answer.

## Examples

### Example 1

```
Input:  strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["a","z"],["abc","bcd","xyz"],["acef"],["az","ba"]]
```

## Hint

Signature = tuple of (ord(c) - ord(first)) % 26 for each char; equal-shift strings share it.
