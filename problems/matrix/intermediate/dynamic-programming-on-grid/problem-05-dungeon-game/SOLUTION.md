# Dungeon Game — Solution

## Brute Force

Try every right/down path. For a fixed path, the minimum initial health required is
determined by the deepest "health debt" reached along it. Concretely, if the running
sum of cell values (a prefix sum) hits a minimum of `S` at some point, the knight
needs at least `1 - S` starting health to stay positive there (and at least `1`
overall). Enumerate all paths and take the minimum over them.

- **Time:** `O(2^(m+n))` paths, each `O(m + n)` to evaluate — exponential.
- **Space:** `O(m + n)` recursion stack.

The trouble is that a **greedy forward** choice ("go to the healthier next room")
fails: a locally healthy step can lead to a fatal region later, and the amount of
health you can bank is capped by needing to stay alive *now*. The requirement
depends on the future, which motivates filling the table backward.

## Optimal Approach (Dynamic Programming on Grid, filled backward)

Let `dp[i][j]` be the **minimum health the knight must have upon entering room
`(i, j)`** in order to survive from there to the princess.

**Recurrence (process from bottom-right to top-left).** From `(i, j)` the knight
moves to `(i+1, j)` or `(i, j+1)`; he will pick whichever requires less health. The
health he needs *before* the current room's effect is applied is the successor
requirement minus this room's value; but he must also always have at least `1`:

```
need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
dp[i][j] = max(1, need)
```

**Base cases (the princess's room and its two borders).**
- `dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])`.
- Last row: `dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])` (can only go
  right).
- Last column: `dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])` (can only go
  down).

A clean way to encode all of this is to pad the table with a sentinel row and column
initialized to `+infinity`, except the two cells adjacent to the destination which
are `1`.

**Why it is correct.** Define the requirement *at entry* to a room as the minimum
health that keeps the knight positive through that room and all the way to the
princess. Entering room `(i, j)` with health `h`, after applying `dungeon[i][j]` he
has `h + dungeon[i][j]`, which must be both `>= 1` (survive this room) and `>=` the
entry requirement of the cheaper successor. Solving for `h` gives exactly the
recurrence. Because a room's requirement depends only on rooms *after* it, we fill
in reverse topological order (bottom-right to top-left), guaranteeing successors are
finalized first. The `max(1, ...)` enforces the "health never drops to 0 or below"
rule even in rooms full of orbs, since banked health cannot exceed what survival now
allows.

**Step by step (Example 1), computing `dp` bottom-up:**

```
dungeon              dp  (min health on entry)
-2  -3   3           7   5   2
-5 -10   1     ->    6  11   5
10  30  -5           1   1   6
```

- `dp[2][2] = max(1, 1 - (-5)) = 6`.
- `dp[2][1] = max(1, 6 - 30) = 1`, `dp[2][0] = max(1, 1 - 10) = 1`.
- `dp[1][2] = max(1, 6 - 1) = 5`, `dp[0][2] = max(1, 5 - 3) = 2`.
- `dp[1][1] = max(1, min(1, 5) - (-10)) = 11`,
  `dp[1][0] = max(1, min(11, 1) - (-5)) = 6`.
- `dp[0][1] = max(1, min(11, 2) - (-3)) = 5`,
  `dp[0][0] = max(1, min(6, 5) - (-2)) = 7`.

`dp[0][0] = 7`, matching the expected output.

**Reference implementation:**

```python
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        INF = float("inf")
        dp = [[INF] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1   # sentinels next to the princess
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(1, need)
        return dp[0][0]
```

- **Time:** `O(m * n)`.
- **Space:** `O(m * n)` (reducible to `O(n)` with a rolling row).

## Key Insights & Edge Cases

- **Fill backward, not forward.** A forward DP that tracks "max health so far" is
  wrong because the constraint (stay alive) points to the future; the requirement to
  survive the *rest* of the path is what composes cleanly.
- **The `max(1, ...)` clamp is essential.** Health must be at least `1` at every
  step, including when a room grants health — you cannot "store" surplus you never
  needed. Dropping the clamp lets negative requirements leak through and undercounts.
- **The princess's room counts.** If the destination itself is a demon, the knight
  still needs enough health to survive entering it.
- **All-positive dungeon.** The answer is `1` (e.g. `[[100]]` -> `1`): he only needs
  to enter alive.
- **Off-by-one on borders.** Using `+infinity` sentinels for the padding row/column
  (except the two cells adjacent to the goal) makes the single recurrence handle the
  last row and last column automatically.
