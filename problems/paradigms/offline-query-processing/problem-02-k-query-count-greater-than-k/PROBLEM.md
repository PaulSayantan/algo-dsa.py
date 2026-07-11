# K-query: Count Elements Greater Than k in a Range

**Difficulty:** Medium

**Source:** SPOJ KQUERY (classic offline Fenwick-tree problem)

## Description

You are given an array `a` of `n` integers (1-indexed) and `q` queries. Each
query is a triple `(i, j, k)` and asks:

> How many elements `a[p]` with `i <= p <= j` satisfy `a[p] > k`?

There are **no updates** to the array — all queries are read-only, and all of
them are available before you must answer any of them. Return the answers in the
order the queries are given.

Design a function that takes the array and a list of queries `(i, j, k)` and
returns a list of counts, one per query.

## Constraints

- `1 <= n <= 3 * 10^4`
- `1 <= a[p] <= 10^9`
- `1 <= q <= 2 * 10^5`
- `1 <= i <= j <= n`
- `1 <= k <= 10^9`

## Examples

### Example 1

```
Input:  a = [5, 1, 2, 3, 4]
        queries = [(2, 4, 1), (4, 4, 4), (1, 5, 2)]
Output: [2, 0, 3]
```

Explanation:
- `(2, 4, 1)`: subarray `a[2..4] = [1, 2, 3]`; elements `> 1` are `2` and `3` → `2`.
- `(4, 4, 4)`: subarray `a[4..4] = [3]`; elements `> 4`: none → `0`.
- `(1, 5, 2)`: subarray `a[1..5] = [5, 1, 2, 3, 4]`; elements `> 2` are
  `5, 3, 4` → `3`.

### Example 2

```
Input:  a = [1, 2, 3, 4, 5, 6, 7]
        queries = [(1, 7, 0), (1, 7, 7), (3, 5, 3)]
Output: [7, 0, 2]
```

Explanation:
- `(1, 7, 0)`: all `7` elements are `> 0` → `7`.
- `(1, 7, 7)`: no element exceeds `7` → `0`.
- `(3, 5, 3)`: subarray `a[3..5] = [3, 4, 5]`; elements `> 3` are `4, 5` → `2`.

## Hint

A range-count-greater-than-`k` query is hard online without heavy structures, but
easy if you fix the threshold `k`. Use **Offline Query Processing**: sort the
queries by `k` in decreasing order and insert array values into a Fenwick tree as
they become `> k`, so that at query time the tree contains exactly the "large"
elements and a prefix sum gives the count in `[i, j]`.
