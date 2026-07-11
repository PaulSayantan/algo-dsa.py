# Sort a K-Sorted (Nearly Sorted) Array

**Difficulty:** Medium

*Source: Classic interview / GeeksforGeeks — "Sort a nearly sorted (or K-sorted) array".*

## Description

You are given an array `nums` that is **almost sorted**: every element is at most `k`
positions away from the position it would occupy in the fully sorted array. Sort the array
into ascending order.

Because the array is nearly sorted, you should exploit that structure rather than running a
full general-purpose sort. Insertion sort is **adaptive** — its inner loop stops as soon as an
element is in place — so on a `k`-sorted array it only ever shifts an element a few slots,
giving `O(n * k)` time. When `k` is small this is close to linear and beats a generic
`O(n log n)` sort in practice.

Return the sorted array (in place is fine).

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= k < nums.length`
- Every element is guaranteed to be at most `k` indices from its final sorted position.
- `-10^9 <= nums[i] <= 10^9`

## Examples

**Example 1**

```
Input:  nums = [3, 1, 2, 5, 4, 7, 6], k = 2
Output: [1, 2, 3, 4, 5, 6, 7]
```
Explanation: No element is more than 2 slots from where it belongs (e.g. `3` moves from
index 0 to index 2). Insertion sort shifts each element at most 2 places.

**Example 2**

```
Input:  nums = [2, 1, 3, 4], k = 1
Output: [1, 2, 3, 4]
```
Explanation: Only the adjacent pair `2, 1` is out of order; each element is at most 1 slot
from its final position.

**Example 3**

```
Input:  nums = [6, 5, 3, 2, 8, 10, 9], k = 3
Output: [2, 3, 5, 6, 8, 9, 10]
```
Explanation: `6` (index 0) and `2` (index 3) are each 3 positions from their sorted spots, so
`k = 3`; every element still lands within `k` shifts.

## Hint

Use **Insertion Sort**. On a `k`-sorted array the inner shift loop runs at most `k` times per
element because the correct slot is never more than `k` positions to the left, so the whole
sort costs `O(n * k)`.
