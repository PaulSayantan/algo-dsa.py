# Round-Robin With Arrival Times

**Difficulty:** Medium

**Source:** Classic — round-robin CPU scheduling with arrivals

## Description

Given `arrival` times and `burst` times for processes `0..n-1` and a time `quantum`, simulate round-robin scheduling and return a list `completion` where `completion[i]` is the time process `i` finishes.

Rules for building the ready queue:
- A process becomes ready at its `arrival` time and is appended to the FIFO ready queue.
- When a running process's quantum ends, any processes that arrived during that quantum (arrival time `<=` the current clock) are enqueued **first**, and only then is the still-unfinished running process requeued at the back.
- If the ready queue is ever empty but processes remain, the clock jumps forward to the next arrival time (the CPU idles).
- Ties (equal arrival times) are broken by process id.

Constraints: `1 <= n`, `0 <= arrival[i]`, `1 <= burst[i]`, `1 <= quantum`.

## Examples

### Example 1

```
Input:  arrival = [0, 1, 2], burst = [5, 3, 8], quantum = 3
Output: [11, 6, 16]
```

**Explanation:** P0 runs [0,3); P1 arrived at 1 and P2 at 2 so the queue is [P1, P2, P0]. P1 runs [3,6) and finishes at 6. P2 runs [6,9). P0 runs [9,11) and finishes at 11. P2 runs [11,14) then [14,16) and finishes at 16.

## Hint

Sort arrivals by `(arrival, id)`; keep a pointer that enqueues every process whose arrival is `<= t` after each quantum, requeuing the running process only afterward; idle-jump the clock to the next arrival when the queue empties.
