# Solution — Tree and Queries

## Brute Force

For each query, DFS the subtree of `v`, tally color frequencies, and count how
many colors reach `k`.

```python
def brute(n, colors, edges, queries):
    from collections import defaultdict, Counter
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v); g[v].append(u)

    def subtree_colors(root):
        seen = {root}
        stack = [root]
        cnt = Counter()
        while stack:
            x = stack.pop()
            cnt[colors[x - 1]] += 1
            for y in g[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
        return cnt

    out = []
    for v, k in queries:
        cnt = subtree_colors(v)
        out.append(sum(1 for f in cnt.values() if f >= k))
    return out
```

- **Time:** `O(m * n)` — each query walks up to `n` vertices; `10^10` worst case.
  Too slow.
- **Space:** `O(n)`.

## Optimal Approach — Euler Flatten + Mo's Algorithm

### Step 1: flatten the tree

Do a DFS from the root. Assign `tin[v]` when you first enter `v` and `tout[v]`
when you finish it. Append `v`'s color to `flat[]` at entry. Key property: the
subtree of `v` is exactly the contiguous slice `flat[tin[v] .. tout[v]]`, and its
length equals the subtree size. Use an **iterative** DFS to avoid recursion-limit
issues for `n = 10^5`.

Now every query `(v, k)` becomes a range query `[tin[v], tout[v]]` on the static
array `flat`, plus a per-query threshold `k`.

### Step 2: maintain two histograms

- `cnt[color]` — occurrences of each color in the current window.
- `atLeast[t]` — number of colors whose current count is **at least** `t`.

Updates:

- **add** color `c`: `cnt[c] += 1; atLeast[cnt[c]] += 1`.
  (When a color's count rises to `cnt[c]`, it now qualifies for threshold
  `cnt[c]`; all smaller thresholds already counted it.)
- **remove** color `c`: `atLeast[cnt[c]] -= 1; cnt[c] -= 1`.

Each query answer is simply `atLeast[k]` (or `0` if `k` exceeds the subtree size,
which `atLeast` handles automatically since no color reaches that count).

### Why `atLeast` works

`atLeast[t]` counts colors with `f >= t`. When a color's frequency increases from
`c` to `c+1`, it newly satisfies threshold `c+1` (it already satisfied `1..c`),
so exactly `atLeast[c+1]` increments. Decreasing from `c` to `c-1` means it no
longer satisfies threshold `c`, so `atLeast[c]` decrements. This keeps every
`atLeast[t]` exact for all `t` simultaneously, giving `O(1)` answers.

### Complexity

Mo's over an array of length `n` with `m` queries and `O(1)` updates:
**`O((n + m) · sqrt(n))`** time, `O(n)` space for the frequency and `atLeast`
tables.

### Reference implementation

```python
from typing import List, Tuple


def tree_and_queries(n, colors, edges, queries):
    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    flat = [0] * n                    # colors in entry order
    timer = 0

    # iterative DFS
    stack = [(1, 0, iter(g[1]))]
    visited = [False] * (n + 1)
    visited[1] = True
    tin[1] = 0
    flat[0] = colors[0]
    timer = 1
    # simpler explicit two-phase DFS:
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    order = []
    st = [(1, 0, False)]              # (node, parent, processed)
    while st:
        node, parent, processed = st.pop()
        if processed:
            tout[node] = len(order) - 1
            continue
        tin[node] = len(order)
        order.append(node)
        st.append((node, parent, True))
        for nxt in g[node]:
            if nxt != parent:
                st.append((nxt, node, False))
    flat = [colors[node - 1] for node in order]

    m = len(queries)
    if m == 0:
        return []
    block = max(1, int(n / (m ** 0.5)))

    qs = [(tin[v], tout[v], k) for (v, k) in queries]
    idx = sorted(
        range(m),
        key=lambda t: (qs[t][0] // block,
                       qs[t][1] if (qs[t][0] // block) % 2 == 0 else -qs[t][1]),
    )

    max_color = max(colors)
    cnt = [0] * (max_color + 1)
    at_least = [0] * (n + 2)          # thresholds 1..n
    ans = [0] * m
    cur_l, cur_r = 0, -1

    def add(i):
        c = flat[i]
        cnt[c] += 1
        at_least[cnt[c]] += 1

    def remove(i):
        c = flat[i]
        at_least[cnt[c]] -= 1
        cnt[c] -= 1

    for t in idx:
        l, r, k = qs[t]
        while cur_r < r:
            cur_r += 1
            add(cur_r)
        while cur_l > l:
            cur_l -= 1
            add(cur_l)
        while cur_r > r:
            remove(cur_r)
            cur_r -= 1
        while cur_l < l:
            remove(cur_l)
            cur_l += 1
        ans[t] = at_least[k] if k <= n else 0
    return ans
```

## Key Insights & Edge Cases

- **Iterative DFS is mandatory.** With `n` up to `10^5`, recursive DFS risks a
  Python `RecursionError` / C++ stack overflow on a degenerate (path) tree.
- **Subtree ⇒ contiguous range** is the whole trick. Once flattened, this is the
  *same* engine as the vanilla "distinct in range" problem, just with a richer
  statistic.
- **`atLeast` indexing:** size it to `n + 2` so `atLeast[k]` is always in bounds
  for `1 <= k <= n`. If `k > subtree_size`, `atLeast[k]` is naturally `0`.
- **Remove order:** decrement `atLeast[cnt[c]]` *before* decrementing `cnt[c]`,
  the exact mirror of add, or the histogram desyncs.
- **Colors up to `10^5`** fit in a direct array; otherwise coordinate-compress.
- This is CF 375D; the same flatten-then-Mo pattern (sometimes called "Mo's on
  trees" or, for path queries, "Mo's on trees with LCA") solves a whole family
  of subtree/path aggregation problems.
