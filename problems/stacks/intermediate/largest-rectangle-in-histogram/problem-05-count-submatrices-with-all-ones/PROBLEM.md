# Count Submatrices With All Ones

**Difficulty:** Medium

**Source:** LeetCode 1504 — Count Submatrices With All Ones

## Description

Given a `mat` of `0`s and `1`s (a list of equal-length rows), return how many rectangular submatrices contain only `1`s. Submatrices are counted by their position, so identical-looking blocks at different locations count separately.

Constraints: `0 <= rows, cols`; every entry is `0` or `1`. An empty matrix has `0` submatrices.

## Examples

### Example 1

```
Input:  mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
```

**Explanation:** 6 single cells that are `1`, plus larger all-`1` blocks such as the 2x1 and 3x1 columns and the 2x2 block, total 13.

### Example 2

```
Input:  mat = [[1,1],[1,1]]
Output: 9
```

**Explanation:** Choosing any contiguous row range (3 options) and any contiguous column range (3 options) yields `3 * 3 = 9` all-`1` submatrices.

## Hint

Turn each row into a histogram of consecutive `1`s reaching up; the number of all-`1` submatrices whose bottom edge is on that row equals the sum, over every column, of the minimum bar height in each subarray ending there — accumulate that sum in O(cols) with a monotonic stack.
