# Count Subarrays With Bounded Range

**Difficulty:** Medium

**Source:** Classic — count subarrays with max - min <= limit

## Description

Given an integer array `nums` and an integer `limit`, return the **number** of non-empty contiguous subarrays in which the difference between the maximum and minimum element is `<= limit`. Because the bounded-range property is monotone (shrinking a valid window keeps it valid), every window ending at index `right` contributes `right - left + 1` valid subarrays.

## Examples

### Example 1

```
Input:  nums = [1,2,3,4], limit = 1
Output: 7
```

**Explanation:** All length-1 (4) plus [1,2],[2,3],[3,4].

## Hint

Same two-deque window as LC 1438, but accumulate (right - left + 1) at every step instead of a max length.
