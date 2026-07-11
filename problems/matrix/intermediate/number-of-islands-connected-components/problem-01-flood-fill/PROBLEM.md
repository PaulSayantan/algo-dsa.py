# Flood Fill

**Difficulty:** Easy

**Source:** LeetCode 733 (Flood Fill)

## Description

You are given an image represented by an `m x n` integer grid `image`, where
`image[i][j]` is the integer pixel value. You are also given three integers
`sr`, `sc`, and `color`.

Perform a **flood fill** starting from the pixel at position `(sr, sc)`:

1. Begin at the starting pixel and note its original color.
2. Paint the starting pixel, and every pixel that is connected to it
   **4-directionally** (up, down, left, right) *and* shares the same original
   color, with the new `color`. This connection continues transitively: any
   pixel connected to an already-painted pixel by these rules is also painted.

Return the modified image after the fill completes.

Note: if the starting pixel already has the target `color`, the image is
returned unchanged (be careful not to loop forever in that case).

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
Input:  image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
```

**Explanation:** Starting from pixel `(1,1)` whose original color is `1`, we
paint every 4-directionally connected pixel of color `1`. The bottom-right
pixel `(2,2)` is color `1` but is only diagonally adjacent to the region, so it
is *not* reached and stays `1`.

### Example 2

```
Input:  image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
```

**Explanation:** The starting pixel already has color `0`, which equals the new
color. Nothing changes, and the algorithm must terminate without revisiting
pixels endlessly.

### Example 3

```
Input:  image = [[0,0,0],[0,1,0]], sr = 1, sc = 1, color = 2
Output: [[0,0,0],[0,2,0]]
```

**Explanation:** The pixel `(1,1)` has original color `1`, and none of its
4-directional neighbours share that color, so only that single pixel is
repainted to `2`.

## Hint

This is the simplest instance of **Number of Islands / Connected Components**:
flood a single region from a seed cell using DFS or BFS, treating "same
original color" as the edge condition. Watch the case where the new color
equals the old one.
