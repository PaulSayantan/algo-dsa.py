# Union–Find on Grid

**Union–Find** (a.k.a. Disjoint Set Union, or DSU) is a data structure that maintains a
partition of elements into disjoint sets and supports two near-constant-time operations:

- `find(x)` — return a canonical representative ("root") of the set containing `x`.
- `union(x, y)` — merge the two sets containing `x` and `y`.

On a **grid**, every cell `(r, c)` is treated as a node. We flatten it to a single integer
id `r * numCols + c` so the DSU can index it with a plain array. Two adjacent land/open
cells are `union`-ed together; a set then represents a connected region. This makes DSU a
natural fit for **connectivity** questions on matrices.

## When to reach for it

Reach for Union–Find on a grid when the problem is fundamentally about *which cells belong to
the same connected component*, especially when:

- **Cells are added incrementally / online** (e.g. land appears one cell at a time) and you
  must report connectivity after each step. DFS/BFS would re-scan the whole grid each time;
  DSU updates in near-O(1).
- You need **component counts, sizes, or membership** and must merge components fast.
- You are modeling **percolation** — does the top connect to the bottom? Add a *virtual*
  top node and a *virtual* bottom node and union border cells to them.
- You want to answer "does A connect to B once all cells with value ≤ t are open?" by
  processing cells in sorted order and unioning as you go (threshold / percolation sweep).
- You are detecting a **redundant connection** — the edge that closes the first cycle is the
  one whose two endpoints were already in the same set.

If the grid is static and you just need one pass, plain DFS/BFS is often simpler. DSU shines
for *incremental*, *percolation*, and *merge-heavy* variants.

## Core template

```python
class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = 0  # number of active/disjoint sets, if you track it

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path halving
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False            # already connected -> this edge is redundant
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra         # union by size
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True
```

## Complexity

With **union by size/rank** + **path compression**, `m` operations over `n` elements run in
`O(m · α(n))` time, where `α` is the inverse Ackermann function (≤ 4 for any realistic input).
Space is `O(n)` for the `parent` (and optional `size`) arrays. For an `R × C` grid, `n = R·C`.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Number of Islands](problem-01-number-of-islands/PROBLEM.md) | Count connected components of land cells | Medium |
| 2 | [Surrounded Regions](problem-02-surrounded-regions/PROBLEM.md) | Virtual "border" node so escaping regions survive | Medium |
| 3 | [Number of Islands II](problem-03-number-of-islands-ii/PROBLEM.md) | Online/incremental connectivity, running component count | Hard |
| 4 | [Making a Large Island](problem-04-making-a-large-island/PROBLEM.md) | Component sizes + trying each flip of a `0` | Hard |
| 5 | [Swim in Rising Water](problem-05-swim-in-rising-water/PROBLEM.md) | Percolation sweep: union in elevation order until source ↔ target | Hard |
