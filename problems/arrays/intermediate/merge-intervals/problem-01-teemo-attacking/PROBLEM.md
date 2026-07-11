# Teemo Attacking

**Difficulty:** Easy

**Source:** LeetCode 495 — Teemo Attacking

## Description

Our hero Teemo is attacking an enemy Ashe with poison attacks. You are given a
**non-decreasing** integer array `timeSeries`, where `timeSeries[i]` denotes that
Teemo attacks Ashe at second `timeSeries[i]`, and an integer `duration`.

When Teemo attacks at second `t`, Ashe becomes poisoned for `duration` seconds —
that is, for the half-open time window `[t, t + duration)`. If Teemo attacks
again **before** the current poison ends, the poison timer is **reset** to last
for another full `duration` seconds starting from the new attack (the effect does
not stack, it only refreshes).

Return the **total number of seconds** that Ashe is poisoned.

You can think of each attack as producing an interval `[t, t + duration)`. Attacks
whose windows overlap or touch merge into one continuous poisoned stretch. The
answer is the summed length of the merged windows.

## Constraints

- `1 <= timeSeries.length <= 10^4`
- `0 <= timeSeries[i], duration <= 10^7`
- `timeSeries` is sorted in **non-decreasing** order.

## Examples

**Example 1**

```
Input:  timeSeries = [1, 4], duration = 2
Output: 4
Explanation: Attack at second 1 poisons the window [1, 3) -> seconds 1 and 2.
             Attack at second 4 poisons the window [4, 6) -> seconds 4 and 5.
             The two windows do not overlap, so the total is 2 + 2 = 4 seconds.
```

**Example 2**

```
Input:  timeSeries = [1, 2], duration = 2
Output: 3
Explanation: Attack at second 1 poisons [1, 3). Attack at second 2 arrives before
             second 3, so the timer resets to [2, 4). The union of [1, 3) and
             [2, 4) is [1, 4), which is 3 seconds long.
```

**Example 3**

```
Input:  timeSeries = [0, 5, 10], duration = 3
Output: 9
Explanation: Windows [0, 3), [5, 8), [10, 13) never overlap, so the total is
             3 + 3 + 3 = 9 seconds.
```

## Hint

Model each attack as an interval `[t, t + duration)` and apply the **Merge
Intervals** idea: consecutive attacks either extend the current poisoned window
(when they overlap) or begin a new one. Because `timeSeries` is already sorted,
a single pass comparing each attack's start against the previous window's end is
enough.
