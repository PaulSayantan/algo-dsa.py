# Number of Recent Calls

**Difficulty:** Easy

**Source:** LeetCode 933 — Number of Recent Calls

## Description

Implement the `RecentCounter` class, which counts the number of recent requests within a time window.

- `RecentCounter()` initializes the counter with zero requests.
- `ping(t)` records a new request at time `t` (in milliseconds) and returns the number of requests that happened in the inclusive range `[t - 3000, t]`.

It is guaranteed that every call to `ping` uses a strictly larger value of `t` than the previous call.

## Examples

### Example 1

```
Input:
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output:
[null, 1, 2, 3, 3]
```

**Explanation:** `ping(1)` -> `[1]` gives 1. `ping(100)` -> `[1, 100]` gives 2. `ping(3001)` -> `[1, 100, 3001]` gives 3 (1 is still within `[1, 3001]`). `ping(3002)` -> `1` falls outside `[2, 3002]`, leaving `[100, 3001, 3002]`, so 3.

## Hint

Keep the request times in a list ordered by arrival; enqueue `t` at the rear, then pop stale times from the front (index 0) while they are less than `t - 3000`.
