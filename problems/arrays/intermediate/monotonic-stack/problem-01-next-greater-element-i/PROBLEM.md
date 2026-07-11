# Next Greater Element I

**Difficulty:** Easy

**Source:** LeetCode 496 — Next Greater Element I

## Description

You are given two **distinct**-valued integer arrays `nums1` and `nums2`, where
`nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that
`nums1[i] == nums2[j]` and determine the **next greater element** of
`nums2[j]` in `nums2`.

The *next greater element* of a value `x` in an array is the first element that
is strictly greater than `x` and appears to its **right** in the same array. If
there is no such element, the answer for that value is `-1`.

Return an array `ans` of the same length as `nums1` such that `ans[i]` is the
next greater element as described above for `nums1[i]`.

## Constraints

- `1 <= nums1.length <= nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 10^4`
- All integers in `nums1` and `nums2` are **unique**.
- All integers of `nums1` also appear in `nums2`.

## Examples

### Example 1

```
Input:  nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]
```

**Explanation:**
- For `4` (at index 2 in `nums2`): there is no greater element to its right, so `-1`.
- For `1` (at index 0 in `nums2`): the next greater element is `3`.
- For `2` (at index 3 in `nums2`): there is no element to its right, so `-1`.

### Example 2

```
Input:  nums1 = [2, 4], nums2 = [1, 2, 3, 4]
Output: [3, -1]
```

**Explanation:**
- For `2` (index 1 in `nums2`): the next greater element to its right is `3`.
- For `4` (index 3 in `nums2`): there is nothing to its right, so `-1`.

## Hint

Precompute the next greater element for **every** value in `nums2` in a single
left-to-right pass using a **Monotonic Stack** (kept decreasing), storing the
results in a hash map, then look up each value from `nums1`.
