# Design Hit Counter

**Difficulty:** Medium

**Source:** LeetCode 362 — Design Hit Counter

## Description

Design a `HitCounter` that counts requests received in the trailing 300-second window. Support two operations:

- `hit(timestamp)` records a hit at time `timestamp` (in seconds).
- `getHits(timestamp)` returns the number of hits in the past 300 seconds, i.e. every recorded hit whose time is strictly greater than `timestamp - 300`.

Calls are made with non-decreasing `timestamp` values, and all timestamps are positive integers.

## Examples

### Example 1

```
Input:  hit 1; hit 100; getHits 150; hit 200; hit 300; getHits 300; getHits 301
Output: 2, 4, 3
```

**Explanation:** At time `150` the hits at `1` and `100` are both inside the 300-second window, so `getHits(150) = 2`. After hits at `200` and `300`, `getHits(300)` counts all four (nothing has expired yet). By `getHits(301)` the hit at time `1` satisfies `1 <= 301 - 300`, so it has expired, leaving `3`.

## Hint

Enqueue each hit's timestamp; on every query, dequeue from the front while the oldest timestamp is `<= timestamp - 300`, then the queue length is the answer.
