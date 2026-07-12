# Number of Recent Calls

**Difficulty:** Easy

**Source:** LeetCode 933 — Number of Recent Calls

## Description

Implement `RecentCounter`, which counts recent requests within a sliding time window.

- `RecentCounter()` initializes the counter with zero requests.
- `ping(t)` records a new request at time `t` (in milliseconds) and returns the number of requests that happened in the inclusive range `[t - 3000, t]`.

It is guaranteed that every call to `ping` uses a strictly larger `t` than the previous call. Back the counter with a singly linked list queue: `enqueue` each new timestamp at the tail, then `dequeue` stale timestamps from the head while they fall before `t - 3000`. The remaining size is the answer.

## Examples

### Example 1

```
Input:
  ["RecentCounter", "ping", "ping", "ping", "ping"]
  [[], [1], [100], [3001], [3002]]
Output:
  [null, 1, 2, 3, 3]
```

**Explanation:** At `ping(3002)` the window is `[2, 3002]`, so the timestamp `1` is dropped from the head, leaving `100, 3001, 3002` — three requests.

## Hint

Enqueue each timestamp at the tail and dequeue from the head while `head < t - 3000`; the queue size is the count.
