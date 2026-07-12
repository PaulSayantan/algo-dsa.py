# Daily Temperatures

**Difficulty:** Medium

**Source:** LeetCode 739 — Daily Temperatures

## Description

Given an array `temperatures`, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th day to get a warmer temperature. If there is no future warmer day, `answer[i] == 0`.

## Examples

### Example 1

```
Input:  temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

## Hint

Keep a decreasing stack of indices; when a warmer day arrives, pop and record the day gap.
