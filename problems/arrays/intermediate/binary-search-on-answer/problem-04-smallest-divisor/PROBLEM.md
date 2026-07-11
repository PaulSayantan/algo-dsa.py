# Find the Smallest Divisor Given a Threshold

**Difficulty:** Medium

**Source:** LeetCode 1283 — Find the Smallest Divisor Given a Threshold

## Description

Given an array of integers `nums` and an integer `threshold`, choose a positive integer `divisor`, divide **all** the array elements by it, and sum the division results.

Each individual division result is **rounded up** to the nearest integer (for example `7 / 3 = 3` and `10 / 2 = 5`).

Find the **smallest** `divisor` such that the resulting sum is less than or equal to `threshold`.

It is guaranteed that there will be an answer.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `1 <= nums[i] <= 10^6`
- `nums.length <= threshold <= 10^6`

## Examples

### Example 1

```
Input:  nums = [1, 2, 5, 9], threshold = 6
Output: 5
Explanation: With divisor 5 the sum is ceil(1/5)+ceil(2/5)+ceil(5/5)+ceil(9/5)
= 1 + 1 + 1 + 2 = 5, which is <= 6.
With divisor 4 the sum is 1 + 1 + 2 + 3 = 7 > 6, so 5 is the smallest that works.
```

### Example 2

```
Input:  nums = [44, 22, 33, 11, 1], threshold = 5
Output: 44
Explanation: There are 5 numbers and threshold 5, so every ceil term must equal 1,
which requires the divisor to be at least the largest element, 44.
With divisor 44 the sum is 1+1+1+1+1 = 5 <= 5; with divisor 43 it is 2+1+1+1+1 = 6 > 5.
```

### Example 3

```
Input:  nums = [21212, 10101, 12121], threshold = 1000000
Output: 1
Explanation: The threshold is huge, so even divisor 1 works: the sum is just
21212 + 10101 + 12121 = 43434 <= 1000000. No smaller positive divisor exists, so 1.
```

## Hint

The answer (a divisor) lies in `[1, max(nums)]`, and the sum of ceil-divisions is monotonically non-increasing as the divisor grows. Use **Binary Search on Answer** to find the smallest divisor whose sum stays within the threshold.
