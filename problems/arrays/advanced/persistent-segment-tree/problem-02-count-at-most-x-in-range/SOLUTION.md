# Count Elements ≤ X in a Subarray — Solution

## Brute Force

For each query `(l, r, x)`, scan `nums[l..r]` and count how many are `≤ x`.

- **Time:** `O(n)` per query → `O(n · q)` overall ≈ `10^{10}`. Too slow.
- **Space:** `O(1)` extra.

A per-query `bisect` on a sorted copy of the full array does not help, because
the constraint restricts *both* the index range `[l, r]` **and** the value
`≤ x`; sorting the whole array loses the positional information.

## Optimal Approach — Persistent Segment Tree over prefixes

Think of a segment tree defined over the **sorted distinct values** of `nums`
(coordinate compression). A leaf for value `v` stores *how many times `v` has
been inserted so far*; internal nodes store subtree counts (i.e., counts of
values in a contiguous value range).

Now build **one version per prefix**:

- `root[-1]` = empty tree (all counts 0).
- `root[i]` = `root[i-1]` with `+1` added at the leaf for `nums[i]`.

Each step is a single point update, so it clones only `O(log n)` nodes. After
processing the whole array we have `n + 1` roots, sharing memory heavily.

### The subtraction trick

The multiset of values in `nums[l..r]` equals
"(values in prefix `0..r`) minus (values in prefix `0..l-1`)". Because both are
segment trees over the *same* value domain with the *same* shape, we can walk
`root[r]` and `root[l-1]` **in lockstep**; at every node the count contributed by
the window is `cnt(root[r]) − cnt(root[l-1])`.

To count values `≤ x`, let `p = ` number of compressed values that are `≤ x`
(found by binary search; can be `0`). Then sum window-counts over the first `p`
leaves — a prefix query on the value domain:

```
def count_le(node_r, node_l, lo, hi, p):
    # p = count of value-positions in [0, p-1] that are <= x
    if p <= lo:            return 0            # value bound below this segment
    if hi < p:             return cnt[node_r] - cnt[node_l]   # whole segment qualifies
    mid = (lo + hi) // 2
    return count_le(left[node_r],  left[node_l],  lo,    mid, p) \
         + count_le(right[node_r], right[node_l], mid+1, hi,  p)
```

Answer for `(l, r, x)` = `count_le(root[r], root[l-1], 0, V-1, p)` where `V` is
the number of distinct values. (Use the empty root for `l == 0`.)

### Build sketch

```
compress values -> rank[v] in [0, V-1]
root[-1] = build_empty(0, V-1)          # or lazily created null node
for i in range(n):
    root[i] = update(root[i-1], 0, V-1, rank[nums[i]], +1)
```

### Why it is correct

Insertions are commutative for counting, and prefix `r` contains exactly the
inserts that prefix `l-1` contains plus those at indices `l..r`. Subtracting the
two node-counts therefore yields the exact frequency of each value in the window
`[l, r]`. Restricting the traversal to value-leaves `< p` (values `≤ x`) gives
the requested "at most `x`" count.

### Complexity

- Build all versions: `O(n log n)` time, `O(n log n)` memory.
- Each query: `O(log n)`.
- Total: `O((n + q) log n)` time — about `10^5 · 17 ≈ 2·10^6` per phase.

## Key Insights & Edge Cases

- **`countLE`, not `countEQ`.** Convert `x` to `p =` number of distinct values
  `≤ x` via `bisect_right` on the sorted uniques. If `p == 0`, the answer is `0`
  (nothing qualifies); if `p == V`, the answer is the full window length
  `r − l + 1`.
- **`l == 0`.** Use the empty (all-zero) tree as `root[l-1]`. A shared "null"
  node with count 0 avoids allocating it.
- **Duplicates.** Coordinate compression must keep multiplicities as *counts* at
  a single leaf — do not create separate leaves per occurrence.
- **`x` smaller than every element / larger than every element.** Handled by
  `p = 0` and `p = V` respectively; no special case needed.
- **Online vs offline.** This structure answers queries **online** (each in
  `O(log n)` with no need to sort queries), which is its advantage over an
  offline BIT + sorted-queries sweep.
- **Equivalent framings.** "Count in value range `[lo, hi]`" or "rank of `x` in
  the window" are the same walk with different value bounds; "k-th smallest in
  window" (Problem 3) descends by comparing `k` against left-child window counts.
