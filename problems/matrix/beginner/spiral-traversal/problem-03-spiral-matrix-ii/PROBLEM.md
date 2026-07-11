# Spiral Matrix II

**Difficulty:** Medium

**Source:** LeetCode 59 — Spiral Matrix II

## Description

Given a positive integer `n`, generate an `n x n` matrix filled with the
elements from `1` to `n^2` placed in **clockwise spiral order**.

The number `1` goes in the top-left cell, and each subsequent integer is written
in the next cell along a clockwise spiral (right, down, left, up, spiraling
inward), so that `n^2` lands in the final cell reached.

## Constraints

- `1 <= n <= 20`

## Examples

### Example 1

```
Input:  n = 3
Output: [[1,2,3],
         [8,9,4],
         [7,6,5]]
```

Explanation: `1,2,3` fill the top row; `4,5` go down the right column; `6,7` go
left along the bottom row; `8` goes up the left column; `9` fills the center.

### Example 2

```
Input:  n = 1
Output: [[1]]
```

Explanation: The only cell receives `1`.

### Example 3

```
Input:  n = 4
Output: [[ 1, 2, 3, 4],
         [12,13,14, 5],
         [11,16,15, 6],
         [10, 9, 8, 7]]
```

Explanation: `1..4` across the top; `5..7` down the right; `8..10` back along
the bottom; `11..12` up the left; then the inner `2 x 2` ring `13,14,15,16`
spirals the same way.

## Hint

Instead of reading cells, you **write** into them. Walk the same four shrinking
boundaries as a clockwise **Spiral Traversal**, assigning an incrementing
counter as you go.
