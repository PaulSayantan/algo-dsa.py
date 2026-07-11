# Tiling a 2×N Board with Dominoes

**Difficulty:** Easy

*Classic combinatorics / introductory tiling DP (a warm-up for LeetCode 790 and Mondriaan's Dream).*

## Description

You are given an integer `n`. Consider a board with **2 rows** and **N columns**
(a `2 × N` grid). You have an unlimited supply of `1 × 2` dominoes. Each domino may be
placed either **horizontally** (covering two side-by-side cells in the same row) or
**vertically** (covering two stacked cells in the same column).

Count the number of distinct ways to tile the entire board so that every cell is covered
by exactly one domino and no domino sticks out of the board or overlaps another.

Because the answer can be large, return it as an ordinary integer (it fits comfortably for
the given constraints; no modulus is required here).

Although this problem has a famous Fibonacci-style recurrence, you are asked to solve it
with a **broken-profile / plug DP**: sweep the board cell by cell while carrying a small
bitmask describing which cells on the moving frontier are already filled. This scales
directly to boards of width `> 2` in the later problems.

## Constraints

- `1 <= n <= 60`
- The board always has exactly 2 rows.
- The answer fits in a 64-bit signed integer for `n <= 60`.

## Examples

### Example 1
```
Input:  n = 1
Output: 1
Explanation: A 2×1 board is covered by exactly one vertical domino. There is only 1 tiling.
```

### Example 2
```
Input:  n = 2
Output: 2
Explanation: A 2×2 board can be tiled with two vertical dominoes, or with two horizontal
dominoes stacked on top of each other. That is 2 tilings.
```

### Example 3
```
Input:  n = 3
Output: 3
Explanation: The 2×3 board admits 3 tilings: three vertical dominoes; or one vertical
domino on the left plus two horizontal dominoes on the right; or two horizontal dominoes
on the left plus one vertical domino on the right.
```

### Example 4
```
Input:  n = 4
Output: 5
Explanation: The counts follow the Fibonacci sequence: f(4) = f(3) + f(2) = 3 + 2 = 5.
```

## Hint

Use **Broken-Profile / Plug DP (bitmask over columns)**. Sweep the two-row board cell by
cell and keep a bitmask of the frontier: a bit records whether a cell is already occupied
by a vertical domino reaching in from the previous column. The width-2 profile makes this
the simplest possible instance of the technique.
