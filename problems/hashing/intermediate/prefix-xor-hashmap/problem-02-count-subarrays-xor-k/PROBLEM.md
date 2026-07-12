# Count Subarrays With XOR Equal to K

**Difficulty:** Medium

**Source:** Classic — subarray XOR equals K (prefix XOR + frequency map)

## Description

Given an integer array `nums` and an integer `k`, return the number of contiguous subarrays whose elements XOR to exactly `k`. Maintain a running prefix XOR `cur` and a frequency map of prefixes seen so far; a subarray ending here has XOR `k` for every earlier prefix equal to `cur ^ k`.

## Examples

### Example 1

```
Input:  nums = [4,2,2,6,4], k = 6
Output: 4
```

### Example 2

```
Input:  nums = [1,1,1,1], k = 0
Output: 4
```

**Explanation:** The four even-length equal-XOR windows all XOR to 0.

## Hint

Seed freq[0] = 1; for each element add freq[cur ^ k] before recording cur.
