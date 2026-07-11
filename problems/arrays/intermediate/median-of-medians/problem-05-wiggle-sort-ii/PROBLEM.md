# Wiggle Sort II

**Difficulty:** Hard

Source: LeetCode 324 "Wiggle Sort II".

## Description

Given an integer array `nums`, reorder it **in place** so that

```
nums[0] < nums[1] > nums[2] < nums[3] > nums[4] < ...
```

That is, every even-indexed element is strictly less than its neighbors and
every odd-indexed element is strictly greater than its neighbors. You may assume
the input always has at least one valid answer.

The natural strategy is: find the median, split the values into a "small" half
and a "large" half, then interleave them so that no two equal elements land in
adjacent wiggle slots. Finding the median is the crux, and it should be done in
**worst-case O(n)** using a deterministic selection — you should not need a full
O(n log n) sort.

The follow-up asks for O(n) time and O(1) extra space; the O(n)-time,
O(n)-space version built on deterministic selection is the intended core here.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 5000`
- It is guaranteed that there will be an answer for the given input array.

## Examples

### Example 1
```
Input:  nums = [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
Explanation: Check the wiggle pattern for [1, 6, 1, 5, 1, 4]:
1 < 6 > 1 < 5 > 1 < 4. Every comparison holds, so this is valid.
(Other valid answers such as [2-way interleavings] are also accepted.)
```

### Example 2
```
Input:  nums = [1, 3, 2, 2, 3, 1]
Output: [2, 3, 1, 3, 1, 2]
Explanation: Check the wiggle pattern for [2, 3, 1, 3, 1, 2]:
2 < 3 > 1 < 3 > 1 < 2. Every comparison holds, so this is valid.
```

## Hint

Find the median with **Median of Medians** (worst-case linear selection), then
place the larger half and smaller half into interleaved positions using an
index mapping so that equal values near the median never end up adjacent.
