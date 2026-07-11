# Flood Fill

**Difficulty:** Easy

**Source:** LeetCode 733 — Flood Fill

## Description

You are given an image represented by an `m x n` integer grid `image`, where
`image[i][j]` is the pixel value (an integer). You are also given three
integers `sr`, `sc`, and `color`.

Perform a **flood fill** starting from the pixel `image[sr][sc]`:

1. Begin at the starting pixel and record its original color.
2. Consider the starting pixel and any pixel connected **4-directionally**
   (up, down, left, right) to it that has the **same original color**, and any
   pixel connected 4-directionally to those, and so on.
3. Replace the color of all such connected pixels with `color`.

Return the modified image after the flood fill.

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
Input:  image = [[1,1,1],
                 [1,1,0],
                 [1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],
         [2,2,0],
         [2,0,1]]
```

**Explanation:** The starting pixel `(1,1)` has color `1`. Every pixel reachable
from it through same-colored (`1`) 4-directional neighbors is recolored to `2`.
The bottom-right pixel `(2,2)` also has value `1`, but it is separated from the
region by `0`s, so it is not connected and stays `1`.

### Example 2

```
Input:  image = [[0,0,0],
                 [0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],
         [0,0,0]]
```

**Explanation:** The starting pixel already has color `0`, which equals the fill
color, so no pixel changes. (This is the classic edge case that would cause an
infinite loop if you do not guard against it.)

## Hint

Model the pixels as graph nodes connected to their same-colored neighbors and
run a **Grid DFS / BFS** from the start pixel, recoloring as you go.
