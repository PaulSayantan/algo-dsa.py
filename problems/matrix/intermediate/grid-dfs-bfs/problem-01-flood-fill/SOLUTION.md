# Flood Fill — Solution

## Brute Force

There is no meaningfully "brute" version distinct from the graph traversal: to
know which pixels belong to the region you must explore connectivity. A naive
approach might repeatedly scan the whole grid, recoloring any same-original-color
pixel adjacent to an already-filled pixel, and repeat until a full pass makes no
change.

- **Time:** `O((R * C)^2)` in the worst case (up to `R * C` passes, each scanning
  all `R * C` cells).
- **Space:** `O(1)` extra.

This is wasteful — a single traversal suffices.

## Optimal Approach (Grid DFS / BFS)

Treat each pixel as a node connected to its 4 orthogonal neighbors. Run one
traversal from the start pixel, following only edges to neighbors that still hold
the **original** color, recoloring each visited pixel to the new color.

**Why it is correct:** The flood-fill region is, by definition, the connected
component of same-colored pixels containing the start. DFS/BFS visits exactly the
nodes reachable from the source through valid edges — i.e. exactly that component.
Recoloring on the way in doubles as the "visited" marker (a pixel that already
has the new color is skipped), which prevents revisiting and infinite loops.

**Critical edge case:** If the start pixel's original color already equals
`color`, recoloring does nothing to mark visited pixels, so the recursion would
loop forever. Guard against it by returning early when `original == color`.

### Step by step

1. Read `original = image[sr][sc]`.
2. If `original == color`, return the image unchanged.
3. DFS/BFS from `(sr, sc)`: set the current pixel to `color`, then recurse into
   each in-bounds neighbor whose value equals `original`.

### Reference implementation (DFS)

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

An iterative BFS with a `collections.deque` works identically and avoids Python's
recursion-depth limit on very large regions.

- **Time:** `O(R * C)` — each pixel is examined a constant number of times.
- **Space:** `O(R * C)` — recursion stack / queue in the worst case (a grid that
  is one big region).

## Key Insights & Edge Cases

- **Same-color guard** is the single most common bug; always handle
  `original == color`.
- Recoloring in place *is* your visited set — no separate structure needed.
- Only same-original-color neighbors are edges; a pixel of a different color acts
  as a wall.
- For huge single-color grids, prefer iterative BFS/DFS to dodge stack overflow.
