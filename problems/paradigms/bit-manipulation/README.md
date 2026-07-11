# Bit Manipulation

**Bit manipulation** is the technique of solving problems by operating directly on the
binary representation of integers using bitwise operators. Instead of treating numbers
as abstract quantities, you treat them as fixed-width strings of bits and use fast,
constant-time hardware operations to inspect, set, clear, toggle, and combine those bits.

## Core operators

| Operator | Name | Effect |
|---|---|---|
| `&` | AND | 1 only where both bits are 1 (masking, testing) |
| `\|` | OR | 1 where either bit is 1 (setting bits) |
| `^` | XOR | 1 where bits differ (toggling, parity, pairing) |
| `~` | NOT | flips every bit |
| `<<` | left shift | multiply by 2^k, build masks (`1 << i`) |
| `>>` | right shift | divide by 2^k, scan bits |

## Essential idioms

- **Test bit `i`:** `(x >> i) & 1`
- **Set bit `i`:** `x | (1 << i)`
- **Clear bit `i`:** `x & ~(1 << i)`
- **Toggle bit `i`:** `x ^ (1 << i)`
- **Lowest set bit:** `x & (-x)`
- **Clear lowest set bit (Brian Kernighan):** `x & (x - 1)`
- **Is power of two:** `x > 0 and (x & (x - 1)) == 0`
- **XOR facts:** `x ^ x == 0`, `x ^ 0 == x`, XOR is commutative & associative.

## When to reach for it

- You need **parity / pairing** (every element appears twice except one -> XOR).
- You must **enumerate all subsets** of a small set (`n <= ~20`) -> iterate masks `0..2^n - 1`.
- You want a **space-efficient set / state** (bitmask DP, visited sets, flags).
- You are counting or manipulating **individual bits** (popcount, bit DP).
- You need **greedy bit-by-bit** construction of an answer (max XOR, bit tries).

## Typical complexity

Individual bitwise ops are **O(1)**. Processing all bits of a `w`-bit integer is
**O(w)** (32 or 64). Subset enumeration over `n` items is **O(2^n)** masks (often
**O(n * 2^n)** with per-mask work). Space is usually **O(1)** beyond the input, or
**O(2^n)** when you memoize over bitmask states.

## Problems

| # | Problem | Summary | Difficulty |
|---|---|---|---|
| 1 | [Single Number](problem-01-single-number/PROBLEM.md) | Find the lone element when every other appears twice, using XOR. | Easy |
| 2 | [Number of 1 Bits](problem-02-number-of-1-bits/PROBLEM.md) | Count set bits (Hamming weight) of an integer. | Easy |
| 3 | [Counting Bits](problem-03-counting-bits/PROBLEM.md) | Compute popcount for every integer in `0..n` via bit DP. | Easy/Medium |
| 4 | [Subsets](problem-04-subsets/PROBLEM.md) | Enumerate the power set using bitmask iteration. | Medium |
| 5 | [Single Number II](problem-05-single-number-ii/PROBLEM.md) | Find the lone element when every other appears three times. | Medium |
| 6 | [Maximum XOR of Two Numbers](problem-06-maximum-xor-of-two-numbers/PROBLEM.md) | Greedily build the largest pairwise XOR bit by bit. | Medium/Hard |
