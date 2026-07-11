# Kth Smallest Element in an Array

**Difficulty:** Easy

Source: Classic selection problem (CLRS "Selection", §9.3). Closely related to
LeetCode 215 "Kth Largest Element in an Array".

## Description

Given an integer array `nums` and an integer `k` (1-indexed), return the
**k-th smallest** element in the array. The element is the value that would sit
at index `k - 1` if the array were sorted in non-decreasing order.

Duplicates count individually toward the rank: in `[2, 2, 3]` the 1st and 2nd
smallest are both `2`, and the 3rd smallest is `3`.

The obvious approach is to sort in O(n log n). The challenge here is to do it in
**worst-case O(n)** time by never fully sorting the array. That rules out the
"sort then index" trick as the intended answer, and it rules out relying on a
random pivot (which is only *expected* linear). You must guarantee a good pivot.

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `k` is 1-indexed (k = 1 asks for the minimum).

## Examples

### Example 1
```
Input:  nums = [12, 3, 5, 7, 4, 19, 26], k = 3
Output: 5
Explanation: Sorted the array is [3, 4, 5, 7, 12, 19, 26]. The element at
index k-1 = 2 is 5, so the 3rd smallest element is 5.
```

### Example 2
```
Input:  nums = [7, 10, 4, 3, 20, 15], k = 4
Output: 10
Explanation: Sorted the array is [3, 4, 7, 10, 15, 20]. The element at
index k-1 = 3 is 10, so the 4th smallest element is 10.
```

### Example 3
```
Input:  nums = [2, 2, 3], k = 2
Output: 2
Explanation: Sorted the array is [2, 2, 3]. Duplicates count individually, so
the 2nd smallest element is the second 2.
```

## Hint

Use the **Median of Medians** algorithm to deterministically choose a pivot that
splits off a constant fraction of the array, giving worst-case linear-time
selection (the deterministic version of Quickselect).
