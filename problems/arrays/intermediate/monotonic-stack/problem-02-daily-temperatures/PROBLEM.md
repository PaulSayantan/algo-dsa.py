# Daily Temperatures

**Difficulty:** Medium

**Source:** LeetCode 739 — Daily Temperatures

## Description

Given an array of integers `temperatures` representing the daily temperatures,
return an array `answer` such that `answer[i]` is the **number of days** you have
to wait after the `i`-th day to get a warmer temperature.

If there is no future day for which this is possible, set `answer[i] == 0`.

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
- Day 0 (73): the next warmer day is day 1 (74) -> wait 1 day.
- Day 2 (75): the next warmer day is day 6 (76) -> wait 4 days.
- Day 3 (71): next warmer is day 5 (72) -> wait 2 days.
- Days 6 (76) and 7 (73) have no warmer day ahead -> 0.

### Example 2

```
Input:  temperatures = [30, 40, 50, 60]
Output: [1, 1, 1, 0]
```

**Explanation:** Every day is immediately followed by a warmer day except the
last, so each answer is `1` except the final `0`.

### Example 3

```
Input:  temperatures = [90, 60, 60, 90]
Output: [0, 2, 1, 0]
```

**Explanation:** Day 1 (60) must wait until day 3 (90) -> 2 days. Day 2 (60)
waits 1 day for day 3 (90). Both `90`s have nothing strictly warmer ahead -> 0.
Note that equal temperatures do **not** count as warmer.

## Hint

Keep a **Monotonic Stack** of **indices** whose temperatures are decreasing.
When a warmer day arrives, it resolves every colder day still on the stack; the
answer is the difference of indices.
