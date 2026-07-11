# Building Bridges — Solution

## Brute Force

Precompute demolition prefix sums `W`, then run the DP directly:

```
W[0] = 0;  W[k] = W[k-1] + c[k]        # 1-indexed
dp[1] = 0
for i in 2 .. N:
    for j in 1 .. i-1:
        dp[i] = min(dp[i], dp[j] + (h[i]-h[j])^2 + (W[i-1] - W[j]))
answer = dp[N]
```

- **Time:** `O(N^2)`.
- **Space:** `O(N)`.

With `N` up to `10^5`, `O(N^2)` is `10^10` — too slow.

## Optimal Approach — Li Chao Tree

### Expand into a minimum over lines

```
dp[i] = min_j ( dp[j] + h[i]^2 - 2 h[i] h[j] + h[j]^2 + W[i-1] - W[j] )
      = h[i]^2 + W[i-1] + min_j ( (-2 h[j]) * h[i] + (dp[j] + h[j]^2 - W[j]) )
```

Each earlier index `j` is a line

```
line_j(x) = m_j * x + b_j,   m_j = -2 h[j],   b_j = dp[j] + h[j]^2 - W[j]
```

queried at `x = h[i]`, and `dp[i] = h[i]^2 + W[i-1] + min_j line_j(h[i])`.

### Why the monotonic CHT fails here — and Li Chao saves us

In Problems 1-4 the heights / prefix sums were sorted, which made both the inserted
slopes and the query points monotone, enabling the `O(N)` deque hull. **Here heights
are arbitrary**, so:

- slopes `-2 h[j]` are inserted in **no particular order**, and
- query points `h[i]` are **not monotone**.

Neither the append-only hull nor the moving pointer is valid. The **Li Chao Tree**
handles exactly this: it stores lines over a coordinate domain (the distinct query
values, here the distinct heights) and supports

- `insert(line)` in `O(log C)`,
- `query(x)` = min over all inserted lines at `x`, in `O(log C)`,

with no assumption on insertion or query order. `C` is the number of distinct query
coordinates after compression.

### How the Li Chao Tree works

Each node owns a contiguous range of query coordinates and stores the single line
that is minimal at that node's **midpoint**. On `insert`:

1. Compare the new line and the stored line at the node's midpoint; keep the one that
   is lower there as the node's line, and let the other become the "candidate" to
   push down.
2. Compare at the left endpoint to decide which half the candidate can still win in,
   and recurse into that half only.

Each insert touches one root-to-leaf path, so `O(log C)`. `query(x)` walks the path
to `x`'s leaf and returns the minimum stored-line value across those nodes.

### Reference implementation

```python
import bisect
from typing import List, Optional, Tuple

class LiChaoTree:
    """Min Li Chao Tree over a fixed sorted list of query coordinates."""
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs)
        self.tree: List[Optional[Tuple[int, int]]] = [None] * (4 * self.n)

    def _f(self, line: Tuple[int, int], x: int) -> int:
        return line[0] * x + line[1]

    def _add(self, node: int, lo: int, hi: int, nw: Tuple[int, int]) -> None:
        if self.tree[node] is None:
            self.tree[node] = nw
            return
        mid = (lo + hi) // 2
        cur = self.tree[node]
        left_better = self._f(nw, self.xs[lo]) < self._f(cur, self.xs[lo])
        mid_better = self._f(nw, self.xs[mid]) < self._f(cur, self.xs[mid])
        if mid_better:
            self.tree[node], nw = nw, cur          # keep lower line at midpoint
        if lo == hi:
            return
        if left_better != mid_better:
            self._add(2 * node, lo, mid, nw)
        else:
            self._add(2 * node + 1, mid + 1, hi, nw)

    def insert(self, m: int, b: int) -> None:
        self._add(1, 0, self.n - 1, (m, b))

    def _query(self, node: int, lo: int, hi: int, idx: int) -> int:
        res = float('inf') if self.tree[node] is None else self._f(self.tree[node], self.xs[idx])
        if lo == hi:
            return res
        mid = (lo + hi) // 2
        if idx <= mid:
            return min(res, self._query(2 * node, lo, mid, idx))
        return min(res, self._query(2 * node + 1, mid + 1, hi, idx))

    def query(self, x: int) -> int:
        idx = bisect.bisect_left(self.xs, x)       # x is guaranteed present here
        return self._query(1, 0, self.n - 1, idx)


def min_bridge_cost(h: List[int], c: List[int]) -> int:
    n = len(h)
    W = [0] * (n + 1)                              # 1-indexed prefix sums of c
    for i in range(1, n + 1):
        W[i] = W[i - 1] + c[i - 1]

    xs = sorted(set(h))                            # coordinate compression
    tree = LiChaoTree(xs)
    INF = float('inf')
    dp = [INF] * (n + 1)                           # dp[i], 1-indexed
    dp[1] = 0

    def height(i: int) -> int:                     # 1-indexed height access
        return h[i - 1]

    # line for j = 1
    tree.insert(-2 * height(1), dp[1] + height(1) ** 2 - W[1])
    for i in range(2, n + 1):
        best = tree.query(height(i))
        dp[i] = best + height(i) ** 2 + W[i - 1]
        tree.insert(-2 * height(i), dp[i] + height(i) ** 2 - W[i])
    return dp[n]
```

- **Time:** `O(N log N)` — one insert and one query per pillar, each `O(log C)` with
  `C <= N`.
- **Space:** `O(N)` for the compressed coordinates and the `4C`-size tree.

## Key Insights & Edge Cases

- **Sorted vs. unsorted is the whole decision.** Sorted slopes/queries -> monotonic
  `O(N)` CHT (Problems 1-4). Arbitrary slopes/queries -> Li Chao Tree here. Recognize
  which regime you are in before coding.
- **Coordinate-compress the query axis.** Query points are heights, so build the tree
  over the sorted distinct heights and index queries with binary search. If queries
  could hit values not present, build the tree over the full `[min, max]` range
  instead.
- **Bridge cost between two kept pillars skips demolished ones**; the `W[i-1] - W[j]`
  term charges exactly the demolition of the pillars strictly between `j` and `i`.
- **`W[i-1]` and `h[i]^2` are `i`-only** and are added after the minimization.
- **`N = 1`:** only pillar `1` exists (it is also the last), `dp[1] = 0` is the answer.
- **Overflow:** `h^2` up to `10^12` and demolition sums up to `10^11`; totals fit in
  signed 64-bit — use `long long` in C++/Java. In Python integers are unbounded, but
  seed the tree with `float('inf')` carefully (or a large sentinel) so empty nodes do
  not poison the min.
- **Alternative:** a `std::multiset`-based dynamic CHT (Kinetic Segment Tree or
  "LineContainer") achieves the same bounds; the Li Chao Tree is usually simpler to
  get correct.
