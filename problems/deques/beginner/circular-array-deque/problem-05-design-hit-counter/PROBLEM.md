# Design Hit Counter

**Difficulty:** Easy

**Source:** LeetCode 362 — Design Hit Counter

## Description

Design a hit counter that records hits and reports how many happened in the past 5 minutes (300 seconds). Timestamps are given in seconds and arrive in monotonically non-decreasing order. Implement:

- `MyHitCounter()` — initialize the counter.
- `hit(timestamp)` — record a hit at `timestamp`.
- `getHits(timestamp)` — return the number of hits in the window `(timestamp - 300, timestamp]`.

Use O(1) extra time and O(300) space per call — do not store one entry per hit.

## Examples

### Example 1

```
Input:  MyHitCounter(); hit(1); hit(2); hit(3); getHits(4); hit(300); getHits(300); getHits(301)
Output: [3, 4, 3]
```

**Explanation:** At time 4 the hits at 1, 2, 3 are all within the last 300 seconds, so `getHits(4) = 3`. After `hit(300)`, `getHits(300)` counts 1, 2, 3, 300 → 4. At time 301 the window is `(1, 301]`, so the hit at second 1 falls off, leaving 3.

## Hint

Keep two fixed arrays of length 300 indexed by `timestamp % 300`: one stores the bucket's timestamp, the other its hit count. On `hit`, if the bucket holds a stale timestamp overwrite it and reset the count to 1; on `getHits`, sum the counts of buckets whose stored timestamp is still inside the window.
