# Kth Largest Element in an Array

**Difficulty:** Medium

**Source:** LeetCode 215 — Kth Largest Element in an Array

## Description

Given an integer array `nums` and an integer `k`, return the **k-th largest element**
in the array.

Note that it is the k-th largest element in **sorted order**, not the k-th *distinct*
element. In other words, if you sorted the array in non-increasing order, you would
return the element at position `k` (1-indexed).

Can you solve it **without** fully sorting the array?

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
```

**Explanation:** Sorted in non-increasing order the array is `[6, 5, 4, 3, 2, 1]`.
The 2nd largest element is `5`.

### Example 2

```
Input:  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

**Explanation:** Sorted in non-increasing order the array is
`[6, 5, 5, 4, 3, 3, 2, 2, 1]`. The 4th element is `4`. Duplicates each count
separately, so both `5`s occupy positions 2 and 3.

### Example 3

```
Input:  nums = [1], k = 1
Output: 1
```

**Explanation:** There is a single element, which is trivially the 1st largest.

## Hint

The k-th largest element is the element that would sit at index `n - k` if the array
were sorted ascending. You can locate exactly that element in expected linear time with
**Quickselect** — partition around a pivot and recurse into only the side that contains
your target index.
