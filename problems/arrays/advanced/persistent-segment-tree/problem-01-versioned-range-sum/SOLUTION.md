# Versioned Range Sum — Solution

## Brute Force

Store each version as its own full array. On `update`, deep-copy the base
version's array, change one cell, and append it as a new version. On `query`,
sum the requested slice.

- **Update:** `O(n)` time and `O(n)` fresh memory per version.
- **Query:** `O(r − l)` = `O(n)` time.
- **Total:** with `m` operations this is `O(n · m)` time and `O(n · m)` memory —
  roughly `10^5 × 2·10^5 = 2·10^10`. Far too slow, and the memory (tens of GB)
  is impossible.

A prefix-sum array per version speeds up queries to `O(1)` but keeps the `O(n)`
copy-per-update cost, so it does not fix the fundamental problem.

## Optimal Approach — Persistent Segment Tree

Keep a segment tree over array **indices** `[0, n−1]` whose leaves store the
element values and whose internal nodes store subtree sums. The key idea:
**never mutate a node**. Each update produces a new tree that shares all but the
`O(log n)` nodes on one root-to-leaf path with its base version.

### Node layout

Use parallel arrays (fast, no GC churn) or small node objects:

```
left[node], right[node]   # child node ids
sum[node]                 # sum of the segment this node covers
```

### Build version 0 — `O(n)`

Recursively build a normal segment tree. Record its root as `roots[0]`.

```
def build(lo, hi):
    node = new_node()
    if lo == hi:
        sum[node] = initial[lo]
        return node
    mid = (lo + hi) // 2
    left[node]  = build(lo, mid)
    right[node] = build(mid + 1, hi)
    sum[node]   = sum[left[node]] + sum[right[node]]
    return node
```

### Update — `O(log n)` time and memory

Copy the current node, then descend into the side containing `index`, recursing
to build a *new* child there while **pointing the other child at the shared old
subtree**.

```
def update(prev, lo, hi, index, value):
    cur = clone(prev)                 # copy left/right/sum from prev
    if lo == hi:
        sum[cur] = value
        return cur
    mid = (lo + hi) // 2
    if index <= mid:
        left[cur]  = update(left[prev],  lo,    mid, index, value)
    else:
        right[cur] = update(right[prev], mid+1, hi,  index, value)
    sum[cur] = sum[left[cur]] + sum[right[cur]]
    return cur
```

`roots[new_version] = update(roots[prev_version], 0, n-1, index, value)`.
Only the path's nodes are cloned; every off-path subtree is shared, so each new
version costs `O(log n)` extra space.

### Query — `O(log n)`

Standard segment-tree range-sum, but starting from the requested version's root:

```
def query(node, lo, hi, l, r):
    if r < lo or hi < l:       return 0
    if l <= lo and hi <= r:    return sum[node]
    mid = (lo + hi) // 2
    return query(left[node],  lo,    mid, l, r) \
         + query(right[node], mid+1, hi,  l, r)
```

### Why it is correct

Persistence follows from immutability: because we never overwrite an existing
node, `roots[k]` and every node reachable from it describe exactly the array
that existed when version `k` was created — even if newer versions later reused
(shared) some of those nodes. Sharing is safe precisely because shared nodes are
read-only. Correctness of the sum query is the same argument as an ordinary
segment tree; version selection just changes which root we start from.

### Complexity

- Build: `O(n)` time, `O(n)` space.
- Each update: `O(log n)` time, `O(log n)` extra nodes.
- Each query: `O(log n)` time.
- Total memory with `m` updates: `O(n + m log n)`.

## Key Insights & Edge Cases

- **Clone, don't mutate.** The single most common bug is editing a node in place
  and corrupting older versions. Every node on the update path must be a fresh
  copy.
- **Version ids are creation order, not the base id.** The i-th update always
  becomes version `i`, regardless of which `prev_version` it branched from. Keep
  a growing `roots` list and append.
- **Branching history.** Because any earlier version can be a base, the version
  graph is a tree. Persistent segment trees handle this for free — nothing special
  is needed beyond keeping every root.
- **Values can be negative and large.** Use 64-bit accumulation for sums (Python
  ints are unbounded, so this is automatic there).
- **Single-element / full-range queries** (`l == r`, or `l == 0 and r == n−1`)
  are handled by the standard range-query base cases; no special-casing needed.
- **Memory.** Prefer index-based parallel arrays over per-node objects in
  performance-critical settings; pre-size them to about `n + m · (⌈log2 n⌉ + 2)`.
