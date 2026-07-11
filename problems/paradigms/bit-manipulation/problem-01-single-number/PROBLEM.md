# Single Number

**Difficulty:** Easy

**Source:** LeetCode 136 — Single Number

## Description

Given a non-empty array of integers `nums`, every element appears **exactly twice**
except for one element which appears **exactly once**. Find that single element.

You must implement a solution with **linear runtime complexity** and use only
**constant extra space**. (This rules out the obvious hash-set / counting approaches
that use O(n) auxiliary memory.)

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Each element in the array appears exactly twice except for one element which appears
  only once.

## Examples

### Example 1
```
Input:  nums = [2, 2, 1]
Output: 1
Explanation: 2 appears twice and cancels out; 1 is left alone.
```

### Example 2
```
Input:  nums = [4, 1, 2, 1, 2]
Output: 4
Explanation: 1 and 2 each appear twice and cancel; only 4 remains.
```

### Example 3
```
Input:  nums = [1]
Output: 1
Explanation: A single element trivially is the answer.
```

## Hint

Think about a bitwise operator that cancels equal values. **Bit Manipulation** — in
particular, the XOR operator has the properties `x ^ x = 0` and `x ^ 0 = x`.
