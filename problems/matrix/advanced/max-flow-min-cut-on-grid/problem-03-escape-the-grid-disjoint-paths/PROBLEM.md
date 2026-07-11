# Escape the Grid (Vertex-Disjoint Paths)

**Difficulty:** Hard

**Source:** Classic (USACO "The Escape" / node-splitting maximum-flow, textbook vertex-disjoint paths)

## Description

You are given an `R × C` grid where each cell is one of:

- `'S'` — a person who wants to escape,
- `'E'` — an exit cell,
- `'.'` — open floor,
- `'#'` — a wall (impassable).

People move one step at a time between orthogonally adjacent (up/down/left/right)
non-wall cells. A person escapes when they reach any exit cell. All people move
**simultaneously**, and — to avoid collisions — **no cell may be used by more than one
person's path** (this includes the starting `'S'` cells and the `'E'` cells; each such cell
serves at most one path).

Return the **maximum number of people who can escape at the same time**.

Because the capacity constraint is on **cells (vertices)**, not edges, this is a
**vertex-disjoint paths** problem. The standard trick is **node-splitting**: replace each
open cell `v` with two nodes `v_in → v_out` joined by a capacity-1 edge, so at most one
path may pass through the cell. Then a max-flow from a super source (attached to every
`'S'`) to a super sink (attached to every `'E'`) equals the answer.

## Constraints

- `1 <= R, C <= 100`
- Each cell is one of `'S'`, `'E'`, `'.'`, `'#'`.
- There may be zero or more `'S'` cells and zero or more `'E'` cells.
- A path may not pass through a wall, and start/exit cells count as used cells.

## Examples

### Example 1

```
Input:
grid = [
  "S.E",
  "S.E"
]
Output: 2
Explanation: Person at (0,0) takes (0,0) -> (0,1) -> (0,2)=exit.
Person at (1,0) takes (1,0) -> (1,1) -> (1,2)=exit.
The two paths share no cell, so both escape.
```

### Example 2

```
Input:
grid = [
  "S.S",
  "#.#",
  "E.E"
]
Output: 1
Explanation: Cell (0,0)'s only non-wall neighbor is (0,1); cell (0,2)'s only non-wall
neighbor is also (0,1). Both people are forced through the single cell (0,1), which can
carry just one path, so at most one person escapes.
```

### Example 3

```
Input:
grid = [
  "S#E"
]
Output: 0
Explanation: The wall at (0,1) separates the person from the exit; no path exists,
so nobody escapes.
```

## Hint

Cells, not edges, are the scarce resource — split every open cell into `in → out` with
capacity 1 (**node-splitting**) and run **Max-Flow / Min-Cut on Grid** from a super source
over all `'S'` cells to a super sink over all `'E'` cells.
