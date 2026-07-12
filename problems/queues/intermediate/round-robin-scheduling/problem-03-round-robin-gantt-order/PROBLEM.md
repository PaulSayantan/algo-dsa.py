# Round-Robin Gantt Order

**Difficulty:** Medium

**Source:** Classic — round-robin CPU scheduling (Gantt chart)

## Description

Given `burst` times for processes `0..n-1` (in arrival order, all arriving at time 0) and a time `quantum`, simulate round-robin scheduling and return the **Gantt order**: the sequence of process ids in the order they are *dispatched onto the CPU*, one entry per time slice.

Each time a process reaches the front of the ready queue it is dispatched (append its id to the sequence) and runs for `min(quantum, remaining)` time units. If it still has work left it is requeued at the back; otherwise it leaves. A process that needs several quanta therefore appears in the sequence once per slice it runs.

This is the order the slices would appear on a Gantt chart, which differs from the order in which processes *complete*.

Constraints: `1 <= n`, `1 <= burst[i]`, `1 <= quantum`.

## Examples

### Example 1

```
Input:  burst = [5, 3, 8], quantum = 3
Output: [0, 1, 2, 0, 2, 2]
```

**Explanation:** P0 runs [0,3) leaving 2, P1 runs [3,6) and finishes, P2 runs [6,9) leaving 5. P0 runs [9,11) and finishes, then P2 runs [11,14) leaving 2 and [14,16) finishing. The dispatch sequence is `[0, 1, 2, 0, 2, 2]`.

### Example 2

```
Input:  burst = [4, 4, 4], quantum = 2
Output: [0, 1, 2, 0, 1, 2]
```

**Explanation:** Each process needs two quanta, so one full pass dispatches `[0, 1, 2]` and the second pass dispatches `[0, 1, 2]` again.

## Hint

FIFO queue of `(id, remaining)`; each turn append the id to the output first, then run `min(quantum, remaining)` and requeue if work remains.
