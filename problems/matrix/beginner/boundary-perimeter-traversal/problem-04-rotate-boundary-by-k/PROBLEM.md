# Rotate the Boundary of a Matrix by K

**Difficulty:** Medium

**Source:** Classic matrix rotation variant (common in competitive-programming practice)

## Description

Given an `m x n` integer matrix and an integer `k`, rotate **only the boundary (outer
ring)** of the matrix **clockwise by `k` positions**. The interior of the matrix stays
unchanged.

Think of the boundary as a circular sequence read clockwise from the top-left corner.
Rotating clockwise by `k` moves every boundary element `k` steps forward along that
clockwise path (the element that "falls off" the end wraps around to the front).

If `B` is the number of boundary cells, rotating by `k` and by `k mod B` give the same
result, so you should reduce `k` modulo `B`. Return the modified matrix.

## Constraints

- `1 <= m, n <= 500`
- `0 <= k <= 10^9`
- `-10^6 <= matrix[i][j] <= 10^6`
- The matrix is rectangular.

## Examples

### Example 1

```
Input:  matrix = [[1, 2, 3],
                  [8, 9, 4],
                  [7, 6, 5]], k = 1
Output: [[8, 1, 2],
         [7, 9, 3],
         [6, 5, 4]]
Explanation: The clockwise boundary is [1,2,3,4,5,6,7,8]. Rotating clockwise by 1 makes
             it [8,1,2,3,4,5,6,7]. Written back clockwise: top row 8,1,2; right column
             3,4; bottom row (reversed) 5,6; left column 7. Interior 9 is unchanged.
```

### Example 2

```
Input:  matrix = [[1, 2, 3, 4],
                  [10, 11, 12, 5],
                  [9, 8, 7, 6]], k = 2
Output: [[9, 10, 1, 2],
         [8, 11, 12, 3],
         [7, 6, 5, 4]]
Explanation: Clockwise boundary [1,2,3,4,5,6,7,8,9,10] (B = 10). Rotating clockwise by 2
             yields [9,10,1,2,3,4,5,6,7,8]. Written back clockwise around the ring; the
             interior 11,12 is untouched.
```

### Example 3 (single row + wrap-around k)

```
Input:  matrix = [[1, 2, 3]], k = 4
Output: [[3, 1, 2]]
Explanation: The row is the whole boundary (B = 3). k = 4 ≡ 1 (mod 3), so it rotates
             right by 1: [1,2,3] → [3,1,2].
```

## Hint

Use **Boundary / Perimeter Traversal**: extract the ring into a list clockwise,
cyclically shift it by `k mod B`, then write it back along the exact same clockwise path.
