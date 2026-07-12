# Task Scheduler

**Difficulty:** Medium

**Source:** LeetCode 621 — Task Scheduler

## Description

Given `tasks` (uppercase letters) and an integer `n`, the same task must be separated by at least `n` intervals. Each interval runs one task or is idle. Return the minimum number of intervals to finish all tasks.

## Examples

### Example 1

```
Input:  tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
```

## Hint

With max frequency f occurring k times: answer = max(len(tasks), (f-1)*(n+1) + k).
