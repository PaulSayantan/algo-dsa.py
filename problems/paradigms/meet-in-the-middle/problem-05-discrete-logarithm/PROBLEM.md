# Discrete Logarithm (Baby-Step Giant-Step)

**Difficulty:** Hard

**Source:** Classic number-theory algorithm — Shanks' Baby-Step Giant-Step
(competitive-programming staple; appears on CP-Algorithms and in cryptography
courses).

## Description

Given integers `a`, `b`, and a **prime** modulus `m`, find the smallest
non-negative integer `x` such that

```
a^x ≡ b   (mod m)
```

If no such `x` exists, return `-1`.

This is the *discrete logarithm* problem: solving `x = log_a(b)` in modular
arithmetic. A linear scan `x = 0, 1, 2, ...` is `O(m)`, which is far too slow
when `m` is large (up to ~`10^9`). The Baby-Step Giant-Step algorithm solves it
in `O(sqrt(m))` by writing the unknown exponent as two "halves" and meeting in
the middle.

Assume `m` is prime and `1 <= a < m` (so `gcd(a, m) = 1`).

## Constraints

- `2 <= m <= 10^9`, `m` prime
- `0 <= a, b < m`
- The answer `x`, if it exists, satisfies `0 <= x < m`

## Examples

### Example 1

```
Input:  a = 2, b = 3, m = 5
Output: 3
```

**Explanation:** Powers of 2 mod 5 are `2^0=1, 2^1=2, 2^2=4, 2^3=3`. The
smallest exponent giving 3 is `x = 3`.

### Example 2

```
Input:  a = 3, b = 13, m = 17
Output: 4
```

**Explanation:** `3^4 = 81 = 4*17 + 13 ≡ 13 (mod 17)`, and no smaller exponent
works, so `x = 4`.

### Example 3

```
Input:  a = 5, b = 3, m = 23
Output: 16
```

**Explanation:** `5^16 ≡ 3 (mod 23)` (verified by fast exponentiation), and it
is the smallest such exponent, so `x = 16`.

## Hint

Write `x = i * ceil(sqrt(m)) - j` with `0 <= j < ceil(sqrt(m))`. Then
`a^x = b` becomes `(a^ceil(sqrt(m)))^i ≡ b * a^j (mod m)`. Precompute all
`b * a^j` (the *baby steps*) into a hash map, then try each `(a^n)^i` (the
*giant steps*) and look for a collision — a **meet in the middle** over the two
halves of the exponent.
