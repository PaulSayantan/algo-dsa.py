# Minimum Adjacent Swaps to Sort

**Difficulty:** Hard

*Source: Classic competitive-programming problem (minimum adjacent swaps to sort = inversion count).*

## Description

Given an array `arr`, you may repeatedly swap any two **adjacent** elements. Return the
**minimum** number of adjacent swaps required to sort the array into non-decreasing order.

This value is exactly the number of **inversions** in the array — pairs `(i, j)` with `i < j`
and `arr[i] > arr[j]` — and it is precisely the number of swaps a plain **Bubble Sort** would
perform. That connection is the whole point of this problem: bubble sort is the algorithm that
achieves this minimum by only ever fixing adjacent out-of-order pairs.

## Constraints

- `1 <= arr.length <= 2000`
- `-10^9 <= arr[i] <= 10^9`
- The array may contain duplicates.

(With `n <= 2000`, an `O(n^2)` bubble-sort-style count is acceptable.)

## Examples

**Example 1**

```
Input:  arr = [2, 8, 5, 3, 9, 4]
Output: 6
```
Explanation: The inversions are (8,5), (8,3), (8,4), (5,3), (5,4), (9,4) — six pairs where a
larger value precedes a smaller one — so a minimum of 6 adjacent swaps sorts the array to
`[2, 3, 4, 5, 8, 9]`.

**Example 2**

```
Input:  arr = [1, 2, 3, 4, 5]
Output: 0
```
Explanation: Already sorted; there are no inversions, so no swaps are needed.

**Example 3**

```
Input:  arr = [3, 2, 3, 1]
Output: 4
```
Explanation: Inversions: (3,2), (3,1), (2,1), (3,1) = 4 pairs. Note the first `3` beats the
`2`, the `1`, and forms an inversion with the trailing `1`; the middle `3` also beats the
trailing `1`; and `2` beats `1`. Equal `3`s do not form an inversion with each other. Four
adjacent swaps yield `[1, 2, 3, 3]`.

## Hint

The answer is the inversion count. You can obtain it directly by running **Bubble Sort** and
counting each adjacent swap, since bubble sort removes exactly one inversion per swap.
