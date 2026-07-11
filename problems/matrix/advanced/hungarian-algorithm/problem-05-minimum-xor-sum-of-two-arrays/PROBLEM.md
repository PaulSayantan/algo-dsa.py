# Minimum XOR Sum of Two Arrays

**Difficulty:** Hard

**Source:** LeetCode 1879 — "Minimum XOR Sum of Two Arrays".

## Description

You are given two integer arrays `nums1` and `nums2`, both of length `n`.

The **XOR sum** of the two arrays is defined as
`(nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n-1] XOR nums2[n-1])`
(0-indexed).

For example, the XOR sum of `[1, 2, 3]` and `[3, 2, 1]` is
`(1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4`.

You may **rearrange the elements of `nums2`** in any order. Return the **minimum**
XOR sum achievable after an optimal rearrangement of `nums2`.

## Constraints

- `n == nums1.length == nums2.length`
- `1 <= n <= 14`
- `0 <= nums1[i], nums2[i] <= 10^7`

## Examples

### Example 1

```
Input:  nums1 = [1, 2], nums2 = [2, 3]
Output: 2
Explanation: Rearrange nums2 to [3, 2]. The XOR sum is (1 XOR 3) + (2 XOR 2)
= 2 + 0 = 2. The other arrangement [2, 3] gives (1 XOR 2) + (2 XOR 3) = 3 + 1
= 4, so 2 is the minimum.
```

### Example 2

```
Input:  nums1 = [1, 0, 3], nums2 = [5, 3, 4]
Output: 8
Explanation: Rearrange nums2 to [5, 4, 3]. The XOR sum is (1 XOR 5) + (0 XOR 4)
+ (3 XOR 3) = 4 + 4 + 0 = 8. No rearrangement of nums2 yields a smaller XOR sum,
so 8 is the minimum.
```

### Example 3

```
Input:  nums1 = [0, 2], nums2 = [0, 3]
Output: 1
Explanation: Keep nums2 as [0, 3]: (0 XOR 0) + (2 XOR 3) = 0 + 1 = 1.
Swapping to [3, 0] gives (0 XOR 3) + (2 XOR 0) = 3 + 2 = 5, so 1 is the minimum.
```

## Hint

Model this as an assignment problem: `cost[i][j] = nums1[i] XOR nums2[j]` is an
`n x n` cost matrix, and you want the minimum-cost perfect matching between the
two arrays. For `n <= 14` a bitmask DP (`O(n * 2^n)`) works, but the general
polynomial tool is the **Hungarian Algorithm** (`O(n^3)`), which scales far
beyond `n = 14`.
