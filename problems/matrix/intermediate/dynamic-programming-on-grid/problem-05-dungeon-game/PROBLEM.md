# Dungeon Game

**Difficulty:** Hard

**Source:** LeetCode 174 — Dungeon Game

## Description

The demons had captured the princess and imprisoned her in the bottom-right corner
of a `dungeon`. The `dungeon` consists of `m x n` rooms laid out in a 2D grid. Our
valiant knight was initially positioned in the top-left room and must fight his way
through `dungeon` to rescue the princess.

The knight has an initial health point represented by a positive integer. **If at
any point his health point drops to `0` or below, he dies immediately.**

Some of the rooms are guarded by demons (represented by negative integers), so the
knight loses health upon entering these rooms; other rooms are either empty
(represented as `0`) or contain magic orbs that increase the knight's health
(represented by positive integers).

To reach the princess as fast as possible, the knight decides to move only
**rightward or downward** in each step.

Return *the knight's minimum initial health so that he can rescue the princess*.

Note that any room can contain threats or power-ups, even the first room the knight
enters and the bottom-right room where the princess is imprisoned.

## Constraints

- `m == dungeon.length`
- `n == dungeon[i].length`
- `1 <= m, n <= 200`
- `-1000 <= dungeon[i][j] <= 1000`

## Examples

### Example 1

```
Input: dungeon = [[-2,-3, 3],
                  [-5,-10, 1],
                  [10, 30,-5]]
Output: 7
```

**Explanation:** With an initial health of `7`, the knight can follow the path
Right -> Right -> Down -> Down. Health after each room stays at least `1`:
`7 -> 5 -> 2 -> 5 -> 6 -> 1`. Any starting health of `6` or less causes death on
some room along every path.

### Example 2

```
Input: dungeon = [[0]]
Output: 1
```

**Explanation:** The single room is empty, so the knight needs at least `1` health
to be alive when he arrives (and stays at `1`).

### Example 3

```
Input: dungeon = [[100]]
Output: 1
```

**Explanation:** Even though the room grants `+100` health, the knight only needs to
*enter* alive. Starting with `1` health he survives (and ends with `101`), so the
minimum initial health is `1`.

## Hint

Use **Dynamic Programming on Grid**, but fill the table from the **bottom-right
corner back to the top-left**. Let `dp[i][j]` be the minimum health needed *upon
entering* cell `(i, j)` to survive the rest of the journey; the forward direction
does not work because the requirement depends on the future, not the past.
