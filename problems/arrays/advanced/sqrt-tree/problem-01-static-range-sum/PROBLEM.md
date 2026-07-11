# Static Range Sum Query

**Difficulty:** Easy

**Source:** Classic (variant of LeetCode 303 "Range Sum Query - Immutable"; SPOJ RMQ family)

## Description

You are given an integer array `nums` of length `n` that will **not** change after
construction. You must answer `q` queries. Each query gives two indices `l` and `r`
(`0 <= l <= r < n`) and asks for the sum of the subarray:

```
nums[l] + nums[l+1] + ... + nums[r]
```

Design a structure that preprocesses `nums` once and then answers each query in
**O(1)** time. This warm-up uses the simplest associative operation — addition — so
you can focus on how the Sqrt Tree decomposes a query into a **suffix piece**, a
**between-blocks piece**, and a **prefix piece**, then combines them with the operation.

Implement `RangeSum` with a constructor that builds the structure and a `query(l, r)`
method that returns the sum over `[l, r]` inclusive.

## Constraints

- `1 <= n <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= q <= 10^5`
- `0 <= l <= r < n`

## Examples

### Example 1

```
Input:
  nums  = [1, 3, 5, 7, 9, 11]
  query(1, 3)
  query(0, 5)

Output:
  15
  36

Explanation:
  query(1, 3) = 3 + 5 + 7 = 15
  query(0, 5) = 1 + 3 + 5 + 7 + 9 + 11 = 36
```

### Example 2

```
Input:
  nums  = [-2, 0, 3, -5, 2, -1]
  query(2, 5)
  query(0, 2)

Output:
  -1
  1

Explanation:
  query(2, 5) = 3 + (-5) + 2 + (-1) = -1
  query(0, 2) = -2 + 0 + 3 = 1
```

## Hint

You can build the answer for any range from three precomputed pieces: a block suffix, a
whole-blocks-between answer, and a block prefix. Build a **Sqrt Tree** over `nums` with
`op = +`. (Addition is invertible, so a prefix-sum array also works here — use this
problem to confirm your Sqrt Tree matches the trivial answer before the harder problems.)
