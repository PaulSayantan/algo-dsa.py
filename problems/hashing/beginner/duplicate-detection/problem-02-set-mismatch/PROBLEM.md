# Set Mismatch

**Difficulty:** Easy

**Source:** LeetCode 645 — Set Mismatch

## Description

The set `s` originally contained the numbers `1..n`. Due to an error, one number is **duplicated** (appearing twice) while another is **missing**. Given the resulting array `nums`, return `[duplicated, missing]`.

## Examples

### Example 1

```
Input:  nums = [1,2,2,4]
Output: [2,3]
```

**Explanation:** 2 is duplicated; 3 is missing.

## Hint

Count values; the value with count 2 is duplicated, the value with count 0 is missing.
