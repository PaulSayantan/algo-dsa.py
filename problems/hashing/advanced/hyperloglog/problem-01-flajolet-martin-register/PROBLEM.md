# Flajolet-Martin Trailing-Zero Register

**Difficulty:** Medium

**Source:** Classic — Flajolet-Martin distinct-count register

## Description

Implement the core Flajolet-Martin register over an `m`-bit hash space (`mod` a power of two). For each added item, hash it with `h(x) = (x * 2654435761 + 40503) mod m` and count the trailing zeros of the hash. Track the maximum trailing-zero count across all adds. `max_trailing_zeros()` returns that exact integer and `estimate()` returns `2 ** max_trailing_zeros()`. (Both are deterministic.)

## Examples

### Example 1

```
Input:  add 1,2,3,7 (mod 256)
Output: 3
```

**Explanation:** h(1)=232=11101000 has 3 trailing zeros, the max.

### Example 2

```
Input:  estimate()
Output: 8
```

**Explanation:** 2 ** 3 = 8.

## Hint

Trailing zeros = count of low-order 0 bits; keep the running max; estimate is 2**max.
