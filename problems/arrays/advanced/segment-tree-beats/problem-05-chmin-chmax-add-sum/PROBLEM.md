# Range chmin, chmax, add, and Range Sum (Full Segment Tree Beats)

**Difficulty:** Very Hard

**Source:** Library Checker — "Range Chmin Chmax Add Range Sum" (also Codeforces
Ping problems / AtCoder; the canonical "full" Segment Tree Beats task)

## Description

You are given an array `nums` of `n` integers (0-indexed). Process a list of
operations of four kinds:

1. **Range chmin** — `[0, l, r, x]`: for `i` in `[l, r)`, `nums[i] = min(nums[i], x)`.
2. **Range chmax** — `[1, l, r, x]`: for `i` in `[l, r)`, `nums[i] = max(nums[i], x)`.
3. **Range add**   — `[2, l, r, x]`: for `i` in `[l, r)`, `nums[i] += x` (`x` may be negative).
4. **Range sum query** — `[3, l, r]`: report the sum of `nums[i]` for `i` in `[l, r)`.

Return the answers to all **sum queries** in order. Ranges are **half-open**:
`[l, r)` covers indices `l, l+1, ..., r-1`.

This is the most general form of Segment Tree Beats. To support all four
operations, each node maintains **both ends** of the value distribution:

- for chmin: the **maximum**, **strict second maximum**, and **count of the max**;
- for chmax: the **minimum**, **strict second minimum**, and **count of the min**;
- the **sum**; plus lazy tags for **add**, and the pending chmin/chmax bounds.

A chmin/chmax that would collide with the "other side" tag (for example a chmin
whose target sits between the min and second-min) forces recursion — exactly the
Beats "break" — while an add tag shifts max, second-max, min, and second-min
uniformly. Handled carefully, the amortized cost is `O((n + q) log^2 n)`.

All indices are 0-indexed with `0 <= l < r <= n`.

## Constraints

- `1 <= n <= 2 * 10^5`
- `1 <= number of operations <= 2 * 10^5`
- `-10^9 <= nums[i] <= 10^9`
- For chmin / chmax / add: `-10^9 <= x <= 10^9`
- For every operation, `0 <= l < r <= n`
- Sums fit in signed 64-bit; Python integers handle this natively.

## Examples

### Example 1

```
Input:
  nums = [1, 2, 3, 4, 5]
  ops  = [[3, 0, 5],
          [0, 0, 5, 3],
          [3, 0, 5],
          [2, 0, 5, 2],
          [3, 0, 5]]

Output: [15, 12, 22]
```

**Explanation:**
- `[3, 0, 5]` -> sum of `[1, 2, 3, 4, 5] = 15`.
- `[0, 0, 5, 3]` -> chmin with `3`: `[1, 2, 3, 3, 3]`.
- `[3, 0, 5]` -> sum `1 + 2 + 3 + 3 + 3 = 12`.
- `[2, 0, 5, 2]` -> add `2` to all: `[3, 4, 5, 5, 5]`.
- `[3, 0, 5]` -> sum `3 + 4 + 5 + 5 + 5 = 22`.

### Example 2

```
Input:
  nums = [-3, 0, 4, 1]
  ops  = [[1, 0, 4, 0],
          [3, 0, 4],
          [0, 1, 3, 1],
          [3, 0, 4]]

Output: [5, 2]
```

**Explanation:**
- `[1, 0, 4, 0]` -> chmax with `0` over `[0, 4)`: only `-3` rises to `0`, giving
  `[0, 0, 4, 1]`.
- `[3, 0, 4]` -> sum `0 + 0 + 4 + 1 = 5`.
- `[0, 1, 3, 1]` -> chmin over `[1, 3)` (indices `1` and `2`) with `1`: index `1`
  keeps `0` (`min(0, 1) = 0`), index `2` drops from `4` to `1`, giving
  `[0, 0, 1, 1]`.
- `[3, 0, 4]` -> sum `0 + 0 + 1 + 1 = 2`.

## Hint

Maintain the **max / second-max / max-count** *and* the **min / second-min /
min-count**, plus **sum** and an **add** lazy tag. Apply **Segment Tree Beats**:
chmin/chmax become `O(1)` tags when the target lies strictly between the extreme
and its second-extreme, otherwise recurse; add shifts all six extreme statistics.
Amortized `O((n + q) log^2 n)`.
