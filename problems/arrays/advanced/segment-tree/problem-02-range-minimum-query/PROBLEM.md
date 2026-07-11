# Range Minimum Query (Mutable)

**Difficulty:** Medium

**Source:** Classic Range Minimum Query (RMQ); equivalent to SPOJ RMQSQ / many
competitive-programming judges. Same shape as LeetCode 307 but with a `min` aggregate.

## Description

Implement a data structure `RangeMin` over an integer array `arr` that supports:

- `update(index, val)` — set `arr[index] = val`.
- `query(left, right)` — return the **minimum** element among
  `arr[left], arr[left + 1], ..., arr[right]` (inclusive).

Operations are interleaved and may each be called many times. The point of the
problem is to support *both* mutation and range-min queries efficiently, rather than
rescanning the range on every query.

## Constraints

- `1 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`
- `0 <= index < arr.length`
- `-10^9 <= val <= 10^9`
- `0 <= left <= right < arr.length`
- Up to `2 * 10^5` total calls across `update` and `query`.

## Examples

### Example 1

```
Input:
["RangeMin", "query", "update", "query"]
[[[2, 5, 1, 4, 9, 3]], [1, 3], [4, -2], [3, 5]]

Output:
[null, 1, null, -2]
```

**Explanation:**
- Build over `[2, 5, 1, 4, 9, 3]`.
- `query(1, 3)` inspects `arr[1..3] = [5, 1, 4]` → minimum is `1`.
- `update(4, -2)` → array becomes `[2, 5, 1, 4, -2, 3]`.
- `query(3, 5)` inspects `arr[3..5] = [4, -2, 3]` → minimum is `-2`.

### Example 2

```
Input:
["RangeMin", "query", "query", "update", "query"]
[[[7, 7, 7]], [0, 2], [1, 1], [0, 100], [0, 2]]

Output:
[null, 7, 7, null, 7]
```

**Explanation:**
- Build over `[7, 7, 7]`.
- `query(0, 2)` → min of `[7, 7, 7]` is `7`.
- `query(1, 1)` → single element `7`.
- `update(0, 100)` → array becomes `[100, 7, 7]`.
- `query(0, 2)` → min of `[100, 7, 7]` is `7`.

## Hint

Use a **Segment Tree** where each node stores the minimum of its range. Only the
merge operation changes from the range-sum version — swap `+` for `min`.
