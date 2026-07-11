# Next Greater Element I

**Difficulty:** Easy

**Source:** LeetCode 496 — Next Greater Element I

## Description

You are given two integer arrays `nums1` and `nums2`, where `nums1` is a **subset** of
`nums2`. All integers in both arrays are **distinct**.

For each element `nums1[i]`, find the **next greater element** in `nums2`. The next greater
element of a value `x` is the first element to the **right** of `x` in `nums2` that is
strictly greater than `x`. If no such element exists, the answer for that value is `-1`.

Return an array `ans` of the same length as `nums1`, where `ans[i]` is the next greater
element of `nums1[i]` as described above.

## Constraints

- `1 <= nums1.length <= nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 10^4`
- All integers in `nums1` and `nums2` are **distinct**.
- Every element of `nums1` also appears in `nums2`.

## Examples

### Example 1

```
Input:  nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]
```

**Explanation:**
- For `4` (in nums2 at index 2): nothing to its right is larger, so `-1`.
- For `1` (in nums2 at index 0): the next element `3` is larger, so `3`.
- For `2` (in nums2 at index 3): nothing to its right, so `-1`.

### Example 2

```
Input:  nums1 = [2, 4], nums2 = [1, 2, 3, 4]
Output: [3, -1]
```

**Explanation:**
- For `2`: the next greater element to its right is `3`.
- For `4`: it is the last element, so there is nothing greater; answer is `-1`.

## Hint

Precompute the next greater element for **every** value in `nums2` in one pass using a
**Monotonic Stack / Queue** (a decreasing stack), then answer each `nums1` query by lookup.
