# Relative Sort Array

**Difficulty:** Easy

**Source:** LeetCode 1122 — Relative Sort Array

## Description

You are given two integer arrays `arr1` and `arr2`. The elements of `arr2` are **distinct**,
and every element of `arr2` also appears somewhere in `arr1`.

Sort the elements of `arr1` so that the relative ordering of items matches the order they
appear in `arr2`. Elements that do **not** appear in `arr2` should be placed at the **end** of
`arr1` in **ascending** order.

Since all values in `arr1` are non-negative integers bounded by 1000, you can tally how many
times each value occurs and then emit them in whatever order you like — first following
`arr2`, then sweeping the remaining values in ascending numeric order.

## Constraints

- `1 <= arr1.length, arr2.length <= 1000`
- `0 <= arr1[i], arr2[i] <= 1000`
- All the elements of `arr2` are **distinct**.
- Each element of `arr2` is present in `arr1`.

## Examples

### Example 1

```
Input:  arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
```

**Explanation:** The values named in `arr2` come first in `arr2`'s order — three `2`s, one
`1`, one `4`, two `3`s, one `9`, one `6`. The leftovers `7` and `19` are not in `arr2`, so
they trail at the end in ascending order.

### Example 2

```
Input:  arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
```

**Explanation:** `22, 28, 8, 6` appear first following `arr2`'s order (each once). The
remaining values `17` and `44` are absent from `arr2`, so they follow in ascending order.

## Hint

The values are bounded by 1000, so use a **Counting Sort** count array indexed by value. Emit
the values named in `arr2` first (draining their counts), then sweep the count array from `0`
upward to append every remaining value in ascending order.
