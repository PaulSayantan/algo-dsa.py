# Three-Way Partition Around a Range

**Difficulty:** Medium

**Source:** GeeksforGeeks — "Three way partitioning of an array around a given range"

## Description

Given an array `arr` and two integers `lowVal` and `highVal` (with `lowVal <= highVal`),
partition the array **in place** into three contiguous regions so that:

1. All elements **strictly less than** `lowVal` come first.
2. All elements in the **inclusive range** `[lowVal, highVal]` come next.
3. All elements **strictly greater than** `highVal` come last.

The relative order **within** each region does not matter — only the three-way grouping
must be correct. Do it in a single pass with constant extra space. Modify `arr` in place;
you may also return it.

## Constraints

- `1 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`
- `-10^9 <= lowVal <= highVal <= 10^9`

## Examples

### Example 1

```
Input:  arr = [1, 2, 3, 3, 4], lowVal = 1, highVal = 2
Output: [1, 2, 3, 3, 4]
```

Explanation: Elements `< 1`: none. In range `[1,2]`: `1, 2`. Elements `> 2`: `3, 3, 4`.
One valid arrangement is `[1, 2, 3, 3, 4]` — the first region is empty, the middle holds
`1,2`, and the last holds `3,3,4`.

### Example 2

```
Input:  arr = [1, 4, 2, -2, 5, 8, 0], lowVal = 2, highVal = 5
Output: [1, 0, -2, 2, 4, 5, 8]
```

Explanation: Elements `< 2`: `1, 0, -2`. In range `[2,5]`: `2, 4, 5`. Elements `> 5`: `8`.
One valid one-pass result is `[1, 0, -2, 2, 4, 5, 8]` (region membership is what matters,
not the internal order).

### Example 3

```
Input:  arr = [7, 7, 7], lowVal = 1, highVal = 3
Output: [7, 7, 7]
```

Explanation: Every element is `> highVal`, so they all land in the third region and the
array is unchanged.

## Hint

This is the general **Dutch National Flag (3-way partition)** with a range instead of a
single pivot: use `< lowVal`, `in [lowVal, highVal]`, and `> highVal` as the three
categories, driven by `low`, `mid`, and `high` pointers.
