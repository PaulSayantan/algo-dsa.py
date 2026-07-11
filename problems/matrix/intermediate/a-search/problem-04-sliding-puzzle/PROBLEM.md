# Sliding Puzzle

**Difficulty:** Hard

**Source:** LeetCode 773 — Sliding Puzzle

## Description

On a `2 x 3` board there are five tiles labeled `1` through `5` and one empty square
represented by `0`. A **move** consists of choosing a tile that is 4-directionally
adjacent to the empty square `0` and swapping it with `0`.

The board is **solved** when it equals:

```
[[1, 2, 3],
 [4, 5, 0]]
```

Given the puzzle board `board`, return the **least number of moves** required to reach
the solved state. If it is impossible, return `-1`.

## Constraints

- `board.length == 2`
- `board[i].length == 3`
- `0 <= board[i][j] <= 5`
- Each value `0..5` appears exactly once in `board`.

## Examples

### Example 1

```
Input: board = [[1,2,3],
                [4,0,5]]
Output: 1
```

**Explanation:** Swap the `0` with the `5` to its right to obtain
`[[1,2,3],[4,5,0]]` in a single move.

### Example 2

```
Input: board = [[1,2,3],
                [5,4,0]]
Output: -1
```

**Explanation:** No sequence of legal slides can solve this configuration; the
permutation has the wrong parity, so the answer is `-1`.

### Example 3

```
Input: board = [[4,1,2],
                [5,0,3]]
Output: 5
```

**Explanation:** One optimal solution takes `5` moves, e.g. sliding tiles so the board
passes through `[[4,1,2],[0,5,3]] -> [[0,1,2],[4,5,3]] -> [[1,0,2],[4,5,3]] ->
[[1,2,0],[4,5,3]] -> [[1,2,3],[4,5,0]]`.

## Hint

Treat each board configuration as a **state** (there are only `6! = 720` of them) and
moves as edges of cost `1`. Use **A\* Search**: order states by `g + h`, where `g` is
moves made and `h` is the **sum of Manhattan distances** of each tile from its goal
position (ignoring the blank). That heuristic never overestimates, so A\* returns the
optimal move count while expanding far fewer states than blind BFS.
