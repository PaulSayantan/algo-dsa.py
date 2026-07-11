# Largest Rectangle in Histogram

**Difficulty:** Hard

**Source:** LeetCode 84 — Largest Rectangle in Histogram

## Description

Given an array `heights` representing the heights of bars in a histogram where each bar has
width `1`, return the **area of the largest rectangle** that can be formed within the
histogram.

The rectangle must be axis-aligned and its height is limited by the shortest bar it spans;
it may span any contiguous range of bars.

This is the **core 1-D subroutine** behind the 2-D Maximal Rectangle problem: once you can
solve a histogram in linear time, you can solve maximal-rectangle-in-a-binary-matrix by
treating each row as the base of a histogram.

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

## Examples

### Example 1

```
Input: heights = [2,1,5,6,2,3]
Output: 10
```

**Explanation:** The bars at indices 2 and 3 have heights 5 and 6. The largest rectangle
spans those two bars at height 5, giving area `5 * 2 = 10`.

### Example 2

```
Input: heights = [2,4]
Output: 4
```

**Explanation:** Taking just the second bar gives `4 * 1 = 4`; taking both bars is limited to
height 2 for area `2 * 2 = 4`. The maximum is `4`.

### Example 3

```
Input: heights = [6,2,5,4,5,1,6]
Output: 12
```

**Explanation:** Bars at indices 2, 3, 4 have heights 5, 4, 5. Spanning all three at the
limiting height 4 gives `4 * 3 = 12`, the largest possible.

## Hint

Use a **monotonic (increasing) stack**. For each bar, when you pop a taller bar you have just
found the full horizontal span over which that bar is the shortest, which is exactly the
width of the largest rectangle of that bar's height. This is the engine used by the
**Maximal Rectangle** technique.
