# Task Scheduler II

**Difficulty:** Medium

**Source:** LeetCode 2365 — Task Scheduler II

## Description

You are given a 0-indexed array `tasks` of task types (integers) that must be completed **in order**, and an integer `space`. Each day you either complete the next task or take a break. After completing a task of a given type, you must wait at least `space` days before completing another task of that **same** type. Return the minimum number of days needed to finish all tasks.

Constraints: `1 <= len(tasks) <= 10^5`, `1 <= tasks[i] <= 10^9`, `1 <= space <= len(tasks)`.

## Examples

### Example 1

```
Input:  tasks = [1, 2, 1, 2, 3, 1], space = 3
Output: 9
```

**Explanation:** Days: 1, 2, idle, task1, task2, idle, task3, idle, task1 → 9 days. Each repeat of a type respects the `space`-day cooldown.

## Hint

Track, per task type, the earliest day it is next available (`finish_day + space + 1`). Advance the day counter, jumping ahead to that ready-time whenever the same type is still cooling down.
