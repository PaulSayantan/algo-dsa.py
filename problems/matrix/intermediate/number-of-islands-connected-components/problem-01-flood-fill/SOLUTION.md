# Flood Fill — Solution

## Brute Force

There is no meaningfully "brute" version of this problem — you must visit every
pixel in the connected region at least once. A naive but correct idea is to
repeatedly scan the whole grid, and on each pass repaint any pixel of the old
color that is adjacent to an already-repainted pixel, stopping when a full pass
makes no changes.

- **Time:** `O((m*n)^2)` in the worst case (up to `m*n` passes, each scanning
  `m*n` cells).
- **Space:** `O(1)` extra beyond the grid.

This is wasteful; a single traversal does the job.

## Optimal Approach (Connected Components / Flood Fill)

Treat the region as a connected component where an edge connects two
4-directionally adjacent pixels **that share the starting pixel's original
color**. Flood outward from the seed with DFS or BFS, recoloring as you go.

**Why it is correct:** every pixel that should be repainted is, by definition,
reachable from `(sr, sc)` through a chain of same-color 4-directional
neighbours. A graph traversal visits exactly the set of reachable nodes — no
more, no less — so it paints precisely the target component.

**The critical edge case:** if `color == originalColor`, recoloring changes
nothing, so a visited pixel can never be distinguished from an unvisited one
and the traversal loops forever. Guard against this by returning early when the
new color equals the old color. (When they differ, the act of repainting *is*
your "visited" marker, so no separate visited set is needed.)

### Step-by-step (DFS)

1. Read `original = image[sr][sc]`.
2. If `original == color`, return `image` immediately.
3. DFS from `(sr, sc)`:
   - Paint the current cell with `color`.
   - For each of the 4 neighbours in bounds whose value equals `original`,
     recurse.
4. Return `image`.

```python
def floodFill(image, sr, sc, color):
    original = image[sr][sc]
    if original == color:
        return image

    rows, cols = len(image), len(image[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != original:
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image
```

An iterative BFS/DFS with an explicit stack or queue is equivalent and avoids
recursion-depth limits on large inputs.

- **Time:** `O(m*n)` — each pixel is examined a constant number of times.
- **Space:** `O(m*n)` worst case for the recursion stack / queue (e.g. a grid
  that is one long snake of same-colored pixels).

## Key Insights & Edge Cases

- **New color == old color** is the classic trap: return early, or you infinite
  loop / stack overflow.
- **Recoloring doubles as the visited marker.** Because painted cells no longer
  match `original`, they are naturally skipped — no separate `visited` set is
  needed (once the early-return guard is in place).
- **Single-pixel region:** if no neighbour matches, only the seed is repainted
  (Example 3).
- **Diagonal neighbours do not connect** — only the 4 orthogonal directions.
- Capture `original` *before* you paint the seed; reading it afterward would
  compare against the new color.
