# Count of Smaller Numbers After Self

**Difficulty:** Hard

**Source:** LeetCode 315 — "Count of Smaller Numbers After Self"

## Description

Given an integer array `nums`, return an integer array `counts` where
`counts[i]` is the number of elements to the **right** of `nums[i]` that are
**smaller** than `nums[i]`. Formally:

```
counts[i] = | { j : j > i and nums[j] < nums[i] } |
```

This is the "per-element" version of inversion counting: instead of a single
total, you must attribute each inversion to its left endpoint `i`. The sum of
all `counts[i]` equals the total number of inversions of `nums`.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Explanation:
  To the right of 5 there are {2, 1} smaller  -> 2
  To the right of 2 there is  {1} smaller     -> 1
  To the right of 6 there is  {1} smaller     -> 1
  To the right of 1 there is  {} smaller      -> 0
```

### Example 2

```
Input:  nums = [-1, -1]
Output: [0, 0]
Explanation: Neither -1 has a strictly smaller element to its right
(the other -1 is equal, not smaller), so both counts are 0.
```

## Hint

Use **Count Inversions (merge sort)** on `(value, original_index)` pairs. When
an element from the right half is merged ahead of some left elements, that right
element is smaller — but here we need to credit the *left* elements instead:
maintain a running count of how many right-half elements have already been
placed, and when you finally emit a left element, add that running count to its
answer slot (indexed by its original position).
