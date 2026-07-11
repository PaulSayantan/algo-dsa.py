# Distinct Elements in Range — Solution

## Brute Force

For each query `(l, r)`, put `nums[l..r]` into a hash set and return its size.

- **Time:** `O(r − l + 1)` per query → `O(n · q)` ≈ `3·10^5 · 2·10^5 = 6·10^{10}`.
  Way too slow.
- **Space:** `O(n)` per query for the set.

There is a well-known **offline** `O((n + q) log n)` solution: sort queries by `r`,
sweep with a Fenwick tree that keeps a `1` at the last occurrence of each value.
That is optimal too — but it requires all queries up front. The persistent
segment tree gives the **same complexity while staying online**.

## Optimal Approach — Persistent Segment Tree over positions

### The "last occurrence" invariant

Maintain a segment tree indexed by **array position** `[0, n−1]` holding 0/1
values. We build one version per prefix so that:

> In version `i`, position `j` holds `1` **iff** `j` is the last index `≤ i` at
> which the value `nums[j]` occurs (within the prefix `0..i`); otherwise `0`.

Then for a query `(l, r)`:

```
answer(l, r) = sum of positions [l, r] in version r
```

### Why that sum is the distinct count

Take any value `v` that appears somewhere in `nums[l..r]`. Its **last** occurrence
within the prefix `0..r` sits at some index `p ≥ l` (it occurs in `[l,r]`, so its
last occurrence in `[0,r]` cannot be earlier than `l`). In version `r`, exactly
that one index `p` is marked `1` for `v`; all earlier occurrences were reset to
`0`. Hence each distinct value in the window contributes exactly one `1` inside
`[l, r]`, and values not in the window contribute none. The range-sum is the
distinct count.

### Building the versions

Track `last[v]` = the most recent index where value `v` was seen (or `-1`).

```
root[-1] = empty tree
last = {}                      # value -> previous index
for i in range(n):
    v = nums[i]
    cur = root[i-1]
    if v in last:
        cur = update(cur, 0, n-1, last[v], 0)   # unmark old occurrence
    cur = update(cur, 0, n-1, i, 1)             # mark new last occurrence
    root[i] = cur
    last[v] = i
```

Each index does at most two point updates, so building all versions is
`O(n log n)` time and memory. (The unmark and mark are ordinary persistent point
updates that clone `O(log n)` nodes each.)

### Answering a query

```
def range_sum(node, lo, hi, l, r):
    if r < lo or hi < l:      return 0
    if l <= lo and hi <= r:   return sum[node]
    mid = (lo + hi) // 2
    return range_sum(left[node],  lo,    mid, l, r) \
         + range_sum(right[node], mid+1, hi,  l, r)

answer = range_sum(root[r], 0, n-1, l, r)
```

`O(log n)` per query, fully online.

### Worked trace (Example 1)

`nums = [1, 1, 2, 1, 3]`. Building the marks (only the final positions that stay
`1` in each version):

| i | value | action                              | marked-1 positions in version i |
|---|-------|-------------------------------------|---------------------------------|
| 0 | 1     | mark 0                              | {0}                             |
| 1 | 1     | unmark 0, mark 1                    | {1}                             |
| 2 | 2     | mark 2                              | {1, 2}                          |
| 3 | 1     | unmark 1, mark 3                    | {2, 3}                          |
| 4 | 3     | mark 4                              | {2, 3, 4}                       |

- Query `(0, 4)` uses version 4, sum over `[0,4]` of `{2,3,4}` = `3`. ✓
- Query `(0, 2)` uses version 2, sum over `[0,2]` of `{1,2}` = `2`. ✓
- Query `(1, 3)` uses version 3, sum over `[1,3]` of `{2,3}` = `2`. ✓

## Key Insights & Edge Cases

- **Query version is `r`, range is `[l, r]`.** A frequent mistake is querying
  version `l` or the whole array; you need version `r` restricted to positions
  `[l, r]`.
- **Two updates per new value occurrence** (unmark previous, mark current) — both
  persistent, chained on the same evolving root before storing it as version `i`.
- **First occurrence of a value** does only the "mark" update (nothing to unmark).
- **Values up to `10^6`.** `last` can be a plain dict/array keyed by value; no
  coordinate compression of positions is needed since the tree is over positions
  `[0, n−1]`.
- **Single-element windows** (`l == r`) work automatically: the position is either
  marked (it is a last occurrence, always true for the rightmost index) → sum 1.
- **Online property is the whole point.** If queries may be given one at a time,
  or answers to earlier queries influence later ones, the offline BIT sweep is not
  applicable but this structure still answers in `O(log n)`.
- **Memory:** `O(n log n)` from up to `2n` point updates; pre-size node arrays to
  about `2n · (⌈log2 n⌉ + 1)` plus the initial build.
