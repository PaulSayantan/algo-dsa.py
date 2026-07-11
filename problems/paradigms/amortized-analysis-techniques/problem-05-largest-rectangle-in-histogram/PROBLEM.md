# Largest Rectangle in Histogram

**Difficulty:** Hard

**Source:** LeetCode 84 — Largest Rectangle in Histogram

## Description

Given an array of integers `heights` representing the histogram's bar heights where the
width of each bar is `1`, return the **area of the largest rectangle** in the histogram.

The rectangle must be axis-aligned and must fit entirely under the bars: its height is
limited by the shortest bar it spans, and its width is the number of consecutive bars it
covers.

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

## Examples

### Example 1

```
Input:  heights = [2, 1, 5, 6, 2, 3]
Output: 10
```

Explanation: The largest rectangle spans bars at indices 2 and 3 (heights 5 and 6). Its
height is limited to `min(5, 6) = 5` and its width is `2`, giving area `5 * 2 = 10`.

### Example 2

```
Input:  heights = [2, 4]
Output: 4
```

Explanation: The best rectangle uses only the second bar: height `4`, width `1`, area
`4`. Using both bars would cap the height at `min(2, 4) = 2` for area `2 * 2 = 4`, which
ties but does not beat it.

### Example 3

```
Input:  heights = [6, 2, 5, 4, 5, 1, 6]
Output: 12
```

Explanation: The largest rectangle spans indices 2..4 (heights 5, 4, 5). Its height is
`min(5, 4, 5) = 4` and its width is `3`, giving area `4 * 3 = 12`.

## Hint

Use **Amortized Analysis Techniques** with a **monotonic increasing stack** of bar
indices. For each bar you pop every taller bar on the stack and, at the moment a bar is
popped, you finally know both its left and right boundaries, so you can compute the
largest rectangle with that bar as the limiting height. Each bar is pushed and popped
exactly once, so the whole scan is O(n).
