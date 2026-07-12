# Round-Robin Task Scheduler

**Difficulty:** Easy

**Source:** Classic — round-robin scheduling

## Description

Implement a `RoundRobin` scheduler over a fixed, non-empty list of task names. It cycles through the tasks in order, wrapping back to the first after the last. Implement `next()`, which returns the task whose turn it is now and then advances the cursor to the next task, and `peek()`, which returns the task that `next()` would hand out on the following call without advancing.

Constraints: the task list is non-empty; task names are strings.

## Examples

### Example 1

```
Input:  RoundRobin(["A", "B", "C"]); next(), next(), next(), next(), peek()
Output: 'A', 'B', 'C', 'A', 'B'
```

**Explanation:** The cursor walks `A -> B -> C` then wraps to `A`. After the fourth `next()` returns `A`, the cursor points at `B`, so `peek()` reports `'B'` without moving.

## Hint

Store a `head` index into the task array and advance it as `(head + 1) % n` on every dispatch — the modulo wrap turns the array into a circular queue.
