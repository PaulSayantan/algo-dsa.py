# Kth Largest Element in an Array (3-way Quickselect)

**Difficulty:** Medium

**Source:** LeetCode 215 — Kth Largest Element in an Array

## Description

Given an integer array `nums` and an integer `k`, return the **kth largest element** in the
array.

Note that it is the kth largest element in **sorted order**, not the kth distinct element.
For example, in `[3, 2, 1, 5, 6, 4]` the 2nd largest element is `5`.

Can you solve it **without fully sorting** the array? The intended approach is
**quickselect using a Dutch National Flag 3-way partition**, which finds the answer in
**expected O(n)** time and is robust even when the array contains **many duplicate values**
(the equal block lets you resolve entire runs of equal keys at once).

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
```

Explanation: Sorted descending: `[6, 5, 4, 3, 2, 1]`. The 2nd largest is `5`.

### Example 2

```
Input:  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

Explanation: Sorted descending: `[6, 5, 5, 4, 3, 3, 2, 2, 1]`. The 4th element is `4`.
Note the duplicate 5s — the kth largest counts positions, not distinct values.

### Example 3

```
Input:  nums = [1], k = 1
Output: 1
```

Explanation: Only one element, which is trivially the 1st largest.

## Hint

Reframe "kth largest" as the index `n - k` in ascending order, then run **quickselect** whose
partition is the **Dutch National Flag (3-way partition)**. After partitioning around a pivot
into `< / == / >` regions, the equal block's index span tells you immediately whether the
target index is settled or which side to recurse into.
