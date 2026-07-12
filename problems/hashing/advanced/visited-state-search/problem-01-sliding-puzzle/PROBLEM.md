# Sliding Puzzle

**Difficulty:** Hard

**Source:** LeetCode 773 — Sliding Puzzle

## Description

On a 2x3 board holding tiles 1-5 and one empty square (0), a move swaps 0 with an adjacent tile. Given the start `board`, return the least number of moves to reach the solved state `[[1,2,3],[4,5,0]]`, or -1 if unsolvable. Serialize each board to a 6-character string and BFS, keeping visited strings in a set.

## Examples

### Example 1

```
Input:  board = [[1,2,3],[4,0,5]]
Output: 1
```

**Explanation:** Swap the 0 with the adjacent 5 once.

### Example 2

```
Input:  board = [[1,2,3],[5,4,0]]
Output: -1
```

**Explanation:** This configuration is unsolvable.

## Hint

Serialize the board to a string; BFS with an adjacency map of where 0 can move; visited set of strings.
