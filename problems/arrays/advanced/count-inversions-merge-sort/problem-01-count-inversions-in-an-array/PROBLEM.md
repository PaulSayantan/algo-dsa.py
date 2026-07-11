# Count Inversions in an Array

**Difficulty:** Medium

**Source:** Classic problem (CLRS 2.3, GeeksforGeeks "Count Inversions", SPOJ INVCNT)

## Description

Given an integer array `a` of length `n`, count the number of **inversions**.
An inversion is a pair of indices `(i, j)` such that:

- `i < j`, and
- `a[i] > a[j]`.

Intuitively, the inversion count tells you how many swaps of *adjacent*
elements a bubble sort would perform to sort the array, and thus how "far" the
array is from being sorted in ascending order.

An array sorted in ascending order has `0` inversions. An array sorted in
strictly descending order has the maximum possible number, `n * (n - 1) / 2`.

Return the total inversion count as an integer. The count can exceed the range
of a 32-bit integer for large inputs, so use a 64-bit type where relevant
(in Python, integers are unbounded, so this is automatic).

## Constraints

- `0 <= n <= 10^5`
- `-10^9 <= a[i] <= 10^9`
- Values are **not** guaranteed to be distinct; equal elements (`a[i] == a[j]`)
  do **not** form an inversion.

## Examples

### Example 1

```
Input:  a = [2, 4, 1, 3, 5]
Output: 3
Explanation: The inversions are the pairs (values) (2,1), (4,1), and (4,3).
By index they are (0,2), (1,2), and (1,3). No other pair is out of order.
```

### Example 2

```
Input:  a = [5, 4, 3, 2, 1]
Output: 10
Explanation: The array is strictly descending, so every one of the
C(5,2) = 10 pairs is an inversion. This is the maximum for n = 5.
```

### Example 3

```
Input:  a = [1, 2, 3, 4]
Output: 0
Explanation: The array is already sorted ascending, so there are no inversions.
```

## Hint

Comparing every pair is `O(n^2)`. Instead, use **Count Inversions (merge sort)**:
split the array, count inversions in each half recursively, then count the
"cross" inversions during the merge step — when an element from the right half
is placed before elements still remaining in the left half, all those remaining
left elements are larger and form inversions.
