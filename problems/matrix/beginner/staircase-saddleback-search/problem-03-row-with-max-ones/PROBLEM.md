# Row with Maximum Number of 1s

**Difficulty:** Easy/Medium

**Source:** GeeksforGeeks — "Row with max 1s" (classic interview problem)

## Description

You are given a boolean 2D array `mat` of size `m x n` where **each row is sorted
in non-decreasing order** — that is, every row consists of some (possibly zero)
`0`s followed by some (possibly zero) `1`s.

Find the **index of the row that contains the maximum number of 1s**. If multiple
rows share the maximum count, return the one with the **smallest index**. If the
matrix contains no `1`s at all, return `-1`.

The goal is to do this in `O(m + n)` time — better than counting each row
separately.

## Constraints

- `1 <= m, n <= 1000`
- `mat[i][j]` is either `0` or `1`.
- Every row is sorted in non-decreasing order (all `0`s appear before all `1`s
  within a row).

## Examples

### Example 1

```
Input:
mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [0, 0, 1, 1],
       [0, 0, 0, 0]]

Output: 1
```

**Explanation:** Row 0 has one `1`, row 1 has three `1`s, row 2 has two `1`s, and
row 3 has zero. Row 1 has the maximum (three), so the answer is index `1`.

### Example 2

```
Input:
mat = [[0, 0],
       [1, 1]]

Output: 1
```

**Explanation:** Row 0 has zero `1`s and row 1 has two `1`s, so row 1 wins.

### Example 3

```
Input:
mat = [[0, 0],
       [0, 0]]

Output: -1
```

**Explanation:** No row contains a `1`, so the answer is `-1`.

## Hint

Because each row is sorted, the boundary between `0`s and `1`s forms a staircase.
Use **Staircase / Saddleback Search**: start at the top-right corner and, whenever
you see a `1`, move left (recording the row); whenever you see a `0`, move down.
The whole scan is `O(m + n)`.
