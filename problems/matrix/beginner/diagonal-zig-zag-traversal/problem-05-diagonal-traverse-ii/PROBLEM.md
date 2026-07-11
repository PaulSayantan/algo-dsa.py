# Diagonal Traverse II

**Difficulty:** Medium

**Source:** LeetCode 1424 — "Diagonal Traverse II"

## Description

Given a 2D integer array `nums`, return all elements of `nums` in **diagonal order**
as shown in the problem's figure.

The catch: `nums` is a **jagged** (ragged) array — different rows may have different
lengths, and some rows may be shorter than others. The diagonals still run in the
`/` (anti-diagonal) direction, grouping cells by the constant `i + j`. Diagonals are
emitted in increasing order of `i + j`, and **within a diagonal the cells are read
bottom-to-top** (i.e. in decreasing order of row index — the cell from the lowest row
comes first).

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i].length <= 10^5`
- `1 <= nums[i][j] <= 10^5`
- The total number of elements across all rows does not exceed `10^5`.

## Examples

### Example 1

```
Input:  nums = [[1,2,3],
                [4,5,6],
                [7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
```

**Explanation:** Grouping by `i + j`: `d0=[(0,0)=1]`, `d1=[(0,1)=2,(1,0)=4]`,
`d2=[(0,2)=3,(1,1)=5,(2,0)=7]`, `d3=[(1,2)=6,(2,1)=8]`, `d4=[(2,2)=9]`. Reading each
diagonal **bottom-to-top** (largest row index first): `1`, then `4,2`, then `7,5,3`,
then `8,6`, then `9`, giving `[1,4,2,7,5,3,8,6,9]`.

### Example 2

```
Input:  nums = [[1,2,3,4,5],
                [6,7],
                [8],
                [9,10,11],
                [12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
```

**Explanation:** Rows have different lengths, so the diagonals are irregular. Still
grouping by `i + j` and reading each diagonal bottom-to-top produces the sequence
above. For example diagonal `i+j=2` contains `(0,2)=3`, `(1,1)=7`, `(2,0)=8`; read
bottom-to-top that is `8,7,3`.

## Hint

Use **Diagonal / Zig-Zag Traversal**: group cells by `i + j` even though rows are
ragged. Appending cells in row-increasing order and reversing (or prepending) yields
the required bottom-to-top order.
