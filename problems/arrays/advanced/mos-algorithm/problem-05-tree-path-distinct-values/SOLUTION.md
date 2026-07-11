# Count Distinct Values on Tree Paths — Solution

## Brute Force

For each query, find the `u→v` path (via LCA or BFS) and count distinct values with a
set.

- Time: `O(q * n)` — a path can be `O(n)` long; with `n = 4*10^4`, `q = 10^5` this is
  `4*10^9`, too slow.
- Space: `O(n)`.

Distinctness does not merge across sub-paths (a value on both sides is counted once),
so there is no persistent-segment-tree "difference" trick for *distinct count* the way
there is for k-th value. The fix is to reduce paths to array ranges and run **Mo's
Algorithm on the tree**.

## Optimal Approach — Euler Tour + LCA + Mo's

### Flattening with an Euler tour

Run a DFS from the root. When you first enter node `x`, record `st[x]` and append `x`
to an Euler array; when you finish `x` (after all children), record `en[x]` and append
`x` again. Each node appears **exactly twice**, so the Euler array has length `2n`.

Key property: in the Euler array, a node `x` lies "on the path from the root to `y`"
in a usable sense depending on whether it appears once or twice inside a range. We
exploit that with a **toggle**: as Mo's pointers move, each time an index is added, we
flip the node's presence.

```
active[node] == True  -> node currently counted
toggle(node):
    if active[node]: active[node] = False; remove value(node)
    else:            active[node] = True;  add    value(node)
```

A node whose *both* occurrences (`st` and `en`) are inside the window gets toggled
twice → net absent. A node with only one occurrence inside → present. That is exactly
the set of nodes on the path, with one correction for the LCA.

### Mapping a path `(u, v)` to a range

WLOG order so `st[u] <= st[v]`. Let `w = LCA(u, v)`.

- **If `w == u`** (`u` is an ancestor of `v`): the path is the chain `u … v`, which
  corresponds to the Euler range `[st[u], st[v]]`. No extra node needed.
- **Otherwise** (`u` and `v` are in different subtrees of `w`): use the range
  `[en[u], st[v]]`. This range covers every node on the path **except `w` itself**, so
  add `val[w]` separately (and remove it after recording the answer).

The reason `en[u]` is used: between `en[u]` and `st[v]`, exactly the nodes on the path
(other than `w`) appear an odd number of times; the rest cancel.

### Running Mo's over the Euler array

Sort the transformed queries `(L, R, extraLCA, id)` by `(L // block, R)` with the
even/odd trick, `block = 2n / √q`. Slide `curL/curR` over the length-`2n` Euler array,
calling `toggle(euler[i])` on each step. After positioning, if `extraLCA != -1`, add
its value, read `distinct`, then remove it again.

### Why it is correct

The toggle guarantees the set of "active" nodes is precisely the multiset of Euler
indices in the window that appear an odd number of times — which, by the ancestor /
cross-subtree case analysis above, is exactly the node set of the path (minus the LCA
in the cross case, restored explicitly). `distinct` is maintained as the number of
values with positive count, identical to problem 1's frequency logic. Because the tree
and values are static, reordering queries preserves each answer.

### Reference implementation (0-indexed nodes, root = 0)

```python
from math import isqrt
from typing import List, Tuple


def tree_path_distinct(n, edges, vals, queries):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)

    LOG = max(1, n.bit_length())
    parent = [0] * n; depth = [0] * n
    st = [0] * n; en = [0] * n; euler = [0] * (2 * n)
    timer = 0

    # Iterative DFS to avoid recursion limits.
    it_stack = [(0, -1, iter(adj[0]))]
    parent[0] = 0
    st[0] = timer; euler[timer] = 0; timer += 1
    while it_stack:
        node, par, it = it_stack[-1]
        moved = False
        for child in it:
            if child != par:
                parent[child] = node; depth[child] = depth[node] + 1
                st[child] = timer; euler[timer] = child; timer += 1
                it_stack.append((child, node, iter(adj[child]))); moved = True
                break
        if not moved:
            en[node] = timer; euler[timer] = node; timer += 1
            it_stack.pop()

    up = [[0] * n for _ in range(LOG)]
    up[0] = parent[:]
    for j in range(1, LOG):
        upj, upj1 = up[j], up[j - 1]
        for v in range(n):
            upj[v] = upj1[upj1[v]]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        d = depth[u] - depth[v]
        for j in range(LOG):
            if (d >> j) & 1:
                u = up[j][u]
        if u == v:
            return u
        for j in range(LOG - 1, -1, -1):
            if up[j][u] != up[j][v]:
                u = up[j][u]; v = up[j][v]
        return up[0][u]

    uniq = sorted(set(vals))
    comp = {x: i for i, x in enumerate(uniq)}
    cv = [comp[x] for x in vals]

    q = len(queries)
    Q = []
    for idx, (u, v) in enumerate(queries):
        if st[u] > st[v]:
            u, v = v, u
        w = lca(u, v)
        if w == u:
            Q.append((st[u], st[v], -1, idx))
        else:
            Q.append((en[u], st[v], w, idx))

    block = max(1, int((2 * n) / max(1, isqrt(max(1, q)))))
    Q.sort(key=lambda x: (x[0] // block, x[1] if (x[0] // block) % 2 == 0 else -x[1]))

    cnt = [0] * len(uniq); active = [False] * n; distinct = 0

    def add_val(c):
        nonlocal distinct
        if cnt[c] == 0:
            distinct += 1
        cnt[c] += 1

    def rem_val(c):
        nonlocal distinct
        cnt[c] -= 1
        if cnt[c] == 0:
            distinct -= 1

    def toggle(node):
        if active[node]:
            active[node] = False; rem_val(cv[node])
        else:
            active[node] = True; add_val(cv[node])

    ans = [0] * q
    curL, curR = 0, -1
    for L, R, extra, idx in Q:
        while curR < R: curR += 1; toggle(euler[curR])
        while curL > L: curL -= 1; toggle(euler[curL])
        while curR > R: toggle(euler[curR]); curR -= 1
        while curL < L: toggle(euler[curL]); curL += 1
        if extra != -1:
            add_val(cv[extra])
        ans[idx] = distinct
        if extra != -1:
            rem_val(cv[extra])
    return ans
```

### Complexity

- Euler tour + binary-lifting tables: `O(n log n)` build, `O(log n)` per LCA.
- Mo's over the length-`2n` array: `O((n + q) * √n)` toggles, each `O(1)`.
- Overall: `O((n + q) * √n + q log n)`. Space: `O(n log n + q)`.

## Key Insights & Edge Cases

- **Toggle, not add/remove-once.** Because each node has two Euler positions, sliding a
  pointer over an occurrence must *flip* the node in/out. Only the parity matters.
- **The LCA correction is essential.** In the cross-subtree case (`[en[u], st[v]]`) the
  LCA is not represented an odd number of times, so add its value explicitly and undo
  it after recording the answer. Forgetting this undercounts by one whenever the LCA's
  value is unique on the path.
- **Ancestor case** (`w == u`) uses `[st[u], st[v]]` and needs *no* extra LCA add.
- **`u == v`** (single node): LCA is the node itself → ancestor case, range
  `[st[u], st[u]]`, giving `1` distinct value.
- **Recursion depth.** Use an iterative DFS (as above); a path graph has depth `n`,
  which blows Python's recursion limit for large `n`.
- **Value compression** is needed because `val[i]` can be up to `10^9`.
- **Block size** is taken over the Euler length `2n`, not `n`.
- Offline & static: all queries known up front, tree unchanged — the standard Mo's
  precondition.
