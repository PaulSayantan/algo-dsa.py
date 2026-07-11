# Largest Rectangle in Histogram

**Difficulty:** Hard

**Source:** LeetCode 84 — Largest Rectangle in Histogram

## Description

Given an array of integers `heights` representing the heights of bars in a histogram, where
the width of each bar is `1`, return the **area of the largest rectangle** that can be formed
within the bounds of the histogram.

The rectangle must be axis-aligned and contiguous: it spans a range of consecutive bars and
its height is limited by the shortest bar in that range.

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

## Examples

### Example 1

```
Input:  heights = [2, 1, 5, 6, 2, 3]
Output: 10
```

**Explanation:** The largest rectangle spans bars at indices 2 and 3 (heights 5 and 6),
limited to height 5 over width 2 → area `5 * 2 = 10`.

### Example 2

```
Input:  heights = [2, 4]
Output: 4
```

**Explanation:** Two candidates matter: the bar of height 4 alone (area `4 * 1 = 4`), or both
bars limited to height 2 (area `2 * 2 = 4`). The maximum is `4`.

## Hint

Use a **Monotonic Stack / Queue** (an increasing stack of indices). Each bar's maximal
rectangle extends left to the previous shorter bar and right to the next shorter bar; the
stack finds both boundaries in a single pass.
