# Domino and Tromino Tiling

**Difficulty:** Medium

*LeetCode 790 — "Domino and Tromino Tiling"*

## Description

You have two types of tiles: a `2 × 1` **domino** and an **L-shaped tromino** (a tromino
covers three cells forming an "L"). Both tiles may be rotated.

Given an integer `n`, return the number of ways to tile a `2 × n` board. Since the answer
may be very large, return it **modulo `10^9 + 7`**.

In a tiling, every square must be covered by a tile, tiles must not overlap, and no tile
may extend outside the board. Two tilings are considered different if and only if there
exist two 4-directionally adjacent cells on the board where one tiling has a tile that the
other tiling does not.

The domino may be placed horizontally (1 row × 2 columns) or vertically (2 rows × 1 column).
The L-tromino has four rotations, each covering a `2 × 2` square minus one corner.

## Constraints

- `1 <= n <= 1000`
- The board has exactly 2 rows and `n` columns.
- Return the count modulo `10^9 + 7`.

## Examples

### Example 1
```
Input:  n = 1
Output: 1
Explanation: A 2×1 board holds exactly one vertical domino. A tromino needs 3 cells and
does not fit, so there is 1 tiling.
```

### Example 2
```
Input:  n = 3
Output: 5
Explanation: The five tilings are shown below (each grid is 2 rows tall, 3 columns wide,
letters mark tiles):

  1) VVV      2) VHH      3) HHV      4) LLV      5) VLL
     VVV         VHH         HHV         LzV         VzL

There are 5 distinct ways to tile a 2×3 board with dominoes and L-trominoes.
```

### Example 3
```
Input:  n = 4
Output: 11
Explanation: Building on the 2×3 case, extending by one column and combining dominoes with
L-trominoes yields 11 distinct tilings.
```

### Example 4
```
Input:  n = 2
Output: 2
Explanation: Two vertical dominoes, or two horizontal dominoes stacked — the trominoes
would leave a single uncovered cell, so only 2 tilings use them-free placements.
```

## Hint

Use **Broken-Profile / Plug DP (bitmask over columns)**. Sweep the two rows column by
column carrying a small bitmask of which cells protrude into the next column. The only
change from the plain 2×N domino count is that your transition set now also enumerates the
four L-tromino placements, which can leave one cell of the next column pre-filled.
