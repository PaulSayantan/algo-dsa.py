# Lights Out

**Difficulty:** Hard

**Source:** Classic puzzle (Tiger Electronics "Lights Out"); a staple linear-algebra-mod-2
problem (e.g. UVa 10309 "Turn the Lights Off", numerous ICPC regionals).

## Description

You are given an `m x n` grid of lights, each either **on** (`1`) or **off** (`0`). Pressing
a cell toggles that cell **and** its orthogonal neighbors (up, down, left, right — cells
off the board are ignored). Pressing a cell twice is the same as not pressing it, so each
cell is pressed either 0 or 1 times, and the order of presses does not matter.

Determine the **minimum number of presses** needed to turn **all** lights off. If it is
impossible, return `-1`.

## Constraints

- `1 <= m, n <= 15`
- `m * n <= 225`
- Each cell of `grid` is `0` (off) or `1` (on).

## Examples

### Example 1

```
Input:
grid = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]
Output: 5

Explanation:
Pressing the 4 corners and the center toggles every light an even number of times
except each turns off correctly, clearing the board with exactly 5 presses. No
smaller set of presses clears a fully-lit 3x3 board.
```

### Example 2

```
Input:
grid = [[1, 0, 0],
        [0, 0, 0]]
Output: -1

Explanation:
On a 2x3 board the press matrix has a non-trivial kernel, so only certain light
patterns are reachable. A single lit corner is NOT in the reachable set, so no
sequence of presses can clear it. The system A p = b is inconsistent.
```

### Example 3

```
Input:
grid = [[0]]
Output: 0

Explanation:
The single light is already off, so zero presses are needed.
```

## Hint

Model it as a linear system over **GF(2)**. Let `p` be the unknown press vector (one bit per
cell) and build a matrix `A` where column `j` marks the cells toggled by pressing cell `j`.
You must solve `A p = b` (mod 2), where `b` is the initial on/off state. Use **Gaussian
Elimination** over GF(2): if a pivot-free row demands `0 = 1` the puzzle is impossible;
otherwise enumerate the free variables to minimize the number of presses.
