# Tree and Queries

**Difficulty:** Hard

**Source:** Codeforces 375D — "Tree and Queries".

## Description

You are given a rooted tree with `n` vertices (the root is vertex `1`). Each
vertex `v` has a color `c[v]`. You must answer `m` queries. Each query gives a
vertex `v` and an integer `k` and asks:

> Considering **only the subtree rooted at `v`**, how many colors occur at least
> `k` times?

Formally, for each color `x`, let `f(x)` be the number of vertices in the
subtree of `v` whose color is `x`. The answer is the number of colors `x` with
`f(x) >= k`. All queries are given up front; the tree and colors never change.

### Turning a subtree into a range (the crux)

Run a DFS and record `tin[v]` (entry time) and `tout[v]` (exit time). Lay the
vertices out in an array `flat` ordered by entry time. Then the subtree of `v`
occupies the **contiguous range** `flat[tin[v] .. tout[v]]`. This "Euler flatten"
converts every subtree query into a **range query** on a static array — exactly
what Mo's algorithm answers offline.

Within a window we keep `cnt[color]` and an auxiliary array `atLeast[t]` = number
of colors whose current count is `>= t`. Adding an occurrence of a color whose
count goes `c → c+1` does `atLeast[c+1] += 1`; removing does `atLeast[c] -= 1`.
Each query `(v, k)` then reads `atLeast[k]` directly.

## Constraints

- `2 <= n <= 10^5`
- `1 <= m <= 10^5`
- `1 <= c[v] <= 10^5`
- `1 <= k <= 10^5`
- The tree is connected with exactly `n - 1` edges, rooted at vertex `1`.

## Examples

### Example 1

```
Input:
  n = 4
  colors = [1, 2, 3, 2]        # color of vertices 1..4
  edges = [(1, 2), (1, 3), (2, 4)]
  queries = [(1, 1), (1, 2), (2, 1), (3, 1)]
Output:
  [3, 1, 1, 1]
```

Explanation (DFS entry order 1,2,4,3 → `flat = [1, 2, 2, 3]`):
- Subtree(1) = whole tree, colors {1:1, 2:2, 3:1}. Colors with count ≥ 1: all
  three → **3**.
- Subtree(1) with k=2: only color 2 has count 2 → **1**.
- Subtree(2) = vertices {2,4}, both color 2 → color 2 count 2 ≥ 1 → **1** color.
- Subtree(3) = {3}, color 3 count 1 ≥ 1 → **1**.

### Example 2

```
Input:
  n = 3
  colors = [1, 1, 2]           # color of vertices 1..3
  edges = [(1, 2), (1, 3)]
  queries = [(1, 1), (1, 2), (2, 1)]
Output:
  [2, 1, 1]
```

Explanation (DFS entry order 1,2,3 → `flat = [1, 1, 2]`):
- Subtree(1) colors {1:2, 2:1}. Colors with count ≥ 1: {1, 2} → **2**.
- Subtree(1) with k=2: only color 1 has count 2 → **1**.
- Subtree(2) = {2}, color 1 count 1 ≥ 1 → **1**.

## Hint

Flatten the tree with an Euler tour so each subtree becomes a contiguous array
range, then answer all `(range, k)` queries **offline** with **Sqrt
Decomposition on Queries (offline)**, maintaining per-color counts plus an
`atLeast[t]` histogram so each query is answered in `O(1)`.
