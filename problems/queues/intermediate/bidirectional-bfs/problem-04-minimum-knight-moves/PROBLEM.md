# Minimum Knight Moves

**Difficulty:** Medium

**Source:** LeetCode 1197 — Minimum Knight Moves

## Description

On an infinite chessboard, a knight starts at `(0, 0)`. A knight moves in an L-shape: two squares along one axis and one square along the other (8 possible moves). Given a target square `(x, y)`, return the minimum number of moves needed for the knight to reach `(x, y)`. A solution always exists. `x` and `y` may be negative.

## Examples

### Example 1

```
Input:  x = 2, y = 1
Output: 1
```

**Explanation:** `(0, 0) -> (2, 1)` is a single knight move.

### Example 2

```
Input:  x = 5, y = 5
Output: 4
```

**Explanation:** Four knight moves suffice, e.g. `(0,0) -> (2,1) -> (4,2) -> (3,4) -> (5,5)`.

## Hint

By symmetry fold the target into the first quadrant, then run BFS from both `(0, 0)` and the target, expanding the smaller frontier until they meet.
