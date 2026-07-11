# Static Range Minimum Query (RMQ)

**Difficulty:** Easy

**Source:** Classic problem (SPOJ RMQSQ / competitive-programming staple)

## Description

You are given an integer array `nums` of length `n` that will **never change**. You
must then answer `q` independent queries. Each query is a pair `(l, r)` (0-indexed,
inclusive on both ends) and asks for the **minimum** value in the subarray
`nums[l..r]`.

Because the array is immutable and the number of queries can be large, you should
preprocess the array once so that each query is answered in constant time.

Return a list containing the answer to every query, in order.

## Constraints

- `1 <= n <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `1 <= q <= 2 * 10^5`
- `0 <= l <= r <= n - 1` for every query

## Examples

### Example 1

```
Input:  nums = [1, 3, 2, 7, 9, 11, 3, 5], queries = [[1, 3], [4, 6], [0, 7]]
Output: [2, 3, 1]
```

Explanation:
- `min(nums[1..3]) = min(3, 2, 7) = 2`
- `min(nums[4..6]) = min(9, 11, 3) = 3`
- `min(nums[0..7]) = min(1, 3, 2, 7, 9, 11, 3, 5) = 1`

### Example 2

```
Input:  nums = [5], queries = [[0, 0]]
Output: [5]
```

Explanation: The only subarray is the single element `5`, whose minimum is `5`.

## Hint

Precompute the minimum of every power-of-two-length block, then answer each query by
combining two (possibly overlapping) blocks. This is a **Sparse Table**. Overlap is
safe here because `min` is idempotent: `min(x, x) = x`.
