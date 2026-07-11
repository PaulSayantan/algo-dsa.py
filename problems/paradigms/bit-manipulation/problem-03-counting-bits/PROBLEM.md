# Counting Bits

**Difficulty:** Easy / Medium

**Source:** LeetCode 338 — Counting Bits

## Description

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i`
(`0 <= i <= n`), `ans[i]` is the number of `1` bits in the binary representation of `i`.

The straightforward approach computes a popcount for each number independently. Try to
do better: compute the whole array in **O(n)** total time by reusing previously computed
answers — a small dynamic program over the bits.

## Constraints

- `0 <= n <= 10^5`
- The returned array must have exactly `n + 1` entries.

## Examples

### Example 1
```
Input:  n = 2
Output: [0, 1, 1]
Explanation:
  0 -> 0b0   -> 0 set bits
  1 -> 0b1   -> 1 set bit
  2 -> 0b10  -> 1 set bit
```

### Example 2
```
Input:  n = 5
Output: [0, 1, 1, 2, 1, 2]
Explanation:
  0 -> 000 -> 0
  1 -> 001 -> 1
  2 -> 010 -> 1
  3 -> 011 -> 2
  4 -> 100 -> 1
  5 -> 101 -> 2
```

### Example 3
```
Input:  n = 0
Output: [0]
Explanation: Only 0 itself, which has no set bits.
```

## Hint

Relate `ans[i]` to a smaller, already-computed index. **Bit Manipulation** — note that
`i` and `i >> 1` differ by only the lowest bit, and `i & (i - 1)` removes one set bit.
