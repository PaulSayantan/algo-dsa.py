# Daily Temperatures

**Difficulty:** Easy

**Source:** LeetCode 739 — Daily Temperatures

## Description

Given an integer array `temperatures` where `temperatures[i]` is the temperature on the `i`-th day, return an array `answer` such that `answer[i]` is the number of days you have to wait after day `i` to get a warmer temperature. If there is no future day with a warmer temperature, set `answer[i] = 0`.

Constraints: `1 <= len(temperatures) <= 10^5`, `30 <= temperatures[i] <= 100`.

## Examples

### Example 1

```
Input:  temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Explanation:** Day 0 (73) warms on day 1; day 2 (75) waits until day 6 (76), a gap of 4; the last two days never get warmer.

## Hint

This is "next greater element" reporting the *distance* — keep a decreasing stack of day indices and, when a warmer day arrives, pop each waiting day and record `current_index - popped_index`.
