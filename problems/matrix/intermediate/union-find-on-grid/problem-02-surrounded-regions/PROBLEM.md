# Surrounded Regions

**Difficulty:** Medium

**Source:** LeetCode 130 (Surrounded Regions)

## Description

You are given an `m x n` matrix `board` containing the characters `'X'` and `'O'`. Capture all
regions that are **4-directionally surrounded** by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s **in that surrounded region**. An `'O'`
is safe (not captured) if and only if it is connected — through a chain of 4-directionally
adjacent `'O'`s — to an `'O'` lying on the **border** of the board. Any `'O'` region that
cannot reach the border is fully enclosed and must be flipped to `'X'`.

Modify the board **in place**.

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`.

## Examples

### Example 1

```
Input:
board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output:
[
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
```

**Explanation:** The three `'O'`s in the middle (rows 1-2) are completely surrounded by `'X'`,
so they are captured and become `'X'`. The `'O'` at row 3, column 1 sits on the bottom border,
so it (and anything connected to it) is safe and stays `'O'`.

### Example 2

```
Input:
board = [
  ["O","X"],
  ["X","O"]
]
Output:
[
  ["O","X"],
  ["X","O"]
]
```

**Explanation:** Both `'O'`s lie on the border, so neither is surrounded. Nothing changes.

## Hint

Create one extra **virtual node** representing "the border / the outside." Union every border
`'O'` to it and union adjacent `'O'`s together with **Union–Find on Grid**. Any `'O'` whose
root is not the virtual node is enclosed and gets flipped.
