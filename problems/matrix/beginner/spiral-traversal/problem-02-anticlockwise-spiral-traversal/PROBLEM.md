# Anti-clockwise Spiral Traversal

**Difficulty:** Easy

**Source:** Classic interview / GeeksforGeeks — "Anti Spiral Traversal of a matrix" variant (counter-clockwise)

## Description

Given an `m x n` matrix, return all of its elements in **counter-clockwise
(anti-clockwise) spiral order**, starting from the top-left corner.

Unlike the standard clockwise spiral, the very first move goes **down** the left
column. Concretely the direction cycle is: down the left column, right along the
bottom row, up the right column, left along the top row, and then spiral inward.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-1000 <= matrix[i][j] <= 1000`

## Examples

### Example 1

```
Input:  matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
Output: [1,4,7,8,9,6,3,2,5]
```

Explanation: Down the left column `1,4,7`; right along the bottom row `8,9`; up
the right column `6,3`; left along the top row `2`; then the lone inner cell `5`.

### Example 2

```
Input:  matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9,10,11,12]]
Output: [1,5,9,10,11,12,8,4,3,2,6,7]
```

Explanation: Left column `1,5,9`; bottom row `10,11,12`; right column `8,4`; top
row `3,2`; then the inner row left-to-right `6,7`.

### Example 3

```
Input:  matrix = [[1],
                  [2],
                  [3]]
Output: [1,2,3]
```

Explanation: A single column is traversed straight down.

## Hint

It is the mirror image of the clockwise walk: keep the same four boundaries
`top`, `bottom`, `left`, `right`, but reverse the direction cycle. A
counter-clockwise **Spiral Traversal**.
