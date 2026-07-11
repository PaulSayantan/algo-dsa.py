# Daily Temperatures

**Difficulty:** Medium

**Source:** LeetCode 739 — Daily Temperatures

## Description

Given an array of integers `temperatures` representing the daily temperatures, return an
array `answer` such that `answer[i]` is the **number of days** you have to wait after the
`i`-th day to get a **warmer** temperature. If there is no future day for which this is
possible, set `answer[i] = 0`.

In other words, for each day, find how many days until a strictly warmer day; the answer is
the *distance* (index gap), not the temperature itself.

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## Examples

### Example 1

```
Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

**Explanation:**
- Day 0 (73): day 1 is 74 (warmer) → wait 1.
- Day 2 (75): the next warmer day is day 6 (76) → wait 4.
- Day 3 (71): day 5 is 72 → wait 2.
- Days 6 (76) and 7 (73): no warmer future day → 0.

### Example 2

```
Input:  temperatures = [30, 40, 50, 60]
Output: [1, 1, 1, 0]
```

**Explanation:** Every day is warmer than the previous, so each waits exactly 1 day,
except the last day, which has no future and gets 0.

## Hint

Use a **Monotonic Stack / Queue** that holds **indices** of days with a non-increasing
temperature. When a warmer day arrives, pop the resolved days and compute the distance as
the difference of indices.
