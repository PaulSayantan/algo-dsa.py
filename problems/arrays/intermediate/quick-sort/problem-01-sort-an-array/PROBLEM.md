# Sort an Array

**Difficulty:** Medium

**Source:** LeetCode 912 — Sort an Array

## Description

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem **without using any built-in sort function** and, ideally,
with the best possible time complexity and the smallest possible additional space.
This is the canonical setting for implementing Quick Sort from scratch: pick a pivot,
partition the array around it, and recurse on each side in place.

Because the input may contain many duplicate values and adversarial orderings (for
example an already-sorted array), a naive fixed-pivot implementation can degrade to
O(n^2). A robust solution randomizes the pivot (or uses median-of-three) so that the
expected running time is O(n log n).

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## Examples

### Example 1

```
Input:  nums = [5, 2, 3, 1]
Output: [1, 2, 3, 5]
Explanation: After sorting the array in ascending order, the values line up as
1, 2, 3, 5.
```

### Example 2

```
Input:  nums = [5, 1, 1, 2, 0, 0]
Output: [0, 0, 1, 1, 2, 5]
Explanation: Duplicate values (two 0s and two 1s) are kept and placed contiguously in
ascending order.
```

### Example 3

```
Input:  nums = [3]
Output: [3]
Explanation: A single-element array is already sorted; the base case returns it
unchanged.
```

## Hint

Use **Quick Sort**: choose a pivot, partition the array so smaller elements sit left
and larger elements sit right, then recurse on both partitions. Randomize the pivot to
avoid the O(n^2) worst case on sorted or duplicate-heavy input.
