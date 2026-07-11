# Range Product Modulo m

**Difficulty:** Hard

**Source:** Classic competitive-programming task (the canonical Sqrt Tree motivating problem)

## Description

Given a static array `nums` of `n` non-negative integers and a modulus `m` (which is **not
necessarily prime** and may share factors with the array values), answer `q` queries. Each
query gives `l` and `r` and asks for:

```
(nums[l] * nums[l+1] * ... * nums[r]) mod m
```

Preprocess once, answer each query in **O(1)**.

This is the textbook problem where **Sqrt Tree is the idiomatic tool**:

- **Prefix products fail.** `product(l..r) = prefix[r] / prefix[l-1]` requires dividing
  modulo `m`, i.e. a modular inverse of `prefix[l-1]`. When `m` is not prime, or when any
  element shares a factor with `m` (so `prefix[l-1]` is **not coprime** to `m`), that inverse
  **does not exist**. The operation is **not invertible**.
- **Sparse tables fail.** Multiplication mod `m` is **not idempotent** (`x·x mod m != x` in
  general), so overlapping the two covering ranges would multiply the overlap twice and give
  the wrong answer.
- **Sqrt Tree works.** It partitions the range into **disjoint** pieces and only relies on
  **associativity**, which modular multiplication has.

Implement `RangeProductMod` with a constructor `(nums, mod)` and `query(l, r)`.

## Constraints

- `1 <= n <= 10^5`
- `0 <= nums[i] < m`
- `2 <= m <= 10^9` (not necessarily prime)
- `1 <= q <= 10^5`
- `0 <= l <= r < n`

## Examples

### Example 1

```
Input:
  nums = [3, 7, 4, 9, 6, 2]
  m    = 100
  query(0, 2)
  query(2, 5)

Output:
  84
  32

Explanation:
  query(0, 2) -> (3 * 7 * 4) mod 100 = 84 mod 100 = 84
  query(2, 5) -> (4 * 9 * 6 * 2) mod 100 = 432 mod 100 = 32
```

### Example 2

```
Input:
  nums = [3, 7, 4, 9, 6, 2]
  m    = 100
  query(1, 3)
  query(0, 5)

Output:
  52
  72

Explanation:
  query(1, 3) -> (7 * 4 * 9) mod 100 = 252 mod 100 = 52
  query(0, 5) -> (3 * 7 * 4 * 9 * 6 * 2) mod 100 = 9072 mod 100 = 72

  Note: the prefix products mod 100 are [1, 3, 21, 84, 56, 36, 72].
  prefix[3] = 56 corresponds to 3*7*4*9 mod 100; you cannot divide by
  56 modulo 100 (gcd(56, 100) = 4 != 1), so prefix products cannot recover
  query(1, 3). This is exactly why a Sqrt Tree is needed.
```

## Hint

Multiplication mod `m` is associative but neither invertible nor idempotent, so both prefix
products and sparse tables break. Split the array into `√n` blocks, precompute per-block
prefix/suffix products mod `m` and the product of every pair of whole blocks mod `m`, then
combine a suffix + between + prefix with exactly two multiplications. Build a **Sqrt Tree**
with `op = (x, y) -> (x * y) % m`.
