# Set Mismatch

**Difficulty:** Easy

**Source:** LeetCode 645 — Set Mismatch

## Description

You have a set that should contain the numbers `1..n`, but one value was duplicated (replacing a missing one). Given the corrupted array `nums`, return `[duplicated, missing]`: the number that appears twice and the number that never appears.

## Examples

### Example 1

```
Input:  nums = [1,2,2,4]
Output: [2,3]
```

### Example 2

```
Input:  nums = [1,1]
Output: [1,2]
```

## Hint

Count occurrences of 1..n; the value with count 2 is the duplicate, the value with count 0 is missing.
