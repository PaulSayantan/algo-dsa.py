# Snakes and Ladders

**Difficulty:** Medium

**Source:** LeetCode 909 — Snakes and Ladders

## Description

Given an `n × n` boustrophedon (boustrophedon = snake-order) board where `board[r][c] = -1` is a normal square and otherwise gives the destination square of a snake/ladder, return the least number of dice moves to reach square `n²` from square `1`, or `-1` if impossible.

## Examples

### Example 1

```
Input:  6x6 board (see LeetCode 909)
Output: 4
```

## Hint

Map the snake-order numbering to (row,col); BFS over squares, each move rolling 1..6 with redirection.
