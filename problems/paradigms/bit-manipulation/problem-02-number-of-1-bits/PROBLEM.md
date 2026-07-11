# Number of 1 Bits (Hamming Weight)

**Difficulty:** Easy

**Source:** LeetCode 191 — Number of 1 Bits

## Description

Write a function that takes a non-negative integer `n` and returns the number of `1`
bits it has in its binary representation (also known as the **Hamming weight**).

Aim for a solution that does not simply convert to a string and count characters —
use bitwise operations so the work scales with the number of set bits or the fixed
word size, not with anything larger.

## Constraints

- `0 <= n <= 2^31 - 1` (a 32-bit unsigned integer).
- The input is given as an integer.

## Examples

### Example 1
```
Input:  n = 11        (binary 0000...1011)
Output: 3
Explanation: The binary form 1011 contains three 1 bits.
```

### Example 2
```
Input:  n = 128       (binary 1000 0000)
Output: 1
Explanation: 128 has a single set bit.
```

### Example 3
```
Input:  n = 0
Output: 0
Explanation: Zero has no set bits.
```

## Hint

You can peel off one set bit at a time. **Bit Manipulation** — the expression
`n & (n - 1)` clears the lowest set bit of `n`.
