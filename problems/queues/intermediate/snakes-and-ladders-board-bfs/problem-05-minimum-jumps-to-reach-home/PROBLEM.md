# Minimum Jumps to Reach Home

**Difficulty:** Medium

**Source:** LeetCode 1654 — Minimum Jumps to Reach Home

## Description

A bug lives on an infinite number line of squares (the board). It starts at square `0` and wants to reach its home at square `x`. On each move the bug jumps along the board according to these rules:

- It can jump exactly `a` squares **forward** (to `position + a`).
- It can jump exactly `b` squares **backward** (to `position - b`).
- It cannot jump backward twice in a row.
- It can never land on a `forbidden` square, and it can never land on a negative square.

Given `forbidden` (a list of forbidden squares), and the integers `a`, `b`, and `x`, return the minimum number of jumps needed for the bug to reach home at square `x`. If there is no possible sequence of jumps that lands the bug on square `x`, return `-1`.

Note: it is guaranteed that `0` is not forbidden, and the bug may jump forward beyond square `x` (there is no upper limit on the board) as long as it never lands on a forbidden square.

Constraints: `1 <= forbidden.length <= 1000`; `1 <= a, b, forbidden[i] <= 2000`; `0 <= x <= 2000`; all `forbidden[i]` are distinct; `x` is not forbidden.

## Examples

### Example 1

```
Input:  forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
```

**Explanation:** The bug jumps `0 -> 3 -> 6 -> 9` using three forward jumps of size `3`.

### Example 2

```
Input:  forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
Output: -1
```

**Explanation:** No sequence of jumps avoids the forbidden squares and lands on `11`.

### Example 3

```
Input:  forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
Output: 2
```

**Explanation:** The bug jumps forward `0 -> 16`, then backward `16 -> 7`.

## Hint

Each reachable square is a board node, but the "no two backward jumps in a row" rule means a node's state is `(position, came_here_by_backward_jump)`. BFS over these states from `(0, False)` gives the fewest jumps; cap the forward positions at something like `max(x, max(forbidden)) + a + b` so the search stays finite.
