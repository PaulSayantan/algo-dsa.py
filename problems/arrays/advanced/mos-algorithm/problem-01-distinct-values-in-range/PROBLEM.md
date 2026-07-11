# Distinct Values in a Range

**Difficulty:** Medium

**Source:** SPOJ DQUERY — "D-query" (the canonical Mo's Algorithm problem)

## Description

You are given a static array `a` of `n` integers (1-indexed) and `q` queries. Each
query is a pair `(l, r)` with `1 <= l <= r <= n`, and asks:

> How many **distinct** values appear in the subarray `a[l..r]` (both endpoints
> inclusive)?

There are no updates to the array between queries, and you are allowed to read all
`q` queries before producing any answer (the problem is **offline**). Return the
answer for each query in the original input order.

## Constraints

- `1 <= n <= 3 * 10^4` (classic SPOJ limit; the same approach scales to `n <= 2*10^5`)
- `1 <= a[i] <= 10^6`
- `1 <= q <= 2 * 10^5`
- `1 <= l <= r <= n`

## Examples

### Example 1

```
Input:
  a = [1, 1, 2, 1, 3]           # 1-indexed: a[1..5]
  queries = [(1, 5), (2, 4), (3, 5)]
Output:
  [3, 2, 3]
```

**Explanation:**
- `(1,5)` → `{1, 1, 2, 1, 3}` has distinct values `{1, 2, 3}` → `3`.
- `(2,4)` → `{1, 2, 1}` has distinct values `{1, 2}` → `2`.
- `(3,5)` → `{2, 1, 3}` has distinct values `{1, 2, 3}` → `3`.

### Example 2

```
Input:
  a = [4, 4, 4, 4]
  queries = [(1, 4), (2, 2)]
Output:
  [1, 1]
```

**Explanation:**
- `(1,4)` → all four elements equal `4`, so exactly `1` distinct value.
- `(2,2)` → a single element `4`, so `1` distinct value.

## Hint

Answers over overlapping ranges are highly correlated: adding or removing one
element changes the distinct-count by at most one. Process the queries **offline**
with **Mo's Algorithm** — sort them by `(l // √n, r)` and slide two pointers,
maintaining a frequency array `cnt[value]` and the running number of distinct values.
