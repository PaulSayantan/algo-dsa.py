# Naive Operations — Range Increment and Range Sum of Floor Divisions

**Difficulty:** Hard

**Source:** HDU 6315 — "Naive Operations" (2018 Multi-University Training)

## Description

There are two arrays of length `n`, both **1-indexed**:

- `a` — starts as all zeros.
- `b` — a fixed given array which is a **permutation of `1..n`** (so every value
  from `1` to `n` appears exactly once).

Process a list of operations of two kinds:

1. **Range increment** — `[0, l, r]`: for every `i` in `[l, r]`, do `a[i] += 1`.
2. **Range floor-sum query** — `[1, l, r]`: report
   `sum over i in [l, r] of floor(a[i] / b[i])`.

Return the answers to all **query** operations in order.

The naive approach recomputes `floor(a[i] / b[i])` for the whole range on every
query, and increments element-by-element. The key observation that makes this a
Segment Tree Beats-style problem: `floor(a[i] / b[i])` increases by exactly `1`
**only** once every `b[i]` increments of `a[i]`. So maintain, for each index, a
countdown `need[i]` = "how many more `+1`s until the quotient ticks up",
initialized to `b[i]`. A range increment is a **range `-1` on the countdown**;
whenever some `need[i]` hits `0`, that index's stored answer increases by `1` and
its countdown resets to `b[i]`. Tracking the **minimum countdown** per node lets
you **stop recursing into any sub-range whose minimum is still `> 0`** (nothing
ticked there) — the same "recurse only past a break condition" idea behind
Segment Tree Beats. Because index `i` can tick at most `(total increments to i) /
b[i]` times, the total corrective work is bounded and the whole run is
near-linear-logarithmic.

All indices are 1-indexed and satisfy `1 <= l <= r <= n`.

## Constraints

- `1 <= n <= 10^5`
- `1 <= number of operations <= 10^5`
- `b` is a permutation of `1..n`
- For every operation, `1 <= l <= r <= n`

## Examples

### Example 1

```
Input:
  b   = [2, 3]
  ops = [[0, 1, 2],
         [1, 1, 2],
         [0, 1, 1],
         [1, 1, 2]]

Output: [0, 1]
```

**Explanation:**
- `[0, 1, 2]` -> `a = [1, 1]`.
- `[1, 1, 2]` -> `floor(1/2) + floor(1/3) = 0 + 0 = 0`.
- `[0, 1, 1]` -> `a = [2, 1]`.
- `[1, 1, 2]` -> `floor(2/2) + floor(1/3) = 1 + 0 = 1`.

### Example 2

```
Input:
  b   = [1, 2, 3, 4, 5, 6]
  ops = [[0, 1, 3],
         [1, 1, 4],
         [0, 1, 6],
         [0, 1, 3],
         [1, 1, 4],
         [1, 2, 5]]

Output: [1, 5, 2]
```

**Explanation:**
- `[0, 1, 3]` -> `a = [1, 1, 1, 0, 0, 0]`.
- `[1, 1, 4]` -> `floor(1/1)+floor(1/2)+floor(1/3)+floor(0/4) = 1+0+0+0 = 1`.
- `[0, 1, 6]` -> `a = [2, 2, 2, 1, 1, 1]`.
- `[0, 1, 3]` -> `a = [3, 3, 3, 1, 1, 1]`.
- `[1, 1, 4]` -> `floor(3/1)+floor(3/2)+floor(3/3)+floor(1/4) = 3+1+1+0 = 5`.
- `[1, 2, 5]` -> `floor(3/2)+floor(3/3)+floor(1/4)+floor(1/5) = 1+1+0+0 = 2`.

## Hint

Do not store `a` directly. Store per node the **minimum remaining countdown**
(`b[i]` minus how many increments have accumulated toward the next tick) plus a
range-sum of stored answers. A range increment lazily decrements the countdown; a
**Segment Tree Beats** break condition stops recursion wherever the minimum is
still positive, and only where it reaches `0` do you tick that leaf's answer and
reset its countdown.
