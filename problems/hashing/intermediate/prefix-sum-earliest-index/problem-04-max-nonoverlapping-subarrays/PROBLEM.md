# Max Non-Overlapping Subarrays With Sum Target

**Difficulty:** Medium

**Source:** LeetCode 1546 — Maximum Number of Non-Overlapping Subarrays With Sum Equals Target

## Description

Given `nums` and an integer `target`, return the maximum number of non-empty, non-overlapping subarrays such that each has a sum equal to `target`.

## Examples

### Example 1

```
Input:  nums = [1,1,1,1,1], target = 2
Output: 2
```

## Hint

Greedy: when cur-target is a seen prefix, cut here (+1) and reset the seen set.
