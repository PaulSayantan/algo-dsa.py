# How Many Numbers Are Smaller Than the Current Number

**Difficulty:** Easy

**Source:** LeetCode 1365 — How Many Numbers Are Smaller Than the Current Number

## Description

Given an array `nums`, for each `nums[i]` count how many other numbers in the array are strictly smaller than it, and return the counts as an array in the same order. Values are in the range `0..100`.

## Examples

### Example 1

```
Input:  nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
```

### Example 2

```
Input:  nums = [6,5,4,8]
Output: [2,1,0,3]
```

## Hint

Bucket the frequency of each value (0..100), take a prefix sum, then prefix[x] answers 'how many are < x'.
