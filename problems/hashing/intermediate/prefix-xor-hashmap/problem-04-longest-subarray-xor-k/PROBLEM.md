# Longest Subarray With XOR Equal to K

**Difficulty:** Medium

**Source:** Classic — longest subarray with a given XOR (earliest-index map)

## Description

Given an integer array `nums` and an integer `k`, return the length of the longest contiguous subarray whose XOR is exactly `k` (0 if none exists). Store the **earliest** index at which each prefix XOR first appears; when the current prefix is `cur`, a subarray ending here has XOR `k` starting just after the earliest prefix equal to `cur ^ k`.

## Examples

### Example 1

```
Input:  nums = [4,2,2,6,4], k = 6
Output: 5
```

**Explanation:** The whole array XORs to 6.

### Example 2

```
Input:  nums = [1,2,3,4,5], k = 0
Output: 4
```

**Explanation:** The window [2,3,4,5] XORs to 0.

## Hint

Seed first = {0: -1}; only record a prefix the first time you see it so lengths are maximised.
