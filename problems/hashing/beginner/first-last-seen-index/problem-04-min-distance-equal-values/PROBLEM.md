# Minimum Distance Between Equal Values

**Difficulty:** Easy

**Source:** Classic — last-seen index distance

## Description

Given an integer array `nums`, return the minimum value of `j - i` over all pairs with `i < j` and `nums[i] == nums[j]`. If no value repeats, return `-1`.

## Examples

### Example 1

```
Input:  nums = [1,2,1,3,1]
Output: 2
```

**Explanation:** The closest pair of 1's is 2 apart.

## Hint

Track the MOST RECENT index of each value; each repeat gives a candidate gap — keep the smallest.
