# Minimum Knight Moves

**Difficulty:** Medium

**Source:** LeetCode 1197 — Minimum Knight Moves

## Description

On an **infinite** chessboard, a knight starts at `(0, 0)`. A knight move changes the position by `(±1, ±2)` or `(±2, ±1)`. Given a target square `(x, y)`, return the minimum number of moves needed to reach `(x, y)` from the origin.

The answer always exists. Constraints: `-300 <= x, y <= 300`.

## Examples

### Example 1

```
Input:  x = 2, y = 1
Output: 1
```

**Explanation:** A single knight move reaches `(2, 1)`.

### Example 2

```
Input:  x = 5, y = 5
Output: 4
```

**Explanation:** Four knight moves is the fewest that lands on `(5, 5)`.

## Hint

BFS over knight moves (unweighted, so the Lee shortest-path idea applies); exploit the board's symmetry by folding the target into one quadrant and bounding the search a little past `(x, y)`.
