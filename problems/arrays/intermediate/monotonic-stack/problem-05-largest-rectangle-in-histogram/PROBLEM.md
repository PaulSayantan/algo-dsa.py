# Largest Rectangle in Histogram

**Difficulty:** Hard

**Source:** LeetCode 84 — Largest Rectangle in Histogram

## Description

Given an array of integers `heights` representing the histogram's bar heights
where the width of each bar is `1`, return the **area of the largest rectangle**
that can be formed within the bounds of the histogram.

The rectangle must be axis-aligned and its height is limited by the shortest bar
it spans; it can span any contiguous range of bars.

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

## Examples

### Example 1

```
Input:  heights = [2, 1, 5, 6, 2, 3]
Output: 10
```

**Explanation:** The largest rectangle spans bars at indices 2 and 3 (heights
`5` and `6`). Its height is `min(5, 6) = 5` and its width is `2`, giving an area
of `5 * 2 = 10`.

### Example 2

```
Input:  heights = [2, 4]
Output: 4
```

**Explanation:** Either take the single bar of height `4` (area `4`), or span
both bars at height `min(2, 4) = 2` for width `2` (area `4`). The maximum is `4`.

### Example 3

```
Input:  heights = [6, 2, 5, 4, 5, 1, 6]
Output: 12
```

**Explanation:** The bars at indices 2, 3, 4 have heights `5, 4, 5`. Spanning all
three at height `min(5, 4, 5) = 4` gives width `3` and area `4 * 3 = 12`, which
is the largest possible.

## Hint

For each bar, the widest rectangle of that bar's height extends until the first
**strictly shorter** bar on each side. A **Monotonic Stack** of indices with
increasing heights finds both boundaries in a single `O(n)` sweep; a sentinel
(or a final flush) handles bars still on the stack at the end.
