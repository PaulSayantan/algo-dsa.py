# Range Updates and Sums

**Difficulty:** Hard

**Source:** CSES Problem Set 1735 — "Range Updates and Sums".

## Description

You are given an array of `n` integers (0-indexed). Then process `q` operations,
each of one of three types over an inclusive index range `[l, r]`:

- **`add(l, r, x)`** — increase *every* element with index in `[l, r]` by `x`.
- **`assign(l, r, x)`** — set *every* element with index in `[l, r]` to `x`.
- **`sum(l, r)`** — report the sum of the elements with index in `[l, r]`.

Return the answers to all `sum` operations, in order.

The challenge is that **two different range updates coexist** on the same tree: an
additive tag and an assignment tag. Their interaction matters. An `assign` must
*erase* any pending `add` on the same range (the overwrite wins), while an `add`
that arrives *after* an `assign` must compose on top of it. Getting this tag
algebra right is the entire difficulty.

## Constraints

- `1 <= n, q <= 2 * 10^5`
- `1 <= x <= 10^9` for `add` and `assign` operations.
- Initial values and all element values fit in a 64-bit signed integer.
- `0 <= l <= r <= n - 1`.

## Examples

### Example 1

```
Input:
  nums = [1, 2, 3, 4, 5]
  assign(0, 2, 4)
  sum(0, 4)
  add(1, 3, 2)
  sum(0, 4)
Output:
  [21, 27]
Explanation:
  Start:            [1, 2, 3, 4, 5]
  assign(0,2,4):    [4, 4, 4, 4, 5]
  sum(0,4):         4 + 4 + 4 + 4 + 5 = 21
  add(1,3,2):       [4, 6, 6, 6, 5]
  sum(0,4):         4 + 6 + 6 + 6 + 5 = 27
```

### Example 2

```
Input:
  nums = [5, 5, 5]
  add(0, 2, 3)
  assign(1, 2, 0)
  sum(0, 2)
  sum(1, 1)
Output:
  [8, 0]
Explanation:
  Start:            [5, 5, 5]
  add(0,2,3):       [8, 8, 8]
  assign(1,2,0):    [8, 0, 0]   (assign overwrites the earlier add on 1..2)
  sum(0,2):         8 + 0 + 0 = 8
  sum(1,1):         0
```

## Hint

Use a **Segment Tree with Lazy Propagation** carrying *two* lazy tags per node: a
pending assignment (with a "present?" flag) and a pending add. Define how they
compose: applying an `assign` clears the node's pending `add` and sets its
assignment; applying an `add` bumps the pending `add` (and the sum by
`x * length`). When pushing down, always push the assignment to a child *before*
the add.
