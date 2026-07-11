# Minimum Knight Moves

**Difficulty:** Medium

**Source:** LeetCode 1197 — Minimum Knight Moves

## Description

In an **infinite** chessboard with coordinates from `-∞` to `+∞`, you have a knight at
square `(0, 0)`. A knight has 8 possible moves, each move being two squares in a
cardinal direction and then one square orthogonal to that (an "L" shape).

Return the **minimum number of steps** needed to move the knight from `(0, 0)` to the
target square `(x, y)`. It is guaranteed the answer exists.

The eight knight moves from `(r, c)` go to:
`(r±1, c±2)` and `(r±2, c±1)`.

## Constraints

- `-300 <= x, y <= 300`
- `0 <= |x| + |y| <= 300`

## Examples

### Example 1

```
Input: x = 2, y = 1
Output: 1
```

**Explanation:** The knight moves directly from `(0, 0)` to `(2, 1)` in a single L-shaped
step.

### Example 2

```
Input: x = 5, y = 5
Output: 4
```

**Explanation:** One optimal sequence is
`(0,0) -> (2,1) -> (4,2) -> (3,4) -> (5,5)`, which reaches the target in `4` moves.
No 3-move sequence can cover the distance.

### Example 3

```
Input: x = 0, y = 0
Output: 0
```

**Explanation:** The knight already stands on the target, so zero moves are required.

## Hint

The board is infinite, so an undirected BFS can fan out into an enormous disk before it
hits the target. Steer the search with **A\* Search**: order the priority queue by
`g + h`, where `g` is the moves taken so far and `h(r, c)` is an admissible lower bound
on the knight moves still needed to reach `(x, y)`. A knight covers at most 3 units of
Manhattan distance and at most 2 units along either axis per move, giving
`h = max(ceil((|dx| + |dy|) / 3), ceil(max(|dx|, |dy|) / 2))`.
