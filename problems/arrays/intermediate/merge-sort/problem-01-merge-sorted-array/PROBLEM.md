# Merge Sorted Array

**Difficulty:** Easy

**Source:** LeetCode 88 — Merge Sorted Array

## Description

You are given two integer arrays `nums1` and `nums2`, both sorted in
**non-decreasing** order, and two integers `m` and `n` representing the number of
elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should **not** be returned by the function, but instead be
stored *inside* the array `nums1`. To accommodate this, `nums1` has a length of
`m + n`, where the first `m` elements denote the elements that should be merged,
and the last `n` elements are set to `0` and should be ignored. `nums2` has a
length of `n`.

This problem isolates the **merge** step that lies at the core of merge sort:
combining two already-sorted sequences into one.

## Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Examples

### Example 1

```
Input:  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

**Explanation:** The arrays we are merging are `[1,2,3]` and `[2,5,6]`. The
result of the merge is `[1,2,2,3,5,6]`, written back into `nums1`.

### Example 2

```
Input:  nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```

**Explanation:** The arrays we are merging are `[1]` and `[]`. There is nothing
to merge in from `nums2`, so `nums1` stays `[1]`.

### Example 3

```
Input:  nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
```

**Explanation:** The arrays we are merging are `[]` and `[1]`. The `0` in `nums1`
is just a placeholder and is overwritten by the `1` from `nums2`.

## Hint

Use the **Merge Sort** merge step. Because writing left-to-right could overwrite
values in `nums1` you have not yet processed, walk **three pointers from the
back** so you always write into already-vacated slots.
