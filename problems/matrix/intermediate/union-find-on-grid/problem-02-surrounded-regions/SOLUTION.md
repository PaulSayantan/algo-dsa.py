# Surrounded Regions — Solution

## Brute Force

Try to decide, for each `'O'`, whether it can reach the border. A naive approach runs a
separate BFS/DFS *from every `'O'`* asking "can I escape to an edge?" That repeats work across
cells in the same region.

- **Time:** `O((m · n)^2)` worst case (a flood fill per cell).
- **Space:** `O(m · n)` for the search stack.

The standard linear fix is a **reverse flood fill**: start DFS/BFS from every border `'O'`,
mark all reachable `'O'`s as "safe," then flip every unmarked `'O'` to `'X'`. That is
`O(m · n)`. Union–Find achieves the same result with an explicit connectivity model, which is
what we practice here.

## Optimal Approach (Union–Find on Grid)

**Idea.** Add a single **virtual "border" node** with id `rows * cols` (one past the last real
cell). The invariant: an `'O'` is *safe* iff it is in the same DSU set as the virtual node.

1. Build a DSU of size `rows * cols + 1`. Let `BORDER = rows * cols`.
2. Sweep every cell. For each `'O'` at `(r, c)`:
   - If `(r, c)` is on the border (`r == 0 || r == rows-1 || c == 0 || c == cols-1`), then
     `union(id(r,c), BORDER)`.
   - Union it with its **right** and **down** neighbors if those are `'O'` (right+down covers
     every adjacency once).
3. Sweep again: for each `'O'` at `(r, c)`, if `find(id(r,c)) != find(BORDER)`, set it to
   `'X'`. Border-connected `'O'`s share the virtual root and are left alone.

**Why it is correct.** Union is transitive, so after step 2 all `'O'`s in one region share a
root. Border `'O'`s are additionally tied to `BORDER`; hence a region's root equals `BORDER`'s
root **iff** at least one of its cells touches the border — exactly the definition of "not
surrounded." Flipping the rest captures precisely the enclosed regions.

- **Time:** `O(m · n · α(m·n))` ≈ `O(m · n)`.
- **Space:** `O(m · n)` for the DSU arrays (`+1` for the virtual node).

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]


class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        BORDER = rows * cols
        dsu = DSU(rows * cols + 1)

        def idx(r, c):
            return r * cols + c

        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "O":
                    continue
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    dsu.union(idx(r, c), BORDER)
                if c + 1 < cols and board[r][c + 1] == "O":
                    dsu.union(idx(r, c), idx(r, c + 1))
                if r + 1 < rows and board[r + 1][c] == "O":
                    dsu.union(idx(r, c), idx(r + 1, c))

        border_root = dsu.find(BORDER)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and dsu.find(idx(r, c)) != border_root:
                    board[r][c] = "X"
```

## Key Insights & Edge Cases

- **The virtual node is the whole trick.** It converts "reaches any of the 4 borders" into a
  single connectivity query, avoiding four separate checks.
- **Compare `find(cell)` to `find(BORDER)`, not to a cached id.** After unions the border
  node's root may change, so recompute `border_root` once before the final sweep (or call
  `find(BORDER)` each time).
- **Border `'O'`s and their whole region stay `'O'`.** Example 2 (all `'O'`s on the border)
  changes nothing.
- **Tiny boards:** a `1 x n` or `m x 1` board is entirely border, so no `'O'` is ever
  captured.
- **Modify in place.** Do the flips on the original `board`; do not allocate a new grid.
- Use path compression + union by size to keep a 200×200 board fast.
