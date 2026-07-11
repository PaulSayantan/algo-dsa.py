# K-th Smallest Number in Range

**Difficulty:** Hard

Source: Classic **range k-th order statistic** problem (SPOJ **MKTHNUM** / "K-th Number",
Codeforces "range k-th smallest"). Solvable online with a Merge Sort Tree.

## Description

You are given a static integer array `nums` of length `n`. Answer `q` queries. Each query
is a triple `(l, r, k)` and asks:

> Consider the subarray `nums[l..r]`. If its elements were sorted in non-decreasing
> order, what is the **k-th smallest** element (1-indexed `k`)?

Indices `l`, `r` are **0-based and inclusive**; `k` is **1-based** (`k = 1` is the minimum
of the subarray). It is guaranteed that `1 <= k <= r - l + 1`. Return one answer per query.

A Merge Sort Tree answers this online: **binary search on the answer value**. For a
candidate value `v`, "count of elements `<= v` in `nums[l..r]`" is a standard Merge Sort
Tree query; find the smallest `v` whose count is `>= k`.

## Constraints

- `1 <= n <= 10^5`
- `1 <= q <= 10^5`
- `-10^9 <= nums[p] <= 10^9`
- `0 <= l <= r <= n - 1`
- `1 <= k <= r - l + 1`

## Examples

### Example 1

```
Input:  nums = [1, 5, 2, 6, 3, 7, 4], queries = [[1, 5, 3], [0, 6, 1], [2, 4, 2]]
Output: [5, 1, 3]
```

Explanation:
- Query `(1, 5, 3)`: subarray `[5, 2, 6, 3, 7]`; sorted `[2, 3, 5, 6, 7]`; 3rd smallest = **5**.
- Query `(0, 6, 1)`: whole array; sorted starts `[1, 2, 3, ...]`; 1st smallest = **1**.
- Query `(2, 4, 2)`: subarray `[2, 6, 3]`; sorted `[2, 3, 6]`; 2nd smallest = **3**.

### Example 2

```
Input:  nums = [4, 4, 2, 2], queries = [[0, 3, 1], [0, 3, 3], [0, 3, 4]]
Output: [2, 4, 4]
```

Explanation:
- Subarray is the whole array `[4, 4, 2, 2]`; sorted `[2, 2, 4, 4]`.
- 1st smallest = **2**, 3rd smallest = **4**, 4th smallest = **4** (duplicates counted).

## Hint

Build a **Merge Sort Tree** that answers "count of elements `<= v` in `nums[l..r]`". Then
**binary search on the value** `v` (over the sorted set of distinct values, or over the
integer range): the answer is the smallest `v` for which that count is `>= k`.

## Follow-up

There is an even faster `O(log n)` per-query method: walk both children of a node while
tracking how many range elements fall in the left half. This turns the Merge Sort Tree /
persistent-segment-tree into a direct k-th selection without the outer value binary
search. The binary-search-on-answer approach above is the simplest to implement.
