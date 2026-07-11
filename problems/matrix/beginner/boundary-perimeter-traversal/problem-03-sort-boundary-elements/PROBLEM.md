# Sort the Boundary Elements of a Matrix

**Difficulty:** Medium

**Source:** Classic matrix manipulation exercise (common in interview prep sets)

## Description

Given an `m x n` integer matrix, **sort only its boundary (outer ring) elements in
non-decreasing order** and write them back onto the boundary in **clockwise** order,
starting from the top-left corner. The interior of the matrix must remain **completely
unchanged**.

Concretely:

1. Read the boundary elements in clockwise order into a list.
2. Sort that list ascending.
3. Write the sorted values back onto the boundary cells, following the same clockwise
   path, so the smallest value ends up at the top-left corner and values increase as you
   walk clockwise around the ring.

Return the modified matrix.

## Constraints

- `1 <= m, n <= 500`
- `-10^6 <= matrix[i][j] <= 10^6`
- The matrix is rectangular.

## Examples

### Example 1

```
Input:  matrix = [[1, 4, 3],
                  [7, 5, 2],
                  [9, 6, 8]]
Output: [[1, 2, 3],
         [9, 5, 4],
         [8, 7, 6]]
Explanation: The clockwise boundary is [1,4,3,2,8,6,9,7]. Sorted it is
             [1,2,3,4,6,7,8,9]. Writing it back clockwise gives the top row 1,2,3,
             right column 4, bottom row 6,7,8 (reversed), left column 9. The interior
             cell 5 is untouched.
```

### Example 2

```
Input:  matrix = [[5, 2, 8, 1],
                  [9, 0, 0, 3],
                  [4, 7, 6, 2]]
Output: [[1, 2, 2, 3],
         [9, 0, 0, 4],
         [8, 7, 6, 5]]
Explanation: Clockwise boundary [5,2,8,1,3,2,6,7,4,9] sorted is
             [1,2,2,3,4,5,6,7,8,9]. Written back clockwise it fills the ring while the
             interior 0,0 stays put.
```

### Example 3 (single row)

```
Input:  matrix = [[3, 1, 2]]
Output: [[1, 2, 3]]
Explanation: The whole row is the boundary, so sorting the boundary sorts the row.
```

## Hint

Use **Boundary / Perimeter Traversal** twice: once to *extract* the ring into a list
(clockwise), and — after sorting — once more with the identical traversal order to
*write* the values back. Keeping the two passes in the same order guarantees correct
placement.
