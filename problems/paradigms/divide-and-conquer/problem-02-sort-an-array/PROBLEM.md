# Sort an Array

**Difficulty:** Medium

**Source:** LeetCode 912 (Sort an Array)

## Description

Given an array of integers `nums`, sort the array in **ascending order** and return
it.

You must solve the problem **without using any built-in sort function**, and the
solution should run in `O(n log n)` time with the smallest space overhead reasonable.

This is the canonical Divide and Conquer exercise: implement **merge sort**. Split the
array into halves, sort each half recursively, then merge the two sorted halves into
one sorted array in linear time.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## Examples

### Example 1

```
Input:  nums = [5, 2, 3, 1]
Output: [1, 2, 3, 5]
```

Explanation: After sorting in ascending order the array becomes `[1, 2, 3, 5]`.

### Example 2

```
Input:  nums = [5, 1, 1, 2, 0, 0]
Output: [0, 0, 1, 1, 2, 5]
```

Explanation: The array contains duplicates (`1` twice, `0` twice); a correct sort
keeps all of them and orders every value ascending.

### Example 3

```
Input:  nums = [3, -1, -1, 4]
Output: [-1, -1, 3, 4]
```

Explanation: Negative values sort before positives; the two `-1`s come first.

## Hint

Use **Divide and Conquer**: recursively split the array into two halves, sort each
half, and then **merge** the two already-sorted halves by repeatedly taking the
smaller front element. The merge step is linear and is where the sortedness is
actually produced.
