# Snakes and Ladders

**Difficulty:** Medium

**Source:** LeetCode 909 — Snakes and Ladders

## Description

You are given an `n x n` integer matrix `board` numbered in a Boustrophedon (boustrophedon / snake) style: square `1` is the bottom-left cell, numbering proceeds left-to-right on the bottom row, then the direction alternates each row moving up, ending at square `n*n`.

Starting at square `1`, each move you roll a die and advance `1..6` squares (never past `n*n`). If the destination square holds a value other than `-1`, you must immediately travel to that value (a snake or a ladder); you take at most one snake/ladder per move. Return the least number of moves to reach square `n*n`, or `-1` if unreachable.

Constraints: `2 <= n <= 20`; each cell is `-1` or a valid square in `[1, n*n]`.

## Examples

### Example 1

```
Input:  board=[[-1,-1,-1,-1,-1,-1],
               [-1,-1,-1,-1,-1,-1],
               [-1,-1,-1,-1,-1,-1],
               [-1,35,-1,-1,13,-1],
               [-1,-1,-1,-1,-1,-1],
               [-1,15,-1,-1,-1,-1]]
Output: 4
```

**Explanation:** Move to square 2 (ladder to 15), then to 17, then to 13 (ladder to 35), then to 35 -> 36 reachable; the shortest sequence takes 4 moves.

## Hint

Squares `1..n*n` are states; from square `s` the die gives neighbors `s+1..s+6`, redirected by a snake/ladder. BFS gives the fewest dice rolls.
