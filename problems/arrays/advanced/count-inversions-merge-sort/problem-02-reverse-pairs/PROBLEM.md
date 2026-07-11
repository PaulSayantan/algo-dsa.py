# Reverse Pairs

**Difficulty:** Hard

**Source:** LeetCode 493 — "Reverse Pairs"

## Description

Given an integer array `nums`, return the number of **reverse pairs**.

A reverse pair is a pair `(i, j)` where:

- `0 <= i < j < nums.length`, and
- `nums[i] > 2 * nums[j]`.

This is a variant of the classic inversion count. Instead of the condition
`a[i] > a[j]`, the "out of order" condition is now `nums[i] > 2 * nums[j]`,
which makes the counting a little more delicate because the sorted order used to
sort the array is *not* the same as the order used to test the pair condition.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Beware of overflow: `2 * nums[j]` can exceed 32-bit range in some languages
  (in Python this is automatic; elsewhere widen to 64-bit before doubling).

## Examples

### Example 1

```
Input:  nums = [1, 3, 2, 3, 1]
Output: 2
Explanation: The reverse pairs are:
  (i=1, j=4): nums[1] = 3 > 2 * nums[4] = 2 * 1 = 2  ->  3 > 2  (valid)
  (i=3, j=4): nums[3] = 3 > 2 * nums[4] = 2 * 1 = 2  ->  3 > 2  (valid)
No other pair satisfies nums[i] > 2 * nums[j].
```

### Example 2

```
Input:  nums = [2, 4, 3, 5, 1]
Output: 3
Explanation: All three valid pairs use j = 4 (nums[j] = 1, so 2*nums[j] = 2):
  (i=1, j=4): 4 > 2   (valid)
  (i=2, j=4): 3 > 2   (valid)
  (i=3, j=4): 5 > 2   (valid)
nums[0] = 2 is not > 2, and no pair with j < 4 qualifies.
```

## Hint

Use **Count Inversions (merge sort)**, but split the merge into two phases: a
dedicated counting scan that tests `left[i] > 2 * right[j]` (advancing over the
right half), followed by the normal merge that keeps the halves sorted. Because
each half is sorted, the count for a fixed `j` grows monotonically, so a single
two-pointer sweep suffices per level.
