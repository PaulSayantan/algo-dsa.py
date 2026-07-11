# Kth Largest Element in an Array

**Difficulty:** Medium

**Source:** LeetCode 215 — Kth Largest Element in an Array

## Description

Given an integer array `nums` and an integer `k`, return the `k`-th largest element in the
array.

Note that it is the `k`-th largest element in *sorted order*, **not** the `k`-th distinct
element. For example, in `[3, 2, 3, 1, 2, 4, 5, 5, 6]` the 4th largest element is `4` (the
sorted-descending order is `6, 5, 5, 4, ...`, and the 4th entry is `4`), even though `4` is
not the 4th *distinct* value.

Can you solve it **without fully sorting** the array — ideally in average linear time?

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
```

**Explanation:** Sorted in descending order the array is `[6, 5, 4, 3, 2, 1]`. The 2nd
largest element is `5`.

### Example 2

```
Input:  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

**Explanation:** Sorted in descending order the array is `[6, 5, 5, 4, 3, 3, 2, 2, 1]`. The
4th element (counting duplicates) is `4`.

### Example 3

```
Input:  nums = [1], k = 1
Output: 1
```

**Explanation:** There is only one element, so the 1st largest is `1` itself.

## Hint

Use **Randomization**: quickselect with a **randomly chosen pivot**. Partition around the
pivot and recurse into only the side that must contain the answer. The random pivot gives
O(n) expected time and defeats adversarial (e.g. already-sorted) inputs that would make a
fixed-pivot version degrade to O(n^2).
