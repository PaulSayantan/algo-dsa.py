# Count Subarrays With XOR Equal to Zero

**Difficulty:** Medium

**Source:** Classic — count zero-XOR subarrays (prefix XOR pairs)

## Description

Given an integer array `nums`, return the number of contiguous subarrays whose elements XOR to `0`. A subarray `(j, i]` XORs to `0` exactly when `prefix[j] == prefix[i]`, so count, for each prefix value, how many pairs of positions share it.

## Examples

### Example 1

```
Input:  nums = [1,1,1,1]
Output: 4
```

**Explanation:** The four even-length runs each XOR to 0.

### Example 2

```
Input:  nums = [1,2,3]
Output: 1
```

**Explanation:** Only the whole array [1,2,3] XORs to 0.

## Hint

Seed freq[0] = 1; for each prefix add the number of times that same prefix has already appeared.
