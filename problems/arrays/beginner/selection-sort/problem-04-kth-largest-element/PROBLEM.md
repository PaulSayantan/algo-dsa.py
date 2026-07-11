# Kth Largest Element in an Array

**Difficulty:** Medium

**Source:** LeetCode 215 — "Kth Largest Element in an Array".

## Description

Given an integer array `nums` and an integer `k`, return the **k-th largest element** in the array.

Note that it is the k-th largest element in **sorted order**, not the k-th *distinct* element. So if
`nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]` and `k = 4`, the sorted (descending) order is
`6, 5, 5, 4, 3, 3, 2, 2, 1` and the 4th largest is `4`.

The intended approach here is a **partial Selection Sort**: run only `k` selection passes, each
moving the next-largest element to the front. After `k` passes, `nums[k-1]` is the answer — you never
have to sort the whole array.

## Constraints

- `1 <= k <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
```

**Explanation:** Descending order is `6, 5, 4, 3, 2, 1`. The 2nd largest is `5`. Two selection passes
pull `6` then `5` to the front, and `nums[1] == 5`.

### Example 2

```
Input:  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

**Explanation:** Descending order is `6, 5, 5, 4, 3, 3, 2, 2, 1`. Counting duplicates, the 4th
largest is `4`.

### Example 3

```
Input:  nums = [1], k = 1
Output: 1
```

**Explanation:** With a single element, the 1st largest is that element itself.

## Hint

You do not need to sort the entire array. Run **Selection Sort** but stop after exactly `k` passes,
each selecting the **maximum** of the unsorted suffix. The element now sitting at index `k - 1` is
the k-th largest.
