# Maximum Dominoes on a Grid with Obstacles

**Difficulty:** Hard

*Classic broken-profile optimization variant (maximum-matching phrasing of the domino-placement problem; appears as "maximum number of dominoes" / "maximum matching on a grid" in competitive programming).*

## Description

You are given an `n × m` grid. Some cells are **blocked** (obstacles) and some are **free**.
You want to place as many `1 × 2` dominoes as possible so that:

- each domino covers two **free**, orthogonally adjacent cells (horizontally or vertically),
- dominoes do not overlap and stay inside the grid,
- no domino covers a blocked cell.

Unlike the earlier problems, you do **not** have to cover every cell — some free cells may be
left uncovered. Return the **maximum number of dominoes** you can place.

The grid is given as a list of strings of equal length: `'.'` is a free cell and `'#'` is a
blocked cell.

## Constraints

- `1 <= n, m <= 12`
- Each row string has length `m`; each character is `'.'` (free) or `'#'` (blocked).
- The answer is an integer in `[0, floor(free_cells / 2)]`.
- Build the profile over the smaller dimension for efficiency.

## Examples

### Example 1
```
Input:  grid = ["...",
                 "..."]
Output: 3
Explanation: A 2×3 board of 6 free cells can be perfectly packed with 3 dominoes, so the
maximum is 3.
```

### Example 2
```
Input:  grid = ["...",
                 ".#."]
Output: 2
Explanation: The center-bottom cell is blocked, leaving 5 free cells. At most floor(5/2) = 2
dominoes fit, and 2 is achievable (e.g. cover the top row with one horizontal domino and one
vertical domino on a side), so the maximum is 2.
```

### Example 3
```
Input:  grid = ["#..",
                 ".#.",
                 "..#"]
Output: 2
Explanation: Blocks sit on the main diagonal, leaving 6 free cells. Only 2 non-overlapping
dominoes can be placed among the remaining adjacent pairs, so the maximum is 2 (not 3).
```

### Example 4
```
Input:  grid = ["....",
                 "....",
                 "....",
                 "...."]
Output: 8
Explanation: A 4×4 board of 16 free cells packs perfectly with 8 dominoes.
```

## Hint

Use **Broken-Profile / Plug DP (bitmask over columns)**. Sweep cell by cell with the usual
width-`min(n,m)` profile, but instead of *counting* full tilings, track the **maximum**
number of dominoes placed for each profile, and add a "leave this cell empty" transition so
partial packings are allowed. Take a `max` at each state instead of a sum.
