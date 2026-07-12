# Round-Robin Waiting Times

**Difficulty:** Medium

**Source:** Classic — round-robin CPU scheduling (waiting time)

## Description

Given `burst` times for processes `0..n-1` (in arrival order, all arriving at time 0) and a time `quantum`, simulate round-robin scheduling and return a list `waiting` where `waiting[i]` is the waiting time of process `i`.

The waiting time of a process is its completion time minus its burst time (equivalently, the total time it spent in the ready queue not running). Return the waiting times indexed by process id.

Constraints: `1 <= n`, `1 <= burst[i]`, `1 <= quantum`.

## Examples

### Example 1

```
Input:  burst = [5, 3, 8], quantum = 3
Output: [6, 3, 8]
```

**Explanation:** Completion times are `[11, 6, 16]`; subtracting burst `[5, 3, 8]` gives `[6, 3, 8]`.

## Hint

Simulate the round-robin: a FIFO queue of `(id, remaining)`, advance a global clock by `min(quantum, remaining)` each turn, record each process's completion time, then subtract its burst.
