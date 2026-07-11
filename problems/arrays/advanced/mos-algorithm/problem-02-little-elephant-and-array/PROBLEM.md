# Little Elephant and Array

**Difficulty:** Medium

**Source:** Codeforces 220B — "Little Elephant and Array"

## Description

You are given a static array `a` of `n` positive integers and `q` queries. Each
query is a pair `(l, r)` with `1 <= l <= r <= n`, and asks:

> How many values `x` appear in the subarray `a[l..r]` **exactly `x` times**?

For example, the value `3` contributes to the answer only if it occurs exactly `3`
times within `a[l..r]`; the value `1` contributes only if it occurs exactly once,
and so on. The array does not change between queries, and you may read all queries
before answering (the problem is **offline**). Return the answer per query in the
original input order.

## Constraints

- `1 <= n, q <= 10^5`
- `1 <= a[i] <= 10^9`
- `1 <= l <= r <= n`

## Examples

### Example 1

```
Input:
  a = [3, 1, 2, 2, 3, 3, 7]      # 1-indexed a[1..7]
  queries = [(1, 7)]
Output:
  [3]
```

**Explanation:** In `a[1..7]` the frequencies are: `1`→1, `2`→2, `3`→3, `7`→1.
- `1` occurs `1` time → matches (`x = cnt = 1`).
- `2` occurs `2` times → matches.
- `3` occurs `3` times → matches.
- `7` occurs `1` time, but `7 != 1` → no.
So `3` values qualify.

### Example 2

```
Input:
  a = [1, 1, 3, 3, 3]            # 1-indexed a[1..5]
  queries = [(1, 2), (1, 5)]
Output:
  [0, 1]
```

**Explanation:**
- `(1,2)` → `{1, 1}`: value `1` occurs `2` times (`1 != 2`, no); no other value.
  Answer `0`.
- `(1,5)` → `{1,1,3,3,3}`: `1` occurs `2` times (no); `3` occurs `3` times (yes).
  Answer `1`.

## Hint

Values above `n` can never satisfy `cnt == x`, so only "small" values matter. Process
the queries **offline** with **Mo's Algorithm**: maintain `cnt[value]` and a running
answer, and on every add/remove of an element update the answer by checking whether
that single value crosses the `cnt == value` condition.
