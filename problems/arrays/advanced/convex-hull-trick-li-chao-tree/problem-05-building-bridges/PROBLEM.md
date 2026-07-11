# Building Bridges

**Difficulty:** Hard

Source: CSES Problem Set — "Building Bridges" (Advanced Techniques).

## Description

There are `N` pillars in a row. Pillar `i` has height `h[i]` and a demolition cost
`c[i]`. You will keep some subset of pillars and connect consecutive kept pillars by
bridges; you must **keep the first and last pillar** (`1` and `N`), and every other
pillar is either kept or demolished.

The cost of building a bridge between two consecutive kept pillars `i` and `j`
(with `i < j` and no kept pillar strictly between them) is `(h[i] - h[j])^2`. The
cost of demolishing a pillar is its `c` value. The total cost is the sum of all
bridge costs plus the sum of `c` over all demolished pillars.

Minimize the total cost. Let `W[k] = c[1] + c[2] + ... + c[k]` (`W[0] = 0`) and let
`dp[i]` be the minimum cost to have pillar `i` kept and reached from pillar `1`:

```
dp[1] = 0
dp[i] = min over 1 <= j < i of ( dp[j] + (h[i] - h[j])^2 + (W[i-1] - W[j]) )
```

The middle term `W[i-1] - W[j]` is the cost of demolishing all pillars strictly
between `j` and `i`. The answer is `dp[N]`. The direct DP is `O(N^2)`.

## Constraints

- `1 <= N <= 10^5`
- `1 <= h[i] <= 10^6` — **heights are NOT sorted** (this is the crux)
- `1 <= c[i] <= 10^6`
- The answer fits in a 64-bit signed integer.

## Examples

### Example 1

```
Input:  N = 5, h = [1, 3, 12, 6, 10], c = [4, 5, 3, 6, 1]
Output: 32
```

Explanation: Keeping only pillars `1` and `5` demolishes pillars `2, 3, 4`
(cost `5 + 3 + 6 = 14`) plus one bridge `(1 - 10)^2 = 81`, total `95`. Keeping
`1, 2, 4, 5` demolishes pillar `3` (cost `3`) and pays bridges
`(1-3)^2 + (3-6)^2 + (6-10)^2 = 4 + 9 + 16 = 29`, total `32`. This is optimal, so the
answer is `32`.

### Example 2

```
Input:  N = 5, h = [3, 5, 3, 2, 4], c = [1, 1, 1, 1, 1]
Output: 3
```

Explanation: Keeping every pillar pays no demolition cost and bridges
`(3-5)^2 + (5-3)^2 + (3-2)^2 + (2-4)^2 = 4 + 4 + 1 + 4 = 13`. A better plan keeps
`1, 3, 5` (heights `3, 3, 4`), demolishing pillars `2` and `4` (cost `1 + 1 = 2`) and
paying bridges `(3-3)^2 + (3-4)^2 = 0 + 1 = 1`, total `3`. That is optimal.

## Hint

Expand `(h[i] - h[j])^2` so that
`dp[i] = h[i]^2 + W[i-1] + min_j ( (-2 h[j]) * h[i] + (dp[j] + h[j]^2 - W[j]) )`.
This is again a minimum over lines evaluated at `x = h[i]` — but because heights are
**not sorted**, the slopes `-2 h[j]` arrive in arbitrary order and queries `h[i]` are
not monotone. The monotonic-deque CHT no longer applies. Use a **Li Chao Tree** (or
CHT with binary search over a balanced structure) to insert arbitrary lines and query
arbitrary points in `O(log)` each.
