# Single Number II

**Difficulty:** Medium

**Source:** LeetCode 137 — Single Number II

## Description

Given an integer array `nums` where every element appears **exactly three times** except
for one element which appears **exactly once**, find the single element.

You must implement a solution with **linear runtime complexity** and use only
**constant extra space**. The plain XOR-everything trick from Single Number I does not
work here, because XOR cancels pairs (even counts), not triples.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Each element in `nums` appears exactly three times except for one element which appears
  exactly once.

## Examples

### Example 1
```
Input:  nums = [2, 2, 3, 2]
Output: 3
Explanation: 2 appears three times; 3 appears once and is the answer.
```

### Example 2
```
Input:  nums = [0, 1, 0, 1, 0, 1, 99]
Output: 99
Explanation: 0 and 1 each appear three times and 99 appears once.
```

### Example 3
```
Input:  nums = [-2, -2, 1, 1, -3, 1, -3, -3, -2, -4]
Output: -4
Explanation: -2, 1, and -3 each appear three times; -4 appears once.
```

## Hint

Count contributions per bit and reduce them modulo 3. **Bit Manipulation** — for each of
the 32 bit positions, the total number of 1s across all elements is a multiple of 3 plus
the single number's bit; take that sum mod 3.
