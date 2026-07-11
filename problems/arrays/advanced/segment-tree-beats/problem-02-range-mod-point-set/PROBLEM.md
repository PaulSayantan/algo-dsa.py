# Range Modulo, Point Assignment, Range Sum

**Difficulty:** Hard

**Source:** Codeforces 438D — "The Child and Sequence"

## Description

You are given an array `nums` of `n` positive integers (1-indexed). Process a
list of operations of three kinds:

1. **Sum query** — `[1, l, r]`: report the sum of `nums[l..r]`.
2. **Range modulo** — `[2, l, r, x]`: for every `i` in `[l, r]`, replace
   `nums[i]` with `nums[i] % x`.
3. **Point assignment** — `[3, k, x]`: set `nums[k] = x`.

Return the answers to all **sum queries** in order.

The interesting operation is the range modulo. A naive pass over `[l, r]` is too
slow, but there is a decisive shortcut: **`nums[i] % x` changes `nums[i]` only
when `nums[i] >= x`**. If `nums[i] < x`, the modulo is a no-op. Moreover, each
time a value *does* actually change under a modulo, it drops to strictly less than
`x <= nums[i]`, so it is **more than halved** (`a % x < a / 2` whenever
`a >= x`). Therefore any single element can be reduced by modulo at most
`O(log(maxV))` times before it becomes small. A segment tree that stores the
range **maximum** and **stops recursing into any sub-range whose maximum is
`< x`** performs the whole workload in near-linear amortized time — the same
"recurse until a break condition holds" idea behind Segment Tree Beats.

All indices are 1-indexed.

## Constraints

- `1 <= n <= 10^5`
- `1 <= number of operations <= 10^5`
- `1 <= nums[i], x <= 10^9`
- For range/sum ops: `1 <= l <= r <= n`
- For point assignment: `1 <= k <= n`, `1 <= x <= 10^9`

## Examples

### Example 1

```
Input:
  nums = [1, 2, 3, 4, 5]
  ops  = [[2, 3, 5, 4],
          [3, 3, 5],
          [1, 2, 5]]

Output: [8]
```

**Explanation:**
- `[2, 3, 5, 4]` takes `nums[3..5] = [3, 4, 5]` mod `4` -> `[3, 0, 1]`, so the
  array is `[1, 2, 3, 0, 1]`.
- `[3, 3, 5]` sets `nums[3] = 5`, giving `[1, 2, 5, 0, 1]`.
- `[1, 2, 5]` sums `nums[2..5] = 2 + 5 + 0 + 1 = 8`.

### Example 2

```
Input:
  nums = [10, 10, 10]
  ops  = [[1, 1, 3],
          [2, 1, 3, 7],
          [1, 1, 3]]

Output: [30, 9]
```

**Explanation:**
- `[1, 1, 3]` sums the array: `10 + 10 + 10 = 30`.
- `[2, 1, 3, 7]` takes every element mod `7`: `[3, 3, 3]`.
- `[1, 1, 3]` sums again: `3 + 3 + 3 = 9`.

## Hint

Augment each segment-tree node with its range **maximum**. During a range-modulo
update, use the **Segment Tree Beats** break condition: if a node's maximum is
strictly less than the modulus `x`, the modulo cannot change anything in that
sub-range, so return immediately without recursing. Because every real reduction
more than halves a value, the total amortized work is near-linear.
