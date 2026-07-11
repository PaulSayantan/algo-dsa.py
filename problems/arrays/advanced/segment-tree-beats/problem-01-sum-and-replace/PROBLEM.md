# Range Square-Root and Range Sum

**Difficulty:** Medium

**Source:** HDU 4027 — "Can you answer these queries II" (classic square-root-on-a-range problem)

## Description

You are given an array `nums` of `n` non-negative integers (1-indexed). You must
process a list of operations of two kinds:

1. **Square-root update** — given a range `[l, r]`, replace every element in that
   range with the floor of its square root: `nums[i] = floor(sqrt(nums[i]))`.
2. **Sum query** — given a range `[l, r]`, report the sum of all elements in that
   range.

Return a list containing the answer to every **sum query**, in the order the
queries appear.

The catch: with up to `2 * 10^5` elements and `2 * 10^5` operations, you cannot
walk the whole range on each square-root update. The saving observation is that
once an element is `0` or `1`, `floor(sqrt(x)) == x`, so the element stops
changing. Every other element drops toward `1` in at most about `6` square-root
steps (since `sqrt` roughly halves the number of bits). A segment tree that
**stops recursing into any sub-range whose values can no longer change** performs
the whole batch of updates in near-linear amortized time — this "recurse until a
break condition holds" idea is the seed of Segment Tree Beats.

Each query is encoded as a list:

- `[1, l, r]` — square-root update on `[l, r]`.
- `[2, l, r]` — sum query on `[l, r]`.

All indices are 1-indexed and satisfy `1 <= l <= r <= n`.

## Constraints

- `1 <= n <= 2 * 10^5`
- `0 <= nums[i] <= 10^18`
- `1 <= number of queries <= 2 * 10^5`
- For each query, `1 <= l <= r <= n`
- The answer to a sum query can exceed 32-bit range; use 64-bit arithmetic
  (Python integers handle this automatically).

## Examples

### Example 1

```
Input:
  nums    = [1, 4, 9, 16, 25]
  queries = [[2, 1, 5], [1, 1, 5], [2, 1, 5]]

Output: [55, 15]
```

**Explanation:**
- `[2, 1, 5]` sums the whole array: `1 + 4 + 9 + 16 + 25 = 55`.
- `[1, 1, 5]` square-roots every element: `[1, 2, 3, 4, 5]`.
- `[2, 1, 5]` sums again: `1 + 2 + 3 + 4 + 5 = 15`.

### Example 2

```
Input:
  nums    = [2, 3, 8]
  queries = [[1, 1, 3], [2, 1, 3], [1, 1, 3], [2, 1, 3]]

Output: [4, 3]
```

**Explanation:**
- `[1, 1, 3]` maps `2 -> 1`, `3 -> 1`, `8 -> 2`, giving `[1, 1, 2]`.
- `[2, 1, 3]` sums: `1 + 1 + 2 = 4`.
- `[1, 1, 3]` maps `1 -> 1`, `1 -> 1`, `2 -> 1`, giving `[1, 1, 1]`.
- `[2, 1, 3]` sums: `1 + 1 + 1 = 3`.

## Hint

Use a **Segment Tree Beats**-style break condition: augment each node with the
range **maximum** so that a square-root update can immediately stop recursing into
any sub-range whose maximum is already `<= 1` (those values are stable). Because
each element becomes stable after only a handful of applications, the total work
across all updates is nearly linear.
