# Pacific Atlantic Water Flow — Solution

## Brute Force

For every cell, run a separate search that tries to flow downhill to any Pacific
border cell, and a second search to any Atlantic border cell; include the cell if
both succeed. Each of the `m * n` cells launches searches over up to `m * n`
cells.

- **Time:** `O((m * n)^2)`.
- **Space:** `O(m * n)` per search.

This is too slow for `200 x 200` and repeats enormous amounts of work.

## Optimal Approach (Reverse multi-source Flood Fill)

Instead of asking, for each cell, "can water flow *out* to an ocean?", flip the
direction: start **at the oceans** and ask "which cells can water flow *in* from,
i.e. which cells drain here?" Flowing downhill out to the ocean is the reverse of
climbing uphill inward from the ocean.

Do two floods:

- **Pacific flood:** seed the traversal with every cell on the top row and left
  column. From a cell, move to a neighbor only if `neighbor_height >=
  current_height` (uphill). Mark all reachable cells as `pacific`.
- **Atlantic flood:** seed with every cell on the bottom row and right column,
  same uphill rule. Mark reachable cells as `atlantic`.

The answer is every cell that is in **both** the `pacific` and `atlantic` sets.

Why it is correct: water flows `A -> B` (downhill) iff `height[B] <= height[A]`,
which is exactly the reverse of the uphill step `B -> A` used by the flood. So a
cell is reachable from the Pacific flood iff there exists a non-increasing
(downhill) path from that cell to some Pacific-border cell — precisely the
condition for its water to reach the Pacific. The same holds for the Atlantic.
The intersection is the set of cells draining to both.

### Step by step

```python
def pacificAtlantic(self, heights):
    if not heights or not heights[0]:
        return []
    m, n = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(r, c, visited, prev_height):
        if (r < 0 or r >= m or c < 0 or c >= n
                or (r, c) in visited
                or heights[r][c] < prev_height):
            return
        visited.add((r, c))
        h = heights[r][c]
        dfs(r + 1, c, visited, h); dfs(r - 1, c, visited, h)
        dfs(r, c + 1, visited, h); dfs(r, c - 1, visited, h)

    for c in range(n):
        dfs(0, c, pacific, heights[0][c])          # top -> Pacific
        dfs(m - 1, c, atlantic, heights[m - 1][c])  # bottom -> Atlantic
    for r in range(m):
        dfs(r, 0, pacific, heights[r][0])          # left -> Pacific
        dfs(r, n - 1, atlantic, heights[r][n - 1])  # right -> Atlantic

    return [[r, c] for r in range(m) for c in range(n)
            if (r, c) in pacific and (r, c) in atlantic]
```

- **Time:** `O(m * n)` — each cell is added to each visited set at most once, and
  each visit inspects a constant number of neighbors. Two floods keep it linear.
- **Space:** `O(m * n)` for the two visited sets plus traversal stack/queue.

## Key Insights & Edge Cases

- **Reverse the flow.** Simulating drainage from every cell is quadratic;
  flooding inward from the borders with the reversed (`>=`) comparison makes it
  linear.
- **`>=`, not `>`.** Water flows to *equal-or-lower* neighbors going out, so the
  reverse step allows moving to *equal-or-higher* cells. Using strict `>` drops
  valid plateaus.
- **Two independent visited sets**, one per ocean, intersected at the end.
- **Border cells trivially reach their own ocean**; corner cells like `(0, n-1)`
  and `(m-1, 0)` touch both oceans directly.
- **Single cell / single row / single column:** every cell borders both oceans,
  so all cells are in the answer (e.g. `[[1]] -> [[0,0]]`).
