# Kth Largest Element in an Array

**Difficulty:** Medium

**Source:** LeetCode 215 — Kth Largest Element in an Array

## Description

Given an integer array `nums` and an integer `k`, return the **k-th largest element**
in the array.

Note that it is the k-th largest element in *sorted order*, not the k-th distinct
element. For example, in `[3, 2, 1, 5, 6, 4]` the 2nd largest element is `5`.

Can you solve it **without fully sorting** the array? A full sort is O(n log n), but
you do not need the whole array in order — you only need one order statistic. The
partition step of Quick Sort lets you discard half the array on each step and find the
answer in **average O(n)** time. This variant of Quick Sort is called **Quickselect**.

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
Explanation: Sorted ascending the array is [1, 2, 3, 4, 5, 6]; the 2nd largest value
is 5.
```

### Example 2

```
Input:  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
Explanation: Sorted ascending it is [1, 2, 2, 3, 3, 4, 5, 5, 6]. Counting from the
largest: 6 (1st), 5 (2nd), 5 (3rd), 4 (4th). Duplicates each count separately.
```

### Example 3

```
Input:  nums = [1], k = 1
Output: 1
Explanation: With one element, the 1st largest is that element itself.
```

## Hint

Use **Quickselect**, a Quick Sort variant. Partition around a (random) pivot; the pivot
lands at its final sorted index. The k-th largest is the element at index
`len(nums) - k` in ascending order, so recurse into only the side that contains that
target index instead of sorting both sides.
