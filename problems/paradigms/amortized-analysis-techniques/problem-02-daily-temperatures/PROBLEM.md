# Daily Temperatures

**Difficulty:** Medium

**Source:** LeetCode 739 — Daily Temperatures

## Description

Given an array of integers `temperatures` representing the daily temperatures, return
an array `answer` such that `answer[i]` is the number of days you have to wait after
the `i`-th day to get a warmer temperature. If there is no future day for which this
is possible, keep `answer[i] == 0` instead.

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## Examples

### Example 1

```
Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

Explanation:
- Day 0 (73): next warmer is day 1 (74) → wait 1.
- Day 1 (74): next warmer is day 2 (75) → wait 1.
- Day 2 (75): next warmer is day 6 (76) → wait 4.
- Day 3 (71): next warmer is day 5 (72) → wait 2.
- Day 4 (69): next warmer is day 5 (72) → wait 1.
- Day 5 (72): next warmer is day 6 (76) → wait 1.
- Day 6 (76): no warmer day after → 0.
- Day 7 (73): no warmer day after → 0.

### Example 2

```
Input:  temperatures = [30, 40, 50, 60]
Output: [1, 1, 1, 0]
```

Explanation: Each day is strictly warmer than the previous, so every day waits exactly
1 day for a warmer temperature. The last day has no future day, so its answer is 0.

### Example 3

```
Input:  temperatures = [90, 80, 70]
Output: [0, 0, 0]
```

Explanation: Temperatures only fall, so no day ever gets warmer afterward; all answers
are 0.

## Hint

Use **Amortized Analysis Techniques** with a **monotonic decreasing stack** of *indices*
of days still waiting for a warmer day. Each index is pushed exactly once and popped at
most once, so even though the inner "pop" loop looks like it could be O(n), the total
work across all days is O(n).
