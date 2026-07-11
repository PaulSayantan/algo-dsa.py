# Maximum Product Subarray

**Difficulty:** Medium

**Source:** LeetCode 152 — Maximum Product Subarray

## Description

Given an integer array `nums`, find a contiguous non-empty subarray within the
array that has the largest **product**, and return that product.

The answer is guaranteed to fit in a 32-bit integer.

Unlike the sum version, products behave differently with negatives: multiplying
by a negative number flips the sign, so a very *small* (negative) running
product can suddenly become the *largest* product when it meets another negative
number. Zeros act as hard resets — any subarray spanning a zero has product `0`.

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is guaranteed to fit in a 32-bit integer.

## Examples

### Example 1

```
Input:  nums = [2, 3, -2, 4]
Output: 6
Explanation: The subarray [2, 3] has the largest product 2 * 3 = 6.
             ([2, 3, -2, 4] would be 2*3*-2*4 = -48, and [4] alone is only 4.)
```

### Example 2

```
Input:  nums = [-2, 0, -1]
Output: 0
Explanation: The best product is 0, from the subarray [0]. No subarray can do
             better: [-2] gives -2, [-1] gives -1, and any span crossing 0 is 0.
```

### Example 3

```
Input:  nums = [-2, 3, -4]
Output: 24
Explanation: The whole array [-2, 3, -4] has product (-2) * 3 * (-4) = 24. Two
             negatives multiply to a positive, so the full span beats any prefix.
```

## Hint

This is a Kadane variant, but a negative number can turn the smallest running
product into the largest. Track **both** the running maximum and running minimum
product ending at each index — a twist on **Kadane's Algorithm**.
