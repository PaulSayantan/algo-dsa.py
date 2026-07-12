# Sliding Puzzle

**Difficulty:** Medium

**Source:** LeetCode 773 — Sliding Puzzle

## Description

On a 2x3 board, tiles are labelled `1`-`5` plus one empty square shown as `0`. A move swaps `0` with a horizontally or vertically adjacent tile. Given the starting `board`, return the least number of moves to reach the solved state `[[1, 2, 3], [4, 5, 0]]`, or `-1` if it is unsolvable.

## Examples

### Example 1

```
Input:  board = [[1, 2, 3], [4, 0, 5]]
Output: 1
```

**Explanation:** Swap `0` with the `5` to its right to reach `[[1, 2, 3], [4, 5, 0]]`.

### Example 2

```
Input:  board = [[1, 2, 3], [5, 4, 0]]
Output: -1
```

**Explanation:** No sequence of slides solves this configuration.

## Hint

Flatten the board to a 6-tuple and BFS from both the start state and the solved state, expanding the smaller frontier; a state seen by both searches means they met.
