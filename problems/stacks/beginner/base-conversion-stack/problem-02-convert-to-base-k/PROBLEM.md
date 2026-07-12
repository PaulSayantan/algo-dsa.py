# Convert to Base K

**Difficulty:** Easy

**Source:** Classic — general base conversion

## Description

Given a non-negative integer `n` and a base `k` (2 ≤ k ≤ 16), return the base-`k` representation as a string, using digits `0-9` then `a-f` for values 10–15. Use a stack of remainders.

## Examples

### Example 1

```
Input:  n = 255, k = 16
Output: "ff"
```

## Hint

Repeatedly take n%k as a digit and n//=k; map 10..15 to 'a'..'f'; pop to assemble.
