# Jewels and Stones

**Difficulty:** Easy

**Source:** LeetCode 771 — Jewels and Stones

## Description

You are given `jewels`, a string of distinct characters that are the jewel types, and `stones`, a string of the stones you have. Return how many of your stones are also jewels. Characters are case-sensitive, so `"a"` and `"A"` are different types.

## Examples

### Example 1

```
Input:  jewels = "aA", stones = "aAAbbbb"
Output: 3
```

## Hint

Put the jewel characters in a set, then count stones whose character is in that set.
