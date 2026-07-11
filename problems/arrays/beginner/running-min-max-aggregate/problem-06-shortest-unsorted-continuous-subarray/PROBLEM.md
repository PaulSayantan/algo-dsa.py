# Shortest Unsorted Continuous Subarray

**Difficulty:** Medium

**Source:** LeetCode 581 — Shortest Unsorted Continuous Subarray

## Description

Given an integer array `nums`, you need to find one continuous subarray such
that if you only sort this subarray in non-decreasing order, then the whole
array will be sorted in non-decreasing order.

Return the length of the shortest such subarray. If the array is already sorted,
return `0`.

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
- A solution running in O(n) time is expected.

## Examples

### Example 1

```
Input:  nums = [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] (indices 1..5) to make the whole
array non-decreasing. That subarray has length 5.
```

### Example 2

```
Input:  nums = [1, 2, 3, 4]
Output: 0
Explanation: The array is already sorted in non-decreasing order, so no
subarray needs sorting.
```

### Example 3

```
Input:  nums = [1, 3, 5, 4, 2]
Output: 4
Explanation: Sorting [3, 5, 4, 2] (indices 1..4) yields [1, 2, 3, 4, 5]. The
first element 1 is already in place, so the shortest window has length 4.
```

## Hint

The right boundary is the **last** index whose value falls below the
**Running Maximum** scanned left to right; the left boundary is the **first**
index whose value exceeds the **Running Minimum** scanned right to left.
