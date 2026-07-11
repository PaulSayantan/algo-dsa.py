# Maximum Sum Circular Subarray

**Difficulty:** Medium

**Source:** LeetCode 918 — Maximum Sum Circular Subarray

## Description

Given a **circular** integer array `nums` of length `n`, return the maximum
possible sum of a **non-empty** subarray of `nums`.

A *circular array* means the end of the array connects to the beginning:
formally, the element after `nums[i]` is `nums[(i + 1) % n]`. A subarray may
therefore wrap around — for example, it can include some suffix of the array
followed by some prefix.

A subarray must be **non-empty**, and it may contain **each array element at
most once** (so a wrapping subarray's length is at most `n`).

## Constraints

- `n == nums.length`
- `1 <= n <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

## Examples

### Example 1

```
Input: nums = [1, -2, 3, -2]
Output: 3
Explanation: The best subarray is [3] (index 2), sum = 3. Here the optimal
answer does not wrap around.
```

### Example 2

```
Input: nums = [5, -3, 5]
Output: 10
Explanation: The best subarray wraps around: [5, 5] using index 2 then index 0
(the element -3 is skipped). Its sum is 10. Total = 7, minimum middle = -3,
so total - min = 7 - (-3) = 10.
```

### Example 3

```
Input: nums = [-3, -2, -3]
Output: -2
Explanation: Every element is negative, so no wrap helps. The best non-empty
subarray is the single element [-2], sum = -2.
```

## Hint

The best subarray either does not wrap (plain Kadane) or wraps — and a wrapping
subarray is the total minus the *minimum-sum* subarray in the middle. Watch the
all-negative case. This is the defining problem for Kadane's — Maximum Circular
Subarray.
