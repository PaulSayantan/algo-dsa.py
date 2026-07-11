# Gorgeous Sequence — Range chmin, Range Max, Range Sum

**Difficulty:** Hard

**Source:** HDU 5306 — "Gorgeous Sequence" (the original Segment Tree Beats problem, Ji Driver 2016)

## Description

You are given an array `nums` of `n` non-negative integers (0-indexed here for
the API). Process a list of operations of three kinds:

1. **Range chmin** — `[0, l, r, x]`: for every `i` in `[l, r]`, replace
   `nums[i]` with `min(nums[i], x)`.
2. **Range max query** — `[1, l, r]`: report the maximum of `nums[l..r]`.
3. **Range sum query** — `[2, l, r]`: report the sum of `nums[l..r]`.

Return the answers to all **query** operations (types 1 and 2) in order.

This is the problem Segment Tree Beats was invented for. A range chmin cannot be
maintained by a normal lazy segment tree because it does not act uniformly on a
range — it lowers only the elements that exceed `x`, leaving the rest untouched,
so there is no single additive/assign tag to push down. The Beats trick is to
store at each node not just the maximum but also the **second-largest distinct
value** and the **count of the maximum**. Then `chmin(x)` on a node has three
cases:

- if `x >= max`, the operation does nothing — stop;
- if `secondMax < x < max`, then chmin only lowers the current maxima down to `x`,
  which we can apply in `O(1)` by adjusting `sum` and `max` — stop;
- otherwise (`x <= secondMax`) the effect is ambiguous, so recurse into children
  and re-merge ("this is where the tree gets beaten").

That third recursion is what gives the technique its name; a potential-function
argument shows the total number of these breaks is bounded, yielding
`O((n + q) log n)` amortized time.

All indices are 0-indexed and satisfy `0 <= l <= r <= n - 1`.

## Constraints

- `1 <= n <= 10^6`
- `1 <= number of operations <= 10^6`
- `0 <= nums[i] <= 2^31 - 1`
- For chmin: `0 <= x <= 2^31 - 1`
- For every operation, `0 <= l <= r <= n - 1`
- Range sums can be large; use 64-bit arithmetic (Python handles this natively).

## Examples

### Example 1

```
Input:
  nums = [5, 4, 3, 2, 1]
  ops  = [[1, 0, 4],
          [0, 0, 4, 3],
          [2, 0, 4],
          [1, 0, 4]]

Output: [5, 12, 3]
```

**Explanation:**
- `[1, 0, 4]` -> max of `[5, 4, 3, 2, 1]` is `5`.
- `[0, 0, 4, 3]` -> chmin with `3`: `[3, 3, 3, 2, 1]` (only `5` and `4` drop to `3`).
- `[2, 0, 4]` -> sum `3 + 3 + 3 + 2 + 1 = 12`.
- `[1, 0, 4]` -> max of `[3, 3, 3, 2, 1]` is `3`.

### Example 2

```
Input:
  nums = [1, 7, 7, 7, 5]
  ops  = [[0, 1, 3, 4],
          [2, 0, 4],
          [1, 1, 3]]

Output: [18, 4]
```

**Explanation:**
- `[0, 1, 3, 4]` -> chmin `nums[1..3]` with `4`: the three `7`s each drop to `4`
  (index `0` and index `4` are outside the range), giving `[1, 4, 4, 4, 5]`.
- `[2, 0, 4]` -> sum of the whole array: `1 + 4 + 4 + 4 + 5 = 18`.
- `[1, 1, 3]` -> max of `nums[1..3] = [4, 4, 4]` is `4`.

## Hint

Store per node: the **maximum**, the **count of the maximum**, the **strict
second maximum**, and the **sum**. Apply a **Segment Tree Beats** chmin: skip if
`x >= max`; apply in `O(1)` if `secondMax < x < max`; otherwise recurse. The
amortized cost is `O((n + q) log n)`.
