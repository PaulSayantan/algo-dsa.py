# Count Balanced Binary Subarrays

**Difficulty:** Medium

**Source:** Classic — count subarrays with equal 0s and 1s (balance frequency)

## Description

Given a binary array `nums`, return the number of contiguous subarrays that contain an equal number of `0`s and `1`s. Map `0` to `-1` and `1` to `+1`; a subarray is balanced exactly when the running balance is identical at its two endpoints, so count the pairs of positions sharing each balance.

## Examples

### Example 1

```
Input:  nums = [0,1,0,1]
Output: 4
```

**Explanation:** [0,1],[1,0],[0,1], and the whole array are all balanced.

### Example 2

```
Input:  nums = [0,0,1,1]
Output: 2
```

**Explanation:** [0,1] (middle) and the whole array [0,0,1,1].

## Hint

Seed freq[0] = 1; for each prefix balance add how many times that balance has already occurred.
