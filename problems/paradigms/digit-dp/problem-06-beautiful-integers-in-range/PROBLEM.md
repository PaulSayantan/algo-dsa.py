# Beautiful Integers in the Range

**Difficulty:** Hard

**Source:** LeetCode 2827 — Number of Beautiful Integers in the Range

## Description

You are given three positive integers `low`, `high`, and `k`.

A number is **beautiful** if it meets **both** of the following conditions:

1. The count of **even digits** in the number is **equal** to the count of
   **odd digits**.
2. The number is **divisible by `k`**.

Return the number of beautiful integers in the inclusive range `[low, high]`.

## Constraints

- `0 < low <= high <= 10^9`
- `0 < k <= 20`

## Examples

### Example 1

```
Input:  low = 10, high = 20, k = 3
Output: 2
Explanation: There are exactly 2 beautiful integers in [10, 20]:
  - 12  -> digits {1, 2}: one odd (1), one even (2) -> balanced; 12 % 3 == 0.
  - 18  -> digits {1, 8}: one odd (1), one even (8) -> balanced; 18 % 3 == 0.
  It can be shown that 12 and 18 are the only beautiful integers in the range.
```

### Example 2

```
Input:  low = 1, high = 10, k = 1
Output: 1
Explanation: Every integer is divisible by k = 1, so only the digit-balance
  condition matters. In [1, 10] the only balanced number is 10
  (digits {1, 0}: one odd, one even). Single-digit numbers 1..9 have one digit,
  which cannot split evenly, so they are not balanced. Output = 1.
```

### Example 3

```
Input:  low = 5, high = 5, k = 2
Output: 0
Explanation: The only candidate is 5, which has a single (odd) digit — it is not
  balanced — and it is not divisible by 2. Output = 0.
```

## Hint

You must count integers in `[low, high]` under a **divisibility** condition
(track the running remainder mod `k`) *and* a **digit-parity balance** condition
(track even-count minus odd-count). Both are accumulative digit properties, and
the range is large — this is a multi-state **Digit DP**, evaluated as
`f(high) - f(low - 1)` with careful leading-zero handling.
