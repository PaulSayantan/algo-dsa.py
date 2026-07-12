# Find Median from Data Stream

**Difficulty:** Hard

**Source:** LeetCode 295 — Find Median from Data Stream

## Description

Design a data structure that supports `addNum(x)` to ingest integers from a stream and `findMedian()` to return the median of all elements so far (as a float).

## Examples

### Example 1

```
Input:  add 1,2; median; add 3; median
Output: 1.5, 2.0
```

## Hint

Max-heap for the lower half, min-heap for the upper half; rebalance so sizes differ by at most 1.
