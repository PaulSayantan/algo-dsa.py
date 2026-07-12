# Custom Sort String

**Difficulty:** Medium

**Source:** LeetCode 791 — Custom Sort String

## Description

You are given `order`, a permutation of some distinct characters, and a string `s`. Sort the characters of `s` so they follow the same relative order as in `order`. Characters of `s` that do not appear in `order` may go in any position; the reference keeps them last, in their original relative order, for a deterministic result.

## Examples

### Example 1

```
Input:  order = "cba", s = "abcd"
Output: "cbad"
```

## Hint

Give each char a rank from `order` (unknown chars get a large rank), then do a stable sort of s by rank.
