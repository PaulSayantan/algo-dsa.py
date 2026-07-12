# Throttling Gateway

**Difficulty:** Medium

**Source:** Classic — HackerRank "Throttling Gateway"

## Description

A gateway receives `requestTime`, a chronologically sorted list of request arrival times in **seconds** (non-decreasing, 1 or more). The gateway enforces three rate limits and **drops** any request that would exceed any of them. Every request — whether accepted or dropped — still counts toward the limits.

A request arriving at time `t` is dropped if, including itself:

- more than `3` requests share the same second `t`, or
- more than `20` requests fall in the trailing 10-second window (times `> t - 10`), or
- more than `60` requests fall in the trailing 60-second window (times `> t - 60`).

Return the total number of dropped requests.

## Examples

### Example 1

```
Input:  requestTime = [1, 1, 1, 1, 2]
Output: 1
```

**Explanation:** The first three requests at second `1` are fine, but the fourth is the 4th in the same second, so it is dropped. The request at second `2` starts a fresh 1-second window and is accepted. One request is dropped.

## Hint

Enqueue every timestamp into per-window queues; on each arrival, pop timestamps that have left each window, then drop the request if any window's queue is now over its limit.
