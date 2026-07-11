# Max-Flow / Min-Cut on Grid

## What it is

A grid (matrix) is often best solved not by DP or search, but by turning it into a
**flow network** and running a max-flow / min-cut algorithm. Cells (and sometimes the
edges between cells) become nodes and arcs with capacities; a super **source** `S` and
super **sink** `T` are attached; then:

- **Maximum flow** `S → T` answers "how much can I push through?" — the size of a
  maximum matching, the number of vertex-disjoint escape routes, etc.
- **Minimum cut** (equal to the max flow by the **Max-Flow Min-Cut Theorem**) answers
  "what is the cheapest way to separate two sides?" — the fewest cells to remove, the
  lowest-energy image segmentation, etc.

Two theorems do most of the heavy lifting:

- **König's theorem**: in a bipartite graph, `max matching = min vertex cover`.
- **Menger's theorem**: `max vertex-disjoint s–t paths = min vertex cut`.

Both reduce to a single max-flow computation once the grid is modeled correctly.

## When to reach for it

Reach for a flow model when the grid problem is one of:

- **Bipartite matching** hidden in a 2-coloring (dominoes = black/white cells) or in
  rows-vs-columns (asteroids, non-attacking rooks with walls).
- **Vertex-disjoint / edge-disjoint paths** ("how many units can travel at once without
  sharing a cell?"). Use **node-splitting** (`v_in → v_out`, capacity = how many paths
  may use the cell) to convert vertex capacities into edge capacities.
- **Optimal 2-way partition / separation** with pairwise smoothness costs (image
  segmentation, project selection, "minimum cells to remove to disconnect"). These are
  **min-cut** problems.

Red flags that suggest flow: "maximum number of disjoint …", "minimum number of cells to
remove to block …", "each cell used at most once", "assign every cell to one of two
labels minimizing pairwise disagreement".

## Modeling toolkit

| Grid feature | Flow gadget |
| --- | --- |
| Cell may host at most `k` paths | Split cell into `v_in → v_out` with capacity `k` |
| Adjacency (can step `u → v`) | Edge `u_out → v_in`, capacity `∞` (or 1 for edge-disjoint) |
| Cell is a source of one unit | `S → v_in`, capacity 1 |
| Cell is a valid exit / sink | `v_out → T`, capacity 1 (or `∞`) |
| Two-color matching | `S → black (cap 1)`, `black → white (cap 1)`, `white → T (cap 1)` |
| Per-cell label cost | `S → v` (cost of one label), `v → T` (cost of the other) |
| Adjacent cells disagree penalty | undirected edge `u ↔ v` of that capacity |

## Complexity

Model with `V` nodes and `E` edges (for an `R×C` grid, both are `O(RC)`), and run
**Dinic's algorithm**:

- General graphs: `O(V^2 · E)`.
- **Unit-capacity** graphs (bipartite matching, vertex-disjoint paths after node
  splitting): `O(E · √V)`.

So a matching or disjoint-paths problem on an `R×C` grid runs in `O((RC)^1.5)`, which is
comfortably fast for grids up to a few hundred per side. Space is `O(V + E) = O(RC)`.

## Problems

| # | Problem | Technique flavor | Difficulty |
| --- | --- | --- | --- |
| 1 | [Domino Tiling with Holes](problem-01-domino-tiling-with-holes/PROBLEM.md) | Bipartite matching via chessboard 2-coloring | Medium |
| 2 | [Asteroids — Minimum Beam Shots](problem-02-asteroids-minimum-shots/PROBLEM.md) | König: min vertex cover = max matching | Medium |
| 3 | [Escape the Grid (Disjoint Paths)](problem-03-escape-the-grid-disjoint-paths/PROBLEM.md) | Node-splitting, vertex-disjoint paths | Hard |
| 4 | [Minimum Cells to Block a Path](problem-04-minimum-cells-to-block-path/PROBLEM.md) | Min vertex cut (Menger's theorem) | Hard |
| 5 | [Image Segmentation Min-Cut](problem-05-image-segmentation-min-cut/PROBLEM.md) | Min-cut energy minimization | Hard |

Work them top to bottom: problems 1–2 build the matching intuition, 3–4 teach
node-splitting and the flow/cut duality, and 5 shows the full min-cut modeling used in
computer vision and operations research.
