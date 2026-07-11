# Median of an Unsorted Array

**Difficulty:** Medium

Source: Classic order-statistics problem (CLRS §9.3, "Medians and order
statistics"). The direct motivating application of Median of Medians.

## Description

Given an unsorted integer array `nums`, return its **lower median** in
**worst-case O(n)** time.

The lower median is defined as the element at 0-indexed position
`(n - 1) // 2` of the sorted array, where `n = len(nums)`. Equivalently, it is
the `⌈n/2⌉`-th smallest element (1-indexed).

- For odd `n`, this is the unique middle element.
- For even `n`, this is the **smaller** of the two middle elements (the left one).

You must not fully sort the array; sorting is O(n log n) and is not the intended
solution. The goal is a deterministic linear-time algorithm.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- The array may contain duplicates.

## Examples

### Example 1
```
Input:  nums = [3, 1, 2]
Output: 2
Explanation: Sorted the array is [1, 2, 3]. n = 3, lower median index is
(3 - 1) // 2 = 1, so the answer is 2.
```

### Example 2
```
Input:  nums = [7, 10, 4, 3, 20, 15]
Output: 7
Explanation: Sorted the array is [3, 4, 7, 10, 15, 20]. n = 6, lower median
index is (6 - 1) // 2 = 2, so the answer is 7 (the smaller of the two middle
values 7 and 10).
```

### Example 3
```
Input:  nums = [5]
Output: 5
Explanation: A single-element array; its median is that element.
```

## Hint

Finding a median is just selecting the element of rank `⌈n/2⌉`. Use **Median of
Medians** to select that rank deterministically in worst-case linear time.
