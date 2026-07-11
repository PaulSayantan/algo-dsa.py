# Maximum XOR of Two Numbers in an Array

**Difficulty:** Medium / Hard

**Source:** LeetCode 421 — Maximum XOR of Two Numbers in an Array

## Description

Given an integer array `nums`, return the **maximum result** of `nums[i] XOR nums[j]`,
where `0 <= i, j < nums.length` (`i` and `j` may be equal, though the maximum is always
achieved by two distinct indices when the array has more than one element).

The brute-force check of all pairs is O(n^2). A better solution builds the answer one bit
at a time, from the most significant bit down, using the structure of XOR: to maximize
the result we greedily try to make each high bit a `1`.

## Constraints

- `1 <= nums.length <= 2 * 10^5`
- `0 <= nums[i] <= 2^31 - 1`

## Examples

### Example 1
```
Input:  nums = [3, 10, 5, 25, 2, 8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28
             (0b00101 XOR 0b11001 = 0b11100 = 28).
```

### Example 2
```
Input:  nums = [2, 4]
Output: 6
Explanation: 2 XOR 4 = 0b010 XOR 0b100 = 0b110 = 6.
```

### Example 3
```
Input:  nums = [0]
Output: 0
Explanation: Only one element, so the best XOR is 0 XOR 0 = 0.
```

## Hint

Build the answer greedily from the highest bit down. **Bit Manipulation** — maintain a
set of bit-prefixes and, for each candidate prefix `answer | (1 << bit)`, check whether
two numbers in the array can produce it (using the fact that `a ^ b = c` iff `a ^ c = b`).
A binary trie of the bits is the classic supporting structure.
