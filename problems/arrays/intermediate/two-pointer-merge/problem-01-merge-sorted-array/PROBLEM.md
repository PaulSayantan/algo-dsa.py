# Merge Sorted Array

**Difficulty:** Easy

**Source:** LeetCode 88 — Merge Sorted Array

## Description

You are given two integer arrays `nums1` and `nums2`, each sorted in
**non-decreasing** order, along with two integers `m` and `n` representing the number
of real elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in non-decreasing order.

The merged result should **not** be returned by the function; instead it must be stored
**inside the array `nums1`**. To make room, `nums1` has a length of `m + n`, where the
first `m` entries are the elements that should be merged and the last `n` entries are
set to `0` and should be ignored. `nums2` has length `n`.

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
Explanation: We merge [1,2,3] and [2,5,6]. The combined sorted result [1,2,2,3,5,6]
             is written back into nums1.
```

### Example 2

```
Input:  nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: nums2 is empty, so nums1 already holds the merged result.
```

### Example 3

```
Input:  nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: nums1 has no real elements (m = 0); the single 0 is a placeholder that gets
             overwritten by nums2's value 1.
```

## Hint

Use the **Two-Pointer Merge** technique. Because `nums1` has spare room at the *end*,
consider walking the pointers from the largest elements downward so you never overwrite
a value you still need to read.
