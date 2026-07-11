# D-query: Number of Distinct Values in a Range

**Difficulty:** Hard

**Source:** SPOJ DQUERY (classic offline Fenwick-tree problem)

## Description

You are given an array `a` of `n` integers (1-indexed) and `q` queries. Each
query is a pair `(l, r)` and asks:

> How many **distinct** values appear among `a[l], a[l+1], ..., a[r]`?

The array is static (no updates), and all queries are known in advance. Return
the answers in the order the queries are given.

Design a function that takes the array and a list of queries `(l, r)` and returns
a list of distinct-count answers, one per query.

## Constraints

- `1 <= n <= 3 * 10^4`
- `1 <= a[p] <= 10^6`
- `1 <= q <= 2 * 10^5`
- `1 <= l <= r <= n`

## Examples

### Example 1

```
Input:  a = [1, 1, 2, 1, 3]
        queries = [(1, 5), (2, 4), (3, 5)]
Output: [3, 2, 3]
```

Explanation:
- `(1, 5)`: values `[1, 1, 2, 1, 3]` → distinct `{1, 2, 3}` → `3`.
- `(2, 4)`: values `[1, 2, 1]` → distinct `{1, 2}` → `2`.
- `(3, 5)`: values `[2, 1, 3]` → distinct `{1, 2, 3}` → `3`.

### Example 2

```
Input:  a = [1, 2, 3, 4, 5]
        queries = [(1, 5), (2, 2), (1, 3)]
Output: [5, 1, 3]
```

Explanation:
- `(1, 5)`: all values distinct → `5`.
- `(2, 2)`: single element `[2]` → `1`.
- `(1, 3)`: values `[1, 2, 3]` → `3`.

## Hint

Counting distinct values online is hard, but there is a clean offline trick.
Use **Offline Query Processing**: sort the queries by their right endpoint `r`
ascending, sweep `r` from left to right keeping only the **last occurrence** of
each value marked in a Fenwick tree, and answer each query as a prefix-sum count
of marked positions in `[l, r]`.
