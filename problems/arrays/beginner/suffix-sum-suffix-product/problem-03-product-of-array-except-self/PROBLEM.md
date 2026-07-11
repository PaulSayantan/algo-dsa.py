# Product of Array Except Self

**Difficulty:** Medium

**Source:** LeetCode 238 — Product of Array Except Self

## Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is
equal to the product of all the elements of `nums` **except** `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in **O(n)** time and **without using the
division operation**.

**Follow up:** Can you solve the problem in O(1) extra space complexity? (The
output array does not count as extra space for space-complexity analysis.)

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit
  integer.

## Examples

### Example 1

```
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Explanation:
answer[0] = 2 * 3 * 4 = 24
answer[1] = 1 * 3 * 4 = 12
answer[2] = 1 * 2 * 4 = 8
answer[3] = 1 * 2 * 3 = 6
```

### Example 2

```
Input:  nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]

Explanation:
Only answer[2] is non-zero, because index 2 is the only position whose "except
self" product omits the single 0 in the array:
answer[2] = (-1) * 1 * (-3) * 3 = 9.
Every other position still includes the 0, so its product is 0.
```

## Hint

Combine a **prefix product** (product of everything to the left of `i`) with a
**Suffix Product** (product of everything to the right of `i`). Multiplying the
two gives the product of all elements except `nums[i]` — no division required.
