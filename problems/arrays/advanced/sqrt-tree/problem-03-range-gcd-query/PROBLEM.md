# Range GCD Query

**Difficulty:** Medium

**Source:** Classic (SPOJ GSS-style; Codeforces "range gcd" problems)

## Description

Given a static array `nums` of `n` positive integers, answer `q` queries. Each query gives
`l` and `r` and asks for the **greatest common divisor** of `nums[l..r]` inclusive:

```
gcd(nums[l], nums[l+1], ..., nums[r])
```

Preprocess once, answer each query in **O(1)**.

`gcd` is **associative** and **idempotent** (`gcd(x, x) = x`), so a sparse table also works.
But `gcd` is **not invertible** — you cannot recover `gcd(l..r)` from two prefix gcds — which
already rules out the prefix-array trick and foreshadows the next problems. Build a Sqrt Tree
with `op = gcd`.

Implement `RangeGCD` with a constructor and `query(l, r)` returning the gcd over `[l, r]`.

## Constraints

- `1 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= q <= 10^5`
- `0 <= l <= r < n`
- Note: `gcd` of a single element is that element.

## Examples

### Example 1

```
Input:
  nums = [12, 18, 6, 9, 24, 36]
  query(0, 2)
  query(3, 5)

Output:
  6
  3

Explanation:
  query(0, 2) -> gcd(12, 18, 6) = 6
  query(3, 5) -> gcd(9, 24, 36) = 3
```

### Example 2

```
Input:
  nums = [12, 18, 6, 9, 24, 36]
  query(0, 5)
  query(4, 5)

Output:
  3
  12

Explanation:
  query(0, 5) -> gcd(12, 18, 6, 9, 24, 36) = 3
  query(4, 5) -> gcd(24, 36) = 12
```

## Hint

The gcd of a range is the gcd of the gcds of any partition of that range. Split into `√n`
blocks, precompute per-block prefix/suffix gcds and the gcd of every pair of whole blocks,
then combine a suffix + between + prefix. Build a **Sqrt Tree** with `op = gcd`. (Prefix
gcds fail because gcd has no inverse — you cannot "divide out" the part outside `[l, r]`.)
