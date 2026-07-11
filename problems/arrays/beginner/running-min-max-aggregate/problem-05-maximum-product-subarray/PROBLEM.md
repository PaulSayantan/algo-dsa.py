# Maximum Product Subarray

**Difficulty:** Medium

**Source:** LeetCode 152 — Maximum Product Subarray

## Description

Given an integer array `nums`, find a contiguous non-empty subarray within the
array that has the largest **product**, and return that product.

The test cases are generated so that the answer fits in a 32-bit integer.

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any prefix of `nums` is guaranteed to fit in a 32-bit integer.
- The subarray must be non-empty.

## Examples

### Example 1

```
Input:  nums = [2, 3, -2, 4]
Output: 6
Explanation: The subarray [2, 3] has the largest product 6. Including -2 would
flip the sign, and [4] alone is only 4.
```

### Example 2

```
Input:  nums = [-2, 0, -1]
Output: 0
Explanation: The result cannot be a product that spans the 0 unless it is 0
itself. [-2] gives -2, [-1] gives -1, and [0] gives 0, so the best is 0.
```

### Example 3

```
Input:  nums = [-2, 3, -4]
Output: 24
Explanation: The whole array [-2, 3, -4] multiplies to 24: two negatives make a
positive. This beats any shorter subarray.
```

## Hint

A negative number can turn the smallest (most negative) running product into the
largest. Carry BOTH a **Running Maximum** and a **Running Minimum** product
ending at the current index, and swap them when the current element is negative.
