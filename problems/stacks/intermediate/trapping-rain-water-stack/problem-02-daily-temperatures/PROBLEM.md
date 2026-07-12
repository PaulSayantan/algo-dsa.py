# Daily Temperatures

**Difficulty:** Medium

**Source:** LeetCode 739 — Daily Temperatures

## Description

Given a list `temperatures` of daily temperatures, return a list `answer` where `answer[i]` is the number of days you must wait after day `i` to get a warmer temperature. If no future day is warmer, set `answer[i]` to `0`.

Constraints: `1 <= len(temperatures) <= 10^5`, `30 <= temperatures[i] <= 100`.

## Examples

### Example 1

```
Input:  temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Explanation:** Day 0 (73) warms up the next day (74), so wait 1. Day 2 (75) waits 4 days until 76.

## Hint

Keep a monotonically decreasing stack of indices; when a warmer day arrives it "closes off" the cooler bars beneath it — pop each and record the index gap, exactly like resolving bars in trapping rain water.
