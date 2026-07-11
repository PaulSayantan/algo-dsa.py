# Largest Rectangle in Histogram

**Difficulty:** Medium / Hard

**Source:** LeetCode 84 — Largest Rectangle in Histogram

## Description

Given an array of integers `heights` representing the heights of the bars of a
histogram, where the width of each bar is `1`, return the **area of the largest
rectangle** that can be formed inside the histogram.

The rectangle must be axis-aligned: it spans a contiguous range of bars
`[l, r]`, and its height is limited by the *shortest* bar in that range. Its
area is therefore `min(heights[l..r]) * (r - l + 1)`.

This is the 1D subroutine that every "largest all-zero submatrix" solution calls
once per row, so mastering it first makes the 2D problems straightforward.

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

## Examples

### Example 1

```
Input:  heights = [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: The bars at indices 2 and 3 have heights 5 and 6. Using height 5
across those 2 bars gives a rectangle of area 5 * 2 = 10, which is the largest
possible.
```

### Example 2

```
Input:  heights = [2, 4]
Output: 4
Explanation: Either take the single bar of height 4 (area 4 * 1 = 4) or both
bars limited to height 2 (area 2 * 2 = 4). The maximum is 4.
```

### Example 3

```
Input:  heights = [2, 1, 2]
Output: 3
Explanation: The shortest bar (height 1) lets a rectangle span all 3 bars for
area 1 * 3 = 3, which beats any single bar (max height 2).
```

## Hint

Use the **Largest All-Zero Submatrix** core subroutine: keep a monotonic
(increasing) stack of bar indices. When a bar shorter than the stack top
arrives, pop and "close off" rectangles, computing each popped bar's maximal
width from the neighboring boundaries.
