# First and Last Position in an Unbounded Sorted Array

**Difficulty:** Medium

**Source:** Variant of LeetCode 34 ("Find First and Last Position of Element in
Sorted Array") adapted to an unknown-size `ArrayReader`

## Description

You are given a sorted-ascending array of integers that **may contain
duplicates**, but its length is hidden. You access it through
`reader.get(i)`, which returns the element at index `i` when in range and the
sentinel `2^31 - 1` for any out-of-bounds index.

Given the `reader` and a `target`, return a pair `[first, last]` where `first`
is the index of the first occurrence of `target` and `last` is the index of its
last occurrence. If `target` does not appear, return `[-1, -1]`.

Because the length is unknown, you must first gallop outward to bound the region
that could contain `target`, then run two boundary binary searches (lower bound
and upper bound) inside that region.

## Constraints

- The readable prefix has length `0 <= n <= 10^9`.
- `-10^9 <= reader.get(i) <= 10^9` for in-range `i`; out-of-bounds returns
  `2^31 - 1`.
- The array is sorted in non-decreasing order; duplicates are allowed.
- The largest valid index fits in a 32-bit signed integer.

## Examples

**Example 1**

```
Input:  arr = [5, 7, 7, 8, 8, 8, 10], target = 8
Output: [3, 5]
Explanation: 8 first appears at index 3 and last appears at index 5. Galloping
bounds the region, then a lower-bound search yields 3 and an upper-bound search
yields 5.
```

**Example 2**

```
Input:  arr = [5, 7, 7, 8, 8, 8, 10], target = 6
Output: [-1, -1]
Explanation: 6 is not present, so both boundaries are -1.
```

**Example 3**

```
Input:  arr = [2, 2], target = 2
Output: [0, 1]
Explanation: Both elements equal the target. get(2) returns the sentinel
2147483647 (out of bounds), which bounds the window; the first occurrence is 0
and the last is 1.
```

## Hint

Use Exponential (Galloping) Search to find an upper bound `hi` where
`reader.get(hi) >= target` (the sentinel counts), then run two bisection
searches inside `[0, hi]`: a lower-bound search for the first index with value
`>= target` and an upper-bound search for the first index with value `> target`.
