# Unique Paths III — Solution

## Brute Force

Enumerate every simple path from the start cell and, for each one that reaches the end cell,
check whether it happened to cover all non-obstacle squares. Without tracking how many
squares remain, you would explore many partial paths that can never be valid, and you would
only discover failure at the very end.

- **Time:** `O(4^(m*n))` — from each cell up to 4 moves, over up to `m * n` cells.
- **Space:** `O(m * n)` for the recursion stack / visited tracking.

Because `m * n <= 20`, an exponential search is acceptable here, but the two prunings below
make it fast in practice.

## Optimal Approach (Backtracking on Grid)

This is a **Hamiltonian-path counting** problem restricted to walkable cells. The key extra
piece of state versus plain Word Search is a **counter of remaining non-obstacle squares**:
a path is only valid when we arrive at the end cell *and* that counter has been fully
consumed.

**Algorithm**

1. Scan the grid once to find the start `(sr, sc)` and count `empty` = number of squares
   with value `0`. The total number of squares the walk must visit is `empty + 1` (all the
   empties plus the start; the end cell is counted as the final step).
2. Run `dfs(r, c, remaining)` where `remaining` is how many squares are still left to visit
   *including* the current one:
   - If `(r, c)` is out of bounds or an obstacle (`-1`) or already visited, return `0`.
   - If `grid[r][c] == 2` (end): return `1` if `remaining == 1` (this end cell is the last
     unvisited square), else `0`.
   - **Choose:** mark `(r, c)` visited (e.g., temporarily set it to `-1`).
   - **Explore:** sum the results of the four neighbors, each called with `remaining - 1`.
   - **Un-choose:** restore `grid[r][c]` to its original value.
   - Return the accumulated total.
3. The answer is `dfs(sr, sc, empty + 2)` — `empty` zeros, plus the start, plus the end.

**Why it is correct.** Every valid walk is a simple path (no repeats, enforced by the
visited marking) that starts at `1` and ends at `2`. The `remaining` counter guarantees we
only count a path when *every* non-obstacle square has been consumed exactly once: reaching
`2` early (with `remaining > 1`) contributes `0`, and reaching `2` after consuming all
squares (`remaining == 1`) contributes exactly `1`. Restoring the cell on backtrack keeps
the "visited" constraint local to the current path, so sibling branches count independently.
Summing over all branches counts each distinct walk once.

**Reference implementation**

```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        empty = 0
        sr = sc = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    empty += 1
                elif grid[r][c] == 1:
                    sr, sc = r, c

        def dfs(r: int, c: int, remaining: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1:
                return 0
            if grid[r][c] == 2:
                return 1 if remaining == 1 else 0

            tmp = grid[r][c]
            grid[r][c] = -1                 # choose: mark visited
            total = (
                dfs(r + 1, c, remaining - 1) +
                dfs(r - 1, c, remaining - 1) +
                dfs(r, c + 1, remaining - 1) +
                dfs(r, c - 1, remaining - 1)
            )
            grid[r][c] = tmp                # un-choose: restore
            return total

        # empty zeros + start + end = empty + 2 squares to visit
        return dfs(sr, sc, empty + 2)
```

- **Time:** `O(4^(m*n))` worst case; the "must cover all squares" and "blocked by obstacle"
  prunings keep it well under that. With `m * n <= 20` this runs instantly.
- **Space:** `O(m * n)` recursion depth. Marking in place avoids a separate visited grid.

## Key Insights & Edge Cases

- **Count the target squares up front.** The `remaining` counter is what distinguishes this
  from a plain reachability search; the whole point is covering *every* empty square.
- **Off-by-one on the counter.** Decide once whether `remaining` includes the current cell
  and the end cell, then keep it consistent. Here `empty + 2` = zeros + start + end, and the
  end contributes when `remaining == 1`.
- **Restore on backtrack** (set the cell back to its original value); reusing `-1` as the
  "visited" sentinel works because obstacles are also skipped, but you must save/restore.
- **No valid path** (Example 3) returns `0` naturally — you either never reach `2`, or reach
  it with squares still remaining.
- **Advanced pruning (optional):** a "dead-end" check — if a still-unvisited empty cell has
  no unvisited walkable neighbor and it is not the current cell, no completion is possible,
  so you can prune early. Not required for `m * n <= 20`.
