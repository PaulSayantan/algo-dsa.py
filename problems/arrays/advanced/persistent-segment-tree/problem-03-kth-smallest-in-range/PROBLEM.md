# K-th Smallest Number in Range

**Difficulty:** Hard

Source: SPOJ **MKTHNUM** ("K-th Number"); also Codeforces / classic
"quantile query". The canonical application of persistent segment trees.

## Description

You are given an integer array `nums` of length `n` and a list of `q` queries.
Each query is a triple `(l, r, k)` and asks:

> If you take the subarray `nums[l..r]` (inclusive) and sort it in
> non-decreasing order, what is the **k-th smallest** element? (`k` is
> **1-indexed**, so `k = 1` is the minimum of the subarray.)

Return the answer to each query, in order. It is guaranteed that
`1 ≤ k ≤ r − l + 1`, so the k-th smallest always exists.

This is the textbook persistent-segment-tree problem: it needs both the
*prefix-versioning* idea (to isolate the window `[l, r]`) and a *descend-by-count*
walk (to locate the order statistic in `O(log n)`).

## Constraints

- `1 ≤ n ≤ 10^5`
- `-10^9 ≤ nums[i] ≤ 10^9`
- `1 ≤ q ≤ 5 × 10^4`
- `0 ≤ l ≤ r < n`
- `1 ≤ k ≤ r − l + 1`

## Examples

### Example 1

```
Input:
  nums = [1, 5, 2, 6, 3, 7, 4]
  queries = [
    (1, 5, 3),     # subarray nums[1..5] = [5,2,6,3,7]; sorted = [2,3,5,6,7]; 3rd = 5
    (0, 6, 1),     # whole array; 1st smallest = 1
    (2, 4, 2),     # nums[2..4] = [2,6,3]; sorted = [2,3,6]; 2nd = 3
  ]

Output: [5, 1, 3]
```

Explanation: For the first query the window is `[5,2,6,3,7]`; sorted it is
`[2,3,5,6,7]` and the 3rd smallest is `5`. The second query is the min of the
whole array, `1`. The third window `[2,6,3]` sorts to `[2,3,6]`, whose 2nd
smallest is `3`.

### Example 2

```
Input:
  nums = [4, 4, 4, 1, 2]
  queries = [
    (0, 2, 2),     # [4,4,4]; sorted = [4,4,4]; 2nd = 4
    (0, 4, 1),     # whole array; min = 1
    (0, 4, 5),     # whole array; 5th (largest) = 4
  ]

Output: [4, 1, 4]
```

Explanation: `[4,4,4]` has every order statistic equal to `4` (duplicates are
counted separately). The whole array sorts to `[1,2,4,4,4]`; the 1st is `1` and
the 5th (max) is `4`.

## Hint

Build a **Persistent Segment Tree** over the compressed value domain, one
version per prefix (version `i` has inserted `nums[0..i]`). For a query, walk
`root[r]` and `root[l−1]` down together: the number of window values in the left
value-half is `leftCount(root[r]) − leftCount(root[l−1])`. If `k ≤` that count,
go left; otherwise subtract it from `k` and go right. The leaf you reach is the
answer.
