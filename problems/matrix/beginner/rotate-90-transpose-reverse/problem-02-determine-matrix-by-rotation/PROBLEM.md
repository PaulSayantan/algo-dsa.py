# Determine Whether Matrix Can Be Obtained By Rotation

**Difficulty:** Easy

**Source:** LeetCode 1886 — Determine Whether Matrix Can Be Obtained By Rotation

## Description

Given two `n × n` binary matrices `mat` and `target`, return `true` if it is
possible to make `mat` equal to `target` by rotating `mat` in **90-degree
increments**, or `false` otherwise.

You may rotate `mat` any number of times (0, 1, 2, or 3 quarter-turns). Each
rotation turns the whole matrix 90° clockwise. The question is whether any of
those four orientations of `mat` matches `target` exactly.

This is a direct application of the Rotate 90° technique: rotate `mat` up to
three times and compare against `target` after each turn (including the original
0-turn orientation).

## Constraints

- `n == mat.length == target.length`
- `n == mat[i].length == target[i].length`
- `1 <= n <= 10`
- `mat[i][j]` and `target[i][j]` are either `0` or `1`.

## Examples

### Example 1

```
Input:  mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
```

Explanation: Rotate `mat` 90° clockwise once. Transpose gives `[[0,1],[1,0]]`
(the two off-diagonal 1s are symmetric), and reversing each row gives
`[[1,0],[0,1]]`, which equals `target`.

### Example 2

```
Input:  mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
```

Explanation: The four rotations of `mat` are `[[0,1],[1,1]]`, `[[1,0],[1,1]]`,
`[[1,1],[1,0]]`, and `[[1,1],[0,1]]`. None of them equals `target`, and `mat`
even has a different number of 1s, so no rotation can match.

### Example 3

```
Input:  mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
```

Explanation: Two 90° clockwise rotations (a 180° turn) map `mat` onto `target`.

## Hint

Use Rotate 90° (transpose + reverse). Rotate `mat` in place up to three times,
comparing to `target` after 0, 1, 2, and 3 turns; return `true` on the first
match.
