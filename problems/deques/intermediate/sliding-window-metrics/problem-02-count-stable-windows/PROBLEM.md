# Count Stable Windows

**Difficulty:** Medium

**Source:** Classic — count fixed-size windows with bounded range

## Description

Given an integer array `nums`, a window size `k`, and a `threshold`, return how many contiguous windows of size `k` are **stable** — that is, the window's range (`max - min`) is `<= threshold`. Track the window max and min with two monotonic deques and test each full window's range.

## Examples

### Example 1

```
Input:  nums = [1,1,1,1], k = 2, threshold = 0
Output: 3
```

**Explanation:** All three windows have range 0 <= 0.

## Hint

Same twin-deque window as the range problem, but increment a counter when max - min <= threshold.
