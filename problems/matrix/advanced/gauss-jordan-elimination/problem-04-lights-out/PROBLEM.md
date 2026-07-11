# Lights Out

**Difficulty:** Medium–Hard

**Source:** Classic puzzle (Tiger Electronics "Lights Out"); a staple GF(2) linear-algebra problem in competitive programming

## Description

You are given an `m × n` grid of lights. Each cell is either **on** (`1`) or
**off** (`0`), described by the matrix `grid`. Pressing a cell **toggles** that
cell **and its orthogonal neighbours** (up, down, left, right — not diagonals).

Your goal is to turn **every** light **off**. Pressing a cell twice is the same as
not pressing it at all (toggles cancel), and the order of presses does not matter,
so a *solution* is simply a **subset** of cells to press.

Return one valid press pattern as an `m × n` 0/1 matrix `p`, where `p[r][c] = 1`
means "press cell `(r, c)`". If it is **impossible** to turn all the lights off,
return `None`.

(Any valid press pattern is accepted; you do not need to minimise the number of
presses.)

## Constraints

- `1 ≤ m, n ≤ 15` (so up to `225` cells / unknowns)
- `grid[r][c] ∈ {0, 1}`
- Toggling is over the 4-neighbourhood plus the pressed cell itself.

## Examples

### Example 1

```
Input:
  grid = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]        # 3×3, all lights on

Output:
  [[1, 0, 1],
   [0, 1, 0],
   [1, 0, 1]]               # press the four corners and the centre (an "X")

Explanation:
  Pressing the corners and centre toggles every light an odd number of
  times exactly where needed; simulating these 5 presses leaves the whole
  board off.
```

### Example 2

```
Input:
  grid = [[1, 1],
          [1, 1]]           # 2×2, all lights on

Output:
  [[1, 1],
   [1, 1]]                  # press all four cells

Explanation:
  In a 2×2 board, pressing a cell toggles itself and its two neighbours
  (3 cells). Pressing all four cells toggles each light exactly 3 times
  (odd), flipping every "on" light to "off".
```

### Example 3

```
Input:
  grid = [[0, 0, 0],
          [0, 0, 0]]        # already all off

Output:
  [[0, 0, 0],
   [0, 0, 0]]               # press nothing

Explanation:
  The board is already solved, so the empty press pattern works.
```

## Hint

Assign a 0/1 unknown `xᵢ` to "do we press cell `i`?". Toggling is addition
**modulo 2**, so each light's final state is a linear equation over `GF(2)`:
`(sum of presses that touch this cell) ≡ grid value (mod 2)`. That is a linear
system `A x ≡ b (mod 2)`. Solve it with **Gauss–Jordan Elimination over GF(2)**,
where "add a multiple of a row" becomes **XOR** of rows and there is no division.
Inconsistency (a `0 = 1` row) means the board is unsolvable.
