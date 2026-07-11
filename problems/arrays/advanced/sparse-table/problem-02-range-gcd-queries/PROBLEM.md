# Range GCD Queries

**Difficulty:** Medium

**Source:** Classic competitive-programming problem (e.g. SPOJ / Codeforces style range-GCD)

## Description

You are given an integer array `nums` of length `n` that never changes, followed by
`q` queries. Each query is a pair `(l, r)` (0-indexed, inclusive) and asks for the
**greatest common divisor** of all elements in `nums[l..r]`, i.e.

```
gcd(nums[l], nums[l+1], ..., nums[r])
```

Preprocess the array once and answer every query fast. Return the list of answers in
order.

Use the convention `gcd(a, b) = gcd(b, a)` and `gcd(x) = x` for a single element. All
elements are positive.

## Constraints

- `1 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= q <= 2 * 10^5`
- `0 <= l <= r <= n - 1`

## Examples

### Example 1

```
Input:  nums = [12, 6, 9, 18, 24], queries = [[0, 1], [2, 4], [0, 4]]
Output: [6, 3, 3]
```

Explanation:
- `gcd(12, 6) = 6`
- `gcd(9, 18, 24) = gcd(gcd(9, 18), 24) = gcd(9, 24) = 3`
- `gcd(12, 6, 9, 18, 24) = 3`

### Example 2

```
Input:  nums = [7, 14, 28], queries = [[1, 2], [0, 0]]
Output: [14, 7]
```

Explanation:
- `gcd(14, 28) = 14`
- `gcd(7) = 7` (single element).

## Hint

`gcd` is **idempotent** — `gcd(x, x) = x` — so overlapping ranges combine safely.
Build a **Sparse Table** where each cell stores the gcd of a power-of-two-length
block, then answer each query in O(1) with two overlapping blocks.
