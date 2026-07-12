# Design Hit Counter

**Difficulty:** Medium

**Source:** LeetCode 362 — Design Hit Counter

## Description

Design a hit counter that counts hits received in the past 5 minutes (300 seconds). Support `hit(timestamp)` records a hit at the given time (in seconds), and `getHits(timestamp)` returns the number of hits in the past 300 seconds, i.e. every hit with time strictly greater than `timestamp - 300`. Calls are made with non-decreasing `timestamp` values. Timestamps are positive integers.

## Examples

### Example 1

```
Input:  hit 1; hit 2; hit 3; getHits 4; hit 300; getHits 300; getHits 301
Output: 3, 4, 3
```

**Explanation:** At time `4` the three early hits are all within 300s. After a hit at `300`, `getHits(300)` counts all four; by `getHits(301)` the hit at time `1` (`1 <= 301 - 300`) has expired, leaving `3`.

## Hint

Enqueue each timestamp into a two-stack FIFO queue; on a query, dequeue from the front while the oldest timestamp is `<= timestamp - 300`, then the queue size is the answer.
