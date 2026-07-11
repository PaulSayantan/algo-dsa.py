# Square Subsets (Product Is a Perfect Square)

**Difficulty:** Hard

**Source:** Codeforces 895C "Square Subsets" (adapted).

## Description

You are given an array `nums` of `n` integers, where every value is small
(`1 <= nums[i] <= 70`). Count the number of **non-empty** subsets whose product is a
**perfect square** (a product `P` such that `P = t^2` for some integer `t`). Subsets are
distinguished by index set, so equal values count as distinct elements.

Because the answer can be huge, return it **modulo `10^9 + 7`**.

## Constraints

- `1 <= n <= 10^5`
- `1 <= nums[i] <= 70`

## Examples

### Example 1

```
Input: nums = [1, 1, 1, 1]
Output: 15

Explanation:
Every element is 1, and any product of 1s is 1 = 1^2, a perfect square. All
non-empty subsets qualify: 2^4 - 1 = 15.
```

### Example 2

```
Input: nums = [2, 2, 2, 2]
Output: 7

Explanation:
A product of 2s is a perfect square exactly when an even number of 2s is chosen.
Non-empty subsets of even size: C(4,2) + C(4,4) = 6 + 1 = 7.
```

### Example 3

```
Input: nums = [2, 3, 6]
Output: 1

Explanation:
2 * 3 * 6 = 36 = 6^2 is the only non-empty subset with a square product.
(2, 3, 6 individually are not squares; 2*3=6, 2*6=12, 3*6=18 are not squares.)
```

## Hint

A product is a perfect square iff **every prime's total exponent is even**. Map each number
to a **parity vector** over the primes `<= 70` (a bit per prime, `1` = odd exponent), so a
square product means the XOR of chosen vectors is `0`. Build a **GF(2) basis** with
**Gaussian Elimination**; if the basis has rank `r`, the count of subsets XOR-ing to `0` is
`2^(n - r)`, and subtract 1 to drop the empty subset.
