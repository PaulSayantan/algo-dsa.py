# Task Dispatch Log

**Difficulty:** Easy

**Source:** Classic — round-robin task dispatch simulation

## Description

A scheduler runs tasks `0..n-1` round-robin on a single core. `work[i]` is the number of time units task `i` needs. In one time slice the scheduler runs the task at the front of the ready queue for up to `quantum` units; if the task still has work left afterward it goes to the **back** of the queue, otherwise it finishes and leaves. Every time a task is picked to run, its id is appended to a dispatch log.

Given `work` (in queue order) and the `quantum`, return the dispatch log: the list of task ids in the exact order they are picked to run (a task appears once per slice it receives).

## Examples

### Example 1

```
Input:  work = [4, 2, 3], quantum = 2
Output: [0, 1, 2, 0, 2]
```

**Explanation:** Task 0 runs (2 left, requeued), task 1 runs and finishes, task 2 runs (1 left, requeued), task 0 runs and finishes, task 2 runs and finishes.

### Example 2

```
Input:  work = [1, 1, 1], quantum = 1
Output: [0, 1, 2]
```

**Explanation:** Each task needs a single slice, so every task is dispatched exactly once in order.

## Hint

deque of `[task_id, work_left]`; each slice popleft, log the id, subtract `min(quantum, work_left)`, and re-enqueue only if work remains.
