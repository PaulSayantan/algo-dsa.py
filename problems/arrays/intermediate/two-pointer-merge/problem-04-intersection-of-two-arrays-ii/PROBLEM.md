# Intersection of Two Arrays II

**Difficulty:** Easy

**Source:** LeetCode 350 — Intersection of Two Arrays II

## Description

Given two integer arrays `nums1` and `nums2`, return an array of their **intersection**.
Each element in the result must appear **as many times as it shows in both arrays**, and
you may return the result in any order.

This is a multiset intersection: if a value appears twice in `nums1` and three times in
`nums2`, it appears `min(2, 3) = 2` times in the output.

**Follow-up:** What if the given arrays are already **sorted**? How would you optimize
your algorithm? (That follow-up is the point of this exercise.)

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

## Examples

### Example 1

```
Input:  nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Explanation: 2 appears twice in nums1 and twice in nums2, so it appears
             min(2,2) = 2 times. 1 is not in nums2, so it is excluded.
```

### Example 2

```
Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: 4 appears once in nums1 and twice in nums2 -> min = 1.
             9 appears once in nums1 and twice in nums2 -> min = 1.
             (Order may vary; [9,4] is also accepted.)
```

### Example 3

```
Input:  nums1 = [1,2,3], nums2 = [4,5,6]
Output: []
Explanation: The two arrays share no values, so the intersection is empty.
```

## Hint

If you first **sort both arrays** (or they arrive sorted per the follow-up), use the
**Two-Pointer Merge** technique: advance the pointer at the smaller element; when the two
elements are equal, emit it and advance both. This runs in linear time after sorting and
uses only `O(1)` extra space.
