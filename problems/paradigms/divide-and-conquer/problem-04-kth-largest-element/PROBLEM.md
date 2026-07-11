# Kth Largest Element in an Array

**Difficulty:** Medium

**Source:** LeetCode 215 (Kth Largest Element in an Array)

## Description

Given an integer array `nums` and an integer `k`, return the **k-th largest element**
in the array.

Note that it is the k-th largest element in **sorted order**, not the k-th distinct
element. (So in `[3, 2, 3, 1, 2, 4, 5, 5, 6]` the 4th largest is `4`, counting
duplicates.)

Can you solve it **without fully sorting** the array? The Divide and Conquer answer is
**quickselect**: partition around a pivot and recurse into only the side that must
contain the answer — giving `O(n)` average time.

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
```

Explanation: Sorted descending the array is `[6, 5, 4, 3, 2, 1]`; the 2nd largest
element is `5`.

### Example 2

```
Input:  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

Explanation: Sorted descending the array is `[6, 5, 5, 4, 3, 3, 2, 2, 1]`. Counting
duplicates, the 4th element is `4`, so the answer is `4`.

### Example 3

```
Input:  nums = [1], k = 1
Output: 1
```

Explanation: The array has one element, which is the 1st largest.

## Hint

Use **Divide and Conquer** (quickselect). Pick a pivot and partition the array so
elements on one side are all larger and the other side all smaller. The pivot lands at
its final sorted position; compare that position to the target rank and **recurse into
only the one side** that must contain the k-th largest — no need to sort or recurse
into both halves.
