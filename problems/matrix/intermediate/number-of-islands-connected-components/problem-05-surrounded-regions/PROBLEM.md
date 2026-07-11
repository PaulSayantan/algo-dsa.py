# Surrounded Regions

**Difficulty:** Medium

**Source:** LeetCode 130 (Surrounded Regions)

## Description

You are given an `m x n` matrix `board` containing the characters `'X'` and
`'O'`. Capture all regions that are **4-directionally surrounded** by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded
region. An `'O'` is **not** captured if it, or any `'O'` connected to it
4-directionally, lies on the **border** of the board (i.e. is connected to an
`'O'` that touches an edge).

Modify the board **in place**.

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

**Explanation:** The `'O'` region in the middle (cells `(1,1)`, `(1,2)`,
`(2,2)`) is completely enclosed by `'X'`, so it is captured and flipped to
`'X'`. The `'O'` at `(3,1)` sits on the bottom border, so it survives.

### Example 2

```
Input: board = [["X"]]
Output: [["X"]]
```

**Explanation:** There are no `'O'`s, so nothing changes.

### Example 3

```
Input: board = [
  ["O","O","O"],
  ["O","O","O"],
  ["O","O","O"]
]
Output: [
  ["O","O","O"],
  ["O","O","O"],
  ["O","O","O"]
]
```

**Explanation:** Every `'O'` is connected to the border, so none are captured
and the board is unchanged.

## Hint

Flip the usual **Connected Components** logic around: instead of finding
regions to capture, flood-fill from the *border* `'O'`s to mark every region
that must be **protected**. Whatever `'O'` remains unmarked is fully surrounded
and gets captured.
