# Game of Life

**Difficulty:** Medium

**Source:** LeetCode 289 — Game of Life

## Description

The board is an `m x n` grid of cells, each of which is `1` (**live**) or `0`
(**dead**). Every cell interacts with its eight neighbors (horizontal, vertical,
and diagonal) using the following four rules, applied **simultaneously** to
produce the next generation:

1. Any live cell with fewer than two live neighbors dies (under-population).
2. Any live cell with two or three live neighbors lives on.
3. Any live cell with more than three live neighbors dies (over-population).
4. Any dead cell with exactly three live neighbors becomes live (reproduction).

Compute the **next state** of the board given its current state. The update must
be **in place** — and because all cells transition simultaneously, you cannot
overwrite a cell with its new value while neighbors still need to read its old
value. The interesting `O(1)`-space solution encodes both the old and the new
state inside each cell so a single grid holds both generations at once.

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 25`
- `board[i][j]` is `0` or `1`.

## Examples

### Example 1

```
Input:  board = [[0,1,0],
                 [0,0,1],
                 [1,1,1],
                 [0,0,0]]
Output: [[0,0,0],
         [1,0,1],
         [0,1,1],
         [0,1,0]]
```

**Explanation:** Applying the four rules to every cell at once produces the next
generation shown. For instance the dead cell `(3,1)` has exactly three live
neighbors (`(2,0)`, `(2,1)`, `(2,2)`), so by rule 4 it becomes live. The dead
cell `(1,1)`, by contrast, has five live neighbors, so it stays dead.

### Example 2

```
Input:  board = [[1,1],
                 [1,0]]
Output: [[1,1],
         [1,1]]
```

**Explanation:** The dead cell `(1,1)` has exactly three live neighbors, so it
becomes live. Each live cell has two or three live neighbors, so all survive.

### Example 3

```
Input:  board = [[0]]
Output: [[0]]
```

**Explanation:** A single dead cell with zero live neighbors stays dead.

## Hint

Use the **Set Matrix Zeroes** family of in-place encoding. Since each cell only
needs to remember its old bit and its new bit, pack both into one integer (for
example `new * 2 + old`, or use bit 0 for the current state and bit 1 for the
next state). Count neighbors from the *low* bit (old state), then shift/divide to
extract the new state in a final pass.
