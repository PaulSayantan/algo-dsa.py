# Intersection of Two Arrays II

**Difficulty:** Easy

**Source:** LeetCode 350 (https://leetcode.com/problems/intersection-of-two-arrays-ii/)

## Description

Given two integer arrays `nums1` and `nums2`, return an array of their
**intersection**. Each element in the result must appear as many times as it
shows in **both** arrays, and you may return the result in any order.

Unlike a set intersection, this keeps multiplicities: if a value appears twice
in `nums1` and three times in `nums2`, it appears `min(2, 3) = 2` times in the
answer. This "minimum of the two counts" phrasing is exactly what frequency
counting handles cleanly.

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

## Examples

### Example 1

```
Input:  nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2, 2]
Explanation: 2 appears twice in nums1 and twice in nums2, so it appears
min(2, 2) = 2 times. 1 appears in nums1 but not nums2, so it is excluded.
```

### Example 2

```
Input:  nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [4, 9]
Explanation: 4 appears once in nums1 and twice in nums2 -> min(1, 2) = 1 time.
9 appears once in nums1 and twice in nums2 -> min(1, 2) = 1 time. The order
[9, 4] is equally valid.
```

### Example 3

```
Input:  nums1 = [1, 2, 2, 1], nums2 = [3, 4]
Output: []
Explanation: The arrays share no common values, so the intersection is empty.
```

## Hint

Use **Frequency Counting with a Hash Map**: count values in the smaller array,
then walk the other array, emitting a value while its remaining count is
positive.
