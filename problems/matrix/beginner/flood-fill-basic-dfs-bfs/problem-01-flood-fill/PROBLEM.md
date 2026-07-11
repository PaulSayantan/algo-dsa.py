# Flood Fill

**Difficulty:** Easy

**Source:** LeetCode 733 — Flood Fill

## Description

You are given an image represented by an `m x n` integer grid `image`, where
`image[i][j]` represents the pixel value of the image.

You are also given three integers `sr`, `sc`, and `color`. You should perform a
**flood fill** on the image starting from the pixel `image[sr][sc]`.

To perform a flood fill:

1. Begin with the starting pixel and change its color to `color`.
2. Perform the same process for each pixel that is **directly adjacent**
   (up, down, left, or right — not diagonally) to the starting pixel and shares
   the **same color** as the starting pixel.
3. Keep repeating this process by checking neighboring pixels of the *updated*
   pixels and modifying their color if it matches the original color of the
   starting pixel.
4. The process stops when there are no more adjacent pixels of the original
   color to update.

Return the modified image after performing the flood fill.

## Constraints

- `m == image.length`
- `n == image[i].length`
- `1 <= m, n <= 50`
- `0 <= image[i][j], color < 2^16`
- `0 <= sr < m`
- `0 <= sc < n`

## Examples

### Example 1

```
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
```

**Explanation:** The starting pixel `(1, 1)` has color `1`. All pixels connected
to it 4-directionally by a path of `1`s are recolored to `2`: that region is the
top row, `(1,0)`, `(1,1)`, and `(2,0)`. The bottom-right pixel `(2,2)` is also a
`1` but is only diagonally adjacent to the region, so it is not connected and
keeps its value.

### Example 2

```
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
```

**Explanation:** The starting pixel already has color `0`, which equals the new
color. No pixel changes value. This is the key edge case: if you recurse without
checking that the color actually differs, you loop forever.

## Hint

Use **Flood Fill (basic DFS/BFS)**: remember the original color of the seed,
then traverse 4-directionally into neighbors that still hold that original color,
recoloring as you go. Guard against the case where the new color equals the old.
