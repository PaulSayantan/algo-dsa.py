# Sign on Fence — Solution

## Brute Force

For each query `(l, r, w)`, slide a width-`w` window across `[l, r]` and take the
max of the window minimums. A sliding-window-minimum (monotonic deque) computes
all window minima for one query in `O(r − l + 1)`.

- **Time:** `O(n)` per query → `O(n · q)` ≈ `10^5 · 10^5 = 10^{10}`. Too slow.
- **Space:** `O(n)`.

## Optimal Approach — Persistent Segment Tree + binary search on version

### Reframing the problem

"Is there a width-`w` block inside `[l, r]` whose minimum is `≥ h`?" is
**monotone in `h`**: raising `h` can only make it harder. A block has minimum
`≥ h` exactly when *all* its planks have height `≥ h`. So:

> The answer to `(l, r, w)` is the **largest `h`** such that, among planks with
> height `≥ h`, there is a run of `≥ w` **consecutive** positions lying inside
> `[l, r]`.

### Versions = "planks of height ≥ threshold"

Sort planks by height, **tallest first**. Insert their *positions* one at a time
into a segment tree over positions `[0, n−1]`, marking an inserted position as
"present". Version `k` is the tree after inserting the `k` tallest planks — i.e.
it contains exactly the planks with height `≥ h_k`, where `h_k` is the height of
the k-th tallest plank. Because insertion is a persistent point update, we keep
all `n + 1` versions in `O(n log n)` memory.

### What each node stores — longest consecutive run

To test "is there a run of `w` present positions inside `[l, r]`", each node keeps
four fields describing the *present* positions in its segment:

```
pref  = length of the longest run of present positions starting at the segment's left end
suf   = length of the longest run of present positions ending at the segment's right end
best  = length of the longest run of present positions anywhere in the segment
length= size of the segment  (constant per node position)
```

Merge (combine left child `L` and right child `R`):

```
pref = L.pref + (L.length if L.pref == L.length else 0)    # spill across boundary if L is full
suf  = R.suf  + (R.length if R.suf  == R.length else 0)
best = max(L.best, R.best, L.suf + R.pref)                  # run crossing the boundary
length = L.length + R.length
```

A single point insertion sets a leaf to `pref = suf = best = 1` (length 1) and
re-merges up the path — `O(log n)` cloned nodes per version.

### Answering a query — binary search over versions

For query `(l, r, w)`, binary-search the number `k` of tallest planks:

```
lo, hi = 1, n            # k = how many tallest planks are "present"
answer = 0
while lo <= hi:
    k = (lo + hi) // 2
    if longest_run_in_range(root[k], l, r) >= w:   # restrict the run to [l, r]
        answer = height_of_kth_tallest[k]          # feasible: try fewer/taller planks
        hi = k - 1
    else:
        lo = k + 1                                  # need more (shorter) planks
return answer
```

`longest_run_in_range(root, l, r)` is a segment-tree query that merges only the
nodes overlapping `[l, r]` (returning a `(pref, suf, best, length)` tuple) and
reports the `best` field of the combined result — the longest run of present
positions confined to `[l, r]`. Each query is `O(log n)` for the range walk times
`O(log n)` binary-search steps = `O(log^2 n)`.

Why the found `k` gives the height: version `k` contains the `k` tallest planks,
whose smallest height is `height_of_kth_tallest[k]`. If a width-`w` consecutive
block exists among them inside `[l, r]`, every plank in that block is `≥` that
height, so a sign there hangs at height `≥ height_of_kth_tallest[k]`; and it is
optimal because using fewer planks (a strictly taller threshold) failed the run
test.

### Worked trace (Example 1, query `(0, 7, 3)`)

`heights = [2,6,4,3,5,7,1,8]`. Tallest-first order of (height, pos):
`(8,7),(7,5),(6,1),(5,4),(4,2),(3,3),(2,0),(1,6)`.

Binary-searching for the smallest `k` whose longest run inside `[0,7]` is `≥ 3`:
inserting the tallest planks, a run of 3 consecutive present positions first
appears once positions `{1,2,3,4,5}`-style adjacency forms. That happens when the
threshold drops to height `3` (planks of height `≥ 3` are positions
`{1,2,3,4,5,7}`, giving the consecutive run `1,2,3,4,5` of length 5 ≥ 3). Height
`4` (positions `{1,2,4,5,7}`) has max run only 2. So the answer is `3`. ✓

### Complexity

- Build all versions: `O(n log n)` time and memory.
- Each query: `O(log^2 n)` (binary search × range walk).
- Total: `O((n + q) log^2 n)` ≈ `10^5 · 17 · 17`, comfortably fast.

## Key Insights & Edge Cases

- **Monotonicity is the unlock.** "min ≥ h" is monotone in `h`, which turns the
  problem into binary search over persistent versions ordered by height.
- **Track runs, not counts.** The novel part is the segment node storing
  `pref/suf/best` so a range query returns the longest consecutive *present* run
  restricted to `[l, r]`. Getting the boundary-spill merge right (only spill when
  a child is completely full) is essential.
- **Restrict the run to `[l, r]`.** Runs must lie inside the query range; the
  range query naturally clips them because out-of-range positions are treated as
  "absent" (they are not merged in).
- **Ties in height.** Planks of equal height can be inserted in any order; the
  binary search keys on `height_of_kth_tallest`, and equal heights collapse to the
  same threshold, so ties do not affect correctness.
- **`w == 1`** reduces to "max height in `[l, r]`" — feasible as soon as any plank
  in range is present (the tallest one), so the answer is the range maximum
  (Example 2 query 1 → `8`).
- **`w == r − l + 1`** forces the whole range as the single block, so the answer is
  the range minimum (Example 2 query 2 → `3`).
- **1-indexed vs 0-indexed heights.** Keep the mapping from `k` (count of inserted
  planks) to the k-th tallest height explicit to avoid off-by-one errors.
