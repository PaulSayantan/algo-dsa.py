# Groups of Special-Equivalent Strings

**Difficulty:** Medium

**Source:** LeetCode 893 — Groups of Special-Equivalent Strings

## Description

Two strings of equal length are *special-equivalent* if you can make them equal using any number of moves, where each move swaps two characters at **even** indices or two characters at **odd** indices. Given an array `words`, return the number of groups of special-equivalent strings.

## Examples

### Example 1

```
Input:  words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
```

## Hint

Signature = (sorted characters at even indices, sorted characters at odd indices); count distinct signatures.
