# Surrounded Regions

**Difficulty:** Medium

**Source:** LeetCode 130 — Surrounded Regions

## Description

You are given an `m x n` matrix `board` containing the characters `'X'` and
`'O'`. **Capture** all regions that are 4-directionally surrounded by `'X'`.

A region is **captured** by flipping all `'O'`s into `'X'`s in that surrounded
region.

A region of `'O'`s is surrounded if **none** of its cells lie on the border of
the board — equivalently, an `'O'` is *safe* (never captured) if it is connected
4-directionally, through other `'O'`s, to an `'O'` on the border.

Modify the board **in place** and return nothing.

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`.

## Examples

### Example 1

```
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
```

**Explanation:** The `'O'`s at `(1,1)`, `(1,2)`, and `(2,2)` form a region with
no cell on the border, so they are surrounded and flipped to `'X'`. The `'O'` at
`(3,1)` is on the bottom border, so it is safe and stays `'O'`.

### Example 2

```
Input: board = [["X"]]
Output: [["X"]]
```

**Explanation:** There are no `'O'`s to capture, so the board is unchanged.

## Hint

Use **Flood Fill (basic DFS/BFS)**: flood from every `'O'` on the border to mark
the safe (unsurrounded) `'O'`s. Then flip every unmarked `'O'` to `'X'` and
restore the marked ones.
