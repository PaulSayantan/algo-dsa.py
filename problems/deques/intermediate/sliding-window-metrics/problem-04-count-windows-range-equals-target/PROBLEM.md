# Count Windows With Range Equal to Target

**Difficulty:** Medium

**Source:** Classic — count fixed-size windows with an exact range

## Description

Given an integer array `nums`, a window size `k`, and an integer `target`, return how many contiguous windows of size `k` have a **range exactly equal to** `target` — that is, `max - min == target`.

Unlike a bounded-threshold count (range `<= threshold`), this asks for an exact match, so you must read the true per-window range and compare it for equality. Track the window max with a decreasing monotonic deque and the window min with an increasing one, then test each full window's range.

Constraints: `1 <= k <= len(nums)`, `len(nums) <= 10^5`, `target >= 0`.

## Examples

### Example 1

```
Input:  nums = [4,2,7,1,1,2], k = 2, target = 3
Output: 0
```

**Explanation:** Windows `[4,2],[2,7],[7,1],[1,1],[1,2]` have ranges 2,5,6,0,1 — none equals 3.

### Example 2

```
Input:  nums = [5,3,5,3,5], k = 2, target = 2
Output: 4
```

**Explanation:** All four windows are `[5,3]` or `[3,5]`, each with range 2, so all four match.

## Hint

Same twin-deque window as the range problem, but increment the counter only when `max - min == target`.
