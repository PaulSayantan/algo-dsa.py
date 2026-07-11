# Maximum Sum Circular Subarray

**Difficulty:** Medium

**Source:** LeetCode 918 — Maximum Sum Circular Subarray

## Description

Given a **circular** integer array `nums` of length `n`, return the maximum
possible sum of a non-empty subarray of `nums`.

A *circular array* means the end of the array connects to the beginning:
formally, the next element of `nums[i]` is `nums[(i + 1) % n]`.

A subarray may only include each element of the fixed buffer `nums` **at most
once**. Formally, for a subarray `nums[i], nums[i+1], ..., nums[j]`, there does
not exist `i <= k1, k2 <= j` with `k1 % n == k2 % n` (no element is used twice).

## Constraints

- `n == nums.length`
- `1 <= n <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

## Examples

### Example 1

```
Input:  nums = [1, -2, 3, -2]
Output: 3
Explanation: The best subarray is [3], with sum 3. It does not need to wrap.
```

### Example 2

```
Input:  nums = [5, -3, 5]
Output: 10
Explanation: The best subarray wraps around: [5, 5] using the last element and
             the first element (5 + 5 = 10). Equivalently, remove the middle -3,
             which is the minimum subarray, from the total sum 7: 7 - (-3) = 10.
```

### Example 3

```
Input:  nums = [-3, -2, -3]
Output: -2
Explanation: All numbers are negative, so the best is the single element [-2].
             The wrap-around formula would give total - min = 0 here, but the
             empty subarray is NOT allowed, so we fall back to plain Kadane.
```

## Hint

The answer is either a normal (non-wrapping) subarray or a wrapping one. A
wrapping maximum equals `total - (minimum subarray sum)`. Run **Kadane's
Algorithm** for both the maximum and the minimum, with one special case when
every element is negative.

## Constraints on the answer

- Non-wrapping case: standard maximum subarray.
- Wrapping case: `totalSum - minSubarraySum`, valid only when the removed
  (minimum) part is not the entire array.
