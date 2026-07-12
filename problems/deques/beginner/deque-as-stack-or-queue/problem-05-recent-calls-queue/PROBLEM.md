# Number of Recent Calls (Deque as a Queue)

**Difficulty:** Easy

**Source:** LeetCode 933 — Number of Recent Requests

## Description

Design a class `RecentCounter` that counts recent requests within a sliding time
window. Implement `ping(t)`, where `t` is the request time in milliseconds. Each
`ping(t)` records a request at time `t` and returns the number of requests that
happened in the inclusive range `[t - 3000, t]`.

Requests arrive in **strictly increasing** order of `t`. Back the counter with a
deque used as a **FIFO queue**: `append` each new time at the right end, then
`popleft` any times from the left end that have fallen outside the 3000 ms window.
The answer is the number of times left in the deque.

## Examples

### Example 1

```
Input:  RecentCounter(); ping(1), ping(100), ping(3001), ping(3002)
Output: 1, 2, 3, 3
```

**Explanation:** at `ping(3002)` the window is `[2, 3002]`, so time `1` is evicted from the left; `[100, 3001, 3002]` remain, giving 3.

## Hint

`append` each `t` at the right; `popleft` while the front is `< t - 3000`. The window size is `len(dq)`.
