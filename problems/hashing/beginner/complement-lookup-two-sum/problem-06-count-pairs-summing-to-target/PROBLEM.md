# Count Pairs Summing to Target

**Difficulty:** Easy

**Source:** Classic — Two Sum pair count variant

## Description

Given an integer array `nums` and an integer `target`, return the number of pairs `(i, j)` with `i < j` and `nums[i] + nums[j] == target`. Count every qualifying index pair, including those formed by equal values.

## Examples

### Example 1

```
Input:  nums = [1,2,3,4], target = 5
Output: 2
```

**Explanation:** Pairs (0,3) and (1,2).

## Hint

Running frequency map: for each x, add how many earlier elements equal (target - x).
