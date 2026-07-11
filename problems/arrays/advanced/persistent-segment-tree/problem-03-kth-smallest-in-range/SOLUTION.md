# K-th Smallest Number in Range — Solution

## Brute Force

For each query, copy `nums[l..r]`, sort it, and return the `k`-th element.

- **Time:** `O((r − l + 1) log(r − l + 1))` per query → up to `O(q · n log n)` ≈
  `5·10^4 · 10^5 · 17` operations. Hopelessly slow.
- **Space:** `O(n)` per query for the copy.

Nth-element/quickselect drops the per-query factor to `O(n)`, still `O(q · n)` ≈
`5·10^9` — too slow for the limits.

## Optimal Approach — Persistent Segment Tree (prefix versions + count descent)

### Setup: coordinate compression

Values can be up to `10^9`, so map them to ranks. Let `sorted_vals` be the sorted
list of **distinct** values and `rank[v]` its index. The segment tree is defined
over `[0, V−1]` where `V = len(sorted_vals)`. A leaf `p` counts occurrences of the
value `sorted_vals[p]`.

### One version per prefix

Just like Problem 2:

```
root[-1] = empty tree                       # all counts 0
for i in range(n):
    root[i] = update(root[i-1], 0, V-1, rank[nums[i]], +1)
```

`update` clones only the `O(log V)` nodes on the path to leaf `rank[nums[i]]` and
increments their counts; everything else is shared with `root[i-1]`.

### Query: walk two versions and descend by count

For window `[l, r]`, the frequency of each value equals
`cnt(root[r]) − cnt(root[l-1])`. To find the k-th smallest, descend from the root:

```
def kth(node_r, node_l, lo, hi, k):
    if lo == hi:
        return sorted_vals[lo]              # this value is the answer
    left_count = cnt[left[node_r]] - cnt[left[node_l]]   # how many window values in left half
    mid = (lo + hi) // 2
    if k <= left_count:
        return kth(left[node_r],  left[node_l],  lo,    mid, k)
    else:
        return kth(right[node_r], right[node_l], mid+1, hi,  k - left_count)
```

Start with `kth(root[r], root[l-1], 0, V-1, k)`. Each step drops one level, so a
query is `O(log V)`.

### Worked trace (Example 1, query `(1, 5, 3)`)

`nums = [1,5,2,6,3,7,4]`, window `nums[1..5] = [5,2,6,3,7]`.
Distinct sorted values: `[1,2,3,4,5,6,7]` → ranks `0..6`.
The window's value-frequency (from `root[5] − root[0]`) marks ranks
`{5→r4, 2→r1, 6→r5, 3→r2, 7→r6}`, i.e. one each at ranks `1,2,4,5,6`.

Descending with `k=3` over value range `[0,6]`:
- `mid=3`: left half `[0,3]` holds ranks `1,2` → `left_count = 2`. `k=3 > 2`,
  go right with `k = 3 − 2 = 1`, range `[4,6]`.
- `mid=5`: left half `[4,5]` holds ranks `4,5` → `left_count = 2`. `k=1 ≤ 2`,
  go left, range `[4,5]`.
- `mid=4`: left half `[4,4]` holds rank `4` → `left_count = 1`. `k=1 ≤ 1`,
  go left, range `[4,4]`.
- leaf `4` → answer `sorted_vals[4] = 5`. ✓

### Why it is correct

`root[r]` counts all values inserted at indices `0..r`; `root[l-1]` counts those
at `0..l-1`. Their node-wise difference is exactly the value histogram of
`nums[l..r]`. Searching that histogram for the smallest prefix of value-space
containing at least `k` elements is precisely the k-th order statistic, and the
count-descent finds it in one root-to-leaf pass.

### Complexity

- Build: `O(n log n)` time and memory.
- Query: `O(log n)`.
- Total: `O((n + q) log n)`.

## Key Insights & Edge Cases

- **Two roots, one descent.** The elegance is comparing `left_count` of the two
  versions at each node — never materialize the window.
- **Duplicates count individually.** Because a leaf stores a *count*, repeated
  values contribute multiple order-statistic slots (see Example 2 where the 2nd
  smallest of `[4,4,4]` is `4`).
- **k is 1-indexed.** `k = 1` is the minimum; `k = r − l + 1` is the maximum.
  Off-by-one here is the most common bug.
- **`l == 0`.** Use the empty tree as `root[l-1]`; a shared null node keeps the
  code and memory clean.
- **Negative values** compress just like positive ones — sorting the distinct
  values handles sign automatically.
- **This generalizes.** Swapping the descent condition yields "k-th largest"
  (go right first) or "rank of value x in window" (Problem 2's `countLE`). The
  same prefix machinery underlies both.
- **Tree-path variant.** Replacing prefix versions with root-to-node versions and
  using `root[u] + root[v] − root[lca] − root[parent(lca)]` extends this to
  "k-th smallest on a path in a tree."
