# Spiral Matrix IV

**Difficulty:** Medium

**Source:** LeetCode 2326 — Spiral Matrix IV

## Description

You are given two integers `m` and `n`, which represent the dimensions of a
matrix, and the `head` of a singly linked list of integers.

Generate an `m x n` matrix that contains the integers from the linked list
presented in **clockwise spiral order** starting from the top-left cell. If
there are remaining empty cells (because the linked list has fewer than `m * n`
nodes), fill them with `-1`.

Return the generated matrix.

## Constraints

- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- The number of nodes in the list is in the range `[1, m * n]`.
- `0 <= Node.val <= 1000`

## Examples

### Example 1

```
Input:  m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[ 3, 0, 2, 6, 8],
         [ 5, 0,-1,-1, 1],
         [ 5, 2, 4, 9, 7]]
```

Explanation: The grid has `3 * 5 = 15` cells but the list holds only `13`
values. The values are written along the clockwise spiral — top row `3,0,2,6,8`,
right column `1,7`, bottom row `9,4,2,5`, left column `5`, then the inner cell
`0` — after which the list is exhausted. The two interior cells never reached
stay `-1`.

### Example 2

```
Input:  m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
```

Explanation: The single row is filled left-to-right with `0,1,2`; the one
leftover cell is padded with `-1`.

### Example 3

```
Input:  m = 2, n = 2, head = [1,2,3,4]
Output: [[1,2],
         [4,3]]
```

Explanation: `1,2` fill the top row; `3` goes to the bottom-right; `4` to the
bottom-left. All four cells are filled, so no `-1` padding is needed.

## Hint

Pre-fill the matrix with `-1`, then walk it as a clockwise **Spiral Traversal**,
advancing the linked-list pointer and stopping the writes once the list runs
out (the `-1` values remain).
