# K-Query (Count Elements Greater Than K)

**Difficulty:** Medium

Source: SPOJ **KQUERY** ("K-query"). A staple problem for practicing the Merge Sort Tree.

## Description

You are given a static sequence `nums` of `n` integers. You must process `q` queries.
Each query is a triple `(i, j, k)` and asks:

> How many elements `nums[p]` with `i <= p <= j` are **strictly greater than** `k`?

Indices are **0-based and inclusive** in this statement. Return one integer per query,
in order.

This is the mirror image of "count `<= x`": the count of elements `> k` in a range equals
`(range length) - (count of elements <= k)`. A Merge Sort Tree answers it directly by
using a `lower_bound`/`upper_bound` inside each node's sorted list.

## Constraints

- `1 <= n <= 3 * 10^4`
- `1 <= q <= 2 * 10^5`
- `1 <= nums[p] <= 10^9`
- `1 <= k <= 10^9`
- `0 <= i <= j <= n - 1`

## Examples

### Example 1

```
Input:  nums = [5, 1, 2, 3, 4], queries = [[0, 4, 2], [1, 3, 3]]
Output: [3, 0]
```

Explanation:
- Query `(0, 4, 2)`: whole array `[5, 1, 2, 3, 4]`; elements `> 2` are `5, 3, 4` -> **3**.
- Query `(1, 3, 3)`: subarray `[1, 2, 3]`; elements `> 3`: none (`3` is not `> 3`) -> **0**.

### Example 2

```
Input:  nums = [7, 7, 7, 7], queries = [[0, 3, 6], [0, 3, 7], [2, 3, 0]]
Output: [4, 0, 2]
```

Explanation:
- Query `(0, 3, 6)`: all four `7`s are `> 6` -> **4**.
- Query `(0, 3, 7)`: no element is strictly greater than `7` -> **0**.
- Query `(2, 3, 0)`: subarray `[7, 7]`, both `> 0` -> **2**.

## Hint

Build a **Merge Sort Tree**. For a node, the count of elements `> k` is
`(node size) - upper_bound(sorted_list, k)`. Sum over the `O(log n)` nodes covering `[i, j]`.
