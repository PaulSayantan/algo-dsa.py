# Distinct Elements in Range

**Difficulty:** Medium

**Source:** Classic problem — SPOJ DQUERY ("D-query"); also appears as "count of
distinct numbers in subarray" on many judges.

## Description

You are given a static array `a` of `n` integers. You must answer `q` queries.
Each query gives two indices `l` and `r` (0-indexed, inclusive) and asks:

> How many **distinct** values appear in the subarray `a[l..r]`?

All queries are known in advance (you may read them all before producing any
answer), and the array is never modified. Return the list of answers, one per
query, in the original query order.

This is the "hello world" of Mo's algorithm: the statistic (count of distinct
values) is trivial to update when one element enters or leaves the window — keep
a frequency table and bump the distinct count when a frequency goes `0 → 1` or
`1 → 0`.

## Constraints

- `1 <= n <= 3 * 10^4`
- `1 <= a[i] <= 10^6`
- `1 <= q <= 2 * 10^5`
- `0 <= l <= r <= n - 1`

## Examples

### Example 1

```
Input:
  a = [1, 1, 2, 1, 3]
  queries = [(0, 4), (1, 2), (3, 4)]
Output:
  [3, 2, 2]
```

Explanation:
- `a[0..4] = [1,1,2,1,3]` → distinct values are {1, 2, 3} → 3.
- `a[1..2] = [1,2]` → distinct values are {1, 2} → 2.
- `a[3..4] = [1,3]` → distinct values are {1, 3} → 2.

### Example 2

```
Input:
  a = [4, 4, 4, 4]
  queries = [(0, 0), (0, 3), (1, 2)]
Output:
  [1, 1, 1]
```

Explanation:
- Every subarray of `[4,4,4,4]` contains only the value 4, so the count of
  distinct values is always 1, regardless of range length.

## Hint

Read every query first, then process them **offline** using **Sqrt
Decomposition on Queries (offline)**: sort the queries so that the window
endpoints move as little as possible, and maintain a frequency array so that
adding/removing a single element updates the distinct-count in `O(1)`.
