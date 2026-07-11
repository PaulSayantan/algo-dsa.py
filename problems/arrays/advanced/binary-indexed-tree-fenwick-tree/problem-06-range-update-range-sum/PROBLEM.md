# Range Update Range Sum

**Difficulty:** Hard

**Source:** Classic competitive-programming problem (e.g. SPOJ HORRIBLE, CSES 1651
"Range Update Queries" is the closely related range-add / point-query variant). Also a
standard interview extension of LeetCode 307.

## Description

Implement a data structure over a 1-indexed integer array of length `n`, initially all
zeros (or given), supporting two operations issued in any interleaved order:

- `rangeUpdate(l, r, delta)`: add the integer `delta` to **every** element in the inclusive
  range `[l, r]`.
- `rangeSum(l, r)`: return the sum of all elements in the inclusive range `[l, r]`.

You are given `n` and a list of operations; process them in order and return the answers to
all `rangeSum` queries as a list.

## Constraints

- `1 <= n <= 2 * 10^5`
- Up to `2 * 10^5` operations total.
- `1 <= l <= r <= n`
- `-10^9 <= delta <= 10^9`; intermediate and final sums fit in 64-bit signed integers.

## Examples

### Example 1

```
Input:
n = 5
ops = [
  ["rangeUpdate", 1, 3, 2],
  ["rangeSum",    1, 5],
  ["rangeUpdate", 2, 5, 3],
  ["rangeSum",    2, 4],
  ["rangeSum",    1, 1]
]

Output: [6, 13, 2]
```

**Explanation:**
- Start: `[0, 0, 0, 0, 0]`.
- `rangeUpdate(1, 3, 2)` → `[2, 2, 2, 0, 0]`.
- `rangeSum(1, 5)` = `2 + 2 + 2 + 0 + 0 = 6`.
- `rangeUpdate(2, 5, 3)` → `[2, 5, 5, 3, 3]`.
- `rangeSum(2, 4)` = `5 + 5 + 3 = 13`.
- `rangeSum(1, 1)` = `2`.

### Example 2

```
Input:
n = 3
ops = [
  ["rangeUpdate", 1, 3, 5],
  ["rangeUpdate", 2, 2, -4],
  ["rangeSum",    1, 3],
  ["rangeSum",    2, 2]
]

Output: [11, 1]
```

**Explanation:**
- Start: `[0, 0, 0]`.
- `rangeUpdate(1, 3, 5)` → `[5, 5, 5]`.
- `rangeUpdate(2, 2, -4)` → `[5, 1, 5]`.
- `rangeSum(1, 3)` = `5 + 1 + 5 = 11`.
- `rangeSum(2, 2)` = `1`.

## Hint

A single Fenwick Tree gives point-update + range-query. To get **range-update +
range-query**, use **two** Binary Indexed Trees (Fenwick Trees) so that a range prefix sum
can be written as a linear function of the index. Apply each range update as a
difference-style update on both trees.
