# Rank Transform of an Array

**Difficulty:** Easy

**Source:** LeetCode 1331 — Rank Transform of an Array

## Description

Given an array of integers `arr`, replace each element with its **rank**.

The rank represents how large the element is. The rules for the rank are:

- Rank is an integer starting from `1`.
- The larger the element, the larger the rank. If two elements are equal, their rank must
  be the same.
- Rank should be as small as possible. In other words, ranks are assigned so that the set
  of distinct values maps onto the consecutive integers `1, 2, 3, ...` with no gaps.

Return the array of ranks.

This is the purest form of coordinate compression: the "compressed index" of each value
(offset to start at 1 instead of 0) is exactly its rank.

## Constraints

- `0 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`

## Examples

### Example 1

```
Input:  arr = [40, 10, 20, 30]
Output: [4, 1, 2, 3]
```

**Explanation:** 40 is the largest (rank 4), 10 is the smallest (rank 1), 20 is the second
smallest (rank 2), and 30 is the third smallest (rank 3).

### Example 2

```
Input:  arr = [100, 100, 100]
Output: [1, 1, 1]
```

**Explanation:** All elements are equal, so they share the same (smallest) rank, 1.

### Example 3

```
Input:  arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
Output: [5, 3, 4, 2, 8, 6, 7, 1, 3]
```

**Explanation:** The sorted distinct values are `[5, 9, 12, 28, 37, 56, 80, 100]`, which map
to ranks `1..8`. Notice both 12's receive rank 3.

## Hint

Use **Coordinate Compression**: sort the distinct values and map each original value to its
1-based position in that sorted-unique list.
