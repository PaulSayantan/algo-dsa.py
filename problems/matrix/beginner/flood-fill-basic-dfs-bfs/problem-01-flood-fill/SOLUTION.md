# Flood Fill — Solution

## Brute Force

There is no meaningfully different "brute force" here; the problem *is* a
traversal. A naive but valid approach is to repeatedly scan the entire grid,
and on each pass recolor any original-color cell that is adjacent to an
already-recolored cell, stopping when a full pass makes no change.

- **Time:** `O((m * n)^2)` in the worst case — up to `O(m * n)` passes, each
  scanning `O(m * n)` cells.
- **Space:** `O(1)` extra.

This is wasteful; a single DFS/BFS visits each cell once.

## Optimal Approach (Flood Fill via DFS/BFS)

Record the seed's **original color** first. If that original color already equals
the target `color`, return immediately — otherwise you would revisit cells
forever, since a recolored cell would still "match" the color you are searching
for. Then traverse from the seed, and for every cell that currently holds the
original color, repaint it to `color` and recurse/enqueue its four neighbors.

Why it is correct: repainting a cell to a color different from the original
doubles as marking it visited. A cell is only entered when it still holds the
original color, so each cell is processed exactly once, and exactly the cells
reachable from the seed through same-original-color neighbors get repainted —
which is the definition of the connected region.

### Step by step (DFS)

1. `original = image[sr][sc]`.
2. If `original == color`, return `image` unchanged.
3. `dfs(r, c)`: if `(r, c)` is out of bounds or `image[r][c] != original`,
   return. Otherwise set `image[r][c] = color` and recurse into
   `(r±1, c)` and `(r, c±1)`.
4. Call `dfs(sr, sc)` and return `image`.

```python
def floodFill(self, image, sr, sc, color):
    original = image[sr][sc]
    if original == color:
        return image
    m, n = len(image), len(image[0])

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != original:
            return
        image[r][c] = color
        dfs(r + 1, c); dfs(r - 1, c)
        dfs(r, c + 1); dfs(r, c - 1)

    dfs(sr, sc)
    return image
```

An iterative BFS/DFS with an explicit queue/stack is equivalent and avoids
recursion-depth limits on large inputs.

- **Time:** `O(m * n)` — each cell is examined a constant number of times.
- **Space:** `O(m * n)` — worst-case recursion/stack depth when the whole grid
  is one region.

## Key Insights & Edge Cases

- **`original == color`**: the make-or-break edge case. Without the early
  return, recoloring a cell leaves it matching the search color and the
  traversal never terminates.
- **Recolor = visited marker.** You do not need a separate visited set; the
  mutation itself prevents re-entry (given the guard above).
- **Diagonal neighbors do not count** — only the four orthogonal directions.
- **Single-cell grid** (`1 x 1`): only the seed is recolored (or nothing, if the
  color already matches).
