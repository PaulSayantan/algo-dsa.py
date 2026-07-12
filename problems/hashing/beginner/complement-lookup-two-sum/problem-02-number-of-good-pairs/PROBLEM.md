# Number of Good Pairs

**Difficulty:** Easy

**Source:** LeetCode 1512 — Number of Good Pairs

## Description

Given an integer array `nums`, a pair `(i, j)` is *good* if `nums[i] == nums[j]` and `i < j`. Return the number of good pairs.

## Examples

### Example 1

```
Input:  nums = [1,2,3,1,1,3]
Output: 4
```

**Explanation:** The good pairs are (0,3),(0,4),(3,4),(2,5).

## Hint

Here the 'complement' is the same value: for each x add the count of equal values seen so far.
