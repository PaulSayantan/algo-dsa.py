# Floor and Ceiling in a Sorted Matrix

**Difficulty:** Medium

**Source:** Classic (matrix variant of "Floor and Ceil in a sorted array",
GeeksforGeeks)

## Description

You are given an `m x n` integer matrix `matrix` sorted in **row-major order**:
each row is sorted in non-decreasing order and the first element of each row is
greater than or equal to the last element of the previous row. Reading the matrix
row by row therefore yields one non-decreasing array of `m * n` values.

Given an integer `target`, return a pair `[floor, ceil]` where:

- **floor** is the largest value in the matrix that is `<= target`, or `-1` if no
  such value exists (i.e. `target` is smaller than every element).
- **ceil** is the smallest value in the matrix that is `>= target`, or `-1` if no
  such value exists (i.e. `target` is larger than every element).

If `target` itself is present, both floor and ceil equal `target`. Solve it in
`O(log(m * n))` time.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 500`
- `-10^9 <= matrix[i][j] <= 10^9`
- The flattened row-major sequence is non-decreasing (duplicates allowed).
- `-10^9 <= target <= 10^9`
- Use `-1` as the sentinel for "does not exist" (all real values may also be
  negative, but the grader treats `-1` positionally as the sentinel here).

## Examples

### Example 1

```
Input:  matrix = [[1, 4, 7],
                  [10, 13, 16]], target = 12
Output: [10, 13]
Explanation: Flattened, the array is [1, 4, 7, 10, 13, 16]. The largest value
             <= 12 is 10 (floor); the smallest value >= 12 is 13 (ceil).
```

### Example 2

```
Input:  matrix = [[1, 4, 7],
                  [10, 13, 16]], target = 7
Output: [7, 7]
Explanation: 7 is present in the matrix, so both floor and ceil equal 7.
```

### Example 3

```
Input:  matrix = [[1, 4, 7],
                  [10, 13, 16]], target = 20
Output: [16, -1]
Explanation: The largest value <= 20 is 16 (floor). No value is >= 20, so ceil is
             -1.
```

## Hint

Use **Binary Search in a Fully-Sorted Matrix**. The ceiling is `lower_bound(target)`
(first flat index with value `>= target`); the floor is the element just before
`lower_bound`, or the element at `lower_bound` if it equals `target`. Map flat
index `idx` to `matrix[idx // n][idx % n]`.
