# Diagonal Traverse

**Difficulty:** Medium

**Source:** LeetCode 498 — "Diagonal Traverse"

## Description

Given an `m x n` matrix `mat`, return an array of all the elements of the array in a
**diagonal zig-zag order**.

Start at the top-left corner. Walk the first anti-diagonal going **up-right**, then
the next anti-diagonal going **down-left**, then up-right again, and so on, snaking
back and forth until you have covered the whole matrix. In other words, consecutive
anti-diagonals (grouped by `i + j`) are emitted in *alternating* directions.

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `-10^5 <= mat[i][j] <= 10^5`

## Examples

### Example 1

```
Input:  mat = [[1,2,3],
               [4,5,6],
               [7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

**Explanation:** Group by `i + j`:
`d0=[1]`, `d1=[2,4]`, `d2=[3,5,7]`, `d3=[6,8]`, `d4=[9]` (each listed top-to-bottom).
Emit even-indexed diagonals bottom-to-top (up-right) and odd-indexed diagonals
top-to-bottom (down-left):
- `d0` (up-right): `1`
- `d1` (down-left): `2, 4`
- `d2` (up-right): `7, 5, 3`
- `d3` (down-left): `6, 8`
- `d4` (up-right): `9`

Concatenated: `[1, 2, 4, 7, 5, 3, 6, 8, 9]`.

### Example 2

```
Input:  mat = [[1,2],
               [3,4]]
Output: [1,2,3,4]
```

**Explanation:** Diagonal `[1]` up, diagonal `[2,3]` down (read `2,3`), diagonal
`[4]` up. Concatenated: `[1, 2, 3, 4]`.

### Example 3

```
Input:  mat = [[1],
               [2],
               [3]]
Output: [1,2,3]
```

**Explanation:** A single column. Each anti-diagonal has one element, so the
direction flips have no visible effect; the output is the column top-to-bottom.

## Hint

Use **Diagonal / Zig-Zag Traversal**: group cells by `i + j`, but *reverse every
other diagonal* before emitting so the walk alternates between up-right and
down-left.
