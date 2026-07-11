# Find Peak Element

**Difficulty:** Medium

**Source:** LeetCode 162 — Find Peak Element

## Description

A **peak element** is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array `nums`, find a peak element and return its
index. If the array contains multiple peaks, return the index to **any** of the
peaks.

You may imagine that `nums[-1] = nums[n] = -∞` (negative infinity). In other
words, an element is always considered strictly greater than a neighbor that is
outside the array. Adjacent elements are guaranteed to be **unequal**
(`nums[i] != nums[i + 1]` for all valid `i`).

You must write an algorithm that runs in `O(log n)` time.

## Constraints

- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

## Examples

### Example 1

```
Input:  nums = [1, 2, 3, 1]
Output: 2
Explanation: 3 is a peak element and its index is 2 (neighbors 2 and 1 are both
smaller).
```

### Example 2

```
Input:  nums = [1, 2, 1, 3, 5, 6, 4]
Output: 5
Explanation: The array has peaks at index 1 (value 2) and index 5 (value 6).
Returning index 5 is accepted; returning 1 would also be accepted.
```

### Example 3

```
Input:  nums = [1]
Output: 0
Explanation: The only element is a peak because both out-of-bounds neighbors are
treated as negative infinity.
```

## Hint

Use **Binary Search** on the *slope*. Compare `nums[mid]` with `nums[mid + 1]`:
if you are going uphill, a peak must lie to the right; if downhill, a peak lies
at `mid` or to the left.
