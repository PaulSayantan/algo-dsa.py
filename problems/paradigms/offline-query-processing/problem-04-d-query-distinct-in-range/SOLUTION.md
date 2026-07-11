# Solution - D-query: Number of Distinct Values in a Range

## Brute Force

For each query, drop the subarray into a set and take its size.

```python
def d_query(a, queries):
    ans = []
    for (l, r) in queries:
        ans.append(len(set(a[l - 1:r])))
    return ans
```

- **Time:** `O(n * q)` in the worst case (each query scans up to `n` elements).
  With `n = 3*10^4`, `q = 2*10^5` that is `6*10^9` — too slow.
- **Space:** `O(n)` for the per-query set.

## Optimal Approach (Offline Query Processing)

The elegant offline trick: **a value should be counted only at its last occurrence
up to the current right endpoint.** If we sweep `r` from `1` to `n` and, for the
prefix `a[1..r]`, keep a `1` in a Fenwick tree at the *most recent* position of
each value (and `0` everywhere else), then the number of distinct values in any
`[l, r]` is simply the count of marked positions in `[l, r]` — because each
distinct value contributes exactly one mark, and that mark sits at its last
occurrence `<= r`, which is inside `[l, r]` iff the value appears in `[l, r]`.

To exploit a single left-to-right sweep, process queries **sorted by `r`**:

1. **Sort queries by `r` ascending**, remembering original indices.
2. Sweep a pointer `ptr` from `1` to `n`. To extend the prefix to include
   position `ptr` with value `v`:
   - If `v` was seen before at position `last[v]`, **unmark** it: `update(last[v], -1)`.
   - **Mark** the new position: `update(ptr, 1)`, and set `last[v] = ptr`.
3. When the sweep has reached the current query's `r`, answer with
   `prefix(r) - prefix(l - 1)`.
4. Scatter answers back to original query order.

```python
def d_query(a, queries):
    n = len(a)
    tree = [0] * (n + 1)                       # 1-indexed Fenwick tree

    def update(pos, delta):
        while pos <= n:
            tree[pos] += delta
            pos += pos & (-pos)

    def prefix(pos):
        s = 0
        while pos > 0:
            s += tree[pos]
            pos -= pos & (-pos)
        return s

    last = {}                                   # value -> its latest position
    order = sorted(range(len(queries)), key=lambda t: queries[t][1])
    ans = [0] * len(queries)
    ptr = 1
    for t in order:
        l, r = queries[t]
        while ptr <= r:                         # extend prefix to r
            v = a[ptr - 1]
            if v in last:
                update(last[v], -1)             # move mark forward
            update(ptr, 1)
            last[v] = ptr
            ptr += 1
        ans[t] = prefix(r) - prefix(l - 1)      # distinct count in [l, r]
    return ans
```

### Why it is correct

Invariant after the prefix has been extended to `r`: for every value `v` that
appears in `a[1..r]`, the Fenwick tree has exactly one `1`, located at the largest
index `<= r` where `v` occurs (its "last occurrence so far"); all earlier
occurrences of `v` are `0`. This is maintained because when a later occurrence of
`v` arrives we first unmark its previous position, then mark the new one.

Given this invariant, count the marks in `[l, r]`. A value `v` present in
`[l, r]` has its unique mark at its last occurrence `p <= r`; since `v` appears in
`[l, r]`, that last occurrence is `>= l` (any occurrence in `[l, r]` is `<= p`, and
`p` itself lies in `[l, r]`), so the mark is inside `[l, r]` and counted once. A
value **not** in `[l, r]` either does not appear in `a[1..r]` (no mark) or its last
occurrence is `< l` (mark outside the range). Hence the mark count equals the
number of distinct values, i.e. `prefix(r) - prefix(l - 1)`.

Sorting by `r` guarantees the sweep pointer only moves forward, so the whole scan
inserts each array position once.

### Step-by-step (Example 1)

`a = [1,1,2,1,3]`. Queries sorted by `r`: `(2,4)`, `(1,5)`, `(3,5)`.

| step | ptr moves to r | marks after extend (positions with 1) | query      | prefix(r)-prefix(l-1) | ans |
|------|----------------|----------------------------------------|------------|-----------------------|-----|
| `(2,4)` r=4 | add pos1(v1),2(v1→move),3(v2),4(v1→move) | {3, 4} (last of 1 is pos4, of 2 is pos3) | l=2,r=4 | prefix(4)-prefix(1)=2 | 2 |
| `(1,5)` r=5 | add pos5(v3) | {3, 4, 5} | l=1,r=5 | prefix(5)-prefix(0)=3 | 3 |
| `(3,5)` r=5 | (already at 5) | {3, 4, 5} | l=3,r=5 | prefix(5)-prefix(2)=3 | 3 |

Note for `(2,4)`: after processing positions 1..4, value `1`'s only mark is at
position 4 and value `2`'s mark is at position 3; marks in `[2,4]` are positions
3 and 4 → `2`. Scatter back to original order `[(1,5),(2,4),(3,5)]` → `[3, 2, 3]`.

- **Time:** `O((n + q) log n + q log q)` — each of the `n` positions triggers at
  most one unmark + one mark (`O(log n)`), each query is two prefix sums, plus the
  sort.
- **Space:** `O(n + q)`.

## Key Insights & Edge Cases

- **"Mark only the last occurrence" is the heart of the trick.** It converts a
  distinct-count into a simple presence count that a Fenwick prefix sum handles.
- **Sort by `r`, sweep `r` forward.** Because marks depend on the prefix `[1..r]`,
  the sweep must be monotone in `r`; that is what makes it a single `O(n)` pass.
- **Values can be large (up to `10^6`)** but the tree is indexed by *position*
  (`1..n`), so no coordinate compression of values is needed — only a hash map
  `last[v]`.
- **Single-element ranges** like `(2,2)` in Example 2 work automatically: exactly
  one mark lies in `[2,2]`.
- **Repeated queries with the same `r`** (e.g. `(1,5)` and `(3,5)`) reuse the same
  prefix state; the pointer does not move for the second one.
- **This is the offline counterpart of a persistent segment tree / merge-sort
  tree**, which would answer the same queries online but with more machinery.
