# Count Inversions in an Array

**Difficulty:** Medium

**Source:** Classic (CLRS Problem 2-4); GeeksforGeeks "Count Inversions";
SPOJ INVCNT

## Description

Given an array `nums` of size `n`, count the number of **inversions** in it.

An **inversion** is a pair of indices `(i, j)` such that `i < j` and
`nums[i] > nums[j]`. Intuitively, the inversion count measures how far the array
is from being sorted in ascending order: a sorted array has `0` inversions, and a
strictly descending array has the maximum `n * (n - 1) / 2` inversions.

Return the total number of inversions.

## Constraints

- `1 <= n <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- The answer can be as large as `n * (n - 1) / 2 ~= 5 * 10^9`, so use a 64-bit
  integer where relevant (Python integers are unbounded).

## Examples

### Example 1

```
Input:  nums = [2, 4, 1, 3, 5]
Output: 3
```

**Explanation:** The inversions are the pairs `(2,1)`, `(4,1)`, and `(4,3)` —
written as values, these are indices `(0,2)`, `(1,2)`, and `(1,3)`. Three pairs
are out of order.

### Example 2

```
Input:  nums = [5, 4, 3, 2, 1]
Output: 10
```

**Explanation:** The array is strictly descending, so **every** pair is an
inversion: `5 * 4 / 2 = 10` pairs.

### Example 3

```
Input:  nums = [1, 2, 3, 4, 5]
Output: 0
```

**Explanation:** The array is already sorted in ascending order, so there are no
inversions.

## Hint

Use **Merge Sort**. While merging two sorted halves, every time you pick an
element from the right half before the left half is exhausted, all the remaining
left-half elements form inversions with it — count them in bulk during the merge.
